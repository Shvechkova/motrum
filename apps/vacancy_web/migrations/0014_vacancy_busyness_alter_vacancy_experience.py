# Generated by Django 5.1.5 on 2025-04-16 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancy_web', '0013_alter_vacancy_type_payments'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancy',
            name='busyness',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Занятость'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='experience',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Опыт'),
        ),
    ]
