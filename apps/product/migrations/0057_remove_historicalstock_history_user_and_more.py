# Generated by Django 5.0.6 on 2024-06-10 09:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0056_alter_historicalstock_prod_alter_stock_prod'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalstock',
            name='history_user',
        ),
        migrations.RemoveField(
            model_name='historicalstock',
            name='lot',
        ),
        migrations.RemoveField(
            model_name='historicalstock',
            name='prod',
        ),
        migrations.DeleteModel(
            name='HistoricalProduct',
        ),
        migrations.DeleteModel(
            name='HistoricalStock',
        ),
    ]
