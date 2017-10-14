# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-10-14 08:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import djangocms_bootstrap4.fields


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
                ('card_type', models.CharField(choices=[('card', 'Card'), ('card-group', 'Card group'), ('card-deck', 'Card deck'), ('card-columns', 'Card columns')], default='card', max_length=255, verbose_name='Card type')),
                ('card_context', models.CharField(blank=True, choices=[('primary', 'Primary'), ('secondary', 'Secondary'), ('success', 'Success'), ('danger', 'Danger'), ('warning', 'Warning'), ('info', 'Info'), ('light', 'Light'), ('dark', 'Dark'), ('transparent', 'Transparent')], max_length=255, verbose_name='Context')),
                ('card_alignment', models.CharField(blank=True, choices=[('text-center', 'Left'), ('text-center', 'Center'), ('text-center', 'Right')], max_length=255, verbose_name='Alignment')),
                ('card_outline', models.BooleanField(default=False, help_text='Uses the border context instead of the background.', verbose_name='Outline')),
                ('tag_type', djangocms_bootstrap4.fields.TagTypeField(choices=[('div', 'div'), ('section', 'section'), ('article', 'article'), ('header', 'header'), ('footer', 'footer'), ('aside', 'aside')], default='div', help_text='Select the HTML tag to be used.', max_length=255, verbose_name='Tag type')),
                ('attributes', djangocms_bootstrap4.fields.AttributesField(blank=True, default=dict, verbose_name='Attributes')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='Bootstrap4CardContent',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='bootstrap4_card_bootstrap4cardcontent', serialize=False, to='cms.CMSPlugin')),
                ('content_type', models.CharField(choices=[('text', 'Text'), ('title', 'Title'), ('subtitle', 'Subtitle'), ('link', 'Link')], default='text', max_length=255, verbose_name='Content type')),
                ('tag_type', djangocms_bootstrap4.fields.TagTypeField(choices=[('h1', 'H1'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('h5', 'H5'), ('h6', 'H6'), ('p', 'P')], default='h1', help_text='Select the HTML tag to be used.', max_length=255, verbose_name='Tag type')),
                ('attributes', djangocms_bootstrap4.fields.AttributesField(blank=True, default=dict, verbose_name='Attributes')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='Bootstrap4CardImage',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='bootstrap4_card_bootstrap4cardimage', serialize=False, to='cms.CMSPlugin')),
                ('content_type', models.CharField(blank=True, choices=[('card-img-top', 'Image top'), ('card-img-bottom', 'Image bottom'), ('card-img-overlay', 'Image overlay')], default='card-img-top', max_length=255, verbose_name='Image type')),
                ('tag_type', djangocms_bootstrap4.fields.TagTypeField(choices=[('div', 'div'), ('section', 'section'), ('article', 'article'), ('header', 'header'), ('footer', 'footer'), ('aside', 'aside')], default='div', help_text='Select the HTML tag to be used.', max_length=255, verbose_name='Tag type')),
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
                ('inner_type', models.CharField(choices=[('header', 'Header'), ('body', 'Body'), ('footer', 'Footer')], default='header', max_length=255, verbose_name='Inner type')),
                ('tag_type', djangocms_bootstrap4.fields.TagTypeField(choices=[('div', 'div'), ('section', 'section'), ('article', 'article'), ('header', 'header'), ('footer', 'footer'), ('aside', 'aside')], default='div', help_text='Select the HTML tag to be used.', max_length=255, verbose_name='Tag type')),
                ('attributes', djangocms_bootstrap4.fields.AttributesField(blank=True, default=dict, verbose_name='Attributes')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
