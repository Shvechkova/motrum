# Generated by Django 5.1.5 on 2025-03-18 09:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0170_alter_historicalorder_status_alter_order_status'),
        ('core', '0043_alter_indexinfoweb_options_typedelivery_actual_and_more'),
        ('product', '0144_categoryproduct_is_send_email'),
        ('specification', '0087_alter_historicalspecification_id_bitrix_and_more'),
        ('user', '0017_remove_adminuser_bitrix_id_client'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountrequisites',
            name='requisitesKpp',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='client.requisitesotherkpp', verbose_name='Реквизиты'),
        ),
        migrations.AlterField(
            model_name='client',
            name='manager',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='user.adminuser'),
        ),
        migrations.AlterField(
            model_name='client',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='order',
            name='account_requisites',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='client.accountrequisites', verbose_name='Расчетный счет'),
        ),
        migrations.AlterField(
            model_name='order',
            name='cart',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='product.cart', verbose_name='Корзина'),
        ),
        migrations.AlterField(
            model_name='order',
            name='manager',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='user.adminuser'),
        ),
        migrations.AlterField(
            model_name='order',
            name='motrum_requisites',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.baseinfoaccountrequisites', verbose_name='Реквизиты мотрум '),
        ),
        migrations.AlterField(
            model_name='order',
            name='requisites',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='client.requisites', verbose_name='Реквизиты заказа'),
        ),
        migrations.AlterField(
            model_name='order',
            name='specification',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='specification.specification', verbose_name='Спецификация'),
        ),
        migrations.AlterField(
            model_name='order',
            name='type_delivery',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.typedelivery', verbose_name='Тип доставки '),
        ),
        migrations.AlterField(
            model_name='requisites',
            name='manager',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.adminuser', verbose_name='Менеджер в битрикс'),
        ),
        migrations.AlterField(
            model_name='requisitesaddress',
            name='requisitesKpp',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='client.requisitesotherkpp', verbose_name='Реквизиты'),
        ),
        migrations.AlterField(
            model_name='requisitesotherkpp',
            name='requisites',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='client.requisites', verbose_name='Реквизиты'),
        ),
    ]
