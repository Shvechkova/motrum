# Generated by Django 5.1.2 on 2024-10-29 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0073_historicalorder_comment_order_comment_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalorder',
            name='bill_name',
            field=models.CharField(blank=True, default=1066, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='bill_name',
            field=models.CharField(blank=True, default=1066, max_length=1000, null=True),
        ),
    ]
