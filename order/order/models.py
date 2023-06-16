from django.db import models
from datetime import datetime
from goods.models import GoodsInfo
from user.models import UserInfo


class OrderInfo(models.Model):
    oid = models.CharField(max_length=20, primary_key=True, verbose_name="large_id")
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE, verbose_name="order_user")
    odate = models.DateTimeField(auto_now=True, verbose_name="time")
    oIsPay = models.BooleanField(default=False, verbose_name="pay_or_not")
    ototal = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="total_price")
    oaddress = models.CharField(max_length=150, verbose_name="order_address")

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = verbose_name

    def __str__(self):
        # return self.user.uname + "in" + str(self.odate) + "'s order'"
        return "{0}in Order{1}".format(self.user.uname, self.odate)



class OrderDetailInfo(models.Model):

    goods = models.ForeignKey(GoodsInfo, on_delete=models.CASCADE, verbose_name="product")
    order = models.ForeignKey(OrderInfo, on_delete=models.CASCADE, verbose_name="order")
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="product_price")
    count = models.IntegerField(verbose_name="product_number")

    class Meta:
        verbose_name = "OrderInfo"
        verbose_name_plural = verbose_name

    def __str__(self):
        # return self.goods.gtitle + "(number is" + str(self.count)  + ")"
        return "{0}(number is{1})".format(self.goods.gtitle, self.count)
