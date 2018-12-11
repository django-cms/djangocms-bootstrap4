# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import djangocms_bootstrap4.fields

from djangocms_bootstrap4.constants import TAG_CHOICES

from ..constants import (
    TAB_TYPE_CHOICES,
    TAB_ALIGNMENT_CHOICES,
    TAB_EFFECT_CHOICES,
    TAB_TEMPLATE_CHOICES,
)


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bootstrap4Tab',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, serialize=False, primary_key=True, to='cms.CMSPlugin', auto_created=True, related_name='bootstrap4_tabs_bootstrap4tab', on_delete=models.CASCADE)),
                ('tab_style', models.CharField(max_length=255, choices=TAB_TEMPLATE_CHOICES, verbose_name='Template', default=TAB_TEMPLATE_CHOICES[0][0], help_text='This is the template that will be used for the component.')),
                ('tab_type', models.CharField(max_length=255, choices=TAB_TYPE_CHOICES, verbose_name='Type', default=TAB_TYPE_CHOICES[0][0])),
                ('tab_alignment', models.CharField(max_length=255, blank=True, choices=TAB_ALIGNMENT_CHOICES, verbose_name='Alignment')),
                ('tab_index', models.PositiveIntegerField(null=True, blank=True, verbose_name='Index', help_text='Index of element to open on page load starting at 1.')),
                ('tab_effect', models.CharField(max_length=255, blank=True, choices=TAB_EFFECT_CHOICES, verbose_name='Animation effect')),
                ('tag_type', djangocms_bootstrap4.fields.TagTypeField(max_length=255, choices=TAG_CHOICES, verbose_name='Tag type', default=TAG_CHOICES[0][0], help_text='Select the HTML tag to be used.')),
                ('attributes', djangocms_bootstrap4.fields.AttributesField(blank=True, verbose_name='Attributes', default=dict)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='Bootstrap4TabItem',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, serialize=False, primary_key=True, to='cms.CMSPlugin', auto_created=True, related_name='bootstrap4_tabs_bootstrap4tabitem', on_delete=models.CASCADE)),
                ('tab_title', models.CharField(max_length=255, verbose_name='Tab title')),
                ('tag_type', djangocms_bootstrap4.fields.TagTypeField(max_length=255, choices=TAG_CHOICES, verbose_name='Tag type', default=TAG_CHOICES[0][0], help_text='Select the HTML tag to be used.')),
                ('attributes', djangocms_bootstrap4.fields.AttributesField(blank=True, verbose_name='Attributes', default=dict)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
