# Generated by Django 5.1.5 on 2025-03-07 10:29

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0142_alter_historicalproductimage_link_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalstock',
            name='data_update_motrum',
            field=models.DateField(blank=True, default=django.utils.timezone.now, editable=False, verbose_name='Дата обновления motrum'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stock',
            name='data_update_motrum',
            field=models.DateField(auto_now=True, verbose_name='Дата обновления motrum'),
        ),
    ]
