# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-10-15 12:31
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models

import djangocms_bootstrap4.fields
from djangocms_bootstrap4.constants import COLOR_STYLE_CHOICES, TAG_CHOICES


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bootstrap4Alerts',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='bootstrap4_alerts_bootstrap4alerts', serialize=False, to='cms.CMSPlugin')),
                ('alert_context', models.CharField(choices=COLOR_STYLE_CHOICES, default=COLOR_STYLE_CHOICES[0][0], max_length=255, verbose_name='Context')),
                ('alert_dismissable', models.BooleanField(default=False, help_text='Allows the alert to be closed.', verbose_name='Dismissable')),
                ('tag_type', djangocms_bootstrap4.fields.TagTypeField(choices=TAG_CHOICES, default=TAG_CHOICES[0][0], help_text='Select the HTML tag to be used.', max_length=255, verbose_name='Tag type')),
                ('attributes', djangocms_bootstrap4.fields.AttributesField(blank=True, default=dict, verbose_name='Attributes')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
