# Generated by Django 5.0.6 on 2024-05-23 13:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0035_alter_productproperty_name_and_more'),
        ('supplier', '0022_supplierpastcategoryproduct_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Описание товара'),
        ),
        migrations.AlterField(
            model_name='product',
            name='vendor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='supplier.vendor', verbose_name='Производитель'),
        ),
    ]