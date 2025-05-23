# Generated by Django 5.0.7 on 2024-07-22 08:16

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0095_alter_categoryproduct_slug_alter_groupproduct_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalprice',
            name='data_update',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Дата обновления'),
        ),
        migrations.AddField(
            model_name='historicalproduct',
            name='data_update',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Дата обновления'),
        ),
        migrations.AddField(
            model_name='historicalstock',
            name='data_update',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Дата обновления'),
        ),
        migrations.AddField(
            model_name='price',
            name='data_update',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Дата обновления'),
        ),
        migrations.AddField(
            model_name='product',
            name='data_update',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Дата обновления'),
        ),
        migrations.AddField(
            model_name='stock',
            name='data_update',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Дата обновления'),
        ),
    ]
