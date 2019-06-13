from django.shortcuts import render, reverse
from django.http import HttpResponseNotFound
from .. import models as web_models
from util.pagination import Pagination
from util.token import logged_add_blog
from django.db.models import Count


@logged_add_blog
def index(request):
    """ 博客网站主页，展示最新的所有文章 """
    if request.method == "GET":
        try:
            plate_id = int(request.GET.get('plate', 0))
        except:
            plate_id = 0
        if plate_id and web_models.WebPlate.objects.filter(nid=plate_id).first():   # 板块id在数据库中存在
            query = {'webplate_id': plate_id, 'is_delete': False}
        else:
            query = {'is_delete': False}
        data_count = web_models.Article.objects.filter(**query).count()
        if data_count:              # 如果该板块下有文章：
            current_pg = request.GET.get('p', 1)
            per_pg_count = 10
            list_count = 3
            p = Pagination(current_pg, data_count, per_pg_count, list_count)
            base_url = reverse('user-web:index')
            pagination = p.gen_pagination(base_url)
            article_lst = web_models.Article.objects.filter(
                **query).select_related('blog', 'blog__user').order_by('-nid')[p.start: p.end]
        else:
            pagination = ""
            article_lst = []

        plate_article = dict(web_models.WebPlate.objects.filter(
            article__is_delete=False).values_list('nid').annotate(article_count=Count('article')))

        plate_lst = web_models.WebPlate.objects.values('nid', 'title')
        for item in plate_lst:
            key = item['nid']
            if key in plate_article:
                item['article_count'] = plate_article[key]
            else:
                item['article_count'] = 0
        return render(
            request,
            'index.html',
            {
                'article_lst': article_lst,
                'pagination': pagination,
                'plate_lst': plate_lst,
                'plate_id': plate_id,
            }
        )
    else:
        return HttpResponseNotFound("说出来你可能不信，该页面被外星人劫持了^_^")


def article_list(request, site):
    """ 博客个人主页: site是个人博客的后缀名， 如 http://xxx/zhuge.html 中的zhuge对应数据库中Blog.site """
    if request.method == "GET":
        blog = web_models.Blog.objects.filter(site=site).select_related('user').first()
        if blog:
            tag_lst = web_models.Tag.objects.filter(
                blog=blog, article__is_delete=False).annotate(article_count=Count('article'))
            category_lst = web_models.Category.objects.filter(
                blog=blog, article__is_delete=False).annotate(article_count=Count('article'))

            # ------------------- 注意： sqlite3使用的时strftime， 而mysql使用的时date_format ------------------- #
            # date_lst = web_models.Article.objects.raw(
            #     """select nid, count(nid) as article_count, strftime("%%Y-%%m", create_time) as archive
            #     from article where blog_id=%s and is_delete=%s group by archive""",
            #     params=(blog.nid, 0))

            date_lst = web_models.Article.objects.filter(blog_id=blog.nid, is_delete=False).extra(
                select={'archive': 'date_format(create_time, "%%Y-%%m")'}).values('archive').annotate(
                article_count=Count('nid'))

            query = {'blog': blog, 'is_delete': False}
            data_count = web_models.Article.objects.filter(**query).count()
            if data_count:
                current_pg = request.GET.get('p', '1')  # 读取第几页,获得的是一个字符串
                per_pg_count = 10
                list_count = 3
                p = Pagination(current_pg, data_count, per_pg_count, list_count)
                base_url = reverse('user-web:home_article_list', args=(site,))
                pagination = p.gen_pagination(base_url)

                article_lst = web_models.Article.objects.filter(**query).order_by('-nid')[p.start: p.end]
            else:
                pagination = ''
                article_lst = []
            return render(
                request,
                'home_article_list.html',
                {
                    "blog": blog,
                    "tag_lst": tag_lst,
                    "category_lst": category_lst,
                    "date_lst": date_lst,
                    "article_lst": article_lst,
                    "pagination": pagination,
                }
            )
    return HttpResponseNotFound("说出来你可能不信，该页面被外星人劫持了^_^")


def article_detail(request, site, nid):
    if request.method == "GET":
        blog = web_models.Blog.objects.filter(site=site).select_related('user').first()
        if blog:
            article = web_models.Article.objects.filter(
                nid=nid, blog=blog, is_delete=False).select_related('category', 'articledetail').first()
            if article:
                tag_lst = web_models.Tag.objects.filter(
                    blog=blog, article__is_delete=False).annotate(article_count=Count('article'))
                category_lst = web_models.Category.objects.filter(
                    blog=blog, article__is_delete=False).annotate(article_count=Count('article'))
                # date_lst = web_models.Article.objects.raw(
                #     """select nid, count(nid) as article_count, strftime("%%Y-%%m", create_time) as archive
                #     from article where blog_id=%s and is_delete=%s group by archive""",
                #     params=(blog.nid, 0))

                date_lst = web_models.Article.objects.filter(blog_id=blog.nid, is_delete=False).extra(
                    select={'archive': 'date_format(create_time, "%%Y-%%m")'}).values('archive').annotate(
                    article_count=Count('nid'))

                tags = web_models.Tag.objects.filter(article=article)       # 多对多反向查询,由于article已经确定是未删除的

                return render(
                    request,
                    'home_article_detail.html',
                    {
                        'blog': blog,
                        "tag_lst": tag_lst,
                        "category_lst": category_lst,
                        "date_lst": date_lst,
                        'article': article,
                        'tags': tags,
                    }
                )
    return HttpResponseNotFound("说出来你可能不信，该页面被外星人劫持了^_^")


def article_query(request, site, condition, val):   # 根据url匹配规则，condition只能是tag, category, date
    if request.method == 'GET':
        blog = web_models.Blog.objects.filter(site=site).select_related('user').first()
        if blog:
            tag_lst = web_models.Tag.objects.filter(
                blog=blog, article__is_delete=False).annotate(article_count=Count('article'))
            category_lst = web_models.Category.objects.filter(
                blog=blog, article__is_delete=False).annotate(article_count=Count('article'))
            # date_lst = web_models.Article.objects.raw(
            #     """select nid, count(nid) as article_count, strftime("%%Y-%%m", create_time) as archive
            #     from article where blog_id=%s and is_delete=%s group by archive""",
            #     params=(blog.nid, 0))

            date_lst = web_models.Article.objects.filter(blog_id=blog.nid, is_delete=False).extra(
                select={'archive': 'date_format(create_time, "%%Y-%%m")'}).values('archive').annotate(
                article_count=Count('nid'))

            # 确定date_count,由于前面已经查询数据库，data_count可以从结果中获得
            dic = {'tag': tag_lst, 'category': category_lst, 'date': date_lst}
            lst = dic[condition]
            data_count = 0
            try:
                value = val if condition == 'date' else int(val)
            except:         # 抛异常是因为int(val)失败，说明用户访问url有问题，如 /tag/2019-05.html
                return HttpResponseNotFound("说出来你可能不信，该页面被外星人劫持了^_^")
            # 从查询结果tag_lsg, category_lsg, date_lst中找到当前url对应的数据总共有多少条。
            for item in lst:
                if condition == 'date':
                    if item.get('archive', '') == value:        # 注意mysql下上述归档聚合返回的是一个字典，sqlite返回的是一个对象
                        data_count = item.get('article_count', 0)
                        break
                else:
                    if item.nid == value:
                        data_count = item.article_count
                        break

            if data_count:
                current_pg = request.GET.get('p', '1')  # 读取第几页,获得的是一个字符串
                per_pg_count = 10
                list_count = 3
                p = Pagination(current_pg, data_count, per_pg_count, list_count)
                base_url = reverse('user-web:home_article_query', args=(site, condition, val))
                pagination = p.gen_pagination(base_url)

                if condition == 'tag':
                    article_query_lst = web_models.Article.objects.filter(
                        blog=blog, is_delete=False, tag__nid=val).order_by('-nid')[p.start: p.end]
                elif condition == 'category':
                    article_query_lst = web_models.Article.objects.filter(
                        blog=blog, is_delete=False, category_id=val).order_by('-nid')[p.start: p.end]
                else:
                    article_query_lst = web_models.Article.objects.filter(blog_id=blog.nid, is_delete=False).extra(
                        where=['date_format(create_time, "%%Y-%%m")=%s'], params=(val, )).order_by(
                        '-nid')[p.start: p.end]

                    # article_query_lst = web_models.Article.objects.filter(blog=blog, is_delete=False).extra(
                    #     where=['strftime("%%Y-%%m", create_time)=%s'], params=(val, )
                    # ).order_by('-nid')[p.start:p.end]
            else:                       # 当总数据为0时，无需分页，也无需查询
                pagination = ''
                article_query_lst = []

            return render(
                request,
                'home_article_query.html',
                {
                    'blog': blog,
                    'tag_lst': tag_lst,
                    "category_lst": category_lst,
                    "date_lst": date_lst,
                    "pagination": pagination,
                    'article_query_lst': article_query_lst,
                }
            )
    return HttpResponseNotFound("说出来你可能不信，该页面被外星人劫持了^_^")
