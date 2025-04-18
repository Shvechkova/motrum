# Generated by Django 5.1.5 on 2025-02-25 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancy_web', '0005_alter_vacancyprice_vacancy'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vacancycategory',
            options={'verbose_name': 'Категория вакансий', 'verbose_name_plural': 'категории вакансий'},
        ),
        migrations.AddField(
            model_name='vacancycategory',
            name='article',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Очередность'),
        ),
    ]
