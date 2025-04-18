# Generated by Django 5.1.2 on 2024-12-02 09:42

import datetime
import django.db.models.deletion
import simple_history.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0128_delete_historicalorder'),
        ('core', '0027_alter_typedelivery_options_and_more'),
        ('product', '0136_alter_productimage_options'),
        ('specification', '0080_historicalproductspecification_date_delivery_bill_and_more'),
        ('user', '0012_alter_adminuser_bitrix_id'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalOrder',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('name', models.PositiveIntegerField(verbose_name='номер заказа')),
                ('id_bitrix', models.PositiveIntegerField(null=True, verbose_name='Номер сделки битрикс')),
                ('date_order', models.DateField(blank=True, default=datetime.date.today, null=True, verbose_name='Дата создания заказа')),
                ('date_completed', models.DateField(blank=True, null=True, verbose_name='Дата завершения')),
                ('date_update', models.DateField(blank=True, editable=False, verbose_name='Дата обновления')),
                ('status', models.CharField(choices=[('', '----'), ('PROCESSING', 'В обработке'), ('PAYMENT', 'Счёт на оплату'), ('IN_MOTRUM', 'Заказ у поставщика'), ('SHIPMENT_AUTO', 'На доставке '), ('SHIPMENT_PICKUP', 'Готов к отгрузке самовывозом'), ('CANCELED', 'Отменен'), ('COMPLETED', 'Заказ завершен')], default='PROCESSING', max_length=100)),
                ('prepay_persent', models.FloatField(blank=True, null=True, verbose_name='Процент предоплаты')),
                ('postpay_persent', models.FloatField(blank=True, null=True, verbose_name='Процент постоплаты')),
                ('comment', models.CharField(blank=True, default=None, max_length=1000, null=True, verbose_name='Комментарий')),
                ('bill_name', models.PositiveIntegerField(default=None, null=True, verbose_name='Номер счета')),
                ('bill_file', models.TextField(blank=True, max_length=100, null=True, verbose_name='Фаил счета')),
                ('bill_file_no_signature', models.TextField(blank=True, max_length=100, null=True, verbose_name='Фаил счета без печатей')),
                ('bill_date_start', models.DateField(blank=True, null=True, verbose_name='Дата создания счета')),
                ('bill_date_stop', models.DateField(blank=True, null=True, verbose_name='Дата окончания счета')),
                ('bill_sum', models.FloatField(blank=True, null=True, verbose_name='Сумма счета')),
                ('bill_sum_paid', models.FloatField(blank=True, default=0, null=True, verbose_name='Оплаченная сумма')),
                ('bill_tag_stop', models.BooleanField(default=True, verbose_name='Действительно')),
                ('act_file', models.TextField(default=None, max_length=100, null=True, verbose_name='Фаил акта поставки')),
                ('history_change_reason', models.TextField(null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('account_requisites', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='client.accountrequisites', verbose_name='Расчетный счет')),
                ('cart', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='product.cart', verbose_name='Корзина')),
                ('client', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='client.client', verbose_name='Клиент')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('manager', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='user.adminuser')),
                ('motrum_requisites', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='core.baseinfoaccountrequisites', verbose_name='Реквизиты мотрум ')),
                ('requisites', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='client.requisites', verbose_name='Реквизиты заказа')),
                ('specification', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='specification.specification', verbose_name='Спецификация')),
                ('type_delivery', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='core.typedelivery', verbose_name='Тип доставки ')),
            ],
            options={
                'verbose_name': 'historical Заказ',
                'verbose_name_plural': 'historical Заказы',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
