# Generated by Django 5.1.2 on 2024-11-07 05:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0129_remove_historicalproduct_in_auto_sale_and_more'),
        ('supplier', '0036_alter_vendor_supplier'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcart',
            name='product_new_sale',
            field=models.FloatField(blank=True, default=None, null=True, verbose_name='Доп.скидка товара нового без добавления в бд'),
        ),
        migrations.AddField(
            model_name='productcart',
            name='product_new_sale_motrum',
            field=models.FloatField(blank=True, default=None, null=True, verbose_name='Скидка мотрум товара нового без добавления в бд'),
        ),
        migrations.AddField(
            model_name='productcart',
            name='product_new_vendor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='supplier.vendor', verbose_name='Производитель'),
        ),
    ]