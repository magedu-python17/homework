from django.contrib import admin
from django.contrib.admin.models import LogEntry

from .models import Sidebar, Link
from typeidea.custom_site import custon_site
from typeidea.base_admin import BaseUseradmin

# Register your models here.


@admin.register(Sidebar, site=custon_site)
class SidebarAdmin(BaseUseradmin):
    list_display = ['title', 'side_type', 'content','status', 'create_time']
    fields = ['title', 'side_type', 'status', 'content']

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        return super().save_model(request, obj, form, change)

@admin.register(Link, site=custon_site)
class LinkAdmin(BaseUseradmin):
    list_display = ['title', 'href', 'status', 'weight', 'create_time']
    fields = ['title', 'href', 'status', 'weight']

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        return  super().save_model(request, obj, form, change)

@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    list_display = ['object_repr', 'object_id', 'action_flag', 'user', 'change_message']



