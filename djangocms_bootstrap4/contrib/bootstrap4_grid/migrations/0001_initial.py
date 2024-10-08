# Generated by Django 1.9.13 on 2017-09-27 21:19
import django.db.models.deletion
from django.db import migrations, models

import djangocms_bootstrap4.fields
from djangocms_bootstrap4.constants import TAG_CHOICES

from ..constants import (
    GRID_COLUMN_ALIGNMENT_CHOICES, GRID_COLUMN_CHOICES, GRID_CONTAINER_CHOICES, GRID_ROW_HORIZONTAL_ALIGNMENT_CHOICES,
    GRID_ROW_VERTICAL_ALIGNMENT_CHOICES,
)


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bootstrap4GridColumn',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='%(app_label)s_%(class)s', serialize=False, to='cms.CMSPlugin')),
                ('column_type', models.CharField(blank=True, choices=GRID_COLUMN_CHOICES, default=GRID_COLUMN_CHOICES[0][0], max_length=255, verbose_name='Column type')),
                ('column_size', djangocms_bootstrap4.fields.IntegerRangeField(blank=True, help_text='Nummeric value from 1 - 12. Spreads the columns evenly when empty.', null=True, verbose_name='Column size')),
                ('column_alignment', models.CharField(blank=True, choices=GRID_COLUMN_ALIGNMENT_CHOICES, max_length=255, verbose_name='Alignment')),
                ('tag_type', djangocms_bootstrap4.fields.TagTypeField(choices=TAG_CHOICES, default=TAG_CHOICES[0][0], help_text='Select the HTML tag to be used.', max_length=255, verbose_name='Tag type')),
                ('attributes', djangocms_bootstrap4.fields.AttributesField(blank=True, default=dict, verbose_name='Attributes')),
                ('xs_col', djangocms_bootstrap4.fields.IntegerRangeField(blank=True, null=True)),
                ('xs_order', djangocms_bootstrap4.fields.IntegerRangeField(blank=True, null=True)),
                ('xs_ml', models.BooleanField(default=False)),
                ('xs_mr', models.BooleanField(default=False)),
                ('sm_col', djangocms_bootstrap4.fields.IntegerRangeField(blank=True, null=True)),
                ('sm_order', djangocms_bootstrap4.fields.IntegerRangeField(blank=True, null=True)),
                ('sm_ml', models.BooleanField(default=False)),
                ('sm_mr', models.BooleanField(default=False)),
                ('md_col', djangocms_bootstrap4.fields.IntegerRangeField(blank=True, null=True)),
                ('md_order', djangocms_bootstrap4.fields.IntegerRangeField(blank=True, null=True)),
                ('md_ml', models.BooleanField(default=False)),
                ('md_mr', models.BooleanField(default=False)),
                ('lg_col', djangocms_bootstrap4.fields.IntegerRangeField(blank=True, null=True)),
                ('lg_order', djangocms_bootstrap4.fields.IntegerRangeField(blank=True, null=True)),
                ('lg_ml', models.BooleanField(default=False)),
                ('lg_mr', models.BooleanField(default=False)),
                ('xl_col', djangocms_bootstrap4.fields.IntegerRangeField(blank=True, null=True)),
                ('xl_order', djangocms_bootstrap4.fields.IntegerRangeField(blank=True, null=True)),
                ('xl_ml', models.BooleanField(default=False)),
                ('xl_mr', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='Bootstrap4GridContainer',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='%(app_label)s_%(class)s', serialize=False, to='cms.CMSPlugin')),
                ('container_type', models.CharField(choices=GRID_CONTAINER_CHOICES, default=GRID_CONTAINER_CHOICES[0][0], help_text='Defines if the grid should use fixed width (<code>.container</code>) or fluid width (<code>.container-fluid</code>).', max_length=255, verbose_name='Container type')),
                ('tag_type', djangocms_bootstrap4.fields.TagTypeField(choices=TAG_CHOICES, default=TAG_CHOICES[0][0], help_text='Select the HTML tag to be used.', max_length=255, verbose_name='Tag type')),
                ('attributes', djangocms_bootstrap4.fields.AttributesField(blank=True, default=dict, verbose_name='Attributes')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='Bootstrap4GridRow',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='%(app_label)s_%(class)s', serialize=False, to='cms.CMSPlugin')),
                ('vertical_alignment', models.CharField(blank=True, choices=GRID_ROW_VERTICAL_ALIGNMENT_CHOICES, help_text='Read more in the <a href="https://getbootstrap.com/docs/4.0/layout/grid/#vertical-alignment" target="_blank">documentation</a>.', max_length=255, verbose_name='Vertical alignment')),
                ('horizontal_alignment', models.CharField(blank=True, choices=GRID_ROW_HORIZONTAL_ALIGNMENT_CHOICES, help_text='Read more in the <a href="https://getbootstrap.com/docs/4.0/layout/grid/#horizontal-alignment" target="_blank">documentation</a>.', max_length=255, verbose_name='Horizontal alignment')),
                ('gutters', models.BooleanField(default=False, help_text='Removes the marginal gutters from the grid.', verbose_name='Remove gutters')),
                ('tag_type', djangocms_bootstrap4.fields.TagTypeField(choices=TAG_CHOICES, default=TAG_CHOICES[0][0], help_text='Select the HTML tag to be used.', max_length=255, verbose_name='Tag type')),
                ('attributes', djangocms_bootstrap4.fields.AttributesField(blank=True, default=dict, verbose_name='Attributes')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
