# Generated by Django 5.1.2 on 2024-11-07 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('specification', '0069_historicalproductspecification_sale_motrum_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalspecification',
            name='number',
            field=models.CharField(default=None, max_length=1000, null=True, verbose_name='Номер спецификации'),
        ),
        migrations.AlterField(
            model_name='specification',
            name='number',
            field=models.CharField(default=None, max_length=1000, null=True, verbose_name='Номер спецификации'),
        ),
    ]