# Generated by Django 5.0.6 on 2024-05-13 13:47

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_alter_lot_options_lot_name_shorts_lot_slug_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lot',
            options={'verbose_name': 'Единица измерения поставщика', 'verbose_name_plural': 'Единицы измерений поставщиков'},
        ),
        migrations.AddField(
            model_name='product',
            name='data_create',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Дата добавления'),
        ),
    ]
