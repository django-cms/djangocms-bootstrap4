# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import aldryn_bootstrap3.model_fields


class Migration(migrations.Migration):

    dependencies = [
        ('aldryn_bootstrap3', '0002_bootstrap3fileplugin'),
    ]

    operations = [
        migrations.AddField(
            model_name='boostrap3imageplugin',
            name='override_height',
            field=models.IntegerField(help_text='if this field is provided - it would be used across all devices instead of default for devices types. If aspect ration is selected - height will be calculated based on that.', null=True, verbose_name='override height', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='boostrap3imageplugin',
            name='override_width',
            field=models.IntegerField(help_text='if this field is provided - it would be used across all devices instead of default for devices types.', null=True, verbose_name='override width', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='boostrap3buttonplugin',
            name='btn_context',
            field=aldryn_bootstrap3.model_fields.Context(default='default', max_length=255, verbose_name='context', choices=[('default', 'Default'), ('primary', 'Primary'), ('success', 'Success'), ('info', 'Info'), ('warning', 'Warning'), ('danger', 'Danger'), ('link', 'Link')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='boostrap3buttonplugin',
            name='link_mailto',
            field=models.EmailField(max_length=75, null=True, verbose_name='email address', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='boostrap3buttonplugin',
            name='txt_context',
            field=aldryn_bootstrap3.model_fields.Context(default='', max_length=255, verbose_name='context', blank=True, choices=[('', 'Default'), ('primary', 'Primary'), ('success', 'Success'), ('info', 'Info'), ('warning', 'Warning'), ('danger', 'Danger'), ('muted ', 'Muted')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='boostrap3imageplugin',
            name='aspect_ratio',
            field=models.CharField(default='', max_length=10, verbose_name='aspect ratio', blank=True, choices=[('1x1', '1x1'), ('4x3', '4x3'), ('16x9', '16x9'), ('16x10', '16x10'), ('21x9', '21x9'), ('3x4', '3x4'), ('9x16', '9x16'), ('10x16', '10x16'), ('9x21', '9x21')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bootstrap3carouselplugin',
            name='aspect_ratio',
            field=models.CharField(default='', max_length=10, verbose_name='aspect ratio', blank=True, choices=[('1x1', '1x1'), ('4x3', '4x3'), ('16x9', '16x9'), ('16x10', '16x10'), ('21x9', '21x9'), ('3x4', '3x4'), ('9x16', '9x16'), ('10x16', '10x16'), ('9x21', '9x21')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bootstrap3carouselslideplugin',
            name='link_mailto',
            field=models.EmailField(max_length=75, null=True, verbose_name='email address', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bootstrap3listgroupitemplugin',
            name='context',
            field=aldryn_bootstrap3.model_fields.Context(default='', max_length=255, blank=True, choices=[('', 'Default'), ('primary', 'Primary'), ('success', 'Success'), ('info', 'Info'), ('warning', 'Warning'), ('danger', 'Danger')]),
            preserve_default=True,
        ),
    ]
