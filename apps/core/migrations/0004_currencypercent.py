# Generated by Django 5.0.6 on 2024-05-27 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_vat_options_rename_code_vat_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='CurrencyPercent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('percent', models.SmallIntegerField(verbose_name='Процент умножения валютных цен')),
            ],
            options={
                'verbose_name': 'Процент умножения валютных цен',
                'verbose_name_plural': 'Процент умножения валютных цен',
            },
        ),
    ]