# Generated by Django 4.0.6 on 2022-09-02 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meat', '0031_alter_products_sku'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='sku',
            field=models.IntegerField(default=1682),
        ),
    ]
