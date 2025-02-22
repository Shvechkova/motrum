# Generated by Django 5.0.7 on 2024-07-26 08:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0101_historicalproduct_data_update_product_data_update'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='historicalproductproperty',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical Характеристика\\свойства', 'verbose_name_plural': 'historical Характеристики\\свойства'},
        ),
        migrations.AlterModelOptions(
            name='productproperty',
            options={'verbose_name': 'Характеристика\\свойства', 'verbose_name_plural': 'Характеристики\\свойства'},
        ),
        migrations.AlterField(
            model_name='currencyrate',
            name='value',
            field=models.FloatField(blank=True, null=True, verbose_name='Курс ЦБ'),
        ),
        migrations.AlterField(
            model_name='currencyrate',
            name='vunit_rate',
            field=models.FloatField(blank=True, null=True, verbose_name='Курс ЦБ за единицу'),
        ),
        migrations.AlterField(
            model_name='groupproduct',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.categoryproduct', verbose_name='Категория Мотрум'),
        ),
        migrations.AlterField(
            model_name='historicalprice',
            name='price_supplier',
            field=models.FloatField(default=0, null=True, verbose_name='Цена в каталоге поставщика в валюте каталога'),
        ),
        migrations.AlterField(
            model_name='historicalprice',
            name='prod',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='product.product', verbose_name='Продукт'),
        ),
        migrations.AlterField(
            model_name='historicalproduct',
            name='autosave_tag',
            field=models.BooleanField(default=True, verbose_name='Автоматическая загрузка'),
        ),
        migrations.AlterField(
            model_name='historicalproductdocument',
            name='hide',
            field=models.BooleanField(default=False, verbose_name='Скрыть'),
        ),
        migrations.AlterField(
            model_name='historicalproductdocument',
            name='link',
            field=models.CharField(max_length=255, null=True, verbose_name='Ссылка у поставщика'),
        ),
        migrations.AlterField(
            model_name='historicalproductimage',
            name='hide',
            field=models.BooleanField(default=False, verbose_name='Скрыть'),
        ),
        migrations.AlterField(
            model_name='historicalproductimage',
            name='link',
            field=models.CharField(max_length=150, verbose_name='Ссылка у поставщика'),
        ),
        migrations.AlterField(
            model_name='historicalproductproperty',
            name='name',
            field=models.CharField(max_length=600, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='historicalproductproperty',
            name='unit_measure',
            field=models.CharField(max_length=600, null=True, verbose_name='Короткое имя значения'),
        ),
        migrations.AlterField(
            model_name='historicalproductproperty',
            name='value',
            field=models.CharField(max_length=600, verbose_name='Значение'),
        ),
        migrations.AlterField(
            model_name='lot',
            name='slug',
            field=models.SlugField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='price',
            name='price_supplier',
            field=models.FloatField(default=0, null=True, verbose_name='Цена в каталоге поставщика в валюте каталога'),
        ),
        migrations.AlterField(
            model_name='price',
            name='prod',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='price', to='product.product', verbose_name='Продукт'),
        ),
        migrations.AlterField(
            model_name='product',
            name='autosave_tag',
            field=models.BooleanField(default=True, verbose_name='Автоматическая загрузка'),
        ),
        migrations.AlterField(
            model_name='productdocument',
            name='hide',
            field=models.BooleanField(default=False, verbose_name='Скрыть'),
        ),
        migrations.AlterField(
            model_name='productdocument',
            name='link',
            field=models.CharField(max_length=255, null=True, verbose_name='Ссылка у поставщика'),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='hide',
            field=models.BooleanField(default=False, verbose_name='Скрыть'),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='link',
            field=models.CharField(max_length=150, verbose_name='Ссылка у поставщика'),
        ),
        migrations.AlterField(
            model_name='productproperty',
            name='name',
            field=models.CharField(max_length=600, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='productproperty',
            name='unit_measure',
            field=models.CharField(max_length=600, null=True, verbose_name='Короткое имя значения'),
        ),
        migrations.AlterField(
            model_name='productproperty',
            name='value',
            field=models.CharField(max_length=600, verbose_name='Значение'),
        ),
    ]
