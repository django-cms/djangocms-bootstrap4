# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import djangocms_bootstrap4.fields

from djangocms_bootstrap4.constants import ALIGN_CHOICES

from ..constants import CODE_TYPE_CHOICES


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bootstrap4Blockquote',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(primary_key=True, to='cms.CMSPlugin', serialize=False, auto_created=True, related_name='bootstrap4_content_bootstrap4blockquote', parent_link=True, on_delete=models.CASCADE)),
                ('quote_content', models.TextField(verbose_name='Quote')),
                ('quote_origin', models.TextField(verbose_name='Cite', blank=True)),
                ('quote_alignment', models.CharField(max_length=255, default=ALIGN_CHOICES[0][0], choices=ALIGN_CHOICES, blank=True, verbose_name='Alignment')),
                ('attributes', djangocms_bootstrap4.fields.AttributesField(default=dict, verbose_name='Attributes', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='Bootstrap4Code',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(primary_key=True, to='cms.CMSPlugin', serialize=False, auto_created=True, related_name='bootstrap4_content_bootstrap4code', parent_link=True, on_delete=models.CASCADE)),
                ('code_content', models.TextField(verbose_name='Code')),
                ('tag_type', models.CharField(max_length=255, default=CODE_TYPE_CHOICES[0][0], choices=CODE_TYPE_CHOICES, verbose_name='Code type')),
                ('attributes', djangocms_bootstrap4.fields.AttributesField(default=dict, verbose_name='Attributes', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
