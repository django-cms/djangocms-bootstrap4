# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-06-10 11:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bootstrap4_tabs', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bootstrap4tab',
            old_name='tab_style',
            new_name='template',
        ),
    ]
