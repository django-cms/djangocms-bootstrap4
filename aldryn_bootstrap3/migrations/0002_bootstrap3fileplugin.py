# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filer.fields.file
import aldryn_bootstrap3.model_fields
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0002_auto_20150606_2003'),
        ('cms', '0011_auto_20150419_1006'),
        ('aldryn_bootstrap3', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bootstrap3FilePlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='+', primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('name', aldryn_bootstrap3.model_fields.MiniText(default='', verbose_name='name', blank=True)),
                ('open_new_window', models.BooleanField(default=False)),
                ('show_file_size', models.BooleanField(default=False)),
                ('icon_left', aldryn_bootstrap3.model_fields.Icon(default='', max_length=255, blank=True)),
                ('icon_right', aldryn_bootstrap3.model_fields.Icon(default='', max_length=255, blank=True)),
                ('classes', aldryn_bootstrap3.model_fields.Classes(default='', help_text='space separated classes that are added to the class. see <a href="http://getbootstrap.com/css/" target="_blank">bootstrap docs</a>', blank=True)),
                ('file', filer.fields.file.FilerFileField(related_name='+', on_delete=django.db.models.deletion.SET_NULL, verbose_name='file', to='filer.File', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
