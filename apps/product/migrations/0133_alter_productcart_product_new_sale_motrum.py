# Generated by Django 5.1.2 on 2024-11-11 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0132_alter_productcart_product_new_sale_motrum'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcart',
            name='product_new_sale_motrum',
            field=models.FloatField(blank=True, default=None, null=True, verbose_name='Скидка мотрум товара нового без добавления в бд'),
        ),
    ]