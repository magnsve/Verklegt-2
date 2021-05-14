# Generated by Django 3.2 on 2021-05-13 19:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_auto_20210513_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartaddress',
            name='city',
            field=models.CharField(default='borg', max_length=255),
        ),
        migrations.AlterField(
            model_name='cartaddress',
            name='country',
            field=models.ForeignKey(default='land', on_delete=django.db.models.deletion.CASCADE, to='cart.country'),
        ),
        migrations.AlterField(
            model_name='cartaddress',
            name='full_name',
            field=models.CharField(default='nafn', max_length=255),
        ),
        migrations.AlterField(
            model_name='cartaddress',
            name='house_number',
            field=models.CharField(default='húsnúmer', max_length=255),
        ),
        migrations.AlterField(
            model_name='cartaddress',
            name='postal_code',
            field=models.CharField(default='póstnúmer', max_length=255),
        ),
        migrations.AlterField(
            model_name='cartaddress',
            name='street_name',
            field=models.CharField(default='götunafn', max_length=255),
        ),
    ]
