# Generated by Django 5.0.5 on 2024-05-08 06:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='adminuser',
            options={'verbose_name': 'Администратор', 'verbose_name_plural': 'Администраторы'},
        ),
    ]