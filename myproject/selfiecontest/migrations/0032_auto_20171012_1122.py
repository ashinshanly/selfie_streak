# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-12 05:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('selfiecontest', '0031_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='receiver',
        ),
        migrations.RemoveField(
            model_name='message',
            name='sender',
        ),
        migrations.DeleteModel(
            name='Message',
        ),
    ]
