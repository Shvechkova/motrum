# Generated by Django 5.1.2 on 2024-11-06 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0127_historicalproduct_add_in_nomenclature_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalprice',
            name='in_auto_sale',
            field=models.BooleanField(default=True, verbose_name='Разрешить применять скидки автоматически'),
        ),
        migrations.AddField(
            model_name='historicalproduct',
            name='in_auto_sale',
            field=models.BooleanField(default=False, verbose_name='Разрешить применять скидки автоматичсеки'),
        ),
        migrations.AddField(
            model_name='price',
            name='in_auto_sale',
            field=models.BooleanField(default=True, verbose_name='Разрешить применять скидки автоматически'),
        ),
        migrations.AddField(
            model_name='product',
            name='in_auto_sale',
            field=models.BooleanField(default=False, verbose_name='Разрешить применять скидки автоматичсеки'),
        ),
    ]