# Generated by Django 5.0.7 on 2024-08-02 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0105_alter_historicalstock_data_update_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalstock',
            name='data_update',
            field=models.DateField(verbose_name='Дата обновления поставщика'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='data_update',
            field=models.DateField(verbose_name='Дата обновления поставщика'),
        ),
    ]
