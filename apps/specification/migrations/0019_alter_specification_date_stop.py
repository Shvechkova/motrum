# Generated by Django 5.0.6 on 2024-06-17 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('specification', '0018_alter_specification_date_stop'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specification',
            name='date_stop',
            field=models.DateField(default='2024-06-20', verbose_name='Дата окончания'),
        ),
    ]