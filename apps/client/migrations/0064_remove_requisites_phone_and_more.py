# Generated by Django 5.1.2 on 2024-10-24 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0063_alter_historicalorder_bill_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='requisites',
            name='phone',
        ),
        migrations.AlterField(
            model_name='historicalorder',
            name='bill_name',
            field=models.CharField(blank=True, default=616, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='bill_name',
            field=models.CharField(blank=True, default=616, max_length=1000, null=True),
        ),
    ]
