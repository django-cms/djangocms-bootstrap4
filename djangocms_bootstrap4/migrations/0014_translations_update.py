# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import djangocms_text_ckeditor.fields
import filer.fields.file
import django.db.models.deletion
from aldryn_bootstrap3.models import Bootstrap3CarouselPlugin
from aldryn_bootstrap3.model_fields import get_additional_styles


class Migration(migrations.Migration):

    dependencies = [
        ('aldryn_bootstrap3', '0013_boostrap3jumbotronplugin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boostrap3blockquoteplugin',
            name='reverse',
            field=models.BooleanField(default=False, help_text='Reverses the position by adding the Bootstrap 3 "blockquote-reverse" class.', verbose_name='Reverse quote'),
        ),
        migrations.AlterField(
            model_name='boostrap3imageplugin',
            name='aspect_ratio',
            field=models.CharField(default='', choices=[('1x1', '1x1'), ('4x3', '4x3'), ('16x9', '16x9'), ('16x10', '16x10'), ('21x9', '21x9'), ('3x4', '3x4'), ('9x16', '9x16'), ('10x16', '10x16'), ('9x21', '9x21')], max_length=255, blank=True, help_text='Determines width and height of the image according to the selected ratio.', verbose_name='Aspect ratio'),
        ),
        migrations.AlterField(
            model_name='bootstrap3accordionplugin',
            name='index',
            field=models.PositiveIntegerField(help_text='Index of element to open on page load (optional).', null=True, verbose_name='Index', blank=True),
        ),
        migrations.AlterField(
            model_name='bootstrap3carouselplugin',
            name='interval',
            field=models.IntegerField(default=5000, help_text='Time (in milliseconds) between items.', verbose_name='Interval'),
        ),
        migrations.AlterField(
            model_name='bootstrap3carouselplugin',
            name='pause',
            field=models.BooleanField(default=True, help_text='Pauses the carousel on hover.', verbose_name='Pause'),
        ),
        migrations.AlterField(
            model_name='bootstrap3carouselplugin',
            name='ride',
            field=models.BooleanField(default=True, help_text='Auto-starts animation of the carousel.', verbose_name='Ride'),
        ),
        migrations.AlterField(
            model_name='bootstrap3carouselplugin',
            name='wrap',
            field=models.BooleanField(default=True, help_text='Loops carousel animation.', verbose_name='Wrap'),
        ),
        migrations.AlterField(
            model_name='bootstrap3carouselslideplugin',
            name='link_file',
            field=filer.fields.file.FilerFileField(on_delete=django.db.models.deletion.SET_NULL, verbose_name='File', blank=True, to='filer.File', null=True),
        ),
        migrations.AlterField(
            model_name='bootstrap3listgroupplugin',
            name='add_list_group_class',
            field=models.BooleanField(default=True, help_text='Adds the list-group and subsequent list-group-item classes.', verbose_name='.list-group'),
        ),
        migrations.AlterField(
            model_name='bootstrap3tabplugin',
            name='index',
            field=models.PositiveIntegerField(help_text='Index of element to open on page load (optional).', null=True, verbose_name='Index', blank=True),
        ),
        migrations.AlterField(
            model_name='boostrap3buttonplugin',
            name='link_file',
            field=filer.fields.file.FilerFileField(on_delete=django.db.models.deletion.SET_NULL, verbose_name='File', blank=True, to='filer.File', null=True),
        ),
        migrations.AlterField(
            model_name='boostrap3jumbotronplugin',
            name='grid',
            field=models.BooleanField(default=False, help_text='Adds a ".container" element inside the "Jumbotron" for use outside of a grid.', verbose_name='Add container'),
        ),
        migrations.AlterField(
            model_name='bootstrap3carouselslideplugin',
            name='content',
            field=djangocms_text_ckeditor.fields.HTMLField(default='', help_text='Content may also be added using child plugins.', verbose_name='Content', blank=True),
        ),
        migrations.AlterField(
            model_name='bootstrap3carouselplugin',
            name='style',
            field=models.CharField(choices=Bootstrap3CarouselPlugin.STYLE_CHOICES + get_additional_styles(), default='standard', max_length=255, verbose_name='Style'),
        ),
        migrations.AlterField(
            model_name='boostrap3imageplugin',
            name='img_responsive',
            field=models.BooleanField(default=True, help_text='Adds the Bootstrap 3 ".img-responsive" class.', verbose_name='.img-responsive'),
        ),
        migrations.AlterField(
            model_name='bootstrap3carouselplugin',
            name='aspect_ratio',
            field=models.CharField(default='', choices=[('1x1', '1x1'), ('4x3', '4x3'), ('16x9', '16x9'), ('16x10', '16x10'), ('21x9', '21x9'), ('3x4', '3x4'), ('9x16', '9x16'), ('10x16', '10x16'), ('9x21', '9x21')], max_length=255, blank=True, help_text='Determines width and height of the image according to the selected ratio.', verbose_name='Aspect ratio'),
        ),
    ]
