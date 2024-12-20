# Generated by Django 5.0.6 on 2024-05-28 05:23

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LogsError',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now, verbose_name='Дата добавления')),
                ('type_error', models.CharField(choices=[('file_structure_error', 'фаил не соответствует нужной структуре'), ('error', 'Ошибка')], default='error', max_length=20)),
            ],
            options={
                'verbose_name': 'Лог ошибок',
                'verbose_name_plural': 'Логи ошибок',
            },
        ),
    ]
