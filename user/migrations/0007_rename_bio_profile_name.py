# Generated by Django 3.2 on 2021-05-14 18:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_searchhistory'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='bio',
            new_name='name',
        ),
    ]