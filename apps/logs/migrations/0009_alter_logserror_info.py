# Generated by Django 5.1.1 on 2024-10-14 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logs', '0008_logsaddproduct'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logserror',
            name='info',
            field=models.CharField(blank=True, max_length=5000, null=True, verbose_name='Инфо о ошибке'),
        ),
    ]