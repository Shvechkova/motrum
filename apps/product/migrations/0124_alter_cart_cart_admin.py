# Generated by Django 5.1.2 on 2024-10-28 07:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0123_cart_cart_admin'),
        ('user', '0010_adminuser_middle_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='cart_admin',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='user.adminuser', verbose_name='Администратор'),
        ),
    ]
