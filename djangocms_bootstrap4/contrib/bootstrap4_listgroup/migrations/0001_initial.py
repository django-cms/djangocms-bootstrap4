# Generated by Django 1.9.13 on 2017-10-15 21:00
import django.db.models.deletion
from django.db import migrations, models

import djangocms_bootstrap4.fields
from djangocms_bootstrap4.constants import COLOR_STYLE_CHOICES, TAG_CHOICES

from ..constants import LISTGROUP_STATE_CHOICES


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bootstrap4ListGroup',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='%(app_label)s_%(class)s', serialize=False, to='cms.CMSPlugin')),
                ('list_group_flush', models.BooleanField(default=False, help_text='Create lists of content in a card with a flush list group.', verbose_name='List group flush')),
                ('tag_type', djangocms_bootstrap4.fields.TagTypeField(choices=TAG_CHOICES, default=TAG_CHOICES[0][0], help_text='Select the HTML tag to be used.', max_length=255, verbose_name='Tag type')),
                ('attributes', djangocms_bootstrap4.fields.AttributesField(blank=True, default=dict, verbose_name='Attributes')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='Bootstrap4ListGroupItem',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='%(app_label)s_%(class)s', serialize=False, to='cms.CMSPlugin')),
                ('list_context', models.CharField(blank=True, choices=COLOR_STYLE_CHOICES, max_length=255, verbose_name='Context')),
                ('list_state', models.CharField(blank=True, choices=LISTGROUP_STATE_CHOICES, max_length=255, verbose_name='State')),
                ('tag_type', djangocms_bootstrap4.fields.TagTypeField(choices=TAG_CHOICES, default=TAG_CHOICES[0][0], help_text='Select the HTML tag to be used.', max_length=255, verbose_name='Tag type')),
                ('attributes', djangocms_bootstrap4.fields.AttributesField(blank=True, default=dict, verbose_name='Attributes')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
