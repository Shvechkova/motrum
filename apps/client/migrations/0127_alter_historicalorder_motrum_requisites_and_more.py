# Generated by Django 5.1.2 on 2024-12-02 09:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0126_alter_historicalorder_motrum_requisites_and_more'),
        ('core', '0027_alter_typedelivery_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalorder',
            name='motrum_requisites',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='core.baseinfoaccountrequisites', verbose_name='Реквизиты мотрум '),
        ),
        migrations.AlterField(
            model_name='order',
            name='motrum_requisites',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.baseinfoaccountrequisites', verbose_name='Реквизиты мотрум '),
        ),
    ]