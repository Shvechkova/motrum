# Generated by Django 5.1.5 on 2025-03-27 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0044_alter_baseinfo_counter_bill_offer'),
    ]

    operations = [
        migrations.AddField(
            model_name='slidermain',
            name='text_after_block',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Текст после текста на 2 строке'),
        ),
        migrations.AddField(
            model_name='slidermain',
            name='text_before_block',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Текст перед блоком'),
        ),
    ]
