from django.db import models

# Create your models here.


class WebPlate(models.Model):
    """
    网站首页分为多少个板块
    """
    class Meta:
        db_table = "webplate"
    nid = models.AutoField(primary_key=True, auto_created=True)
    title = models.CharField(max_length=48)


class User(models.Model):
    class Meta:
        db_table = "user"
    nid = models.AutoField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=48, null=False, default=None, unique=True, verbose_name="用户登录名")
    email = models.EmailField(verbose_name="邮箱", unique=True)
    pwd = models.CharField(max_length=128, verbose_name="密码")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    nickname = models.CharField(max_length=48, verbose_name="昵称", null=True)
    avatar = models.ImageField(upload_to="static/img/avatar/", null=True, verbose_name="头像")

    # 正向查找通过fans来查询用户有多少粉丝，
    # 多对多必须定义related_name以反向查找管理器对象名，用于查找用户关注的人
    fans = models.ManyToManyField(to="User",
                                  through="UserFans",
                                  through_fields=('user', 'follower'),
                                  verbose_name='粉丝们',
                                  related_name="interests")

    def __str__(self):
        return self.name


class Blog(models.Model):
    class Meta:
        db_table = "blog"
    nid = models.AutoField(primary_key=True, auto_created=True)
    user = models.OneToOneField(to="User", to_field="nid", null=True, on_delete=models.SET_NULL)
    site = models.CharField(max_length=32, unique=True, verbose_name="个人博客主页名")
    title = models.CharField(max_length=64, verbose_name="个人博客标题")
    theme = models.CharField(max_length=32, default="warm.css", verbose_name="个人博客主题")
    memo = models.CharField(max_length=255, null=True, default=None, verbose_name="座右铭")

    def __str__(self):
        return self.site


class UserFans(models.Model):
    class Meta:
        db_table = "userfans"
        unique_together = [("user", "follower")]
    nid = models.AutoField(primary_key=True, auto_created=True)
    user = models.ForeignKey(to="User", to_field="nid", related_name="users",
                             null=True, on_delete=models.SET_NULL, verbose_name="博主")
    follower = models.ForeignKey(to="User", to_field='nid', related_name="followers",
                                 null=True, on_delete=models.SET_NULL, verbose_name="粉丝")

    def __str__(self):
        return "{}<-{}".format(self.user.name, self.follower.name)


class Tag(models.Model):
    class Meta:
        db_table = "tag"
    nid = models.AutoField(primary_key=True, auto_created=True)
    title = models.CharField(max_length=32, verbose_name="文章标签")
    blog = models.ForeignKey(to="Blog", to_field="nid", null=True, on_delete=models.SET_NULL, verbose_name="所属博客")
    is_delete = models.BooleanField(verbose_name="逻辑删除", default=False)

    def delete(self, using=None, keep_parents=False):
        self.is_delete = True
        self.save()
        for a2t in self.articlem2mtag_set.all():
            a2t.delete()

    def __str__(self):
        return self.title


class Category(models.Model):
    class Meta:
        db_table = "category"
    nid = models.AutoField(primary_key=True, auto_created=True)
    title = models.CharField(max_length=32, verbose_name="文章分类")
    blog = models.ForeignKey(to="Blog", to_field="nid", null=True, on_delete=models.SET_NULL, verbose_name="所属博客")
    is_delete = models.BooleanField(verbose_name='逻辑删除', default=False)

    def delete(self, using=None, keep_parents=False):
        self.is_delete = True
        self.save()
        for a in self.article_set.all():    # TODO 是否有必要将一对多的一段置为null，可以在Article查询时添加category__is_delete
            a.category_id = None
            a.save()

    def __str__(self):
        return self.title


class Article(models.Model):
    class Meta:
        db_table = "article"
    nid = models.AutoField(primary_key=True, auto_created=True)
    blog = models.ForeignKey(to="Blog", to_field='nid', null=True, on_delete=models.SET_NULL, verbose_name="所属博客")
    title = models.CharField(max_length=128, verbose_name="文章标题")
    summary = models.CharField(max_length=255, verbose_name="文章概要")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    read_count = models.IntegerField(default=0, verbose_name="阅读次数")
    comment_count = models.IntegerField(default=0, verbose_name="评论次数")
    up_count = models.IntegerField(default=0, verbose_name="赞次数")
    down_count = models.IntegerField(default=0, verbose_name="踩次数")
    tag = models.ManyToManyField(to="Tag", through="ArticleM2MTag", through_fields=["article", "tag"])
    category = models.ForeignKey(to="Category", to_field="nid", null=True, on_delete=models.SET_NULL, verbose_name="分类")
    webplate = models.ForeignKey(to='WebPlate', to_field='nid', null=True, on_delete=models.SET_NULL,
                                 verbose_name="所属网站分类")
    is_delete = models.BooleanField(verbose_name='逻辑删除', default=False)

    def delete(self, using=None, keep_parents=False):
        self.is_delete = True
        self.save()
        self.articledetail.delete()                 # 将文章内容逻辑删除
        for a2t in self.articlem2mtag_set.all():    # 将文章标签逻辑删除
            a2t.delete()

    def __str__(self):
        return self.title


class ArticleDetail(models.Model):
    class Meta:
        db_table = "articlecontent"
    nid = models.AutoField(primary_key=True, auto_created=True)
    content = models.TextField(verbose_name="文章内容")
    article = models.OneToOneField(to="Article", to_field="nid", null=True, on_delete=models.SET_NULL,
                                   verbose_name="所属文章")
    is_delete = models.BooleanField(verbose_name="删除标记", default=False)

    def delete(self, using=None, keep_parents=False):
        self.is_delete = True
        self.save()

    def __str__(self):
        return '{}-{}的正文'.format(self.nid, self.article.title)


class ArticleM2MTag(models.Model):
    class Meta:
        db_table = "articlem2mtag"
        unique_together = (("article", "tag"),)
    nid = models.AutoField(primary_key=True, auto_created=True)
    article = models.ForeignKey(to="Article", to_field="nid", null=True, on_delete=models.SET_NULL, verbose_name="文章")
    tag = models.ForeignKey(to="Tag", to_field="nid", null=True, on_delete=models.SET_NULL, verbose_name="标签")
    is_delete = models.BooleanField(verbose_name="删除标记", default=False)

    def delete(self, using=None, keep_parents=False):
        self.is_delete = True
        self.save()

    def __str__(self):
        return "{}-{}".format(self.article.title, self.tag.title if self.tag else None)
