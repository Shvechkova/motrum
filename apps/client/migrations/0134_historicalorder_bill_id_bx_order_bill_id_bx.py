# Generated by Django 5.1.4 on 2024-12-19 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0133_alter_documentshipment_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalorder',
            name='bill_id_bx',
            field=models.PositiveIntegerField(default=None, null=True, verbose_name='Номер id счета bitrix'),
        ),
        migrations.AddField(
            model_name='order',
            name='bill_id_bx',
            field=models.PositiveIntegerField(default=None, null=True, verbose_name='Номер id счета bitrix'),
        ),
    ]