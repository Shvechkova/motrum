# Generated by Django 5.1.2 on 2024-12-02 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_adminuser_bitrix_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminuser',
            name='bitrix_id',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Номер менеджера битрикс'),
        ),
    ]