# Generated by Django 5.1.2 on 2024-11-22 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0106_requisites_number_spec'),
    ]

    operations = [
        migrations.AddField(
            model_name='requisites',
            name='contract_date',
            field=models.DateField(blank=True, null=True, verbose_name='Договор дата'),
        ),
    ]
