# Generated by Django 4.0.6 on 2022-09-02 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meat', '0060_alter_products_sku'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='sku',
            field=models.IntegerField(default=1372),
        ),
    ]
