# Generated by Django 5.1.1 on 2024-10-22 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0051_requisites_tel_alter_order_bill_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='postpay_persent',
            field=models.FloatField(blank=True, null=True, verbose_name='Процент постоплаты'),
        ),
        migrations.AddField(
            model_name='order',
            name='prepay_persent',
            field=models.FloatField(blank=True, null=True, verbose_name='Процент предоплаты'),
        ),
        migrations.AlterField(
            model_name='order',
            name='bill_name',
            field=models.CharField(blank=True, default=9924, max_length=1000, null=True),
        ),
    ]