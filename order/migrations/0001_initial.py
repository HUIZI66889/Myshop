# Generated by Django 2.2.5 on 2019-09-17 07:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('oid', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='large_id')),
                ('odate', models.DateTimeField(auto_now=True, verbose_name='time')),
                ('oIsPay', models.BooleanField(default=False, verbose_name='pay_or_not')),
                ('ototal', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='total_price')),
                ('oaddress', models.CharField(max_length=150, verbose_name='order_address')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.UserInfo', verbose_name='order_user')),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Order',
            },
        ),
        migrations.CreateModel(
            name='OrderDetailInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='product_price')),
                ('count', models.IntegerField(verbose_name='product_number')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.GoodsInfo', verbose_name='product')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.OrderInfo', verbose_name='order')),
            ],
            options={
                'verbose_name': 'OrderInfo',
                'verbose_name_plural': 'OrderInfo',
            },
        ),
    ]
