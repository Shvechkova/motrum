# Generated by Django 5.1.5 on 2025-02-25 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancy_web', '0008_remove_vacancyprice_type_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancy',
            name='first',
            field=models.FloatField(blank=True, null=True, verbose_name='от'),
        ),
        migrations.AddField(
            model_name='vacancy',
            name='fixed',
            field=models.FloatField(blank=True, null=True, verbose_name='фиксированная сумма'),
        ),
        migrations.AddField(
            model_name='vacancy',
            name='last',
            field=models.FloatField(blank=True, null=True, verbose_name='до'),
        ),
        migrations.AddField(
            model_name='vacancy',
            name='type_payments',
            field=models.CharField(default=0, max_length=500, verbose_name='Условия выплат'),
            preserve_default=False,
        ),
    ]
