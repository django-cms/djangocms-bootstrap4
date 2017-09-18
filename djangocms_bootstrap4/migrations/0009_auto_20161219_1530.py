# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import filer.fields.folder
import aldryn_bootstrap3.model_fields
import filer.fields.image
import filer.fields.file
import django.db.models.deletion
import cms.models.fields
import djangocms_attributes_field.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
        ('aldryn_bootstrap3', '0008_auto_20160820_2332'),
    ]

    operations = [
        migrations.CreateModel(
            name='Boostrap3CitePlugin',
            fields=[
                ('classes', aldryn_bootstrap3.model_fields.Classes(default='', help_text='Space separated classes that are added to the class. See <a href="http://getbootstrap.com/css/" target="_blank">Bootstrap 3 documentation</a>.', verbose_name='Classes', blank=True)),
                ('attributes', djangocms_attributes_field.fields.AttributesField(default=dict, verbose_name='Attributes', blank=True)),
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='aldryn_bootstrap3_boostrap3citeplugin', primary_key=True, serialize=False, to='cms.CMSPlugin')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.RemoveField(
            model_name='boostrap3buttonplugin',
            name='responsive',
        ),
        migrations.RemoveField(
            model_name='boostrap3buttonplugin',
            name='responsive_print',
        ),
        migrations.AddField(
            model_name='boostrap3alertplugin',
            name='attributes',
            field=djangocms_attributes_field.fields.AttributesField(default=dict, verbose_name='Attributes', blank=True),
        ),
        migrations.AddField(
            model_name='boostrap3blockquoteplugin',
            name='attributes',
            field=djangocms_attributes_field.fields.AttributesField(default=dict, verbose_name='Attributes', blank=True),
        ),
        migrations.AddField(
            model_name='boostrap3iconplugin',
            name='attributes',
            field=djangocms_attributes_field.fields.AttributesField(default=dict, verbose_name='Attributes', blank=True),
        ),
        migrations.AddField(
            model_name='boostrap3imageplugin',
            name='attributes',
            field=djangocms_attributes_field.fields.AttributesField(default=dict, verbose_name='Attributes', blank=True),
        ),
        migrations.AddField(
            model_name='boostrap3labelplugin',
            name='attributes',
            field=djangocms_attributes_field.fields.AttributesField(default=dict, verbose_name='Attributes', blank=True),
        ),
        migrations.AddField(
            model_name='boostrap3panelbodyplugin',
            name='attributes',
            field=djangocms_attributes_field.fields.AttributesField(default=dict, verbose_name='Attributes', blank=True),
        ),
        migrations.AddField(
            model_name='boostrap3panelfooterplugin',
            name='attributes',
            field=djangocms_attributes_field.fields.AttributesField(default=dict, verbose_name='Attributes', blank=True),
        ),
        migrations.AddField(
            model_name='boostrap3panelheadingplugin',
            name='attributes',
            field=djangocms_attributes_field.fields.AttributesField(default=dict, verbose_name='Attributes', blank=True),
        ),
        migrations.AddField(
            model_name='boostrap3panelplugin',
            name='attributes',
            field=djangocms_attributes_field.fields.AttributesField(default=dict, verbose_name='Attributes', blank=True),
        ),
        migrations.AddField(
            model_name='boostrap3spacerplugin',
            name='attributes',
            field=djangocms_attributes_field.fields.AttributesField(default=dict, verbose_name='Attributes', blank=True),
        ),
        migrations.AddField(
            model_name='boostrap3wellplugin',
            name='attributes',
            field=djangocms_attributes_field.fields.AttributesField(default=dict, verbose_name='Attributes', blank=True),
        ),
        migrations.AddField(
            model_name='bootstrap3accordionitemplugin',
            name='attributes',
            field=djangocms_attributes_field.fields.AttributesField(default=dict, verbose_name='Attributes', blank=True),
        ),
        migrations.AddField(
            model_name='bootstrap3accordionplugin',
            name='attributes',
            field=djangocms_attributes_field.fields.AttributesField(default=dict, verbose_name='Attributes', blank=True),
        ),
        migrations.AddField(
            model_name='bootstrap3carouselplugin',
            name='attributes',
            field=djangocms_attributes_field.fields.AttributesField(default=dict, verbose_name='Attributes', blank=True),
        ),
        migrations.AddField(
            model_name='bootstrap3columnplugin',
            name='attributes',
            field=djangocms_attributes_field.fields.AttributesField(default=dict, verbose_name='Attributes', blank=True),
        ),
        migrations.AddField(
            model_name='bootstrap3fileplugin',
            name='attributes',
            field=djangocms_attributes_field.fields.AttributesField(default=dict, verbose_name='Attributes', blank=True),
        ),
        migrations.AddField(
            model_name='bootstrap3listgroupitemplugin',
            name='attributes',
            field=djangocms_attributes_field.fields.AttributesField(default=dict, verbose_name='Attributes', blank=True),
        ),
        migrations.AddField(
            model_name='bootstrap3listgroupplugin',
            name='attributes',
            field=djangocms_attributes_field.fields.AttributesField(default=dict, verbose_name='Attributes', blank=True),
        ),
        migrations.AddField(
            model_name='bootstrap3rowplugin',
            name='attributes',
            field=djangocms_attributes_field.fields.AttributesField(default=dict, verbose_name='Attributes', blank=True),
        ),
        migrations.AlterField(
            model_name='boostrap3alertplugin',
            name='classes',
            field=aldryn_bootstrap3.model_fields.Classes(default='', help_text='Space separated classes that are added to the class. See <a href="http://getbootstrap.com/css/" target="_blank">Bootstrap 3 documentation</a>.', verbose_name='Classes', blank=True),
        ),
        migrations.AlterField(
            model_name='boostrap3alertplugin',
            name='cmsplugin_ptr',
            field=models.OneToOneField(parent_link=True, related_name='aldryn_bootstrap3_boostrap3alertplugin', primary_key=True, serialize=False, to='cms.CMSPlugin'),
        ),
        migrations.AlterField(
            model_name='boostrap3alertplugin',
            name='icon',
            field=aldryn_bootstrap3.model_fields.Icon(default='', max_length=255, verbose_name='Title icon', blank=True),
        ),
        migrations.AlterField(
            model_name='boostrap3blockquoteplugin',
            name='classes',
            field=aldryn_bootstrap3.model_fields.Classes(default='', help_text='Space separated classes that are added to the class. See <a href="http://getbootstrap.com/css/" target="_blank">Bootstrap 3 documentation</a>.', verbose_name='Classes', blank=True),
        ),
        migrations.AlterField(
            model_name='boostrap3blockquoteplugin',
            name='cmsplugin_ptr',
            field=models.OneToOneField(parent_link=True, related_name='aldryn_bootstrap3_boostrap3blockquoteplugin', primary_key=True, serialize=False, to='cms.CMSPlugin'),
        ),
        migrations.AlterField(
            model_name='boostrap3blockquoteplugin',
            name='reverse',
            field=models.BooleanField(default=False, help_text='Reversing the position by adding the Bootstrap 3 "blockquote-reverse" class.', verbose_name='Reverse quote'),
        ),
        migrations.AlterField(
            model_name='boostrap3buttonplugin',
            name='btn_block',
            field=models.BooleanField(default=False, verbose_name='Block'),
        ),
        migrations.AlterField(
            model_name='boostrap3buttonplugin',
            name='btn_context',
            field=aldryn_bootstrap3.model_fields.Context(default='default', max_length=255, verbose_name='Context', choices=[('default', 'Default'), ('primary', 'Primary'), ('success', 'Success'), ('info', 'Info'), ('warning', 'Warning'), ('danger', 'Danger'), ('link', 'Link')]),
        ),
        migrations.AlterField(
            model_name='boostrap3buttonplugin',
            name='btn_size',
            field=aldryn_bootstrap3.model_fields.Size(default='md', max_length=255, verbose_name='Size', blank=True),
        ),
        migrations.AlterField(
            model_name='boostrap3buttonplugin',
            name='classes',
            field=aldryn_bootstrap3.model_fields.Classes(default='', help_text='Space separated classes that are added to the class. See <a href="http://getbootstrap.com/css/" target="_blank">Bootstrap 3 documentation</a>.', verbose_name='Classes', blank=True),
        ),
        migrations.AlterField(
            model_name='boostrap3buttonplugin',
            name='cmsplugin_ptr',
            field=models.OneToOneField(parent_link=True, related_name='aldryn_bootstrap3_boostrap3buttonplugin', primary_key=True, serialize=False, to='cms.CMSPlugin'),
        ),
        migrations.AlterField(
            model_name='boostrap3buttonplugin',
            name='icon_left',
            field=aldryn_bootstrap3.model_fields.Icon(default='', max_length=255, verbose_name='Icon left', blank=True),
        ),
        migrations.AlterField(
            model_name='boostrap3buttonplugin',
            name='icon_right',
            field=aldryn_bootstrap3.model_fields.Icon(default='', max_length=255, verbose_name='Icon right', blank=True),
        ),
        migrations.AlterField(
            model_name='boostrap3buttonplugin',
            name='label',
            field=models.CharField(default='', max_length=255, verbose_name='Display name', blank=True),
        ),
        migrations.AlterField(
            model_name='boostrap3buttonplugin',
            name='link_anchor',
            field=models.CharField(help_text='Appends the value only after the internal or external link. Do <em>not</em> include a preceding "#" symbol.', max_length=255, verbose_name='Anchor', blank=True),
        ),
        migrations.AlterField(
            model_name='boostrap3buttonplugin',
            name='link_attributes',
            field=djangocms_attributes_field.fields.AttributesField(default=dict, verbose_name='Attributes', blank=True),
        ),
        migrations.AlterField(
            model_name='boostrap3buttonplugin',
            name='link_mailto',
            field=models.EmailField(max_length=255, null=True, verbose_name='Email address', blank=True),
        ),
        migrations.AlterField(
            model_name='boostrap3buttonplugin',
            name='link_page',
            field=cms.models.fields.PageField(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='cms.Page', help_text='If provided, overrides the external link.', null=True, verbose_name='Internal link'),
        ),
        migrations.AlterField(
            model_name='boostrap3buttonplugin',
            name='link_phone',
            field=models.CharField(max_length=255, null=True, verbose_name='Phone', blank=True),
        ),
        migrations.AlterField(
            model_name='boostrap3buttonplugin',
            name='link_target',
            field=models.CharField(blank=True, max_length=255, verbose_name='Target', choices=[('_blank', 'Open in new window'), ('_self', 'Open in same window'), ('_parent', 'Delegate to parent'), ('_top', 'Delegate to top')]),
        ),
        migrations.AlterField(
            model_name='boostrap3buttonplugin',
            name='link_url',
            field=models.URLField(default='', help_text='Provide a valid URL to an external website.', verbose_name='External link', blank=True),
        ),
        migrations.AlterField(
            model_name='boostrap3buttonplugin',
            name='txt_context',
            field=aldryn_bootstrap3.model_fields.Context(default='', max_length=255, verbose_name='Context', blank=True, choices=[('', 'Default'), ('primary', 'Primary'), ('success', 'Success'), ('info', 'Info'), ('warning', 'Warning'), ('danger', 'Danger'), ('muted ', 'Muted')]),
        ),
        migrations.AlterField(
            model_name='boostrap3buttonplugin',
            name='type',
            field=aldryn_bootstrap3.model_fields.LinkOrButton(default='lnk', max_length=255, verbose_name='Type'),
        ),
        migrations.AlterField(
            model_name='boostrap3iconplugin',
            name='classes',
            field=aldryn_bootstrap3.model_fields.Classes(default='', help_text='Space separated classes that are added to the class. See <a href="http://getbootstrap.com/css/" target="_blank">Bootstrap 3 documentation</a>.', verbose_name='Classes', blank=True),
        ),
        migrations.AlterField(
            model_name='boostrap3iconplugin',
            name='cmsplugin_ptr',
            field=models.OneToOneField(parent_link=True, related_name='aldryn_bootstrap3_boostrap3iconplugin', primary_key=True, serialize=False, to='cms.CMSPlugin'),
        ),
        migrations.AlterField(
            model_name='boostrap3imageplugin',
            name='alt',
            field=aldryn_bootstrap3.model_fields.MiniText(default='', verbose_name='Alternative text', blank=True),
        ),
        migrations.AlterField(
            model_name='boostrap3imageplugin',
            name='aspect_ratio',
            field=models.CharField(default='', choices=[('1x1', '1x1'), ('4x3', '4x3'), ('16x9', '16x9'), ('16x10', '16x10'), ('21x9', '21x9'), ('3x4', '3x4'), ('9x16', '9x16'), ('10x16', '10x16'), ('9x21', '9x21')], max_length=255, blank=True, help_text='Influences width height of the image according to the selected ratio.', verbose_name='Aspect ratio'),
        ),
        migrations.AlterField(
            model_name='boostrap3imageplugin',
            name='classes',
            field=aldryn_bootstrap3.model_fields.Classes(default='', help_text='Space separated classes that are added to the class. See <a href="http://getbootstrap.com/css/" target="_blank">Bootstrap 3 documentation</a>.', verbose_name='Classes', blank=True),
        ),
        migrations.AlterField(
            model_name='boostrap3imageplugin',
            name='cmsplugin_ptr',
            field=models.OneToOneField(parent_link=True, related_name='aldryn_bootstrap3_boostrap3imageplugin', primary_key=True, serialize=False, to='cms.CMSPlugin'),
        ),
        migrations.AlterField(
            model_name='boostrap3imageplugin',
            name='file',
            field=filer.fields.image.FilerImageField(related_name='+', on_delete=django.db.models.deletion.SET_NULL, verbose_name='Image', to='filer.Image', null=True),
        ),
        migrations.AlterField(
            model_name='boostrap3imageplugin',
            name='img_responsive',
            field=models.BooleanField(default=True, help_text='whether to treat the image as using 100% width of the parent container (sets the img-responsive class).', verbose_name='.img-responsive'),
        ),
        migrations.AlterField(
            model_name='boostrap3imageplugin',
            name='override_height',
            field=models.IntegerField(help_text='The image height as number in pixels. Example: "720" and not "720px".', null=True, verbose_name='Override height', blank=True),
        ),
        migrations.AlterField(
            model_name='boostrap3imageplugin',
            name='override_width',
            field=models.IntegerField(help_text='The image width as number in pixels. Example: "720" and not "720px".', null=True, verbose_name='Override width', blank=True),
        ),
        migrations.AlterField(
            model_name='boostrap3imageplugin',
            name='shape',
            field=models.CharField(default='', max_length=255, verbose_name='Shape', blank=True, choices=[('rounded', '.img-rounded'), ('circle', '.img-circle')]),
        ),
        migrations.AlterField(
            model_name='boostrap3imageplugin',
            name='thumbnail',
            field=models.BooleanField(default=False, help_text='Adds the Bootstrap 3 ".img-thumbnail" class.', verbose_name='.img-thumbnail'),
        ),
        migrations.AlterField(
            model_name='boostrap3imageplugin',
            name='title',
            field=aldryn_bootstrap3.model_fields.MiniText(default='', verbose_name='Title', blank=True),
        ),
        migrations.AlterField(
            model_name='boostrap3imageplugin',
            name='use_original_image',
            field=models.BooleanField(default=False, help_text='Outputs the raw image without cropping.', verbose_name='Use original image'),
        ),
        migrations.AlterField(
            model_name='boostrap3labelplugin',
            name='classes',
            field=aldryn_bootstrap3.model_fields.Classes(default='', help_text='Space separated classes that are added to the class. See <a href="http://getbootstrap.com/css/" target="_blank">Bootstrap 3 documentation</a>.', verbose_name='Classes', blank=True),
        ),
        migrations.AlterField(
            model_name='boostrap3labelplugin',
            name='cmsplugin_ptr',
            field=models.OneToOneField(parent_link=True, related_name='aldryn_bootstrap3_boostrap3labelplugin', primary_key=True, serialize=False, to='cms.CMSPlugin'),
        ),
        migrations.AlterField(
            model_name='boostrap3labelplugin',
            name='label',
            field=models.CharField(default='', max_length=255, verbose_name='Label', blank=True),
        ),
        migrations.AlterField(
            model_name='boostrap3panelbodyplugin',
            name='classes',
            field=aldryn_bootstrap3.model_fields.Classes(default='', help_text='Space separated classes that are added to the class. See <a href="http://getbootstrap.com/css/" target="_blank">Bootstrap 3 documentation</a>.', verbose_name='Classes', blank=True),
        ),
        migrations.AlterField(
            model_name='boostrap3panelbodyplugin',
            name='cmsplugin_ptr',
            field=models.OneToOneField(parent_link=True, related_name='aldryn_bootstrap3_boostrap3panelbodyplugin', primary_key=True, serialize=False, to='cms.CMSPlugin'),
        ),
        migrations.AlterField(
            model_name='boostrap3panelfooterplugin',
            name='classes',
            field=aldryn_bootstrap3.model_fields.Classes(default='', help_text='Space separated classes that are added to the class. See <a href="http://getbootstrap.com/css/" target="_blank">Bootstrap 3 documentation</a>.', verbose_name='Classes', blank=True),
        ),
        migrations.AlterField(
            model_name='boostrap3panelfooterplugin',
            name='cmsplugin_ptr',
            field=models.OneToOneField(parent_link=True, related_name='aldryn_bootstrap3_boostrap3panelfooterplugin', primary_key=True, serialize=False, to='cms.CMSPlugin'),
        ),
        migrations.AlterField(
            model_name='boostrap3panelheadingplugin',
            name='classes',
            field=aldryn_bootstrap3.model_fields.Classes(default='', help_text='Space separated classes that are added to the class. See <a href="http://getbootstrap.com/css/" target="_blank">Bootstrap 3 documentation</a>.', verbose_name='Classes', blank=True),
        ),
        migrations.AlterField(
            model_name='boostrap3panelheadingplugin',
            name='cmsplugin_ptr',
            field=models.OneToOneField(parent_link=True, related_name='aldryn_bootstrap3_boostrap3panelheadingplugin', primary_key=True, serialize=False, to='cms.CMSPlugin'),
        ),
        migrations.AlterField(
            model_name='boostrap3panelheadingplugin',
            name='title',
            field=aldryn_bootstrap3.model_fields.MiniText(default='', help_text='Panels can have additional plugins.', verbose_name='Title', blank=True),
        ),
        migrations.AlterField(
            model_name='boostrap3panelplugin',
            name='classes',
            field=aldryn_bootstrap3.model_fields.Classes(default='', help_text='Space separated classes that are added to the class. See <a href="http://getbootstrap.com/css/" target="_blank">Bootstrap 3 documentation</a>.', verbose_name='Classes', blank=True),
        ),
        migrations.AlterField(
            model_name='boostrap3panelplugin',
            name='cmsplugin_ptr',
            field=models.OneToOneField(parent_link=True, related_name='aldryn_bootstrap3_boostrap3panelplugin', primary_key=True, serialize=False, to='cms.CMSPlugin'),
        ),
        migrations.AlterField(
            model_name='boostrap3spacerplugin',
            name='classes',
            field=aldryn_bootstrap3.model_fields.Classes(default='', help_text='Space separated classes that are added to the class. See <a href="http://getbootstrap.com/css/" target="_blank">Bootstrap 3 documentation</a>.', verbose_name='Classes', blank=True),
        ),
        migrations.AlterField(
            model_name='boostrap3spacerplugin',
            name='cmsplugin_ptr',
            field=models.OneToOneField(parent_link=True, related_name='aldryn_bootstrap3_boostrap3spacerplugin', primary_key=True, serialize=False, to='cms.CMSPlugin'),
        ),
        migrations.AlterField(
            model_name='boostrap3spacerplugin',
            name='size',
            field=aldryn_bootstrap3.model_fields.Size(default='md', max_length=255, verbose_name='Size', blank=True),
        ),
        migrations.AlterField(
            model_name='boostrap3wellplugin',
            name='classes',
            field=aldryn_bootstrap3.model_fields.Classes(default='', help_text='Space separated classes that are added to the class. See <a href="http://getbootstrap.com/css/" target="_blank">Bootstrap 3 documentation</a>.', verbose_name='Classes', blank=True),
        ),
        migrations.AlterField(
            model_name='boostrap3wellplugin',
            name='cmsplugin_ptr',
            field=models.OneToOneField(parent_link=True, related_name='aldryn_bootstrap3_boostrap3wellplugin', primary_key=True, serialize=False, to='cms.CMSPlugin'),
        ),
        migrations.AlterField(
            model_name='boostrap3wellplugin',
            name='size',
            field=aldryn_bootstrap3.model_fields.Size(default='md', max_length=255, verbose_name='Size', blank=True),
        ),
        migrations.AlterField(
            model_name='bootstrap3accordionitemplugin',
            name='classes',
            field=aldryn_bootstrap3.model_fields.Classes(default='', help_text='Space separated classes that are added to the class. See <a href="http://getbootstrap.com/css/" target="_blank">Bootstrap 3 documentation</a>.', verbose_name='Classes', blank=True),
        ),
        migrations.AlterField(
            model_name='bootstrap3accordionitemplugin',
            name='cmsplugin_ptr',
            field=models.OneToOneField(parent_link=True, related_name='aldryn_bootstrap3_bootstrap3accordionitemplugin', primary_key=True, serialize=False, to='cms.CMSPlugin'),
        ),
        migrations.AlterField(
            model_name='bootstrap3accordionitemplugin',
            name='title',
            field=aldryn_bootstrap3.model_fields.MiniText(default='', verbose_name='Title', blank=True),
        ),
        migrations.AlterField(
            model_name='bootstrap3accordionplugin',
            name='classes',
            field=aldryn_bootstrap3.model_fields.Classes(default='', help_text='Space separated classes that are added to the class. See <a href="http://getbootstrap.com/css/" target="_blank">Bootstrap 3 documentation</a>.', verbose_name='Classes', blank=True),
        ),
        migrations.AlterField(
            model_name='bootstrap3accordionplugin',
            name='cmsplugin_ptr',
            field=models.OneToOneField(parent_link=True, related_name='aldryn_bootstrap3_bootstrap3accordionplugin', primary_key=True, serialize=False, to='cms.CMSPlugin'),
        ),
        migrations.AlterField(
            model_name='bootstrap3accordionplugin',
            name='index',
            field=models.PositiveIntegerField(help_text='Index of element that should be opened on page load (leave it empty if none of the items should be opened)', null=True, verbose_name='Index', blank=True),
        ),
        migrations.AlterField(
            model_name='bootstrap3carouselplugin',
            name='aspect_ratio',
            field=models.CharField(default='', max_length=255, verbose_name='Aspect ratio', blank=True, choices=[('1x1', '1x1'), ('4x3', '4x3'), ('16x9', '16x9'), ('16x10', '16x10'), ('21x9', '21x9'), ('3x4', '3x4'), ('9x16', '9x16'), ('10x16', '10x16'), ('9x21', '9x21')]),
        ),
        migrations.AlterField(
            model_name='bootstrap3carouselplugin',
            name='classes',
            field=aldryn_bootstrap3.model_fields.Classes(default='', help_text='Space separated classes that are added to the class. See <a href="http://getbootstrap.com/css/" target="_blank">Bootstrap 3 documentation</a>.', verbose_name='Classes', blank=True),
        ),
        migrations.AlterField(
            model_name='bootstrap3carouselplugin',
            name='cmsplugin_ptr',
            field=models.OneToOneField(parent_link=True, related_name='aldryn_bootstrap3_bootstrap3carouselplugin', primary_key=True, serialize=False, to='cms.CMSPlugin'),
        ),
        migrations.AlterField(
            model_name='bootstrap3carouselplugin',
            name='pause',
            field=models.BooleanField(default=True, help_text='Pauses the cycling of the carousel on mouseenter and resumes the cycling of the carousel on mouseleave.', verbose_name='Pause'),
        ),
        migrations.AlterField(
            model_name='bootstrap3carouselplugin',
            name='style',
            field=models.CharField(default='standard', max_length=255, verbose_name='Style', choices=[('standard', 'Standard')]),
        ),
        migrations.AlterField(
            model_name='bootstrap3carouselplugin',
            name='transition_effect',
            field=models.CharField(default='', max_length=255, verbose_name='Transition effect', blank=True, choices=[('slide', 'Slide')]),
        ),
        migrations.AlterField(
            model_name='bootstrap3carouselplugin',
            name='wrap',
            field=models.BooleanField(default=True, help_text='Whether the carousel should cycle continuously or have hard stops.', verbose_name='Wrap'),
        ),
        migrations.AlterField(
            model_name='bootstrap3carouselslidefolderplugin',
            name='classes',
            field=aldryn_bootstrap3.model_fields.Classes(default='', help_text='Space separated classes that are added to the class. See <a href="http://getbootstrap.com/css/" target="_blank">Bootstrap 3 documentation</a>.', verbose_name='Classes', blank=True),
        ),
        migrations.AlterField(
            model_name='bootstrap3carouselslidefolderplugin',
            name='cmsplugin_ptr',
            field=models.OneToOneField(parent_link=True, related_name='aldryn_bootstrap3_bootstrap3carouselslidefolderplugin', primary_key=True, serialize=False, to='cms.CMSPlugin'),
        ),
        migrations.AlterField(
            model_name='bootstrap3carouselslidefolderplugin',
            name='folder',
            field=filer.fields.folder.FilerFolderField(verbose_name='Folder', to='filer.Folder'),
        ),
        migrations.AlterField(
            model_name='bootstrap3carouselslideplugin',
            name='classes',
            field=aldryn_bootstrap3.model_fields.Classes(default='', help_text='Space separated classes that are added to the class. See <a href="http://getbootstrap.com/css/" target="_blank">Bootstrap 3 documentation</a>.', verbose_name='Classes', blank=True),
        ),
        migrations.AlterField(
            model_name='bootstrap3carouselslideplugin',
            name='cmsplugin_ptr',
            field=models.OneToOneField(parent_link=True, related_name='aldryn_bootstrap3_bootstrap3carouselslideplugin', primary_key=True, serialize=False, to='cms.CMSPlugin'),
        ),
        migrations.AlterField(
            model_name='bootstrap3carouselslideplugin',
            name='image',
            field=filer.fields.image.FilerImageField(related_name='+', on_delete=django.db.models.deletion.SET_NULL, verbose_name='Image', to='filer.Image', null=True),
        ),
        migrations.AlterField(
            model_name='bootstrap3carouselslideplugin',
            name='link_anchor',
            field=models.CharField(help_text='Appends the value only after the internal or external link. Do <em>not</em> include a preceding "#" symbol.', max_length=255, verbose_name='Anchor', blank=True),
        ),
        migrations.AlterField(
            model_name='bootstrap3carouselslideplugin',
            name='link_attributes',
            field=djangocms_attributes_field.fields.AttributesField(default=dict, verbose_name='Attributes', blank=True),
        ),
        migrations.AlterField(
            model_name='bootstrap3carouselslideplugin',
            name='link_mailto',
            field=models.EmailField(max_length=255, null=True, verbose_name='Email address', blank=True),
        ),
        migrations.AlterField(
            model_name='bootstrap3carouselslideplugin',
            name='link_page',
            field=cms.models.fields.PageField(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='cms.Page', help_text='If provided, overrides the external link.', null=True, verbose_name='Internal link'),
        ),
        migrations.AlterField(
            model_name='bootstrap3carouselslideplugin',
            name='link_phone',
            field=models.CharField(max_length=255, null=True, verbose_name='Phone', blank=True),
        ),
        migrations.AlterField(
            model_name='bootstrap3carouselslideplugin',
            name='link_target',
            field=models.CharField(blank=True, max_length=255, verbose_name='Target', choices=[('_blank', 'Open in new window'), ('_self', 'Open in same window'), ('_parent', 'Delegate to parent'), ('_top', 'Delegate to top')]),
        ),
        migrations.AlterField(
            model_name='bootstrap3carouselslideplugin',
            name='link_text',
            field=models.CharField(max_length=255, verbose_name='Link text', blank=True),
        ),
        migrations.AlterField(
            model_name='bootstrap3carouselslideplugin',
            name='link_url',
            field=models.URLField(default='', help_text='Provide a valid URL to an external website.', verbose_name='External link', blank=True),
        ),
        migrations.AlterField(
            model_name='bootstrap3columnplugin',
            name='classes',
            field=aldryn_bootstrap3.model_fields.Classes(default='', help_text='Space separated classes that are added to the class. See <a href="http://getbootstrap.com/css/" target="_blank">Bootstrap 3 documentation</a>.', verbose_name='Classes', blank=True),
        ),
        migrations.AlterField(
            model_name='bootstrap3columnplugin',
            name='cmsplugin_ptr',
            field=models.OneToOneField(parent_link=True, related_name='aldryn_bootstrap3_bootstrap3columnplugin', primary_key=True, serialize=False, to='cms.CMSPlugin'),
        ),
        migrations.AlterField(
            model_name='bootstrap3columnplugin',
            name='tag',
            field=models.SlugField(default='div', verbose_name='Tag'),
        ),
        migrations.AlterField(
            model_name='bootstrap3fileplugin',
            name='classes',
            field=aldryn_bootstrap3.model_fields.Classes(default='', help_text='Space separated classes that are added to the class. See <a href="http://getbootstrap.com/css/" target="_blank">Bootstrap 3 documentation</a>.', verbose_name='Classes', blank=True),
        ),
        migrations.AlterField(
            model_name='bootstrap3fileplugin',
            name='cmsplugin_ptr',
            field=models.OneToOneField(parent_link=True, related_name='aldryn_bootstrap3_bootstrap3fileplugin', primary_key=True, serialize=False, to='cms.CMSPlugin'),
        ),
        migrations.AlterField(
            model_name='bootstrap3fileplugin',
            name='file',
            field=filer.fields.file.FilerFileField(related_name='+', on_delete=django.db.models.deletion.SET_NULL, verbose_name='File', to='filer.File', null=True),
        ),
        migrations.AlterField(
            model_name='bootstrap3fileplugin',
            name='name',
            field=aldryn_bootstrap3.model_fields.MiniText(default='', verbose_name='Name', blank=True),
        ),
        migrations.AlterField(
            model_name='bootstrap3fileplugin',
            name='open_new_window',
            field=models.BooleanField(default=False, verbose_name='Open in new window'),
        ),
        migrations.AlterField(
            model_name='bootstrap3fileplugin',
            name='show_file_size',
            field=models.BooleanField(default=False, verbose_name='Show file size'),
        ),
        migrations.AlterField(
            model_name='bootstrap3listgroupitemplugin',
            name='classes',
            field=aldryn_bootstrap3.model_fields.Classes(default='', help_text='Space separated classes that are added to the class. See <a href="http://getbootstrap.com/css/" target="_blank">Bootstrap 3 documentation</a>.', verbose_name='Classes', blank=True),
        ),
        migrations.AlterField(
            model_name='bootstrap3listgroupitemplugin',
            name='cmsplugin_ptr',
            field=models.OneToOneField(parent_link=True, related_name='aldryn_bootstrap3_bootstrap3listgroupitemplugin', primary_key=True, serialize=False, to='cms.CMSPlugin'),
        ),
        migrations.AlterField(
            model_name='bootstrap3listgroupitemplugin',
            name='context',
            field=aldryn_bootstrap3.model_fields.Context(default='default', max_length=255, verbose_name='Context', choices=[('default', 'Default'), ('primary', 'Primary'), ('success', 'Success'), ('info', 'Info'), ('warning', 'Warning'), ('danger', 'Danger')]),
        ),
        migrations.AlterField(
            model_name='bootstrap3listgroupitemplugin',
            name='state',
            field=models.CharField(blank=True, max_length=255, verbose_name='State', choices=[('active', 'Active'), ('disabled', 'Disabled')]),
        ),
        migrations.AlterField(
            model_name='bootstrap3listgroupitemplugin',
            name='title',
            field=aldryn_bootstrap3.model_fields.MiniText(default='', verbose_name='Title', blank=True),
        ),
        migrations.AlterField(
            model_name='bootstrap3listgroupplugin',
            name='add_list_group_class',
            field=models.BooleanField(default=True, help_text='Whether to add the list-group and subsequent list-group-item classes.', verbose_name='.list-group'),
        ),
        migrations.AlterField(
            model_name='bootstrap3listgroupplugin',
            name='classes',
            field=aldryn_bootstrap3.model_fields.Classes(default='', help_text='Space separated classes that are added to the class. See <a href="http://getbootstrap.com/css/" target="_blank">Bootstrap 3 documentation</a>.', verbose_name='Classes', blank=True),
        ),
        migrations.AlterField(
            model_name='bootstrap3listgroupplugin',
            name='cmsplugin_ptr',
            field=models.OneToOneField(parent_link=True, related_name='aldryn_bootstrap3_bootstrap3listgroupplugin', primary_key=True, serialize=False, to='cms.CMSPlugin'),
        ),
        migrations.AlterField(
            model_name='bootstrap3rowplugin',
            name='classes',
            field=aldryn_bootstrap3.model_fields.Classes(default='', help_text='Space separated classes that are added to the class. See <a href="http://getbootstrap.com/css/" target="_blank">Bootstrap 3 documentation</a>.', verbose_name='Classes', blank=True),
        ),
        migrations.AlterField(
            model_name='bootstrap3rowplugin',
            name='cmsplugin_ptr',
            field=models.OneToOneField(parent_link=True, related_name='aldryn_bootstrap3_bootstrap3rowplugin', primary_key=True, serialize=False, to='cms.CMSPlugin'),
        ),
    ]
