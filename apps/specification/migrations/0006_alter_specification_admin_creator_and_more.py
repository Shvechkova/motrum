# Generated by Django 5.0.6 on 2024-05-30 13:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('specification', '0005_alter_specification_currency_product_and_more'),
        ('user', '0002_alter_adminuser_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specification',
            name='admin_creator',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='user.adminuser'),
        ),
        migrations.AlterField(
            model_name='specification',
            name='file',
            field=models.CharField(default=None, max_length=40, null=True, verbose_name='фаил в системе'),
        ),
        migrations.AlterField(
            model_name='specification',
            name='total_amount',
            field=models.IntegerField(default=None, null=True, verbose_name='процент скидки'),
        ),
    ]