# Generated by Django 4.1 on 2022-08-27 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_profile_image_alter_user_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_profile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='profile_image/'),
        ),
    ]