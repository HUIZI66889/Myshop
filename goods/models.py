from django.db import models
from tinymce.models import HTMLField  # 使用富文本编辑框要在settings文件中安装
# 将一对多的关系维护在GoodsInfo中维护，另外商品信息与分类信息都属于重要信息需要使用逻辑删除


class TypeInfo(models.Model):
    # 商品分类信息
    isDelete = models.BooleanField(default=False)
    ttitle = models.CharField(max_length=20, verbose_name="Classification")

    class Meta:
        verbose_name = "Product Type"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.ttitle


class GoodsInfo(models.Model):
    # 具体商品信息
    isDelete = models.BooleanField(default=False)  # 逻辑删除
    gtitle = models.CharField(max_length=20, verbose_name="Product Name", unique=True)
    gpic = models.ImageField(upload_to='df_goods', verbose_name="Image path")
    gprice = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Product Price")  # 商品价格小数位为两位，整数位为3位
    gunit = models.CharField(max_length=20, default='Pieces', verbose_name="Unit")
    # gclick = models.IntegerField(verbose_name="Clicks")
    gjianjie = models.CharField(max_length=100, verbose_name="Introduction")
    gkucun = models.IntegerField(verbose_name="Inventory")
    gcontent = HTMLField(max_length=1000, verbose_name="Details")
    gtype = models.ForeignKey(TypeInfo, on_delete=models.CASCADE, verbose_name="Classification")  # 外键关联TypeInfo表
    # gadv = models.BooleanField(default=False) #商品是否推荐

    class Meta:
        verbose_name = "Products"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.gtitle