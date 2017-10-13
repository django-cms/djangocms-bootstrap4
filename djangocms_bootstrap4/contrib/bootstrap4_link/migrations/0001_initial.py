# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-10-12 06:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import djangocms_attributes_field.fields
import djangocms_link.validators

from djangocms_link.models import get_templates, TARGET_CHOICES

from ..constants import LINK_CHOICES, LINK_SIZES
from ..models import COLOR_STYLES


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bootstrap4Link',
            fields=[
                ('template', models.CharField(choices=get_templates(), default=get_templates()[0][0], max_length=255, verbose_name='Template')),
                ('name', models.CharField(blank=True, max_length=255, verbose_name='Display name')),
                ('external_link', models.URLField(blank=True, help_text='Provide a valid URL to an external website.', max_length=2040, validators=[djangocms_link.validators.IntranetURLValidator(intranet_host_re=None)], verbose_name='External link')),
                ('anchor', models.CharField(blank=True, help_text='Appends the value only after the internal or external link. Do <em>not</em> include a preceding "#" symbol.', max_length=255, verbose_name='Anchor')),
                ('mailto', models.EmailField(blank=True, max_length=255, verbose_name='Email address')),
                ('phone', models.CharField(blank=True, max_length=255, verbose_name='Phone')),
                ('target', models.CharField(blank=True, choices=TARGET_CHOICES, max_length=255, verbose_name='Target')),
                ('attributes', djangocms_attributes_field.fields.AttributesField(blank=True, default=dict, verbose_name='Attributes')),
                ('cmsplugin_ptr', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='bootstrap4_link_bootstrap4link', serialize=False, to='cms.CMSPlugin')),
                ('link_type', models.CharField(choices=LINK_CHOICES, default=LINK_CHOICES[0][0], help_text='Adds either the .btn-* or .text-* classes.', max_length=255, verbose_name='Type')),
                ('link_context', models.CharField(choices=COLOR_STYLES, default=COLOR_STYLES[0][0], max_length=255, verbose_name='Context')),
                ('link_size', models.CharField(blank=True, choices=LINK_SIZES, default=LINK_SIZES[0][0], max_length=255, verbose_name='Size')),
                ('link_outline', models.BooleanField(default=False, help_text='Applies the .btn-outline class to the elements.', verbose_name='Outline')),
                ('link_block', models.BooleanField(default=False, help_text='Extends the button to the width of its container.', verbose_name='Block')),
                ('internal_link', models.ForeignKey(blank=True, help_text='If provided, overrides the external link.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='cms.Page', verbose_name='Internal link')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
