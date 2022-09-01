# Generated by Django 1.9.13 on 2017-10-15 10:02
import django.db.models.deletion
from django.db import migrations, models

import djangocms_bootstrap4.fields
from djangocms_bootstrap4.constants import TAG_CHOICES

from ..constants import CARD_ALIGNMENT_CHOICES, CARD_INNER_TYPE_CHOICES, CARD_TAG_CHOICES, CARD_TYPE_CHOICES
from ..models import CARD_COLOR_STYLE_CHOICES, CARD_TEXT_STYLES


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bootstrap4Card',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='bootstrap4_card_bootstrap4card', serialize=False, to='cms.CMSPlugin')),
                ('card_type', models.CharField(choices=CARD_TYPE_CHOICES, default=CARD_TYPE_CHOICES[0][0], max_length=255, verbose_name='Card type')),
                ('card_context', models.CharField(blank=True, choices=CARD_COLOR_STYLE_CHOICES, max_length=255, verbose_name='Background context')),
                ('card_alignment', models.CharField(blank=True, choices=CARD_ALIGNMENT_CHOICES, max_length=255, verbose_name='Alignment')),
                ('card_outline', models.BooleanField(default=False, help_text='Uses the border context instead of the background.', verbose_name='Outline')),
                ('card_text_color', models.CharField(blank=True, choices=CARD_TEXT_STYLES, max_length=255, verbose_name='Text context')),
                ('tag_type', djangocms_bootstrap4.fields.TagTypeField(choices=TAG_CHOICES, default=TAG_CHOICES[0][0], help_text='Select the HTML tag to be used.', max_length=255, verbose_name='Tag type')),
                ('attributes', djangocms_bootstrap4.fields.AttributesField(blank=True, default=dict, verbose_name='Attributes')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='Bootstrap4CardInner',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='bootstrap4_card_bootstrap4cardinner', serialize=False, to='cms.CMSPlugin')),
                ('inner_type', models.CharField(choices=CARD_INNER_TYPE_CHOICES, default=CARD_INNER_TYPE_CHOICES[0][0], help_text='Define the structure of the plugin.', max_length=255, verbose_name='Inner type')),
                ('tag_type', djangocms_bootstrap4.fields.TagTypeField(choices=TAG_CHOICES, default=TAG_CHOICES[0][0], help_text='Select the HTML tag to be used.', max_length=255, verbose_name='Tag type')),
                ('attributes', djangocms_bootstrap4.fields.AttributesField(blank=True, default=dict, verbose_name='Attributes')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
