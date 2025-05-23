# Generated by Django 5.0.6 on 2024-05-15 13:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_vat_options_rename_code_vat_name'),
        ('product', '0021_alter_price_price_motrum_alter_price_price_supplier_and_more'),
        ('supplier', '0014_alter_discount_category_catalog'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='price',
            options={'verbose_name': 'Цена', 'verbose_name_plural': 'Цены'},
        ),
        migrations.AlterModelOptions(
            name='productproperty',
            options={'verbose_name': 'Характеристика \\свойства', 'verbose_name_plural': 'Характеристики\\свойства'},
        ),
        migrations.AlterModelOptions(
            name='stock',
            options={'verbose_name': 'Остаток', 'verbose_name_plural': 'Остатки'},
        ),
        migrations.AddField(
            model_name='price',
            name='prod',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='prod_price', to='product.product'),
        ),
        migrations.AddField(
            model_name='stock',
            name='prod',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='prod_stock', to='product.product'),
        ),
        migrations.AlterField(
            model_name='price',
            name='currency',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.currency', verbose_name='Валюта'),
        ),
        migrations.AlterField(
            model_name='price',
            name='vat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.vat', verbose_name='НДС'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='product.categoryproduct', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='product',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='product.groupproduct', verbose_name='Группа'),
        ),
        migrations.AlterField(
            model_name='product',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='products', to='supplier.supplier', verbose_name='Поставщик'),
        ),
        migrations.AlterField(
            model_name='product',
            name='vendor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='supplier.vendor', verbose_name='Производитель'),
        ),
        migrations.AlterField(
            model_name='productdocument',
            name='link',
            field=models.CharField(max_length=100, null=True, verbose_name='ссылка у поставщика'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='lot',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.lot', verbose_name='Единица измерения поставщика'),
        ),
    ]
