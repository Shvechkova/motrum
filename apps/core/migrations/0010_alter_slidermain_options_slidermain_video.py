# Generated by Django 5.1 on 2024-08-13 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_slidermain'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='slidermain',
            options={'verbose_name': 'Слайдер на главной', 'verbose_name_plural': 'Слайдер на главной'},
        ),
        migrations.AddField(
            model_name='slidermain',
            name='video',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Ссылка на видео'),
        ),
    ]
