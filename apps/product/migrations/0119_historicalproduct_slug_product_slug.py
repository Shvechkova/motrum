# Generated by Django 5.1.1 on 2024-10-01 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0118_alter_historicalstock_stock_motrum_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalproduct',
            name='slug',
            field=models.SlugField(max_length=600, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(max_length=600, null=True),
        ),
    ]
