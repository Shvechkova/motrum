# Generated by Django 5.1.4 on 2024-12-13 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('specification', '0081_historicalproductspecification_client_shipment_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalproductspecification',
            name='product_price_catalog',
            field=models.FloatField(blank=True, null=True, verbose_name='Цена в каталоге в момент покупки'),
        ),
        migrations.AddField(
            model_name='productspecification',
            name='product_price_catalog',
            field=models.FloatField(blank=True, null=True, verbose_name='Цена в каталоге в момент покупки'),
        ),
    ]