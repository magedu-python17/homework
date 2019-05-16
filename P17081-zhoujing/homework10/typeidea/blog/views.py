from datetime import date

from django.core.cache import  cache
from django.db.models import Q,F
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse,HttpRequest
from django.views.generic import ListView, DetailView


from blog.models import Post, Category, Tag
from config.models import Sidebar


# Create your views here.
# function view
# def post_list(requset:HttpRequest, category_id=None, tag_id=None):
#
#     tag = None
#     category = None
#     if tag_id:
#         tag, post_list = Post.get_by_tag(tag_id)
#
#     elif category_id:
#         category, post_list = Post.get_by_category(category_id)
#     else:
#         post_list = Post.latest_post()
#     context = {
#         'tag':tag,
#         'category':category,
#         'post_list':post_list,
#         'sidebars':Sidebar.get_all(),
#         'test':Post.get_hots()
#     }
#     context.update(Category.get_navs())
#     print(context)
#     return render(requset, 'blog/list.html', context=context)
#
# def post_detail(requset:HttpRequest, post_id):
#     try:
#         print(post_id)
#         post = Post.objects.get(pk=post_id)
#     except Exception:
#         post = None
#
#     context = {
#         'post':post,
#         'sidebars': Sidebar.get_all(),
#     }
#     context.update(Category.get_navs())
#     return render(requset, 'blog/detail.html', context=context)
#  class view

class CommonViewMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'sidebars':Sidebar.get_all()
        })
        context.update(Category.get_navs())
        return context


class IndexView(CommonViewMixin, ListView):

    queryset = Post.latest_post()
    paginate_by = 1
    context_object_name = 'post_list'
    template_name = 'blog/list.html'


class CategoryView(IndexView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_id = self.kwargs.get('category_id')
        category = get_object_or_404(Category, pk=category_id)
        context.update({
            'category':category
        })
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.kwargs.get('category_id')
        return queryset.filter(category_id = category_id)


class TagView(IndexView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tag_id = self.kwargs.get('tag_id')
        tag = get_object_or_404(Tag, pk=tag_id)
        context.update({
            'tag':tag
        })
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        tag_id = self.kwargs.get('tag_id')
        return queryset.filter(tag__id = tag_id)

class PostDetailView(CommonViewMixin, DetailView):

    queryset = Post.latest_post()
    template_name = 'blog/detail.html'
    context_object_name = 'post'
    pk_url_kwarg = 'post_id'

    def handle_visited(self):
        increase_pv = False
        increase_uv = False
        uid = self.request.uid
        pv_key = 'pv:%s:%s' %(uid, self.request.path)
        uv_key = 'uv:%s:%s:%s' %(uid, str(date.today()), self.request.path)
        if not cache.get(pv_key):
            increase_pv = True
            cache.set(pv_key, 1, 60*1)

        if not cache.get(uv_key):
            increase_uv = True
            cache.set(pv_key, 1, 24*60*60)

        if increase_uv and increase_pv:
            Post.objects.filter(pk=self.object.id).update(pv=F('pv') + 1, uv=F('uv') + 1)

        elif increase_pv:
            Post.objects.filter(pk=self.object.id).update(pv=F('pv') + 1)

        elif increase_uv:
            Post.objects.filter(pk=self.object.id).update(uv=F('uv') + 1)





class SearchView(IndexView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context.update({
            'keyword':self.request.GET.get('keyword', '')
        })
        return context

    def get_queryset(self):
        qureyset = super().get_queryset()
        keyword = self.request.GET.get('keyword','')
        if not keyword:
            return qureyset
        return qureyset.filter(Q(title__icontains=keyword) | Q(desc__icontains=keyword))

class AuthorView(IndexView):

    def get_queryset(self):
        qureyset = super().get_queryset()
        author_id = self.kwargs.get('user_id')
        return qureyset.filter(user_id=author_id)


# 心得   queryset -> get_context_data -> get_pagenate_by -> get_context_obj_name -> paginate_queryset -> get_template_names