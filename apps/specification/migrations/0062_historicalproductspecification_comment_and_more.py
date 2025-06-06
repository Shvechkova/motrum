# Generated by Django 5.1.1 on 2024-10-16 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('specification', '0061_historicalproductspecification_product_new_article_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalproductspecification',
            name='comment',
            field=models.CharField(blank=True, default=None, max_length=1000, null=True, verbose_name='Комментарий'),
        ),
        migrations.AddField(
            model_name='historicalproductspecification',
            name='text_delivery',
            field=models.CharField(blank=True, default=None, max_length=1000, null=True, verbose_name='Дата поставки товара текстом для счета'),
        ),
        migrations.AddField(
            model_name='historicalspecification',
            name='comment',
            field=models.CharField(blank=True, default=None, max_length=1000, null=True, verbose_name='Комментарий'),
        ),
        migrations.AddField(
            model_name='productspecification',
            name='comment',
            field=models.CharField(blank=True, default=None, max_length=1000, null=True, verbose_name='Комментарий'),
        ),
        migrations.AddField(
            model_name='productspecification',
            name='text_delivery',
            field=models.CharField(blank=True, default=None, max_length=1000, null=True, verbose_name='Дата поставки товара текстом для счета'),
        ),
        migrations.AddField(
            model_name='specification',
            name='comment',
            field=models.CharField(blank=True, default=None, max_length=1000, null=True, verbose_name='Комментарий'),
        ),
    ]
