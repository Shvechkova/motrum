# Generated by Django 5.0.6 on 2024-05-30 05:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_currencypercent_percent'),
        ('specification', '0003_alter_specification_date_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productspecification',
            options={'verbose_name': 'Спецификация продукт', 'verbose_name_plural': 'Спецификации Продукты'},
        ),
        migrations.AddField(
            model_name='specification',
            name='tag_currency',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.currency'),
        ),
        migrations.AlterField(
            model_name='specification',
            name='date_stop',
            field=models.DateField(default='2024-05-27', verbose_name='Дата окончания'),
        ),
        migrations.AlterField(
            model_name='specification',
            name='tag_stop',
            field=models.BinaryField(default=False, verbose_name='недействительно'),
        ),
    ]
