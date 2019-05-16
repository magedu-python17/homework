from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.views.generic import ListView
from blog.views import CommonViewMixin

from .models import Link
# Create your views here.

class LinkView(CommonViewMixin, ListView):

    queryset = Link.objects.filter(status=Link.STATUS_NARMAL)
    context_object_name = 'link_list'
    template_name = 'config/links.html'



