# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filer.fields.file
import filer.fields.folder
import filer.fields.image
import aldryn_bootstrap3.model_fields
import djangocms_text_ckeditor.fields
import django.db.models.deletion
import cms.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0002_auto_20150606_2003'),
        ('cms', '0011_auto_20150419_1006'),
    ]

    operations = [
        migrations.CreateModel(
            name='Boostrap3AlertPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='+', primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('context', aldryn_bootstrap3.model_fields.Context(default='default', max_length=255)),
                ('icon', aldryn_bootstrap3.model_fields.Icon(default='', max_length=255, blank=True)),
                ('classes', aldryn_bootstrap3.model_fields.Classes(default='', help_text='space separated classes that are added to the class. see <a href="http://getbootstrap.com/css/" target="_blank">bootstrap docs</a>', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='Boostrap3BlockquotePlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='+', primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('reverse', models.BooleanField(default=False)),
                ('classes', aldryn_bootstrap3.model_fields.Classes(default='', help_text='space separated classes that are added to the class. see <a href="http://getbootstrap.com/css/" target="_blank">bootstrap docs</a>', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='Boostrap3ButtonPlugin',
            fields=[
                ('link_url', models.URLField(default='', verbose_name='link', blank=True)),
                ('link_anchor', models.CharField(help_text='Adds this value as an anchor (#my-anchor) to the link.', max_length=128, verbose_name='anchor', blank=True)),
                ('link_mailto', models.EmailField(max_length=75, null=True, verbose_name='mailto', blank=True)),
                ('link_phone', models.CharField(max_length=40, null=True, verbose_name='Phone', blank=True)),
                ('link_target', models.CharField(blank=True, max_length=100, verbose_name='target', choices=[('', 'same window'), ('_blank', 'new window'), ('_parent', 'parent window'), ('_top', 'topmost frame')])),
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='+', primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('label', models.CharField(default='', max_length=256, verbose_name='label', blank=True)),
                ('type', aldryn_bootstrap3.model_fields.LinkOrButton(default='lnk', max_length=10)),
                ('btn_context', aldryn_bootstrap3.model_fields.Context(default='default', max_length=255, verbose_name='context', blank=True, choices=[('default', 'Default'), ('primary', 'Primary'), ('success', 'Success'), ('info', 'Info'), ('warning', 'Warning'), ('danger', 'Danger'), ('link', 'Link Button'), ('', 'Custom')])),
                ('btn_size', aldryn_bootstrap3.model_fields.Size(default='md', max_length=255, verbose_name='size', blank=True)),
                ('btn_block', models.BooleanField(default=False, verbose_name='block')),
                ('txt_context', aldryn_bootstrap3.model_fields.Context(default='', max_length=255, verbose_name='context', blank=True, choices=[('', 'None'), ('primary', 'Primary'), ('success', 'Success'), ('info', 'Info'), ('warning', 'Warning'), ('danger', 'Danger'), ('muted', 'Muted')])),
                ('icon_left', aldryn_bootstrap3.model_fields.Icon(default='', max_length=255, blank=True)),
                ('icon_right', aldryn_bootstrap3.model_fields.Icon(default='', max_length=255, blank=True)),
                ('classes', aldryn_bootstrap3.model_fields.Classes(default='', help_text='space separated classes that are added to the class. see <a href="http://getbootstrap.com/css/" target="_blank">bootstrap docs</a>', blank=True)),
                ('responsive', aldryn_bootstrap3.model_fields.Responsive(default='', blank=True)),
                ('responsive_print', aldryn_bootstrap3.model_fields.ResponsivePrint(default='', blank=True)),
                ('link_file', filer.fields.file.FilerFileField(on_delete=django.db.models.deletion.SET_NULL, verbose_name='file', blank=True, to='filer.File', null=True)),
                ('link_page', cms.models.fields.PageField(on_delete=django.db.models.deletion.SET_NULL, verbose_name='page', blank=True, to='cms.Page', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin', models.Model),
        ),
        migrations.CreateModel(
            name='Boostrap3IconPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='+', primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('icon', aldryn_bootstrap3.model_fields.Icon(default='', max_length=255, blank=True)),
                ('classes', aldryn_bootstrap3.model_fields.Classes(default='', help_text='space separated classes that are added to the class. see <a href="http://getbootstrap.com/css/" target="_blank">bootstrap docs</a>', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='Boostrap3ImagePlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='+', primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('alt', aldryn_bootstrap3.model_fields.MiniText(default='', verbose_name='alt', blank=True)),
                ('title', aldryn_bootstrap3.model_fields.MiniText(default='', verbose_name='title', blank=True)),
                ('aspect_ratio', models.CharField(default='', max_length=10, verbose_name='aspect ratio', blank=True, choices=[('1x1', '1x1'), ('4x3', '4x3'), ('16x9', '16x9'), ('16x10', '16x10'), ('21x9', '21x9'), ('1x1', '1x1'), ('3x4', '3x4'), ('9x16', '9x16'), ('10x16', '10x16'), ('9x21', '9x21')])),
                ('thumbnail', models.BooleanField(default=False, help_text="add the 'thumbnail' border", verbose_name='thumbnail')),
                ('shape', models.CharField(default='', max_length=64, verbose_name='shape', blank=True, choices=[('rounded', 'rounded'), ('circle', 'circle')])),
                ('classes', aldryn_bootstrap3.model_fields.Classes(default='', help_text='space separated classes that are added to the class. see <a href="http://getbootstrap.com/css/" target="_blank">bootstrap docs</a>', blank=True)),
                ('img_responsive', models.BooleanField(default=True, help_text='whether to treat the image as using 100% width of the parent container (sets the img-responsive class).', verbose_name='class: img-responsive')),
                ('file', filer.fields.image.FilerImageField(related_name='+', on_delete=django.db.models.deletion.SET_NULL, verbose_name='file', blank=True, to='filer.Image', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='Boostrap3LabelPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='+', primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('label', models.CharField(default='', max_length=256, verbose_name='label', blank=True)),
                ('context', aldryn_bootstrap3.model_fields.Context(default='default', max_length=255, choices=[('default', 'Default'), ('primary', 'Primary'), ('success', 'Success'), ('info', 'Info'), ('warning', 'Warning'), ('danger', 'Danger')])),
                ('classes', aldryn_bootstrap3.model_fields.Classes(default='', help_text='space separated classes that are added to the class. see <a href="http://getbootstrap.com/css/" target="_blank">bootstrap docs</a>', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='Boostrap3PanelBodyPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='+', primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('classes', aldryn_bootstrap3.model_fields.Classes(default='', help_text='space separated classes that are added to the class. see <a href="http://getbootstrap.com/css/" target="_blank">bootstrap docs</a>', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='Boostrap3PanelFooterPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='+', primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('classes', aldryn_bootstrap3.model_fields.Classes(default='', help_text='space separated classes that are added to the class. see <a href="http://getbootstrap.com/css/" target="_blank">bootstrap docs</a>', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='Boostrap3PanelHeadingPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='+', primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('title', aldryn_bootstrap3.model_fields.MiniText(default='', help_text='Alternatively you can add plugins', verbose_name='title', blank=True)),
                ('classes', aldryn_bootstrap3.model_fields.Classes(default='', help_text='space separated classes that are added to the class. see <a href="http://getbootstrap.com/css/" target="_blank">bootstrap docs</a>', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='Boostrap3PanelPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='+', primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('context', aldryn_bootstrap3.model_fields.Context(default='default', max_length=255, choices=[('default', 'Default'), ('primary', 'Primary'), ('success', 'Success'), ('info', 'Info'), ('warning', 'Warning'), ('danger', 'Danger')])),
                ('classes', aldryn_bootstrap3.model_fields.Classes(default='', help_text='space separated classes that are added to the class. see <a href="http://getbootstrap.com/css/" target="_blank">bootstrap docs</a>', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='Boostrap3SpacerPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='+', primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('size', aldryn_bootstrap3.model_fields.Size(default='md', max_length=255, blank=True)),
                ('classes', aldryn_bootstrap3.model_fields.Classes(default='', help_text='space separated classes that are added to the class. see <a href="http://getbootstrap.com/css/" target="_blank">bootstrap docs</a>', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='Boostrap3WellPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='+', primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('size', aldryn_bootstrap3.model_fields.Size(default='md', max_length=255, blank=True)),
                ('classes', aldryn_bootstrap3.model_fields.Classes(default='', help_text='space separated classes that are added to the class. see <a href="http://getbootstrap.com/css/" target="_blank">bootstrap docs</a>', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='Bootstrap3AccordionItemPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('title', aldryn_bootstrap3.model_fields.MiniText(default='', verbose_name='title', blank=True)),
                ('context', aldryn_bootstrap3.model_fields.Context(default='default', max_length=255, choices=[('default', 'Default'), ('primary', 'Primary'), ('success', 'Success'), ('info', 'Info'), ('warning', 'Warning'), ('danger', 'Danger')])),
                ('classes', aldryn_bootstrap3.model_fields.Classes(default='', help_text='space separated classes that are added to the class. see <a href="http://getbootstrap.com/css/" target="_blank">bootstrap docs</a>', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='Bootstrap3AccordionPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('index', models.PositiveIntegerField(help_text='index of element that should be opened on page load (leave it empty if none of the items should be opened)', null=True, verbose_name='index', blank=True)),
                ('classes', aldryn_bootstrap3.model_fields.Classes(default='', help_text='space separated classes that are added to the class. see <a href="http://getbootstrap.com/css/" target="_blank">bootstrap docs</a>', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='Bootstrap3CarouselPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('style', models.CharField(default='standard', max_length=50, verbose_name='Style', choices=[('standard', 'Standard')])),
                ('aspect_ratio', models.CharField(default='', max_length=10, verbose_name='aspect ratio', blank=True, choices=[('1x1', '1x1'), ('4x3', '4x3'), ('16x9', '16x9'), ('16x10', '16x10'), ('21x9', '21x9'), ('1x1', '1x1'), ('3x4', '3x4'), ('9x16', '9x16'), ('10x16', '10x16'), ('9x21', '9x21')])),
                ('transition_effect', models.CharField(default='', max_length=50, verbose_name='Transition Effect', blank=True, choices=[('slide', 'Slide')])),
                ('ride', models.BooleanField(default=True, help_text='Whether to mark the carousel as animating starting at page load.', verbose_name='Ride')),
                ('interval', models.IntegerField(default=5000, help_text='The amount of time to delay between automatically cycling an item.', verbose_name='Interval')),
                ('wrap', models.BooleanField(default=True, help_text='Whether the carousel should cycle continuously or have hard stops.')),
                ('pause', models.BooleanField(default=True, help_text='Pauses the cycling of the carousel on mouseenter and resumes the cycling of the carousel on mouseleave.')),
                ('classes', aldryn_bootstrap3.model_fields.Classes(default='', help_text='space separated classes that are added to the class. see <a href="http://getbootstrap.com/css/" target="_blank">bootstrap docs</a>', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='Bootstrap3CarouselSlideFolderPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('classes', aldryn_bootstrap3.model_fields.Classes(default='', help_text='space separated classes that are added to the class. see <a href="http://getbootstrap.com/css/" target="_blank">bootstrap docs</a>', blank=True)),
                ('folder', filer.fields.folder.FilerFolderField(verbose_name='folder', to='filer.Folder')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='Bootstrap3CarouselSlidePlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('link_url', models.URLField(default='', verbose_name='link', blank=True)),
                ('link_anchor', models.CharField(help_text='Adds this value as an anchor (#my-anchor) to the link.', max_length=128, verbose_name='anchor', blank=True)),
                ('link_mailto', models.EmailField(max_length=75, null=True, verbose_name='mailto', blank=True)),
                ('link_phone', models.CharField(max_length=40, null=True, verbose_name='Phone', blank=True)),
                ('link_target', models.CharField(blank=True, max_length=100, verbose_name='target', choices=[('', 'same window'), ('_blank', 'new window'), ('_parent', 'parent window'), ('_top', 'topmost frame')])),
                ('link_text', models.CharField(max_length=200, verbose_name='link text', blank=True)),
                ('content', djangocms_text_ckeditor.fields.HTMLField(default='', help_text='alternatively add sub plugins as content', verbose_name='Content', blank=True)),
                ('classes', aldryn_bootstrap3.model_fields.Classes(default='', help_text='space separated classes that are added to the class. see <a href="http://getbootstrap.com/css/" target="_blank">bootstrap docs</a>', blank=True)),
                ('image', filer.fields.image.FilerImageField(related_name='+', on_delete=django.db.models.deletion.SET_NULL, verbose_name='image', blank=True, to='filer.Image', null=True)),
                ('link_file', filer.fields.file.FilerFileField(on_delete=django.db.models.deletion.SET_NULL, verbose_name='file', blank=True, to='filer.File', null=True)),
                ('link_page', cms.models.fields.PageField(on_delete=django.db.models.deletion.SET_NULL, verbose_name='page', blank=True, to='cms.Page', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin', models.Model),
        ),
        migrations.CreateModel(
            name='Bootstrap3ColumnPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('classes', aldryn_bootstrap3.model_fields.Classes(default='', help_text='space separated classes that are added to the class. see <a href="http://getbootstrap.com/css/" target="_blank">bootstrap docs</a>', blank=True)),
                ('tag', models.SlugField(default='div')),
                ('xs_col', aldryn_bootstrap3.model_fields.IntegerField(default=None, null=True, verbose_name='col-xs-', blank=True)),
                ('xs_offset', aldryn_bootstrap3.model_fields.IntegerField(default=None, null=True, verbose_name='offset-', blank=True)),
                ('xs_push', aldryn_bootstrap3.model_fields.IntegerField(default=None, null=True, verbose_name='push-', blank=True)),
                ('xs_pull', aldryn_bootstrap3.model_fields.IntegerField(default=None, null=True, verbose_name='pull-', blank=True)),
                ('sm_col', aldryn_bootstrap3.model_fields.IntegerField(default=None, null=True, verbose_name='col-sm-', blank=True)),
                ('sm_offset', aldryn_bootstrap3.model_fields.IntegerField(default=None, null=True, verbose_name='offset-', blank=True)),
                ('sm_push', aldryn_bootstrap3.model_fields.IntegerField(default=None, null=True, verbose_name='push-', blank=True)),
                ('sm_pull', aldryn_bootstrap3.model_fields.IntegerField(default=None, null=True, verbose_name='pull-', blank=True)),
                ('md_col', aldryn_bootstrap3.model_fields.IntegerField(default=None, null=True, verbose_name='col-md-', blank=True)),
                ('md_offset', aldryn_bootstrap3.model_fields.IntegerField(default=None, null=True, verbose_name='offset-', blank=True)),
                ('md_push', aldryn_bootstrap3.model_fields.IntegerField(default=None, null=True, verbose_name='push-', blank=True)),
                ('md_pull', aldryn_bootstrap3.model_fields.IntegerField(default=None, null=True, verbose_name='pull-', blank=True)),
                ('lg_col', aldryn_bootstrap3.model_fields.IntegerField(default=None, null=True, verbose_name='col-lg-', blank=True)),
                ('lg_offset', aldryn_bootstrap3.model_fields.IntegerField(default=None, null=True, verbose_name='offset-', blank=True)),
                ('lg_push', aldryn_bootstrap3.model_fields.IntegerField(default=None, null=True, verbose_name='push-', blank=True)),
                ('lg_pull', aldryn_bootstrap3.model_fields.IntegerField(default=None, null=True, verbose_name='pull-', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='Bootstrap3ListGroupItemPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('title', aldryn_bootstrap3.model_fields.MiniText(default='', verbose_name='title', blank=True)),
                ('context', aldryn_bootstrap3.model_fields.Context(default='', max_length=255, blank=True, choices=[('', 'None'), ('primary', 'Primary'), ('success', 'Success'), ('info', 'Info'), ('warning', 'Warning'), ('danger', 'Danger')])),
                ('state', models.CharField(blank=True, max_length=255, verbose_name='state', choices=[('active', 'active'), ('disabled', 'disabled')])),
                ('classes', aldryn_bootstrap3.model_fields.Classes(default='', help_text='space separated classes that are added to the class. see <a href="http://getbootstrap.com/css/" target="_blank">bootstrap docs</a>', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='Bootstrap3ListGroupPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('classes', aldryn_bootstrap3.model_fields.Classes(default='', help_text='space separated classes that are added to the class. see <a href="http://getbootstrap.com/css/" target="_blank">bootstrap docs</a>', blank=True)),
                ('add_list_group_class', models.BooleanField(default=True, help_text='whether to add the list-group and list-group-item classes', verbose_name='class: list-group')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='Bootstrap3RowPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('classes', aldryn_bootstrap3.model_fields.Classes(default='', help_text='space separated classes that are added to the class. see <a href="http://getbootstrap.com/css/" target="_blank">bootstrap docs</a>', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
