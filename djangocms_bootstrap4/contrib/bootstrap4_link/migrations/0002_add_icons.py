# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import djangocms_icon.fields


class Migration(migrations.Migration):

    dependencies = [
        ('bootstrap4_link', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bootstrap4link',
            name='icon_left',
            field=djangocms_icon.fields.Icon(default='', verbose_name='Icon left', blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='bootstrap4link',
            name='icon_right',
            field=djangocms_icon.fields.Icon(default='', verbose_name='Icon right', blank=True, max_length=255),
        ),
    ]
