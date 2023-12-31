# Generated by Django 3.2.19 on 2023-06-16 06:17

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='goodsinfo',
            options={'verbose_name': 'Products', 'verbose_name_plural': 'Products'},
        ),
        migrations.AlterModelOptions(
            name='typeinfo',
            options={'verbose_name': 'Product Type', 'verbose_name_plural': 'Product Type'},
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='gcontent',
            field=tinymce.models.HTMLField(max_length=1000, verbose_name='Details'),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='gjianjie',
            field=models.CharField(max_length=100, verbose_name='Introduction'),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='gkucun',
            field=models.IntegerField(verbose_name='Inventory'),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='gpic',
            field=models.ImageField(upload_to='df_goods', verbose_name='Image path'),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='gprice',
            field=models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Product Price'),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='gtitle',
            field=models.CharField(max_length=20, unique=True, verbose_name='Product Name'),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='gtype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.typeinfo', verbose_name='Classification'),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='gunit',
            field=models.CharField(default='Pieces', max_length=20, verbose_name='Unit'),
        ),
        migrations.AlterField(
            model_name='typeinfo',
            name='ttitle',
            field=models.CharField(max_length=20, verbose_name='Classification'),
        ),
    ]
