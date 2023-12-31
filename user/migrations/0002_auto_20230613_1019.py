# Generated by Django 3.0 on 2023-06-13 02:19

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='goodsbrowser',
            options={'verbose_name': 'User Browsing History', 'verbose_name_plural': 'User Browsing History'},
        ),
        migrations.AlterModelOptions(
            name='userinfo',
            options={'verbose_name': 'User Info', 'verbose_name_plural': 'User Info'},
        ),
        migrations.AlterField(
            model_name='goodsbrowser',
            name='browser_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='browsing time'),
        ),
        migrations.AlterField(
            model_name='goodsbrowser',
            name='good',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.GoodsInfo', verbose_name='Product ID'),
        ),
        migrations.AlterField(
            model_name='goodsbrowser',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.UserInfo', verbose_name='user ID'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='uaddress',
            field=models.CharField(default='', max_length=100, verbose_name='address'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='uemail',
            field=models.EmailField(max_length=254, unique=True, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='uname',
            field=models.CharField(max_length=20, unique=True, verbose_name='username'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='uphone',
            field=models.CharField(default='', max_length=11, verbose_name='Phone number'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='upwd',
            field=models.CharField(max_length=40, verbose_name='user password'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='ushou',
            field=models.CharField(default='', max_length=20, verbose_name='Shipping address'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='uyoubian',
            field=models.CharField(default='', max_length=6, verbose_name='post code'),
        ),
    ]
