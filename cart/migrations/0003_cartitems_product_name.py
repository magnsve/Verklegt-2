# Generated by Django 3.2 on 2021-05-12 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_auto_20210511_1937'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitems',
            name='product_name',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
