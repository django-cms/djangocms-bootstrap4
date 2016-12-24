# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import aldryn_bootstrap3.model_fields
import djangocms_attributes_field.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
        ('aldryn_bootstrap3', '0011_bootstrap3responsiveplugin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bootstrap3TabItemPlugin',
            fields=[
                ('title', models.CharField(max_length=255, verbose_name='Tab title')),
                ('icon', aldryn_bootstrap3.model_fields.Icon(default='', max_length=255, verbose_name='Title icon', blank=True)),
                ('classes', aldryn_bootstrap3.model_fields.Classes(default='', help_text='Space separated classes that are added to the class. See <a href="http://getbootstrap.com/css/" target="_blank">Bootstrap 3 documentation</a>.', verbose_name='Classes', blank=True)),
                ('attributes', djangocms_attributes_field.fields.AttributesField(default=dict, verbose_name='Attributes', blank=True)),
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='aldryn_bootstrap3_bootstrap3tabitemplugin', primary_key=True, serialize=False, to='cms.CMSPlugin')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='Bootstrap3TabPlugin',
            fields=[
                ('index', models.PositiveIntegerField(help_text='Index of element that should be opened on page load (leave it empty if none of the items should be opened)', null=True, verbose_name='Index', blank=True)),
                ('style', models.CharField(default='nav-tabs', max_length=255, verbose_name='Display type', choices=[('nav-tabs', 'Tabs'), ('nav-tabs nav-justified', 'Tabs justified'), ('nav-pills', 'Pills'), ('nav-pills nav-justified', 'Pills justified')])),
                ('effect', models.CharField(blank=True, max_length=255, verbose_name='Animation effect', choices=[('fade', 'Fade')])),
                ('classes', aldryn_bootstrap3.model_fields.Classes(default='', help_text='Space separated classes that are added to the class. See <a href="http://getbootstrap.com/css/" target="_blank">Bootstrap 3 documentation</a>.', verbose_name='Classes', blank=True)),
                ('attributes', djangocms_attributes_field.fields.AttributesField(default=dict, verbose_name='Attributes', blank=True)),
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='aldryn_bootstrap3_bootstrap3tabplugin', primary_key=True, serialize=False, to='cms.CMSPlugin')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
