# Generated by Django 5.1.5 on 2025-01-31 08:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0140_productcart_tag_auto_document'),
        ('supplier', '0042_remove_vendor_supplier'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcart',
            name='supplier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='supplier.supplier', verbose_name='Поставщик'),
        ),
    ]
