# Generated by Django 5.0.6 on 2024-05-15 13:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0022_alter_price_options_alter_productproperty_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productdocument',
            options={'verbose_name': 'Документация', 'verbose_name_plural': 'Документации'},
        ),
        migrations.AlterModelOptions(
            name='productimage',
            options={'verbose_name': 'Изображение', 'verbose_name_plural': 'Изображения'},
        ),
    ]