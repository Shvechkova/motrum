# Generated by Django 5.0.6 on 2024-06-19 05:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0076_alter_historicalproduct_article_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalproduct',
            name='category',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='product.categoryproduct', verbose_name='Категория Мотрум'),
        ),
        migrations.AlterField(
            model_name='historicalproduct',
            name='group',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='product.groupproduct', verbose_name='Группа Мотрум'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='product.categoryproduct', verbose_name='Категория Мотрум'),
        ),
        migrations.AlterField(
            model_name='product',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='product.groupproduct', verbose_name='Группа Мотрум'),
        ),
    ]
