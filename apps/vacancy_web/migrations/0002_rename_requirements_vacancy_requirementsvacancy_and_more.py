# Generated by Django 5.1 on 2024-08-14 07:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vacancy_web', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Requirements_vacancy',
            new_name='RequirementsVacancy',
        ),
        migrations.RenameModel(
            old_name='Working_conditions',
            new_name='WorkingConditions',
        ),
    ]
