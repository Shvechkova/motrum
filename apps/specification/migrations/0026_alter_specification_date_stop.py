# Generated by Django 5.0.6 on 2024-07-03 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('specification', '0025_alter_specification_date_stop'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specification',
            name='date_stop',
            field=models.DateField(default='2024-07-06', verbose_name='Дата окончания'),
        ),
    ]
