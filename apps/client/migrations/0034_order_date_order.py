# Generated by Django 5.1.1 on 2024-09-16 07:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0033_alter_order_bill_date_start_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='date_order',
            field=models.DateField(blank=True, default=datetime.date.today, null=True, verbose_name='Дата создания заказа'),
        ),
    ]
