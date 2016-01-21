# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aldryn_bootstrap3', '0004_auto_20151211_1333'),
    ]

    operations = [
        migrations.AddField(
            model_name='boostrap3imageplugin',
            name='use_original_image',
            field=models.BooleanField(default=False, help_text='use original image in templates instead of generated thumbnails.', verbose_name='use original image'),
        ),
    ]
