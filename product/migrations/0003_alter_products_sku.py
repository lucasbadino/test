# Generated by Django 4.0.6 on 2022-09-03 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_products_sku'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='sku',
            field=models.IntegerField(default=1017, unique=True),
        ),
    ]
