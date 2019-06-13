from django.shortcuts import render, reverse
from django.http import HttpResponseNotFound, JsonResponse
from django.db.models import Count
from util.menu_manager import permission
from util.pagination import Pagination
from web import models as web_models


@permission
def tag(request):
    action_map = {
        'get': tag_get,
        'add': tag_add,
        'edit': tag_edit,
        'delete': tag_delete,
    }
    t = None
    if request.method == 'GET':
        t = request.GET.get('t', 'get')
    elif request.method == 'POST':
        t = request.POST.get('t', 'get')
    print(t, request.method)
    if t and t in request.user_action:
        return action_map.get(t)(request, request.method)
    return HttpResponseNotFound("说出来你可能不信，该页面被外星人劫持了^_^")


def tag_get(request, method):
    if method == 'GET':
        bid = request.logged_blog.nid
        data_count = web_models.Tag.objects.filter(blog_id=bid, is_delete=False).count()
        if data_count:
            current_pg = request.GET.get('p', 1)
            per_pg_count = 10
            list_count = 3
            p = Pagination(current_pg, data_count, per_pg_count, list_count)
            base_url = "{}?t=get".format(reverse('app-backend:backend-tag'))
            pagination = p.gen_pagination(base_url)

            # 因为在模型类中Article和Tag类的delete方法中同时对中间表处理，因此只需查询中间表是否delete即可
            article_count_dic = dict(web_models.ArticleM2MTag.objects.filter(
                article__blog_id=bid, is_delete=False).values_list(
                'tag_id').annotate(article_count=Count('article_id')))

            tag_lst = web_models.Tag.objects.filter(
                blog_id=bid, is_delete=False).values('nid', 'title').order_by('-nid')[p.start: p.end]

            for item in tag_lst:
                key = item['nid']
                if key in article_count_dic:
                    item['article_count'] = article_count_dic[key]
                else:
                    item['article_count'] = 0
        else:
            pagination = ""
            tag_lst = []
        return render(request, 'backend_tag.html', {'tag_lst': tag_lst, 'pagination': pagination})
    return HttpResponseNotFound("说出来你可能不信，该页面被外星人劫持了^_^")


def tag_add(request, method):
    if method == 'POST':
        title = request.POST.get('title', '').strip()
        bid = request.logged_blog.nid
        if 0 < len(title) <= 32:
            res = web_models.Tag.objects.filter(title=title, blog_id=bid).first()
            ret = {'status': 399, 'msg': {'redirect': reverse("app-backend:backend-tag")}}
            if not res:
                web_models.Tag.objects.create(title=title, blog_id=bid)
            elif res.is_delete:               # 如果该标签已被逻辑删除，那么恢复该分类
                res.is_delete = False
                res.save()
            else:
                ret = {'status': 499, 'msg': {'tip': {
                    'remove': ".item-fm>li>label+span",
                    'after': ".item-fm>li>label",
                    'content': ["<span style='color: red'>该标签名已存在</span>"],
                }}}
        else:
            ret = {'status': 499, 'msg': {'tip': {
                'remove': ".item-fm>li>label+span",
                'after': ".item-fm>li>label",
                'content': ["<span style='color: red'>标签名不能为空或长度超出允许范围</span>"],
            }}}
        return JsonResponse(ret)
    return HttpResponseNotFound("说出来你可能不信，该页面被外星人劫持了^_^")


def tag_edit(request, method):
    if method == "POST":
        nid = request.POST.get('nid', 0)
        title = request.POST.get('title', '').strip()
        try:
            le = len(title)
            if le == 0 or le > 32:
                ret = {'status': 499, 'msg': '标签名不能为空或过长'}
            else:
                res = web_models.Tag.objects.filter(
                    nid=nid, blog_id=request.logged_blog.nid, is_delete=False).first()
                if not res:
                    ret = {'status': 499, 'msg': '找不到该记录'}
                else:
                    num = web_models.Tag.objects.filter(
                        title=title, blog_id=request.logged_blog.nid, is_delete=False).count()
                    if num:
                        ret = {'status': 499, 'msg': '该标签名已经存在'}
                    else:
                        res.title = title
                        res.save()
                        ret = {'status': 299}
            return JsonResponse(ret)
        except Exception as e:
            print(e)
    return HttpResponseNotFound("说出来你可能不信，该页面被外星人劫持了^_^")


def tag_delete(request, method):
    if method == 'GET':
        try:
            nid = int(request.GET.get('nid', 0))        # 确保传递过来的nid是一个数字，而非字符串。
            res = web_models.Tag.objects.filter(nid=nid, blog_id=request.logged_blog.nid, is_delete=False).first()
            if res:
                res.delete()
                ret = {'status': 299, 'msg': '<td style="color: red">该分类已删除</td>'}
                return JsonResponse(ret)
        except Exception as e:
            print(e)
    return JsonResponse({'status': 499, 'msg': 'bad request'})
