from django.db import models

from datetime import datetime

from goods.models import GoodsInfo

# Create your models here.


class UserInfo(models.Model):

    uname = models.CharField(max_length=20, verbose_name="username", unique=True)
    upwd = models.CharField(max_length=40, verbose_name="user password", blank=False)
    uemail = models.EmailField(verbose_name="email", unique=True)
    ushou = models.CharField(max_length=20, default="", verbose_name="Shipping address")
    uaddress = models.CharField(max_length=100, default="", verbose_name="address")
    uyoubian = models.CharField(max_length=6, default="", verbose_name="post code")
    uphone = models.CharField(max_length=11, default="", verbose_name="Phone number")
    # default,blank是python层面的约束，不影响数据库表结构，修改时不需要迁移 python manage.py makemigrations

    class Meta:
        verbose_name = "User Info"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.uname


class GoodsBrowser(models.Model):

    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE, verbose_name="user ID")
    good = models.ForeignKey(GoodsInfo, on_delete=models.CASCADE, verbose_name="Product ID")
    browser_time = models.DateTimeField(default=datetime.now, verbose_name="browsing time")

    class Meta:
        verbose_name = "User Browsing History"
        verbose_name_plural = verbose_name
