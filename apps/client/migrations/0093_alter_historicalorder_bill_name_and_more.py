# Generated by Django 5.1.2 on 2024-11-06 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0092_alter_historicalorder_bill_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalorder',
            name='bill_name',
            field=models.CharField(blank=True, default=6025, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='bill_name',
            field=models.CharField(blank=True, default=6025, max_length=1000, null=True),
        ),
    ]