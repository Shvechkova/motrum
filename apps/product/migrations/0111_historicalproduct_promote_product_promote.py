# Generated by Django 5.1 on 2024-08-13 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0110_categoryproduct_article_home_web'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalproduct',
            name='promote',
            field=models.BooleanField(default=False, verbose_name='Продвижение на главной в слайдере'),
        ),
        migrations.AddField(
            model_name='product',
            name='promote',
            field=models.BooleanField(default=False, verbose_name='Продвижение на главной в слайдере'),
        ),
    ]