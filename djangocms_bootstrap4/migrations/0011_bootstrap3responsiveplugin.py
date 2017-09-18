# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import aldryn_bootstrap3.model_fields
import djangocms_attributes_field.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
        ('aldryn_bootstrap3', '0010_bootstrap3codeplugin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bootstrap3ResponsivePlugin',
            fields=[
                ('device_breakpoints', aldryn_bootstrap3.model_fields.Responsive(default='visible-xs visible-sm visible-md visible-lg', verbose_name='Devices', blank=True)),
                ('print_breakpoints', aldryn_bootstrap3.model_fields.ResponsivePrint(default='visible-print', verbose_name='Print', blank=True)),
                ('classes', aldryn_bootstrap3.model_fields.Classes(default='', help_text='Space separated classes that are added to the class. See <a href="http://getbootstrap.com/css/" target="_blank">Bootstrap 3 documentation</a>.', verbose_name='Classes', blank=True)),
                ('attributes', djangocms_attributes_field.fields.AttributesField(default=dict, verbose_name='Attributes', blank=True)),
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='aldryn_bootstrap3_bootstrap3responsiveplugin', primary_key=True, serialize=False, to='cms.CMSPlugin')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.AlterField(
            model_name='bootstrap3carouselplugin',
            name='aspect_ratio',
            field=models.CharField(default='', max_length=255, verbose_name='Aspect ratio', blank=True),
        ),
    ]
