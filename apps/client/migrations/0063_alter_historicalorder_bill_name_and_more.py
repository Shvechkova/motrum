# Generated by Django 5.1.2 on 2024-10-24 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0062_alter_order_bill_name_historicalorder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalorder',
            name='bill_name',
            field=models.CharField(blank=True, default=2068, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='bill_name',
            field=models.CharField(blank=True, default=2068, max_length=1000, null=True),
        ),
    ]
