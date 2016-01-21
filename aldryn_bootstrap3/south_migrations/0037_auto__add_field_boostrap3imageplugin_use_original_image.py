# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Boostrap3ImagePlugin.use_original_image'
        db.add_column(u'aldryn_bootstrap3_boostrap3imageplugin', 'use_original_image',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Boostrap3ImagePlugin.use_original_image'
        db.delete_column(u'aldryn_bootstrap3_boostrap3imageplugin', 'use_original_image')


    models = {
        u'aldryn_bootstrap3.boostrap3alertplugin': {
            'Meta': {'object_name': 'Boostrap3AlertPlugin', '_ormbases': ['cms.CMSPlugin']},
            'classes': (u'django.db.models.fields.TextField', [], {'default': "u''", 'blank': 'True'}),
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "u'+'", 'unique': 'True', 'primary_key': 'True', 'to': "orm['cms.CMSPlugin']"}),
            'context': (u'django.db.models.fields.CharField', [], {'default': "u'default'", 'max_length': '255'}),
            'icon': (u'django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '255', 'blank': 'True'})
        },
        u'aldryn_bootstrap3.boostrap3blockquoteplugin': {
            'Meta': {'object_name': 'Boostrap3BlockquotePlugin', '_ormbases': ['cms.CMSPlugin']},
            'classes': (u'django.db.models.fields.TextField', [], {'default': "u''", 'blank': 'True'}),
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "u'+'", 'unique': 'True', 'primary_key': 'True', 'to': "orm['cms.CMSPlugin']"}),
            'reverse': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'aldryn_bootstrap3.boostrap3buttonplugin': {
            'Meta': {'object_name': 'Boostrap3ButtonPlugin', '_ormbases': ['cms.CMSPlugin']},
            'btn_block': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'btn_context': (u'django.db.models.fields.CharField', [], {'default': "u'default'", 'max_length': '255'}),
            'btn_size': (u'django.db.models.fields.CharField', [], {'default': "u'md'", 'max_length': '255', 'blank': 'True'}),
            'classes': (u'django.db.models.fields.TextField', [], {'default': "u''", 'blank': 'True'}),
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "u'+'", 'unique': 'True', 'primary_key': 'True', 'to': "orm['cms.CMSPlugin']"}),
            'icon_left': (u'django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '255', 'blank': 'True'}),
            'icon_right': (u'django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '255', 'blank': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '256', 'blank': 'True'}),
            'link_anchor': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'link_file': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['filer.File']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'link_mailto': ('django.db.models.fields.EmailField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'link_page': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Page']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'link_phone': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'link_target': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'link_url': ('django.db.models.fields.URLField', [], {'default': "u''", 'max_length': '200', 'blank': 'True'}),
            'responsive': (u'django.db.models.fields.TextField', [], {'default': "u''", 'blank': 'True'}),
            'responsive_print': (u'django.db.models.fields.TextField', [], {'default': "u''", 'blank': 'True'}),
            'txt_context': (u'django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '255', 'blank': 'True'}),
            'type': (u'django.db.models.fields.CharField', [], {'default': "u'lnk'", 'max_length': '10'})
        },
        u'aldryn_bootstrap3.boostrap3iconplugin': {
            'Meta': {'object_name': 'Boostrap3IconPlugin', '_ormbases': ['cms.CMSPlugin']},
            'classes': (u'django.db.models.fields.TextField', [], {'default': "u''", 'blank': 'True'}),
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "u'+'", 'unique': 'True', 'primary_key': 'True', 'to': "orm['cms.CMSPlugin']"}),
            'icon': (u'django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '255'})
        },
        u'aldryn_bootstrap3.boostrap3imageplugin': {
            'Meta': {'object_name': 'Boostrap3ImagePlugin', '_ormbases': ['cms.CMSPlugin']},
            'alt': (u'django.db.models.fields.TextField', [], {'default': "u''", 'blank': 'True'}),
            'aspect_ratio': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '10', 'blank': 'True'}),
            'classes': (u'django.db.models.fields.TextField', [], {'default': "u''", 'blank': 'True'}),
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "u'+'", 'unique': 'True', 'primary_key': 'True', 'to': "orm['cms.CMSPlugin']"}),
            'file': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'+'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['filer.Image']"}),
            'img_responsive': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'override_height': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'override_width': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'shape': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '64', 'blank': 'True'}),
            'thumbnail': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'title': (u'django.db.models.fields.TextField', [], {'default': "u''", 'blank': 'True'}),
            'use_original_image': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'aldryn_bootstrap3.boostrap3labelplugin': {
            'Meta': {'object_name': 'Boostrap3LabelPlugin', '_ormbases': ['cms.CMSPlugin']},
            'classes': (u'django.db.models.fields.TextField', [], {'default': "u''", 'blank': 'True'}),
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "u'+'", 'unique': 'True', 'primary_key': 'True', 'to': "orm['cms.CMSPlugin']"}),
            'context': (u'django.db.models.fields.CharField', [], {'default': "u'default'", 'max_length': '255'}),
            'label': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '256', 'blank': 'True'})
        },
        u'aldryn_bootstrap3.boostrap3panelbodyplugin': {
            'Meta': {'object_name': 'Boostrap3PanelBodyPlugin', '_ormbases': ['cms.CMSPlugin']},
            'classes': (u'django.db.models.fields.TextField', [], {'default': "u''", 'blank': 'True'}),
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "u'+'", 'unique': 'True', 'primary_key': 'True', 'to': "orm['cms.CMSPlugin']"})
        },
        u'aldryn_bootstrap3.boostrap3panelfooterplugin': {
            'Meta': {'object_name': 'Boostrap3PanelFooterPlugin', '_ormbases': ['cms.CMSPlugin']},
            'classes': (u'django.db.models.fields.TextField', [], {'default': "u''", 'blank': 'True'}),
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "u'+'", 'unique': 'True', 'primary_key': 'True', 'to': "orm['cms.CMSPlugin']"})
        },
        u'aldryn_bootstrap3.boostrap3panelheadingplugin': {
            'Meta': {'object_name': 'Boostrap3PanelHeadingPlugin', '_ormbases': ['cms.CMSPlugin']},
            'classes': (u'django.db.models.fields.TextField', [], {'default': "u''", 'blank': 'True'}),
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "u'+'", 'unique': 'True', 'primary_key': 'True', 'to': "orm['cms.CMSPlugin']"}),
            'title': (u'django.db.models.fields.TextField', [], {'default': "u''", 'blank': 'True'})
        },
        u'aldryn_bootstrap3.boostrap3panelplugin': {
            'Meta': {'object_name': 'Boostrap3PanelPlugin', '_ormbases': ['cms.CMSPlugin']},
            'classes': (u'django.db.models.fields.TextField', [], {'default': "u''", 'blank': 'True'}),
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "u'+'", 'unique': 'True', 'primary_key': 'True', 'to': "orm['cms.CMSPlugin']"}),
            'context': (u'django.db.models.fields.CharField', [], {'default': "u'default'", 'max_length': '255'})
        },
        u'aldryn_bootstrap3.boostrap3spacerplugin': {
            'Meta': {'object_name': 'Boostrap3SpacerPlugin', '_ormbases': ['cms.CMSPlugin']},
            'classes': (u'django.db.models.fields.TextField', [], {'default': "u''", 'blank': 'True'}),
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "u'+'", 'unique': 'True', 'primary_key': 'True', 'to': "orm['cms.CMSPlugin']"}),
            'size': (u'django.db.models.fields.CharField', [], {'default': "u'md'", 'max_length': '255', 'blank': 'True'})
        },
        u'aldryn_bootstrap3.boostrap3wellplugin': {
            'Meta': {'object_name': 'Boostrap3WellPlugin', '_ormbases': ['cms.CMSPlugin']},
            'classes': (u'django.db.models.fields.TextField', [], {'default': "u''", 'blank': 'True'}),
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "u'+'", 'unique': 'True', 'primary_key': 'True', 'to': "orm['cms.CMSPlugin']"}),
            'size': (u'django.db.models.fields.CharField', [], {'default': "u'md'", 'max_length': '255', 'blank': 'True'})
        },
        u'aldryn_bootstrap3.bootstrap3accordionitemplugin': {
            'Meta': {'object_name': 'Bootstrap3AccordionItemPlugin', '_ormbases': ['cms.CMSPlugin']},
            'classes': (u'django.db.models.fields.TextField', [], {'default': "u''", 'blank': 'True'}),
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'context': (u'django.db.models.fields.CharField', [], {'default': "u'default'", 'max_length': '255'}),
            'title': (u'django.db.models.fields.TextField', [], {'default': "u''", 'blank': 'True'})
        },
        u'aldryn_bootstrap3.bootstrap3accordionplugin': {
            'Meta': {'object_name': 'Bootstrap3AccordionPlugin', '_ormbases': ['cms.CMSPlugin']},
            'classes': (u'django.db.models.fields.TextField', [], {'default': "u''", 'blank': 'True'}),
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'index': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'aldryn_bootstrap3.bootstrap3carouselplugin': {
            'Meta': {'object_name': 'Bootstrap3CarouselPlugin', '_ormbases': ['cms.CMSPlugin']},
            'aspect_ratio': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '10', 'blank': 'True'}),
            'classes': (u'django.db.models.fields.TextField', [], {'default': "u''", 'blank': 'True'}),
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'interval': ('django.db.models.fields.IntegerField', [], {'default': '5000'}),
            'pause': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'ride': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'style': ('django.db.models.fields.CharField', [], {'default': "u'standard'", 'max_length': '50'}),
            'transition_effect': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '50', 'blank': 'True'}),
            'wrap': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        u'aldryn_bootstrap3.bootstrap3carouselslidefolderplugin': {
            'Meta': {'object_name': 'Bootstrap3CarouselSlideFolderPlugin', '_ormbases': ['cms.CMSPlugin']},
            'classes': (u'django.db.models.fields.TextField', [], {'default': "u''", 'blank': 'True'}),
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'folder': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['filer.Folder']"})
        },
        u'aldryn_bootstrap3.bootstrap3carouselslideplugin': {
            'Meta': {'object_name': 'Bootstrap3CarouselSlidePlugin', '_ormbases': ['cms.CMSPlugin']},
            'classes': (u'django.db.models.fields.TextField', [], {'default': "u''", 'blank': 'True'}),
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'content': ('djangocms_text_ckeditor.fields.HTMLField', [], {'default': "u''", 'blank': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'+'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['filer.Image']"}),
            'link_anchor': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'link_file': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['filer.File']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'link_mailto': ('django.db.models.fields.EmailField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'link_page': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Page']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'link_phone': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'link_target': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'link_text': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'link_url': ('django.db.models.fields.URLField', [], {'default': "u''", 'max_length': '200', 'blank': 'True'})
        },
        u'aldryn_bootstrap3.bootstrap3columnplugin': {
            'Meta': {'object_name': 'Bootstrap3ColumnPlugin', '_ormbases': ['cms.CMSPlugin']},
            'classes': (u'django.db.models.fields.TextField', [], {'default': "u''", 'blank': 'True'}),
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            u'lg_col': (u'django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            u'lg_offset': (u'django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            u'lg_pull': (u'django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            u'lg_push': (u'django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            u'md_col': (u'django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            u'md_offset': (u'django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            u'md_pull': (u'django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            u'md_push': (u'django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            u'sm_col': (u'django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            u'sm_offset': (u'django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            u'sm_pull': (u'django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            u'sm_push': (u'django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'tag': ('django.db.models.fields.SlugField', [], {'default': "u'div'", 'max_length': '50'}),
            u'xs_col': (u'django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            u'xs_offset': (u'django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            u'xs_pull': (u'django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            u'xs_push': (u'django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'})
        },
        u'aldryn_bootstrap3.bootstrap3fileplugin': {
            'Meta': {'object_name': 'Bootstrap3FilePlugin', '_ormbases': ['cms.CMSPlugin']},
            'classes': (u'django.db.models.fields.TextField', [], {'default': "u''", 'blank': 'True'}),
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "u'+'", 'unique': 'True', 'primary_key': 'True', 'to': "orm['cms.CMSPlugin']"}),
            'file': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'+'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['filer.File']"}),
            'icon_left': (u'django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '255', 'blank': 'True'}),
            'icon_right': (u'django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '255', 'blank': 'True'}),
            'name': (u'django.db.models.fields.TextField', [], {'default': "u''", 'blank': 'True'}),
            'open_new_window': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'show_file_size': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'aldryn_bootstrap3.bootstrap3listgroupitemplugin': {
            'Meta': {'object_name': 'Bootstrap3ListGroupItemPlugin', '_ormbases': ['cms.CMSPlugin']},
            'classes': (u'django.db.models.fields.TextField', [], {'default': "u''", 'blank': 'True'}),
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'context': (u'django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '255', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'title': (u'django.db.models.fields.TextField', [], {'default': "u''", 'blank': 'True'})
        },
        u'aldryn_bootstrap3.bootstrap3listgroupplugin': {
            'Meta': {'object_name': 'Bootstrap3ListGroupPlugin', '_ormbases': ['cms.CMSPlugin']},
            'add_list_group_class': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'classes': (u'django.db.models.fields.TextField', [], {'default': "u''", 'blank': 'True'}),
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'aldryn_bootstrap3.bootstrap3rowplugin': {
            'Meta': {'object_name': 'Bootstrap3RowPlugin', '_ormbases': ['cms.CMSPlugin']},
            'classes': (u'django.db.models.fields.TextField', [], {'default': "u''", 'blank': 'True'}),
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'depth': ('django.db.models.fields.PositiveIntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'numchild': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'path': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'cms.page': {
            'Meta': {'ordering': "('path',)", 'unique_together': "(('publisher_is_draft', 'site', 'application_namespace'), ('reverse_id', 'site', 'publisher_is_draft'))", 'object_name': 'Page'},
            'application_namespace': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'application_urls': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'changed_by': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'depth': ('django.db.models.fields.PositiveIntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_navigation': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'is_home': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'languages': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'limit_visibility_in_menu': ('django.db.models.fields.SmallIntegerField', [], {'default': 'None', 'null': 'True', 'db_index': 'True', 'blank': 'True'}),
            'login_required': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'navigation_extenders': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '80', 'null': 'True', 'blank': 'True'}),
            'numchild': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': "orm['cms.Page']"}),
            'path': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'placeholders': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['cms.Placeholder']", 'symmetrical': 'False'}),
            'publication_date': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'publication_end_date': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'publisher_is_draft': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'publisher_public': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'publisher_draft'", 'unique': 'True', 'null': 'True', 'to': "orm['cms.Page']"}),
            'reverse_id': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'revision_id': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'djangocms_pages'", 'to': u"orm['sites.Site']"}),
            'soft_root': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'template': ('django.db.models.fields.CharField', [], {'default': "'INHERIT'", 'max_length': '100'}),
            'xframe_options': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'filer.file': {
            'Meta': {'object_name': 'File'},
            '_file_size': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'folder': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'all_files'", 'null': 'True', 'to': u"orm['filer.Folder']"}),
            'has_all_mandatory_data': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_public': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '255', 'blank': 'True'}),
            'original_filename': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'owned_files'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'polymorphic_ctype': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'polymorphic_filer.file_set+'", 'null': 'True', 'to': u"orm['contenttypes.ContentType']"}),
            'sha1': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '40', 'blank': 'True'}),
            'uploaded_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        u'filer.folder': {
            'Meta': {'ordering': "(u'name',)", 'unique_together': "((u'parent', u'name'),)", 'object_name': 'Folder'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            u'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'filer_owned_folders'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'children'", 'null': 'True', 'to': u"orm['filer.Folder']"}),
            u'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'uploaded_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        'filer.image': {
            'Meta': {'object_name': 'Image'},
            '_height': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            '_width': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'author': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'date_taken': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'default_alt_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'default_caption': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'file_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['filer.File']", 'unique': 'True', 'primary_key': 'True'}),
            'must_always_publish_author_credit': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'must_always_publish_copyright': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'subject_location': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '64', 'null': 'True', 'blank': 'True'})
        },
        u'sites.site': {
            'Meta': {'ordering': "(u'domain',)", 'object_name': 'Site', 'db_table': "u'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['aldryn_bootstrap3']