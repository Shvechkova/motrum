# Generated by Django 5.1.2 on 2024-10-25 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0065_alter_historicalorder_bill_file_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalorder',
            name='bill_name',
            field=models.CharField(blank=True, default=1566, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='bill_name',
            field=models.CharField(blank=True, default=1566, max_length=1000, null=True),
        ),
    ]