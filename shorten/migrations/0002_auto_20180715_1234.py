# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-07-15 07:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shorten', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bitly',
            old_name='short_code',
            new_name='model_short_code',
        ),
    ]
