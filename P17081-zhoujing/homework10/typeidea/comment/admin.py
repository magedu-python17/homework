from django.contrib import admin

from .models import Comment
from typeidea.custom_site import custon_site

# Register your models here.

@admin.register(Comment, site=custon_site)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['target', 'nickname', 'content', 'website', 'email', 'create_time']
