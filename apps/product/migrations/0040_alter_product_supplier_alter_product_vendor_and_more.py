# Generated by Django 5.0.6 on 2024-05-30 13:05

import django.db.models.deletion
import smart_selects.db_fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0039_remove_productdocument_file_and_more'),
        ('supplier', '0024_delete_supplierpastcategoryproduct_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='supplier.supplier', verbose_name='Поставщик'),
        ),
        migrations.AlterField(
            model_name='product',
            name='vendor',
            field=smart_selects.db_fields.ChainedForeignKey(blank=True, chained_field='supplier', chained_model_field='supplier', null=True, on_delete=django.db.models.deletion.PROTECT, to='supplier.vendor', verbose_name='Производитель'),
        ),
        migrations.AlterField(
            model_name='productdocument',
            name='type_doc',
            field=models.CharField(choices=[('InstallationProduct', 'Руководство по монтажу и эксплуатации'), ('DimensionDrawing', 'Габаритные чертежи'), ('Passport', 'Паспорт'), ('WiringDiagram', 'Схема подключения'), ('Models3d', '3D модели'), ('Brochure', 'Брошюра'), ('Certificates', 'Сертификат'), ('Other', 'Другое')], default='Other', max_length=40, verbose_name='Тип документации'),
        ),
    ]