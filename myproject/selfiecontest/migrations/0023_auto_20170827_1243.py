# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-27 07:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selfiecontest', '0022_auto_20170818_2355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picto',
            name='image',
            field=models.FileField(upload_to='media/'),
        ),
    ]
