# Generated by Django 5.1.5 on 2025-02-14 12:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0151_phoneclient'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientRequisites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.client')),
                ('requisitesotherkpp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.requisitesotherkpp', verbose_name='')),
            ],
        ),
    ]
