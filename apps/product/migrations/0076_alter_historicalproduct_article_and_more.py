# Generated by Django 5.0.6 on 2024-06-17 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0075_alter_historicalproduct_article_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalproduct',
            name='article',
            field=models.CharField(max_length=50, verbose_name='Артикул мотрум'),
        ),
        migrations.AlterField(
            model_name='product',
            name='article',
            field=models.CharField(max_length=50, verbose_name='Артикул мотрум'),
        ),
    ]