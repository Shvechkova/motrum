# Generated by Django 5.0.5 on 2024-05-08 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_currency_vat_delete_testmodel'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vat',
            options={'verbose_name': 'НДС', 'verbose_name_plural': 'НДС'},
        ),
        migrations.RenameField(
            model_name='vat',
            old_name='code',
            new_name='name',
        ),
    ]
