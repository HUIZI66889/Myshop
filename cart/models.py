from django.db import models

from user.models import UserInfo
from goods.models import GoodsInfo
# 当多对多关系，则新建一张表，在再第三张表中维护表关系
# 用户表与商品表则将关系维护在购物车表中

# 在购物车的逻辑删除与物理删除  选择物理删除，
# 购物车中的商品不属于重要的信息，可以直接删除


class CartInfo(models.Model):

    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE, verbose_name="user")
    goods = models.ForeignKey(GoodsInfo, on_delete=models.CASCADE, verbose_name="goods")
    count = models.IntegerField(verbose_name="")  # 记录用户买个多少单位的商品

    class Meta:
        verbose_name = "cart"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.uname + 'cart'
