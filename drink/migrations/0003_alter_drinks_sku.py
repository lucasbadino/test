# Generated by Django 4.1 on 2022-08-20 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drink', '0002_alter_drinks_sku'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drinks',
            name='sku',
            field=models.IntegerField(default=1292),
        ),
    ]
