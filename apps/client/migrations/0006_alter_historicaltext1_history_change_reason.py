# Generated by Django 5.0.6 on 2024-06-13 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0005_text2_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicaltext1',
            name='history_change_reason',
            field=models.TextField(null=True),
        ),
    ]
