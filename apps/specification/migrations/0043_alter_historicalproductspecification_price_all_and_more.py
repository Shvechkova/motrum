# Generated by Django 5.0.7 on 2024-07-26 08:11

import apps.specification.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('specification', '0042_remove_historicalspecification_wholesale_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalproductspecification',
            name='price_all',
            field=models.FloatField(blank=True, null=True, verbose_name='Цена всего товара на момент формирования'),
        ),
        migrations.AlterField(
            model_name='historicalproductspecification',
            name='price_one',
            field=models.FloatField(verbose_name='Цена одного на момент формирования'),
        ),
        migrations.AlterField(
            model_name='historicalspecification',
            name='currency_product',
            field=models.BooleanField(default=False, verbose_name='Валютные товары в спецификации'),
        ),
        migrations.AlterField(
            model_name='historicalspecification',
            name='file',
            field=models.TextField(default=None, max_length=100, null=True, verbose_name='Фаил'),
        ),
        migrations.AlterField(
            model_name='historicalspecification',
            name='id_bitrix',
            field=models.PositiveIntegerField(verbose_name='Номер сделки битрикс'),
        ),
        migrations.AlterField(
            model_name='productspecification',
            name='price_all',
            field=models.FloatField(blank=True, null=True, verbose_name='Цена всего товара на момент формирования'),
        ),
        migrations.AlterField(
            model_name='productspecification',
            name='price_one',
            field=models.FloatField(verbose_name='Цена одного на момент формирования'),
        ),
        migrations.AlterField(
            model_name='specification',
            name='currency_product',
            field=models.BooleanField(default=False, verbose_name='Валютные товары в спецификации'),
        ),
        migrations.AlterField(
            model_name='specification',
            name='file',
            field=models.FileField(default=None, null=True, upload_to=apps.specification.utils.get_document_path, verbose_name='Фаил'),
        ),
        migrations.AlterField(
            model_name='specification',
            name='id_bitrix',
            field=models.PositiveIntegerField(verbose_name='Номер сделки битрикс'),
        ),
    ]