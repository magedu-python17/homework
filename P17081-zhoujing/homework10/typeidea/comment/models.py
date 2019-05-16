from django.db import models
from django.db.models import Q

from blog.models import Post
# Create your models here.


# Create your models here.
class Comment(models.Model):
    STATUS_NARMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NARMAL, '正常'),
        (STATUS_DELETE, '删除')
    )

    id = models.AutoField(primary_key=True)
    nickname = models.CharField(max_length=50, verbose_name='昵称')
    email = models.EmailField(verbose_name='邮箱')
    website = models.URLField(verbose_name='网站')
    target = models.CharField(max_length=500, verbose_name='评论目标')
    content = models.CharField(max_length=2000, verbose_name='内容')
    status = models.PositiveIntegerField(default=STATUS_NARMAL, choices=STATUS_ITEMS, verbose_name='状态')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='评论时间')

    class Meta:
        db_table = 'comment'
        verbose_name = verbose_name_plural = '评论'

    @classmethod
    def get_by_target(cls, target):
        return cls.objects.filter(Q(target=target) & Q(status=cls.STATUS_NARMAL))
