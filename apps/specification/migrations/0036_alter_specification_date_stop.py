# Generated by Django 5.0.7 on 2024-07-18 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('specification', '0035_alter_specification_date_stop'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specification',
            name='date_stop',
            field=models.DateField(default='2024-07-21', verbose_name='Дата окончания'),
        ),
    ]
