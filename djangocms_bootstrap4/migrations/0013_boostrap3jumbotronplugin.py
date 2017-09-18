# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import aldryn_bootstrap3.model_fields
import djangocms_attributes_field.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
        ('aldryn_bootstrap3', '0012_bootstrap3tabplugin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Boostrap3JumbotronPlugin',
            fields=[
                ('label', models.CharField(max_length=255, verbose_name='Label', blank=True)),
                ('grid', models.BooleanField(default=False, help_text='Adds a "container" element inside of the "Jumbotron"for use outside of a grid.', verbose_name='Add container')),
                ('classes', aldryn_bootstrap3.model_fields.Classes(default='', help_text='Space separated classes that are added to the class. See <a href="http://getbootstrap.com/css/" target="_blank">Bootstrap 3 documentation</a>.', verbose_name='Classes', blank=True)),
                ('attributes', djangocms_attributes_field.fields.AttributesField(default=dict, verbose_name='Attributes', blank=True)),
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='aldryn_bootstrap3_boostrap3jumbotronplugin', primary_key=True, serialize=False, to='cms.CMSPlugin')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
