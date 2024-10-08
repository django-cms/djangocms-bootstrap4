# Generated by Django 1.9.13 on 2017-10-15 21:05
import django.db.models.deletion
from django.db import migrations, models

import djangocms_attributes_field.fields
import djangocms_link.validators
import djangocms_text_ckeditor.fields
import filer.fields.image
from djangocms_link.models import TARGET_CHOICES, get_templates

import djangocms_bootstrap4.fields
from djangocms_bootstrap4.constants import TAG_CHOICES

from ..constants import CAROUSEL_PAUSE_CHOICES, CAROUSEL_RIDE_CHOICES, CAROUSEL_TEMPLATE_CHOICES


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
        ('filer', '0007_auto_20161016_1055'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bootstrap4Carousel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='%(app_label)s_%(class)s', serialize=False, to='cms.CMSPlugin')),
                ('carousel_style', models.CharField(choices=CAROUSEL_TEMPLATE_CHOICES, default=CAROUSEL_TEMPLATE_CHOICES[0][0], help_text='This is the template that will be used for the component.', max_length=255, verbose_name='Template')),
                ('carousel_interval', models.IntegerField(default=5000, help_text='The amount of time to delay between automatically cycling an item. If false, carousel will not automatically cycle.', verbose_name='Interval')),
                ('carousel_controls', models.BooleanField(default=True, help_text='Adding in the previous and next controls.', verbose_name='Controls')),
                ('carousel_indicators', models.BooleanField(default=True, help_text='Adding in the indicators to the carousel.', verbose_name='Indicators')),
                ('carousel_keyboard', models.BooleanField(default=True, help_text='Whether the carousel should react to keyboard events.', verbose_name='Keyboard')),
                ('carousel_pause', models.CharField(choices=CAROUSEL_PAUSE_CHOICES, default=CAROUSEL_PAUSE_CHOICES[0][0], help_text='If set to "hover", pauses the cycling of the carousel on "mouseenter" and resumes the cycling of the carousel on "mouseleave". If set to "false", hovering over the carousel won\'t pause it.', max_length=255, verbose_name='Pause')),
                ('carousel_ride', models.CharField(choices=CAROUSEL_RIDE_CHOICES, default=CAROUSEL_RIDE_CHOICES[0][0], help_text='Autoplays the carousel after the user manually cycles the first item. If "carousel", autoplays the carousel on load.', max_length=255, verbose_name='Ride')),
                ('carousel_wrap', models.BooleanField(default=True, help_text='Whether the carousel should cycle continuously or have hard stops.', verbose_name='Wrap')),
                ('tag_type', djangocms_bootstrap4.fields.TagTypeField(choices=TAG_CHOICES, default=TAG_CHOICES[0][0], help_text='Select the HTML tag to be used.', max_length=255, verbose_name='Tag type')),
                ('attributes', djangocms_bootstrap4.fields.AttributesField(blank=True, default=dict, verbose_name='Attributes')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='Bootstrap4CarouselSlide',
            fields=[
                ('template', models.CharField(choices=get_templates(), default=get_templates()[0][0], max_length=255, verbose_name='Template')),
                ('name', models.CharField(blank=True, max_length=255, verbose_name='Display name')),
                ('external_link', models.URLField(blank=True, help_text='Provide a valid URL to an external website.', max_length=2040, validators=[djangocms_link.validators.IntranetURLValidator(intranet_host_re=None)], verbose_name='External link')),
                ('anchor', models.CharField(blank=True, help_text='Appends the value only after the internal or external link. Do <em>not</em> include a preceding "#" symbol.', max_length=255, verbose_name='Anchor')),
                ('mailto', models.EmailField(blank=True, max_length=255, verbose_name='Email address')),
                ('phone', models.CharField(blank=True, max_length=255, verbose_name='Phone')),
                ('target', models.CharField(blank=True, choices=TARGET_CHOICES, max_length=255, verbose_name='Target')),
                ('attributes', djangocms_attributes_field.fields.AttributesField(blank=True, default=dict, verbose_name='Attributes')),
                ('cmsplugin_ptr', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='%(app_label)s_%(class)s', serialize=False, to='cms.CMSPlugin')),
                ('carousel_content', djangocms_text_ckeditor.fields.HTMLField(blank=True, default='', help_text='Content may also be added using child plugins.', verbose_name='Content')),
                ('tag_type', djangocms_bootstrap4.fields.TagTypeField(choices=TAG_CHOICES, default=TAG_CHOICES[0][0], help_text='Select the HTML tag to be used.', max_length=255, verbose_name='Tag type')),
                ('carousel_image', filer.fields.image.FilerImageField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='filer.Image', verbose_name='Slide image')),
                ('internal_link', models.ForeignKey(blank=True, help_text='If provided, overrides the external link.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='cms.Page', verbose_name='Internal link')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
