from django.contrib import sitemaps
from django.urls import reverse

from .models import Post

class PostSitemap(sitemaps.Sitemap):
    changefreq = 'always'
    priority = 1
    protocol = 'https'

    def items(self):
        return Post.objects.filter(status=Post.STATUS_NARMAL)

    def location(self, obj):
        return reverse('post-detail', args=[obj.id])
