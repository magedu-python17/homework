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
from .views import account, home


app_name = 'user-web'
urlpatterns = [
    path('reg.html', account.ajax_reg, name='reg'),
    path('login.html', account.ajax_login, name='login'),
    path('logout.html', account.ajax_logout, name='logout'),
    path('check_code', account.check_code, name="check_code"),
    path('<str:site>.html', home.article_list, name="home_article_list"),
    re_path(r'^(?P<site>\w+)/(?P<condition>((tag)|(category)|(date)))/(?P<val>\w+(-\w+)*).html$',
            home.article_query, name="home_article_query"),
    path('<str:site>/<int:nid>.html', home.article_detail, name="home_article_detail"),
    path('', home.index, name='index'),
]
