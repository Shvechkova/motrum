# Generated by Django 5.0.7 on 2024-07-23 09:45

import datetime
import django.db.models.deletion
import simple_history.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_calendarholiday_json_date'),
        ('product', '0098_historicalstock_data_transit_and_more'),
        ('specification', '0039_alter_specification_date_stop'),
        ('supplier', '0032_alter_supplier_file'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='specification',
            name='date_stop',
            field=models.DateField(verbose_name='Дата окончания'),
        ),
        migrations.CreateModel(
            name='HistoricalProductSpecification',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, null=True, verbose_name='количество товара')),
                ('price_one', models.FloatField(verbose_name='цена одного на момент формирования')),
                ('price_all', models.FloatField(blank=True, null=True, verbose_name='цена всего товара на момент формирования')),
                ('price_exclusive', models.BooleanField(default=False, verbose_name='Цена по запросу')),
                ('history_change_reason', models.TextField(null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='product.product', verbose_name='Продукты')),
                ('product_currency', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='core.currency', verbose_name='Валюта')),
                ('specification', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='specification.specification', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'historical Спецификация продукт',
                'verbose_name_plural': 'historical Спецификации Продукты',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalSpecification',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('id_bitrix', models.PositiveIntegerField(verbose_name='номер сделки битрикс')),
                ('date', models.DateField(default=datetime.datetime.now, verbose_name='Дата добавления')),
                ('date_stop', models.DateField(verbose_name='Дата окончания')),
                ('currency_product', models.BooleanField(default=False, verbose_name='валютные товары в спецификации')),
                ('tag_stop', models.BooleanField(default=True, verbose_name='Действительно')),
                ('total_amount', models.FloatField(default=None, null=True, verbose_name='Сумма спецификации')),
                ('file', models.TextField(default=None, max_length=100, null=True, verbose_name='фаил')),
                ('history_change_reason', models.TextField(null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('admin_creator', models.ForeignKey(blank=True, db_constraint=False, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Администратор')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('wholesale', models.ForeignKey(blank=True, db_constraint=False, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='supplier.discount', verbose_name='Скидка оптовая')),
            ],
            options={
                'verbose_name': 'historical Спецификация',
                'verbose_name_plural': 'historical Спецификации',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]