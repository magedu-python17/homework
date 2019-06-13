from django.contrib import admin

# Register your models here.
from . import models
admin.site.register(models.Role)
admin.site.register(models.User2Role)
admin.site.register(models.Permission)
admin.site.register(models.Action)
admin.site.register(models.Permission2Action)
admin.site.register(models.Role2Permission2Action)
admin.site.register(models.Menu)














