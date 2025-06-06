# Generated by Django 5.1.2 on 2024-11-12 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0100_historicalorder_bill_name_order_bill_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalorder',
            name='bill_name',
            field=models.PositiveIntegerField(default=None, null=True, verbose_name='Номер счета'),
        ),
        migrations.AlterField(
            model_name='order',
            name='bill_name',
            field=models.PositiveIntegerField(default=None, null=True, verbose_name='Номер счета'),
        ),
    ]
