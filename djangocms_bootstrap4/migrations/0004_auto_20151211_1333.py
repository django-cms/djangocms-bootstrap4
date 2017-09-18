# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import filer.fields.image
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aldryn_bootstrap3', '0003_auto_20151113_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boostrap3buttonplugin',
            name='link_mailto',
            field=models.EmailField(max_length=254, null=True, verbose_name='mailto', blank=True),
        ),
        migrations.AlterField(
            model_name='boostrap3imageplugin',
            name='file',
            field=filer.fields.image.FilerImageField(related_name='+', on_delete=django.db.models.deletion.SET_NULL, verbose_name='file', to='filer.Image', null=True),
        ),
        migrations.AlterField(
            model_name='boostrap3imageplugin',
            name='override_height',
            field=models.IntegerField(help_text='if this field is provided it will be used to scale image. If aspect ration is selected - height will be calculated based on that.', null=True, verbose_name='override height', blank=True),
        ),
        migrations.AlterField(
            model_name='boostrap3imageplugin',
            name='override_width',
            field=models.IntegerField(help_text='if this field is provided it will be used to scale image.', null=True, verbose_name='override width', blank=True),
        ),
        migrations.AlterField(
            model_name='bootstrap3carouselslideplugin',
            name='image',
            field=filer.fields.image.FilerImageField(related_name='+', on_delete=django.db.models.deletion.SET_NULL, verbose_name='image', to='filer.Image', null=True),
        ),
        migrations.AlterField(
            model_name='bootstrap3carouselslideplugin',
            name='link_mailto',
            field=models.EmailField(max_length=254, null=True, verbose_name='mailto', blank=True),
        ),
    ]
