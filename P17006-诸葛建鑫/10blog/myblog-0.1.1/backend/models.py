from django.db import models

# Create your models here.


class Role(models.Model):
    class Meta:
        db_table = 'role'
        verbose_name_plural = "角色"
    nid = models.AutoField(primary_key=True, auto_created=True)
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title


class User2Role(models.Model):
    class Meta:
        db_table = 'user2role'
        verbose_name_plural = '用户分配角色'
    nid = models.AutoField(primary_key=True, auto_created=True)
    user = models.ForeignKey(to='web.User', to_field='nid', null=True, on_delete=models.SET_NULL, verbose_name="用户")
    role = models.ForeignKey(to='Role', to_field='nid', null=True, on_delete=models.SET_NULL, verbose_name="角色")

    def __str__(self):
        return "{}-{}".format(self.user.name, self.role.title)


class Permission(models.Model):
    class Meta:
        db_table = "permission"
        verbose_name_plural = "权限表"
    nid = models.AutoField(primary_key=True, auto_created=True)
    title = models.CharField(max_length=128, verbose_name="url名称")
    url = models.CharField(max_length=128, verbose_name="url路径")
    menu = models.ForeignKey(to="Menu", to_field='nid', null=True, on_delete=models.SET_NULL,
                             verbose_name="菜单", blank=True)

    def __str__(self):
        return "{}-{}".format(self.title, self.url)


class Action(models.Model):
    class Meta:
        db_table = "action"
        verbose_name_plural = "操作"
    nid = models.AutoField(primary_key=True, auto_created=True)
    title = models.CharField(max_length=32, verbose_name="操作名称")
    code = models.CharField(max_length=32, verbose_name="查询字符串")

    def __str__(self):
        return "{}({})".format(self.title, self.code)


class Permission2Action(models.Model):
    class Meta:
        db_table = "permission2action"
        verbose_name_plural = "权限分配操作"
    """
        权限即url，对于一个用户管理的url: http://127.0.0.1/user.html，它有4个权限：
            http://127.0.0.1/user.html?t=get        获取用户信息
            http://127.0.0.1/user.html?t=post       创建用户
            http://127.0.0.1/user.html?t=delete     删除用户
            http://127.0.0.1/user.html?t=put        修改用户
        在url表中存放http:127.0.0.1/user.html
        在action表中存放?t=get, ?t=post ...
        """
    nid = models.AutoField(primary_key=True, auto_created=True)
    p = models.ForeignKey(to="Permission", to_field='nid', null=True, on_delete=models.SET_NULL, verbose_name="权限")
    a = models.ForeignKey(to="Action", to_field='nid', null=True, on_delete=models.SET_NULL, verbose_name="操作")

    def __str__(self):
        return "{}-{}:({}?t={})".format(self.p.title, self.a.title, self.p.url, self.a.code)


class Role2Permission2Action(models.Model):
    class Meta:
        db_table = "Role2Permission2Action"
        verbose_name_plural = "角色分配(权限+操作)"
    nid = models.AutoField(primary_key=True, auto_created=True)
    p2a = models.ForeignKey(
        to="Permission2Action", to_field='nid', null=True, on_delete=models.SET_NULL, verbose_name="权限+动作")
    role = models.ForeignKey(to="Role", to_field='nid', null=True, on_delete=models.SET_NULL, verbose_name="角色")

    def __str__(self):
        return "{}: {}".format(self.role.title, self.p2a)


class Menu(models.Model):
    class Meta:
        db_table = "menu"
        verbose_name_plural = "多级菜单"
    """
        权限（url）挂载到菜单下
        根据python字典引用的特性，实现多级菜单
    """
    nid = models.AutoField(primary_key=True, auto_created=True)
    title = models.CharField(max_length=32, verbose_name="菜单名")
    parent = models.ForeignKey(to="self", to_field='nid', null=True, on_delete=models.SET_NULL, related_name="sons",
                               blank='True', verbose_name="上级菜单")

    def __str__(self):
        return "{}: (parent:{})".format(self.title, self.parent.title if self.parent else "")
