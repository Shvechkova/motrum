# Generated by Django 5.1 on 2024-08-21 04:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0024_alter_cart_session_key'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productcart',
            name='cart',
        ),
        migrations.RemoveField(
            model_name='productcart',
            name='product',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='ProductCart',
        ),
    ]