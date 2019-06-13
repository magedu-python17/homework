from django.shortcuts import render, reverse
from django.http import JsonResponse, HttpResponse, HttpResponseNotFound
from ..customForm.articleForm import ArticleForm
from web import models as web_models
from util.menu_manager import permission
from util.pagination import Pagination
import uuid
import json


@permission
def article(request):
    action_map = {
        'get': article_get,
        'add': article_add,
        'edit': article_edit,
        'delete': ajax_article_delete,
    }
    t = None
    if request.method == 'GET':
        t = request.GET.get('t', 'get')
    elif request.method == 'POST':
        t = request.POST.get('t', 'get')

    if t and t in request.user_action:
        return action_map.get(t)(request, request.method)
    return HttpResponseNotFound("说出来你可能不信，该页面被外星人劫持了^_^")


def article_get(request, method):
    if method == "GET":
        bid = request.logged_blog.nid
        data_count = web_models.Article.objects.filter(blog_id=bid, is_delete=False).count()
        if data_count:
            current_pg = request.GET.get('p', 1)
            per_pg_count = 10
            list_count = 3
            p = Pagination(current_pg, data_count, per_pg_count, list_count)
            pagination = p.gen_pagination("{}?t=get".format(reverse('app-backend:backend-article')))
            article_lst = web_models.Article.objects.filter(
                blog_id=bid, is_delete=False).order_by('-nid')[p.start: p.end]
        else:
            pagination = ""
            article_lst = []
        return render(request, 'backend_article.html', {'article_lst': article_lst, 'pagination': pagination})
    else:
        return HttpResponseNotFound("说出来你可能不信，该页面被外星人劫持了^_^")


def article_add(request, method):
    if method == 'GET':
        afm = ArticleForm(request)
        return render(request, 'backend_article_add.html', {"afm": afm})
    elif method == 'POST':
        afm = ArticleForm(request, request.POST)
        if afm.is_valid():
            data = afm.cleaned_data
            tags = data['tag_id']
            tags.extend(data['new_tag'])
            tags = set(tags)        # 去重，避免用户自定义便签同已有的重复
            try:
                a = web_models.Article.objects.create(
                    blog_id=request.logged_blog.nid, title=data['title'], summary=data['summary'],
                    category_id=data['category_id'], webplate_id=data['webplate_id'])
                web_models.ArticleDetail.objects.create(content=data['content'], article_id=a.nid)
                for t in tags:
                    web_models.ArticleM2MTag.objects.create(article_id=a.nid, tag_id=t)
                ret = {
                    'status': 399,
                    'msg': reverse('user-web:home_article_detail', args=(request.logged_blog.site, a.nid)),
                }
                return JsonResponse(ret)
            except Exception as e:
                print('err in article_add', e)
                return JsonResponse({'status': 399, 'msg': 'errors.html'})      # TODO 错误页面
        else:
            lst_order = ['title', 'summary', 'content', 'category_id', 'tag_id', 'new_tag', 'webplate_id']
            dic = json.loads(afm.errors.as_json())
            err = [dic.get(lo, [{}])[0].get('message', '') for lo in lst_order]
            ea = dic.get("__all__", [{}])[0].get('message', '')
            if ea:
                err.append(ea)
            return JsonResponse({'status': 499, 'msg': err})
    return HttpResponseNotFound("说出来你可能不信，该页面被外星人劫持了^_^")


def article_edit(request, method):
    bid = request.logged_blog.nid
    if method == 'GET':
        aid = request.GET.get('aid', None)
        if aid:
            art = web_models.Article.objects.filter(
                blog_id=bid, nid=aid).select_related('articledetail').first()
            if art:
                initial = {'title': art.title, 'summary': art.summary, 'content': art.articledetail.content,
                           'category_id': art.category_id,
                           'tag_id': list(art.articlem2mtag_set.filter(is_delete=False).values_list('tag_id', flat=True)),
                           'webplate_id': art.webplate_id}
                afm = ArticleForm(request, initial=initial)
                return render(request, 'backend_article_edit.html', {'afm': afm, 'aid': aid})
    elif method == 'POST':
        aid = request.POST.get('aid', None)
        if aid and web_models.Article.objects.filter(nid=aid, blog_id=bid):     # 要求该文章是该博主的
            afm = ArticleForm(request, request.POST)
            if afm.is_valid():
                data = afm.cleaned_data
                tags = data['tag_id']
                tags.extend(data['new_tag'])
                # 去重，避免用户自定义便签同已有的重复, 注意：需要转化为整数，因为tags列表中是字符串，而old_tags从数据库中取出为整数
                tags = set(map(int, tags))
                try:
                    web_models.Article.objects.filter(nid=aid).update(
                        title=data['title'], summary=data['summary'],
                        category_id=data['category_id'], webplate_id=data['webplate_id'])
                    web_models.ArticleDetail.objects.filter(article_id=aid).update(content=data['content'])
                    old_tags = dict(web_models.ArticleM2MTag.objects.filter(
                        article_id=aid).values_list('tag_id', 'is_delete'))
                    # print(old_tags, tags)
                    # 逻辑删除旧的tag： is_delete=True
                    for a2t in web_models.ArticleM2MTag.objects.filter(article_id=aid).exclude(tag_id__in=tags):
                        # print('logic delete', a2t.tag_id)
                        a2t.delete()
                    # 如果已经存在了，查看是否已逻辑删除，是就恢复；如果不存在，则创建关系
                    for t in tags:
                        if t in old_tags and old_tags[t]:       # 如果old_tags[t]为True,说明该记录逻辑删除，需把它恢复
                            # print('resume', t)
                            web_models.ArticleM2MTag.objects.filter(
                                article_id=aid, tag_id=t).update(is_delete=False)
                        elif t not in old_tags:
                            # print('new', t)
                            web_models.ArticleM2MTag.objects.create(article_id=aid, tag_id=t)
                    ret = {
                        'status': 399,
                        'msg': reverse('user-web:home_article_detail', args=(request.logged_blog.site, aid)),
                    }
                    return JsonResponse(ret)
                except Exception as e:
                    print(e)        # 执行最下面的HttpResponseNotFound返回错误页面
            else:
                lst_order = ['title', 'summary', 'content', 'category_id', 'tag_id', 'new_tag', 'webplate_id']
                dic = json.loads(afm.errors.as_json())
                err = [dic.get(lo, [{}])[0].get('message', '') for lo in lst_order]
                ea = dic.get("__all__", [{}])[0].get('message', '')
                if ea:
                    err.append(ea)
                return JsonResponse({'status': 499, 'msg': err})
    return HttpResponseNotFound("说出来你可能不信，该页面被外星人劫持了^_^")


def ajax_article_delete(request, method):
    if method == 'GET':
        aid = request.GET.get('aid', None)
        print(aid, request.logged_blog.nid)
        if aid:
            art = web_models.Article.objects.filter(nid=aid, blog_id=request.logged_blog.nid, is_delete=False).first()
            if art:                 # 要求该文章是该博主的
                try:
                    art.delete()
                    ret = {'status': 299, 'msg': '<td style="color:red">该文章已删除</td>'}
                    return JsonResponse(ret)
                except Exception as e:
                    print(e)
    return JsonResponse({'status': 404, 'msg': 'bad request'})


def article_pic(request):
    """
    kindeditor上传文件时可以接收一个返回值，用于在iframe中显示，如下dic中
        error表示上传的文件、图片是否有误， error为0表示没有错误
        url表示获取上传的文件、图片的url地址。
        message:表示如果上传错误，页面上的显示的错误信息
    :param request:
    :return:
    """
    dic = {
        'error': 0,
        'url': '',
        'message': 'success',
    }
    if request.method == 'POST':
        print(request.POST)
        print(request.FILES)
        uid = uuid.uuid4().hex
        obj = request.FILES.get('imgFile')
        suffix = obj.name.rsplit('.', maxsplit=1)[-1]
        name = 'IMG-{}.{}'.format(uid, suffix)
        url = '/'.join(['/static/img', name])
        fp = '/'.join(['static/img', name])
        dic['url'] = url
        print(url, fp)
        with open(fp, 'wb') as f:
            for chunk in obj.chunks():
                f.write(chunk)
        return JsonResponse(dic)



































