from django.shortcuts import render, reverse
from django.http import HttpResponseNotFound, JsonResponse
from django.db.models import Count
from util.menu_manager import permission
from util.pagination import Pagination
from web import models as web_models


@permission
def category(request):
    action_map = {
        'get': category_get,
        'add': category_add,
        'edit': category_edit,
        'delete': category_delete,
    }
    t = None
    if request.method == 'GET':
        t = request.GET.get('t', 'get')
    elif request.method == 'POST':
        t = request.POST.get('t', 'get')
    if t and t in request.user_action:
        return action_map.get(t)(request, request.method)
    return HttpResponseNotFound("说出来你可能不信，该页面被外星人劫持了^_^")


def category_get(request, method):
    if method == 'GET':
        bid = request.logged_blog.nid
        data_count = web_models.Category.objects.filter(blog_id=bid, is_delete=False).count()
        if data_count:
            current_pg = request.GET.get('p', 1)
            per_pg_count = 10
            list_count = 3
            p = Pagination(current_pg, data_count, per_pg_count, list_count)
            base_url = "{}?t=get".format(reverse('app-backend:backend-category'))
            pagination = p.gen_pagination(base_url)

            article_count_dic = dict(web_models.Article.objects.filter(
                blog_id=bid, is_delete=False, category__is_delete=False).values_list(
                'category_id').annotate(article_count=Count('nid')))

            category_lst = web_models.Category.objects.filter(
                blog_id=bid, is_delete=False).values('nid', 'title').order_by('-nid')[p.start: p.end]

            for item in category_lst:
                key = item['nid']
                if key in article_count_dic:
                    item['article_count'] = article_count_dic[key]
                else:
                    item['article_count'] = 0
        else:
            pagination = ""
            category_lst = []
        return render(request, 'backend_category.html', {'category_lst': category_lst, 'pagination': pagination})
    return HttpResponseNotFound("说出来你可能不信，该页面被外星人劫持了^_^")


def category_add(request, method):
    if method == 'POST':
        title = request.POST.get('title', '').strip()
        if 0 < len(title) <= 32:
            res = web_models.Category.objects.filter(title=title, blog_id=request.logged_blog.nid).first()
            ret = {'status': 399, 'msg': {'redirect': reverse("app-backend:backend-category")}}
            if not res:
                web_models.Category.objects.create(title=title, blog_id=request.logged_blog.nid)
            elif res.is_delete:               # 如果该分类已被逻辑删除，那么恢复该分类
                res.is_delete = False
                res.save()
            else:
                ret = {'status': 499, 'msg': {'tip': {
                    'remove': ".item-fm>li>label+span",
                    'after': ".item-fm>li>label",
                    'content': ["<span style='color: red'>该类名已存在</span>"],
                }}}
        else:
            ret = {'status': 499, 'msg': {'tip': {
                'remove': ".item-fm>li>label+span",
                'after': ".item-fm>li>label",
                'content': ["<span style='color: red'>类名不能为空或长度超出允许范围</span>"],
            }}}
        return JsonResponse(ret)
    return HttpResponseNotFound("说出来你可能不信，该页面被外星人劫持了^_^")


def category_edit(request, method):
    if method == "POST":
        nid = request.POST.get('nid', 0)
        title = request.POST.get('title', '').strip()
        try:
            le = len(title)
            if le == 0 or le > 32:
                ret = {'status': 499, 'msg': '分类名不能为空或过长'}
            else:
                c = web_models.Category.objects.filter(
                    nid=nid, blog_id=request.logged_blog.nid, is_delete=False).first()
                if not c:
                    ret = {'status': 499, 'msg': '找不到该记录'}
                else:
                    # 判断用户输入的类名是否已经存在
                    num = web_models.Category.objects.filter(
                        title=title, blog_id=request.logged_blog.nid, is_delete=False).count()
                    if num:
                        ret = {'status': 499, 'msg': '该类名已经存在'}
                    else:
                        c.title = title
                        c.save()
                        ret = {'status': 299}
            return JsonResponse(ret)
        except Exception as e:
            print(e)
    return HttpResponseNotFound("说出来你可能不信，该页面被外星人劫持了^_^")


def category_delete(request, method):
    if method == 'GET':
        try:
            nid = int(request.GET.get('nid', 0))        # 确保传递过来的nid是一个数字，而非字符串。
            c = web_models.Category.objects.filter(nid=nid, blog_id=request.logged_blog.nid, is_delete=False).first()
            if c:
                c.delete()
                ret = {'status': 299, 'msg': '<td style="color: red">该分类已删除</td>'}
                return JsonResponse(ret)
        except Exception as e:
            print(e)
    return JsonResponse({'status': 499, 'msg': 'bad request'})
