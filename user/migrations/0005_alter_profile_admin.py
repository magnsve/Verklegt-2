# Generated by Django 3.2 on 2021-05-04 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_remove_profile_super_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='admin',
            field=models.BooleanField(default=False),
        ),
    ]