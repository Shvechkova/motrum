# Generated by Django 5.1.4 on 2025-01-17 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0138_productcart_product_sale_motrum'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcart',
            name='sale_client',
            field=models.FloatField(blank=True, default=None, null=True, verbose_name='Скидка клиента из парсинга фаила'),
        ),
    ]
