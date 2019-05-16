from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from typeidea.custom_site import custon_site


from .models import Category, Tag, Post
from .adminforms import PostAdminForms
from typeidea.base_admin import BaseUseradmin

# Register your models here.



class CategoryUserFilter(admin.SimpleListFilter):

    title = '分类过滤器'
    parameter_name = 'user_category'

    #先到LOOK里找 不是None 就调 queryset
    def lookups(self, request, model_admin):
        return Category.objects.filter(user=request.user).values_list('id', 'name')

    # value 是查询字符串
    def queryset(self, request, queryset):
        print(queryset)
        category_id = self.value()
        if category_id:
            return queryset.filter(category_id=self.value())
        return queryset

# 内置改变
# class PostInline(admin.StackedInline):
#     fields = ('title', 'desc')
#     extra = 1
#     model = Post



@admin.register(Category, site=custon_site)
class CategoryAdmin(BaseUseradmin):
    # inlines = [PostInline,]  内置
    list_display = ['name', 'status', 'is_nav', 'create_time','post_number']
    fields = ('name', 'status', 'is_nav')

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        return super().save_model(request, obj, form, change)

    def post_number(self,obj):
        return '共{}篇文章'.format(obj.post_set.count())
    post_number.short_description = '文章总数'




@admin.register(Tag, site=custon_site)
class TagAdmin(BaseUseradmin):
    list_display = ['name', 'status', 'create_time']
    fields = ('name', 'status')

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        return super().save_model(request, obj, form, change)


@admin.register(Post, site=custon_site)
class PostAdmin(BaseUseradmin):
    form = PostAdminForms
    list_display = [
        'title', 'category','user', 'status',
        'create_time', 'operator'
    ]
    list_display_links = []

    list_filter = [CategoryUserFilter]                     #右侧过滤器
    search_fields = ['title', 'category__name']     # 搜索框

    actions_on_top = True      # 动作 ——————【执行】
    actions_on_bottom = True

    save_on_top = True  #保存选项
    #自定义字段的展示
    exclude = ('user',)

    # fields = (
    #     ('category', 'title'),
    #     'desc',
    #     'status',
    #     'content',
    #     'tag',
    # )
    # 自定义显示格式
    fieldsets = (
        ('基础配置',{
            'description':'基础配置描述',
            'fields':(
                ('title', 'category'),
                'status',
            ),
        }),
        ('内容', {
            'fields':(
                'desc',
                'content',
            ),
        }),
        ('额外信息',{
            'classes':('collapse',),
            'fields':('tag',),
        })
    )
    # 水平显示的字段
    filter_horizontal = ('tag',)


    def operator(self, obj):
        return format_html(
            '<a href="{}">编辑</a>',
            reverse('cus_admin:blog_post_change',args=(obj.id,))
        )
    operator.short_description = '操作'

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        return super().save_model(request, obj, form, change)

    # 显示内容的处理
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(user = request.user)

    # class Media:
    #     css = {
    #         'all': ("https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css",),
    #     }
    #     js = ('https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/js/bootstrap.bundle.js',)

