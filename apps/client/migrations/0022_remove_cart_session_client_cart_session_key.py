# Generated by Django 5.1 on 2024-08-19 13:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0021_rename_session_cart_session_client'),
        ('sessions', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='session_client',
        ),
        migrations.AddField(
            model_name='cart',
            name='session_key',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='session_keys', to='sessions.session'),
        ),
    ]
