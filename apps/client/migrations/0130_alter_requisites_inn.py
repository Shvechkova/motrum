# Generated by Django 5.1.2 on 2024-12-03 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0129_historicalorder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requisites',
            name='inn',
            field=models.CharField(max_length=12, verbose_name='ИНН'),
        ),
    ]