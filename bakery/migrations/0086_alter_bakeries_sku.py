# Generated by Django 4.1 on 2022-09-03 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bakery', '0085_remove_bakeries_unic_alter_bakeries_sku'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bakeries',
            name='sku',
            field=models.IntegerField(default=1802),
        ),
    ]
