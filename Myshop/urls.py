from django.contrib import admin
from django.urls import path, re_path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^', include('goods.urls', namespace='df_goods')),
    re_path(r'^user/', include('user.urls', namespace='df_user')),
    re_path(r'^cart/', include('cart.urls', namespace='df_cart')),
    re_path(r'^order/', include('order.urls', namespace='df_order')),
    re_path(r'^tinymce/', include('tinymce.urls')),  # Config to use rich text editor
]
