# Generated by Django 5.0.7 on 2024-08-06 13:29

import apps.core.utils_web
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0108_groupproduct_image_alter_categoryproduct_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoryproduct',
            name='is_view_home_web',
            field=models.BooleanField(default=False, verbose_name='Отображение на главной сайта'),
        ),
        migrations.AlterField(
            model_name='groupproduct',
            name='image',
            field=models.ImageField(null=True, upload_to=apps.core.utils_web.get_file_path_catalog_web, verbose_name='Изображение категории'),
        ),
    ]