# Generated by Django 5.1.2 on 2024-11-27 13:18

import apps.specification.utils
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0108_orderdocumentbill'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalorder',
            name='bill_file_no_signature',
            field=models.TextField(blank=True, max_length=100, null=True, verbose_name='Фаил счета без печатей'),
        ),
        migrations.AddField(
            model_name='order',
            name='bill_file_no_signature',
            field=models.FileField(blank=True, null=True, upload_to=apps.specification.utils.get_document_bill_path, verbose_name='Фаил счета без печатей'),
        ),
        migrations.AddField(
            model_name='orderdocumentbill',
            name='bill_file_no_signature',
            field=models.FileField(blank=True, null=True, upload_to=apps.specification.utils.get_document_bill_path, verbose_name='Фаил счета без печатей'),
        ),
        migrations.CreateModel(
            name='PaymentTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True, verbose_name='Дата оплаты')),
                ('amount', models.FloatField(blank=True, null=True, verbose_name='Сумма счета')),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='client.order', verbose_name='Заказ')),
            ],
        ),
    ]