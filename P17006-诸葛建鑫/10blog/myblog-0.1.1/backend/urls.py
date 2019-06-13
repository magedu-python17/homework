"""myBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, re_path
from .views import backend
from .views import article
from .views import category
from .views import tag


app_name = 'app-backend'
urlpatterns = [
    path('article.html', article.article, name="backend-article"),
    path('article-pic', article.article_pic, name='backend-article-pic'),
    path('category.html', category.category, name='backend-category'),
    path('tag.html', tag.tag, name="backend-tag"),
    path('logout.html', backend.logout, name="backend-logout"),
    path('', backend.index, name='backend-index'),
    re_path('set', backend.develop, name='backend-set'),            # 待开发
    re_path('(interest)|(updown).html', backend.develop, name='backend-interest'),
]
