# Generated by Django 5.1.4 on 2024-12-05 05:38

import tinymce.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects_web', '0011_alter_projectclientcategoryprojectmarking_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projecttextblock',
            name='text',
            field=tinymce.models.HTMLField(blank=True, null=True, verbose_name='Текст абзаца'),
        ),
    ]