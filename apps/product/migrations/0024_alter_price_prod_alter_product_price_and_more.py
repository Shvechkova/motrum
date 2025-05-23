# Generated by Django 5.0.6 on 2024-05-16 04:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0023_alter_productdocument_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price',
            name='prod',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='prod_price', to='product.product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.price'),
        ),
        migrations.AlterField(
            model_name='product',
            name='stock',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.stock'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='prod',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='prod_stock', to='product.product'),
        ),
    ]
