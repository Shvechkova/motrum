# Generated by Django 5.0.6 on 2024-06-07 07:59

import django.db.models.deletion
import django.utils.timezone
import simple_history.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_currencypercent_percent'),
        ('product', '0040_alter_product_supplier_alter_product_vendor_and_more'),
        ('supplier', '0024_delete_supplierpastcategoryproduct_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='groupproduct',
            name='article_name',
        ),
        migrations.CreateModel(
            name='HistoricalPrice',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('vat_include', models.BooleanField(default=True, verbose_name='Включен ли налог в цену')),
                ('price_supplier', models.FloatField(blank=True, null=True, verbose_name='Цена в каталоге поставщика в валюте каталога')),
                ('rub_price_supplier', models.FloatField(blank=True, null=True, verbose_name='Цена в каталоге поставщика в рублях + НДС')),
                ('price_motrum', models.FloatField(blank=True, null=True, verbose_name='Цена поставщика для Motrum в рублях')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('currency', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='core.currency', verbose_name='Валюта')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('prod', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='product.product')),
                ('sale', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='supplier.discount', verbose_name='Примененная скидка')),
                ('vat', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='core.vat', verbose_name='НДС')),
            ],
            options={
                'verbose_name': 'historical Цена',
                'verbose_name_plural': 'historical Цены',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalProduct',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('article', models.PositiveIntegerField(verbose_name='Артикул мотрум')),
                ('article_supplier', models.CharField(max_length=50, verbose_name='Артикул поставщика')),
                ('additional_article_supplier', models.CharField(blank=True, max_length=50, null=True, verbose_name='Дополнительный артикул поставщика')),
                ('description', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Описание товара')),
                ('name', models.CharField(max_length=350, verbose_name='Название товара')),
                ('check_image_upgrade', models.BooleanField(default=False, verbose_name='было изменено вручную')),
                ('check_document_upgrade', models.BooleanField(default=False, verbose_name='было изменено вручную')),
                ('check_property_upgrade', models.BooleanField(default=False, verbose_name='было изменено вручную')),
                ('data_create', models.DateField(default=django.utils.timezone.now, verbose_name='Дата добавления')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('category', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='product.categoryproduct', verbose_name='Категория')),
                ('category_supplier_all', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='supplier.suppliercategoryproductall', verbose_name='Приходящая категории товара от поставщиков')),
                ('group', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='product.groupproduct', verbose_name='Группа')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('supplier', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='supplier.supplier', verbose_name='Поставщик')),
                ('vendor', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='supplier.vendor', verbose_name='Производитель')),
            ],
            options={
                'verbose_name': 'historical Товар',
                'verbose_name_plural': 'historical Товары',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalStock',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('stock_supplier', models.PositiveIntegerField(verbose_name='Остаток на складе поставщика в единицах поставщика')),
                ('lot_complect', models.PositiveIntegerField(default=1, verbose_name='Содержание набора (комплекта) в штуках')),
                ('stock_supplier_unit', models.PositiveIntegerField(verbose_name='Остаток на складе поставщика в штуках')),
                ('stock_motrum', models.PositiveIntegerField(verbose_name='Остаток на складе Motrum в штуках')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('lot', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='product.lot', verbose_name='Единица измерения поставщика')),
                ('prod', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='product.product')),
            ],
            options={
                'verbose_name': 'historical Остаток',
                'verbose_name_plural': 'historical Остатки',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]