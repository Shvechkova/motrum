# Generated by Django 5.1.1 on 2024-10-22 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('specification', '0067_alter_historicalspecification_cart_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalspecification',
            name='date_delivery',
            field=models.CharField(blank=True, default=None, max_length=1000, null=True, verbose_name='Дата поставки'),
        ),
        migrations.AddField(
            model_name='specification',
            name='date_delivery',
            field=models.CharField(blank=True, default=None, max_length=1000, null=True, verbose_name='Дата поставки'),
        ),
    ]