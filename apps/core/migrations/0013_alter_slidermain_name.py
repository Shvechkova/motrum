# Generated by Django 5.1 on 2024-08-13 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_slidermain_link_slidermain_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slidermain',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Название слайда для админки'),
        ),
    ]
