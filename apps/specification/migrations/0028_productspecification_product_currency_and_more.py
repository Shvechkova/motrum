# Generated by Django 5.0.6 on 2024-07-05 06:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_currencypercent_percent'),
        ('specification', '0027_alter_specification_date_stop'),
    ]

    operations = [
        migrations.AddField(
            model_name='productspecification',
            name='product_currency',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.currency', verbose_name='Валюта'),
        ),
        migrations.AlterField(
            model_name='specification',
            name='date_stop',
            field=models.DateField(default='2024-07-08', verbose_name='Дата окончания'),
        ),
    ]