# Generated by Django 5.1 on 2024-08-14 10:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0016_alter_accountrequisites_account_requisites'),
        ('user', '0009_delete_client'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='manager',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='user.adminuser'),
        ),
    ]
