# Generated by Django 4.0.6 on 2022-09-03 02:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_alter_products_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='unic',
        ),
    ]