# Generated by Django 5.0.7 on 2024-07-22 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0096_historicalprice_data_update_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalproduct',
            name='check_to_order',
            field=models.BooleanField(default=True, verbose_name='Доступность к заказу'),
        ),
        migrations.AddField(
            model_name='product',
            name='check_to_order',
            field=models.BooleanField(default=True, verbose_name='Доступность к заказу'),
        ),
    ]
