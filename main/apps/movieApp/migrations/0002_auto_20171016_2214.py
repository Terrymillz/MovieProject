# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-16 22:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movieApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='watchlist',
            old_name='_type',
            new_name='media_type',
        ),
    ]
