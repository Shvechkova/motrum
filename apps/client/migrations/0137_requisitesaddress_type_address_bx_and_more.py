# Generated by Django 5.1.4 on 2024-12-25 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0136_requisitesaddress'),
    ]

    operations = [
        migrations.AddField(
            model_name='requisitesaddress',
            name='type_address_bx',
            field=models.CharField(choices=[(1, 'Фактический адрес'), (4, 'Адрес регистрации'), (6, 'Юридический адрес'), (9, 'Адрес бенефициара')], default=4, max_length=100),
        ),
        migrations.AlterField(
            model_name='requisitesaddress',
            name='city',
            field=models.CharField(max_length=150, verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='requisitesaddress',
            name='country',
            field=models.CharField(max_length=100, verbose_name='Страна'),
        ),
        migrations.AlterField(
            model_name='requisitesaddress',
            name='province',
            field=models.CharField(max_length=150, verbose_name='Область'),
        ),
        migrations.AlterField(
            model_name='requisitesaddress',
            name='region',
            field=models.CharField(max_length=150, verbose_name='Регион'),
        ),
    ]
