# Generated by Django 5.1.1 on 2024-10-16 10:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0040_alter_order_cart_alter_order_specification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requisites',
            name='client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='client.client', verbose_name='Клиент'),
        ),
    ]