from django.contrib.auth.models import User
from django.db.models import QuerySet
from django.db import models
from django.utils.functional import cached_property

import mistune
# Create your models here.
class Category(models.Model):
    STATUS_NARMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NARMAL,'正常'),
        (STATUS_DELETE, '删除')
    )

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=48, verbose_name='名称')
    status = models.PositiveIntegerField(default=STATUS_NARMAL, choices=STATUS_ITEMS,verbose_name='状态')
    is_nav = models.BooleanField(default=False, verbose_name='是否为导航栏')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    user = models.ForeignKey(User, verbose_name='作者')

    class Meta:
        db_table = 'category'
        verbose_name = verbose_name_plural = '分类'

    @classmethod
    def get_navs(cls):
        categories = cls.objects.filter(status=cls.STATUS_NARMAL)
        nav_categories = []
        normal_categories = []
        for cate in categories:
            nav_categories.append(cate) if cate.is_nav == True else normal_categories.append(cate)
        return {
            'navs':nav_categories,
            'normal':normal_categories
        }


    def __repr__(self):
        return self.name

    __str__ = __repr__

class Tag(models.Model):
    STATUS_NARMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NARMAL,'正常'),
        (STATUS_DELETE, '删除')
    )

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=48, verbose_name='名称')
    status = models.PositiveIntegerField(default=STATUS_NARMAL, choices=STATUS_ITEMS,verbose_name='状态')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    user = models.ForeignKey(User, verbose_name='作者')

    class Meta:
        db_table = 'tag'
        verbose_name = verbose_name_plural = '标签'

    def __repr__(self):
        return self.name

    __str__ = __repr__

class Post(models.Model):
    STATUS_NARMAL = 1
    STATUS_DELETE = 0
    STATUS_DARFT = 2
    STATUS_ITEMS = (
        (STATUS_NARMAL,'正常'),
        (STATUS_DELETE, '删除'),
        (STATUS_DARFT, '草稿')

    )

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, verbose_name='标题')
    desc = models.CharField(max_length=1024, verbose_name='摘要', blank=True)
    content = models.TextField(verbose_name='正文', help_text='正文为markdown格式')
    status = models.PositiveIntegerField(default=STATUS_NARMAL, choices=STATUS_ITEMS,verbose_name='状态')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    user = models.ForeignKey(User, verbose_name='作者')
    category = models.ForeignKey(Category, verbose_name='类别')
    tag = models.ManyToManyField(Tag, verbose_name='标签')
    pv = models.PositiveIntegerField(default=1)
    uv = models.PositiveIntegerField(default=1)
    content_html = models.TextField(verbose_name='正文html格式', blank=True, editable=False)

    class Meta:
        db_table = 'post'
        verbose_name = verbose_name_plural = '文章'
        ordering = ['-id']

    @staticmethod
    def get_by_category(category_id):
        try:
            category = Category.objects.get(pk=category_id)
        except Exception:
            category = None
            post_list = []
        else:
            post_list: QuerySet = category.post_set.filter(status=Post.STATUS_NARMAL).select_related('user', 'category')
        return category, post_list

    @staticmethod
    def get_by_tag(tag_id):
        try:
            tag = Tag.objects.get(pk=tag_id)
        except Exception:
            tag = None
            post_list = []
        else:
            post_list = tag.post_set.filter(status=Post.STATUS_NARMAL).select_related('user', 'category')

        return tag, post_list

    @staticmethod
    def latest_post():
        return Post.objects.filter(status=Post.STATUS_NARMAL)

    @classmethod
    def get_hots(cls):
        return cls.objects.filter(status=cls.STATUS_NARMAL).order_by('-pv').only('id', 'title', 'pv')

    def save(self, *args, **kwargs):
        self.content_html = mistune.markdown(self.content)
        super().save(*args, **kwargs)

    @cached_property
    def tags(self):
        return ','.join(self.tag.values_list('name', flat=True))


    def __repr__(self):
        return self.title

    __str__ = __repr__