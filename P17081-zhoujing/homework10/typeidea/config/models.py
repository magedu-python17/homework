from django.db import models
from django.contrib.auth.models import User
from django.template.loader import render_to_string

from blog.models import Post
from comment.models import Comment

# Create your models here.
class Sidebar(models.Model):
    STATUS_SHOW= 1
    STATUS_HIDE = 0
    STATUS_ITEMS = (
        (STATUS_SHOW, '显示'),
        (STATUS_HIDE, '隐藏'),
    )

    DISPLAY_HTML = 1
    DISPLAY_LATEST = 2
    DISPLAY_HOT = 3
    DISPLAY_COMMENT = 4
    SIDETYPE = (
        (DISPLAY_HTML, 'HTML'),
        (DISPLAY_LATEST, '最新文章'),
        (DISPLAY_HOT, '最热文章'),
        (DISPLAY_COMMENT, '最近评论')
    )

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, verbose_name='标题')
    status = models.PositiveIntegerField(default=STATUS_SHOW, choices=STATUS_ITEMS, verbose_name='状态')
    side_type = models.PositiveIntegerField(default=1, choices=SIDETYPE, verbose_name='展示类型')
    content = models.CharField(max_length=500, blank=True, verbose_name='内容', help_text='如果不是HTML类型则可以为空')
    user = models.ForeignKey(User, verbose_name='作者')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        db_table = 'sidebar'
        verbose_name = verbose_name_plural = '侧栏'

    @classmethod
    def get_all(cls):
        return cls.objects.filter(status=cls.STATUS_SHOW)

    @property
    def content_html(self):
        result = ''
        if self.side_type == self.DISPLAY_HTML:
            result = self.content
        elif self.side_type == self.DISPLAY_HOT:
            context = {
                'post_list':Post.get_hots()
            }
            result = render_to_string('config/blocks/sidebar_posts.html',context)
        elif self.side_type == self.DISPLAY_LATEST:
            context = {
                'post_list':Post.latest_post()
            }
            result = render_to_string('config/blocks/sidebar_posts.html', context)
        else:
            context = {
                'comments':Comment.objects.filter(status=Comment.STATUS_NARMAL).order_by('-id')
            }
            result = render_to_string('config/blocks/sidebar_comment.html', context)
        return result

class Link(models.Model):
    STATUS_NARMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NARMAL, '正常'),
        (STATUS_DELETE, '删除'),
    )

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, verbose_name='标题')
    href = models.URLField(verbose_name='链接')
    status = models.PositiveIntegerField(default=STATUS_NARMAL, choices=STATUS_ITEMS, verbose_name='状态')
    weight = models.PositiveIntegerField(default=1, choices=zip(range(1,6),range(1,6)),
                                         verbose_name='权重', help_text='权重高显示靠前')
    user = models.ForeignKey(User, verbose_name='作者')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        db_table = 'link'
        verbose_name = verbose_name_plural = '友链'


