# Generated by Django 5.0.7 on 2024-08-07 05:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('specification', '0044_alter_historicalspecification_admin_creator'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalspecification',
            name='date_update',
            field=models.DateField(blank=True, default=datetime.datetime.now, editable=False, verbose_name='Дата обновления'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='specification',
            name='date_update',
            field=models.DateField(auto_now=True, verbose_name='Дата обновления'),
        ),
    ]