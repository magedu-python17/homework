"""typeidea URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.sitemaps import views as sitemap_view
from blog.sitemap import PostSitemap

from .custom_site import custon_site
# from blog.views import post_detail, post_list
from blog.views import (
    PostDetailView, IndexView, CategoryView,
    TagView, SearchView, AuthorView
)
from config.views import LinkView
from comment.views import CommentView

urlpatterns = [
    url(r'^$',IndexView.as_view(), name='index'),
    url(r'^post/(?P<post_id>\d+).html$',PostDetailView.as_view(), name='post-detail'),
    url(r'category/(?P<category_id>\d+)/$',CategoryView.as_view(), name='category-list'),
    url(r'tag/(?P<tag_id>\d+)/$',TagView.as_view(), name='tag-list'),
    url(r'^links/$', LinkView.as_view() ,name='links'),
    url(r'^search/$',SearchView.as_view(), name='search'),
    url(r'^comment/$',CommentView.as_view(), name='comment'),
    url(r'^author/(?P<user_id>\d+)/$',AuthorView.as_view(), name='author'),
    url(r'^superadmin/', admin.site.urls, name='super-admin'),
    url(r'^admin/', custon_site.urls, name='admin'),
    url(r'^sitemap\.xml$', sitemap_view.sitemap, {'sitemaps':{'posts':PostSitemap}}),

]
