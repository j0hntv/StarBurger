# Generated by Django 3.2 on 2021-10-22 19:04

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('foodcartapp', '0037_auto_20210125_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='contact_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None, verbose_name='контактный телефон'),
        ),
    ]