# Generated by Django 5.1.2 on 2024-12-02 09:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0122_alter_historicalorder_motrum_requisites_and_more'),
        ('core', '0027_alter_typedelivery_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalorder',
            name='motrum_requisites123',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='core.baseinfo', verbose_name='Реквизиты мотрум '),
        ),
        migrations.AddField(
            model_name='order',
            name='motrum_requisites123',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.baseinfo', verbose_name='Реквизиты мотрум '),
        ),
    ]
