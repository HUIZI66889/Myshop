# Generated by Django 2.2.5 on 2019-09-17 07:15

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TypeInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isDelete', models.BooleanField(default=False)),
                ('ttitle', models.CharField(max_length=20, verbose_name='分类')),
            ],
            options={
                'verbose_name': '商品类型',
                'verbose_name_plural': '商品类型',
            },
        ),
        migrations.CreateModel(
            name='GoodsInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isDelete', models.BooleanField(default=False)),
                ('gtitle', models.CharField(max_length=20, unique=True, verbose_name='商品名称')),
                ('gpic', models.ImageField(upload_to='df_goods', verbose_name='图片路径')),
                ('gprice', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='商品价格')),
                ('gunit', models.CharField(default='个', max_length=20, verbose_name='单位')),
                ('gjianjie', models.CharField(max_length=100, verbose_name='简介')),
                ('gkucun', models.IntegerField(verbose_name='库存')),
                ('gcontent', tinymce.models.HTMLField(max_length=1000, verbose_name='详情')),
                ('gtype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.TypeInfo', verbose_name='分类')),
            ],
            options={
                'verbose_name': '商品',
                'verbose_name_plural': '商品',
            },
        ),
    ]
