# Generated by Django 5.1 on 2024-09-11 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('specification', '0057_historicalproductspecification_product_new_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalproductspecification',
            name='date_delivery',
            field=models.DateField(null=True, verbose_name='Дата поставки товара'),
        ),
        migrations.AlterField(
            model_name='productspecification',
            name='date_delivery',
            field=models.DateField(null=True, verbose_name='Дата поставки товара'),
        ),
    ]
