# Generated by Django 4.0.6 on 2022-08-25 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drink', '0010_alter_drinks_sku'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drinks',
            name='sku',
            field=models.IntegerField(default=101),
        ),
    ]
