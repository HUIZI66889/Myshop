from django.conf.urls import url

from .views import *

app_name = 'df_goods'

urlpatterns = [
    url('^$', index, name="index"),
    url('^list(\d+)_(\d+)_(\d+)/$', good_list, name="good_list"),
    url('^(\d+)/detail$', detail, name="detail"),
    url('^(\d+)/comment$', comment, name="comment"),
    url(r'^search/', ordinary_search, name="ordinary_search"),  # 全文检索
]
