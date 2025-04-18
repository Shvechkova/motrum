# Generated by Django 5.1.2 on 2024-11-08 10:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('specification', '0076_alter_historicalproductspecification_price_one_original_new_and_more'),
        ('supplier', '0036_alter_vendor_supplier'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalproductspecification',
            name='vendor',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='supplier.vendor', verbose_name='Производитель'),
        ),
        migrations.AddField(
            model_name='productspecification',
            name='vendor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='supplier.vendor', verbose_name='Производитель'),
        ),
    ]
