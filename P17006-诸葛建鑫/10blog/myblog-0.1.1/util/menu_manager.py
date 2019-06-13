import re
from backend import models as backend_models
from functools import wraps
from .token import validate_token
from django.shortcuts import redirect, reverse
from django.http import HttpResponse
from django.utils.safestring import mark_safe
from web import models as web_models


class MenuManager(object):
    def __init__(self, request, user_id, use_session=True):
        """
        permission2action_dic = {permission1: [action1, action2], permission2: [action3], ...} 去重
        menu_leaf_lst = [permission1, permission2, ....] 去重
        menu_lst = 菜单项
        """
        self.request = request
        self.user_id = user_id
        self.current_url = request.path_info
        self.permission2action_dic = {}
        self.menu_leaf_lst = []
        self.menu_lst = []
        self.use_session = use_session
        self.init_data()

    def init_data(self):
        if self.use_session:
            res = self.init_from_session()
            if res is False:
                self.init_from_sql()
        else:
            self.init_from_sql()

    def init_from_session(self):
        permission_info = self.request.session.get("permission_info")
        if permission_info:
            self.permission2action_dic = permission_info['permission2action_dic']
            self.menu_leaf_lst = permission_info['menu_leaf_lst']
            self.menu_lst = permission_info['menu_lst']
            return True
        return False

    def init_from_sql(self):
        # 查询该用户拥有的所有角色
        role_lst = backend_models.Role.objects.filter(user2role__user_id=self.user_id)

        # 查询该用户角色下的所有权限+动作（去重）
        permission2action_lst = backend_models.Permission2Action.objects.filter(
            role2permission2action__role__in=role_lst).values('p__url', 'a__code').distinct()
        self.permission2action_dic = {}
        for per in permission2action_lst:
            p, a = per['p__url'], per['a__code']
            if self.permission2action_dic.get(p, None):
                self.permission2action_dic[p].append(a)
            else:
                self.permission2action_dic[p] = [a]

        # 查询该用户角色下的所有权限（去重，且要求有挂载目录）,注意，此处最好不要对它格式化，因为它是可变对象，一方更改会同步作用到另一方
        # active等状态也不能在此处就修改，因为会被写入session,如果在此处就做修改，那么每次生产的菜单都是第一次的展开格式
        self.menu_leaf_lst = list(backend_models.Permission2Action.objects.filter(
            role2permission2action__role__in=role_lst, p__menu__isnull=False).values(
            'p_id', 'p__title', 'p__url', 'p__menu_id').distinct())

        # 查询所有菜单项，注意，此时还不能给菜单构建有序层级关系，因为需要根据url来确定哪些时active。
        self.menu_lst = list(backend_models.Menu.objects.values('nid', 'title', 'parent_id'))

        if self.use_session:
            self.request.session['permission_info'] = {
                'permission2action_dic': self.permission2action_dic,
                'menu_leaf_lst': self.menu_leaf_lst,
                'menu_lst': self.menu_lst,
            }

    def _gen_menu_level_lst(self):
        """ 根据用户访问的url, 将对应的菜单设置为active； 筛选出包含有效连接的菜单选项； 将菜单构建为有序层级关系"""
        # 格式化,并添加active, status状态信息，active需要根据用户访问的地址来确定，默认都先设置为False
        # 注意，不能在self.menu_leaf_lst原址上进行修改，因为可变对象会同步更新
        menu_leaf_lst = [
            {
                'nid': item['p_id'],
                'title': item['p__title'],
                'url': item['p__url'],
                'parent_id': item['p__menu_id'],
                'status': True,
                'active': False,
            }
            for item in self.menu_leaf_lst
        ]
        menu_dic = {
            item['nid']: {
                'nid': item['nid'],
                'title': item['title'],
                'parent_id': item['parent_id'],
                'child': [],
                'status': False,
                'active': False
            }
            for item in self.menu_lst
        }

        for item in menu_leaf_lst:
            parent_id = item['parent_id']
            if re.match(item['url'], self.current_url):
                item['active'] = True
                p_id = parent_id
                while p_id:         # 注意，active不会发生重复更新的问题，因为url是唯一的，也就是说该循环只执行一次
                    menu_dic[p_id]['active'] = True
                    p_id = menu_dic[p_id]['parent_id']  # 如果为None,说明已经到顶级菜单，循环借宿
            p_id = parent_id
            while p_id:             # 注意， status会发生重复更新问题，当多个leaf挂载同一个菜单下会发生
                if menu_dic[p_id].get('status', None):
                    break
                menu_dic[p_id]['status'] = True
                p_id = menu_dic[p_id]['parent_id']
            menu_dic[parent_id]['child'].append(item)

        # 构建菜单项的层级关系(由于menu_dic.value()中每一项是一个字典，是可变类型，因此，只要将子menu添加到该字典的child中即可)
        # TODO 要求菜单有序时，此处需要对menu_dic进行排序，再迭代 sorted(lambda v: v.order, menu_dic.values())
        menu_level_lst = []
        for item in menu_dic.values():
            if not item.get('status', None):         # 过滤掉末级菜单项不是叶子节点的菜单项（因为这些菜单项没有url）
                continue
            if not item['parent_id']:
                menu_level_lst.append(item)
            else:
                parent_item = menu_dic[item['parent_id']]
                if parent_item.get('child', None):
                    parent_item['child'].append(item)
                else:
                    parent_item['child'] = [item]
        return menu_level_lst

    def _menu2html(self, lst):
        """如果从父结点开始也可以实现，但是需要递归； 如果从叶子菜单的父结点开始，依次向上，就可以避免递归。"""
        template = """
        <div class="menu-item"><div class="menu-item-title {}">{}</div><div class="menu-item-content">{}</div></div>
        """
        ret = ""
        for item in lst:
            active = "active" if item.get("active") else ""
            if item.get('child', None):
                title = '<i class="fa {}" aria-hidden="true"></i> {}'.format(
                    "fa-caret-down" if active else "fa-caret-right",
                    item["title"]
                )
                content = self._menu2html(item['child'])
                ret += template.format(active, title, content)
            else:
                ret += "<a class='menu-item-option {}' href={}>{}</a>".format(active, item.get("url", "#"), item['title'])
        return ret

    @property
    def html(self):
        """
            css样式如下，即可实现多级菜单
             .menu-item-content {
                margin-left: 20px;
                display: none
            }
            .menu-item-content>a {
                display: block;
            }
            .menu-item-content.active {
                display: block;
            }
        """
        menu_level_lst = self._gen_menu_level_lst()
        return self._menu2html(menu_level_lst)

    @property
    def action(self):
        """返回当前url允许执行的操作，如增、删等"""
        # print('222222222', self.current_url)
        for url, action in self.permission2action_dic.items():
            if re.fullmatch(url, self.current_url):
                # print('11111111', url)
                return action


def permission(fn):
    @wraps(fn)
    def _wrap(request, *args, **kwargs):
        token = request.COOKIES.get("jwt_token", None)
        if token is not None:
            try:
                payload = validate_token(token)
                mm = MenuManager(request, payload['nid'])
                # print(mm.permission2action_dic)
                logged_blog = web_models.Blog.objects.filter(nid=payload['nid']).select_related('user').first()
                action_lst = mm.action
                # print(action_lst)       # TODO 调试用
                if action_lst:
                    request.user_menu = mark_safe(mm.html)
                    request.user_action = action_lst
                    request.logged_blog = logged_blog
                    return fn(request, *args, **kwargs)
                else:
                    return HttpResponse("无权限访问")
            except Exception as e:
                print('1111', e)
        return redirect(reverse("user-web:login"))
    return _wrap
