# Generated by Django 5.1 on 2024-08-13 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0014_requisites_contract'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountrequisites',
            name='bic',
            field=models.CharField(max_length=10, verbose_name='БИК'),
        ),
        migrations.AlterField(
            model_name='accountrequisites',
            name='kpp',
            field=models.CharField(max_length=10, verbose_name='КПП'),
        ),
        migrations.AlterField(
            model_name='requisites',
            name='inn',
            field=models.CharField(max_length=12, verbose_name='ИНН'),
        ),
        migrations.AlterField(
            model_name='requisites',
            name='kpp',
            field=models.CharField(max_length=10, verbose_name='КПП'),
        ),
        migrations.AlterField(
            model_name='requisites',
            name='ogrn',
            field=models.CharField(max_length=15, verbose_name='ОГРН'),
        ),
        migrations.AlterField(
            model_name='requisites',
            name='postal_post_code',
            field=models.CharField(max_length=10, verbose_name='Почтовый адрес :индекс'),
        ),
    ]