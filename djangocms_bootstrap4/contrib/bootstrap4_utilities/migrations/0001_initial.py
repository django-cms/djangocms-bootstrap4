# Generated by Django 1.9.13 on 2017-10-15 10:47
import django.db.models.deletion
from django.db import migrations, models

import djangocms_bootstrap4.fields
from djangocms_bootstrap4.constants import DEVICE_CHOICES, TAG_CHOICES

from ..constants import SPACER_PROPERTY_CHOICES, SPACER_SIDE_CHOICES, SPACER_SIZE_CHOICES


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bootstrap4Spacing',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='%(app_label)s_%(class)s', serialize=False, to='cms.CMSPlugin')),
                ('space_property', models.CharField(choices=SPACER_PROPERTY_CHOICES, default=SPACER_PROPERTY_CHOICES[0][0], max_length=255, verbose_name='Property')),
                ('space_sides', models.CharField(blank=True, choices=SPACER_SIDE_CHOICES, default=SPACER_SIDE_CHOICES[0][0], max_length=255, verbose_name='Sides')),
                ('space_size', models.CharField(choices=SPACER_SIZE_CHOICES, default=SPACER_SIZE_CHOICES[0][0], max_length=255, verbose_name='Size')),
                ('space_device', models.CharField(blank=True, choices=DEVICE_CHOICES, max_length=255, verbose_name='Device')),
                ('tag_type', djangocms_bootstrap4.fields.TagTypeField(choices=TAG_CHOICES, default=TAG_CHOICES[0][0], help_text='Select the HTML tag to be used.', max_length=255, verbose_name='Tag type')),
                ('attributes', djangocms_bootstrap4.fields.AttributesField(blank=True, default=dict, verbose_name='Attributes')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
