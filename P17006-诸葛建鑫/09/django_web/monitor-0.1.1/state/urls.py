from django.urls import re_path
from .views import state_show

urlpatterns = [
    re_path('^(?P<ip>(?:\d{1,3}\.){3}\d{1,3})$', state_show),
]

