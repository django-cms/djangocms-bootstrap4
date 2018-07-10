# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import djangocms_bootstrap4.fields


class Migration(migrations.Migration):

    dependencies = [
        ('bootstrap4_grid', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bootstrap4gridcolumn',
            name='lg_offset',
            field=djangocms_bootstrap4.fields.IntegerRangeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bootstrap4gridcolumn',
            name='md_offset',
            field=djangocms_bootstrap4.fields.IntegerRangeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bootstrap4gridcolumn',
            name='sm_offset',
            field=djangocms_bootstrap4.fields.IntegerRangeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bootstrap4gridcolumn',
            name='xl_offset',
            field=djangocms_bootstrap4.fields.IntegerRangeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bootstrap4gridcolumn',
            name='xs_offset',
            field=djangocms_bootstrap4.fields.IntegerRangeField(blank=True, null=True),
        ),
    ]
