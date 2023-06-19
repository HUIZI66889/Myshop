from django.urls import re_path

from .views import *

app_name = 'df_goods'

urlpatterns = [
    re_path('^$', index, name="index"),
    re_path('^list(\d+)_(\d+)_(\d+)/$', good_list, name="good_list"),
    re_path('^(\d+)/detail$', detail, name="detail"),
    re_path('^(\d+)/comment$', comment, name="comment"),
    re_path(r'^search/', ordinary_search, name="ordinary_search"),  # Global search
]
