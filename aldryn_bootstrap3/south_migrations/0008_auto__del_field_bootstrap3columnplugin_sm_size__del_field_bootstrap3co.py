# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        db.rename_column(u'aldryn_bootstrap3_bootstrap3columnplugin', u'sm_size', u'sm_col')
        db.rename_column(u'aldryn_bootstrap3_bootstrap3columnplugin', u'lg_size', u'lg_col')
        db.rename_column(u'aldryn_bootstrap3_bootstrap3columnplugin', u'xs_size', u'xs_col')
        db.rename_column(u'aldryn_bootstrap3_bootstrap3columnplugin', u'md_size', u'md_col')

        # Adding field 'Bootstrap3ColumnPlugin.xs_push'
        db.add_column(u'aldryn_bootstrap3_bootstrap3columnplugin', u'xs_push',
                      self.gf('django.db.models.fields.IntegerField')(default=0, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Bootstrap3ColumnPlugin.xs_pull'
        db.add_column(u'aldryn_bootstrap3_bootstrap3columnplugin', u'xs_pull',
                      self.gf('django.db.models.fields.IntegerField')(default=0, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Bootstrap3ColumnPlugin.sm_push'
        db.add_column(u'aldryn_bootstrap3_bootstrap3columnplugin', u'sm_push',
                      self.gf('django.db.models.fields.IntegerField')(default=0, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Bootstrap3ColumnPlugin.sm_pull'
        db.add_column(u'aldryn_bootstrap3_bootstrap3columnplugin', u'sm_pull',
                      self.gf('django.db.models.fields.IntegerField')(default=0, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Bootstrap3ColumnPlugin.md_push'
        db.add_column(u'aldryn_bootstrap3_bootstrap3columnplugin', u'md_push',
                      self.gf('django.db.models.fields.IntegerField')(default=0, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Bootstrap3ColumnPlugin.md_pull'
        db.add_column(u'aldryn_bootstrap3_bootstrap3columnplugin', u'md_pull',
                      self.gf('django.db.models.fields.IntegerField')(default=0, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Bootstrap3ColumnPlugin.lg_push'
        db.add_column(u'aldryn_bootstrap3_bootstrap3columnplugin', u'lg_push',
                      self.gf('django.db.models.fields.IntegerField')(default=0, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Bootstrap3ColumnPlugin.lg_pull'
        db.add_column(u'aldryn_bootstrap3_bootstrap3columnplugin', u'lg_pull',
                      self.gf('django.db.models.fields.IntegerField')(default=0, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        db.rename_column(u'aldryn_bootstrap3_bootstrap3columnplugin', u'sm_col', u'sm_size')
        db.rename_column(u'aldryn_bootstrap3_bootstrap3columnplugin', u'lg_col', u'lg_size')
        db.rename_column(u'aldryn_bootstrap3_bootstrap3columnplugin', u'xs_col', u'xs_size')
        db.rename_column(u'aldryn_bootstrap3_bootstrap3columnplugin', u'md_col', u'md_size')

        # Deleting field 'Bootstrap3ColumnPlugin.xs_push'
        db.delete_column(u'aldryn_bootstrap3_bootstrap3columnplugin', u'xs_push')

        # Deleting field 'Bootstrap3ColumnPlugin.xs_pull'
        db.delete_column(u'aldryn_bootstrap3_bootstrap3columnplugin', u'xs_pull')

        # Deleting field 'Bootstrap3ColumnPlugin.sm_push'
        db.delete_column(u'aldryn_bootstrap3_bootstrap3columnplugin', u'sm_push')

        # Deleting field 'Bootstrap3ColumnPlugin.sm_pull'
        db.delete_column(u'aldryn_bootstrap3_bootstrap3columnplugin', u'sm_pull')

        # Deleting field 'Bootstrap3ColumnPlugin.md_push'
        db.delete_column(u'aldryn_bootstrap3_bootstrap3columnplugin', u'md_push')

        # Deleting field 'Bootstrap3ColumnPlugin.md_pull'
        db.delete_column(u'aldryn_bootstrap3_bootstrap3columnplugin', u'md_pull')

        # Deleting field 'Bootstrap3ColumnPlugin.lg_push'
        db.delete_column(u'aldryn_bootstrap3_bootstrap3columnplugin', u'lg_push')

        # Deleting field 'Bootstrap3ColumnPlugin.lg_pull'
        db.delete_column(u'aldryn_bootstrap3_bootstrap3columnplugin', u'lg_pull')


    models = {
        u'aldryn_bootstrap3.boostrap3blockquoteplugin': {
            'Meta': {'object_name': 'Boostrap3BlockquotePlugin', '_ormbases': ['cms.CMSPlugin']},
            'classes': (u'django.db.models.fields.TextField', [], {'default': "u''", 'blank': 'True'}),
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "u'+'", 'unique': 'True', 'primary_key': 'True', 'to': "orm['cms.CMSPlugin']"}),
            'reverse': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'aldryn_bootstrap3.boostrap3buttonplugin': {
            'Meta': {'object_name': 'Boostrap3ButtonPlugin', '_ormbases': ['cms.CMSPlugin']},
            'anchor': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'classes': (u'django.db.models.fields.TextField', [], {'default': "u''", 'blank': 'True'}),
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "u'+'", 'unique': 'True', 'primary_key': 'True', 'to': "orm['cms.CMSPlugin']"}),
            'context': (u'django.db.models.fields.CharField', [], {'default': "u'link'", 'max_length': '255'}),
            'icon_left': (u'django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '255', 'blank': 'True'}),
            'icon_right': (u'django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '255', 'blank': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '256', 'blank': 'True'}),
            'mailto': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'page_link': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Page']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'size': (u'django.db.models.fields.CharField', [], {'default': "u'md'", 'max_length': '255', 'blank': 'True'}),
            'target': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'default': "u''", 'max_length': '200', 'blank': 'True'})
        },
        u'aldryn_bootstrap3.bootstrap3columnplugin': {
            'Meta': {'object_name': 'Bootstrap3ColumnPlugin', '_ormbases': ['cms.CMSPlugin']},
            'classes': (u'django.db.models.fields.TextField', [], {'default': "u''", 'blank': 'True'}),
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            u'lg_col': ('django.db.models.fields.IntegerField', [], {'default': '1', 'null': 'True', 'blank': 'True'}),
            u'lg_offset': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            u'lg_pull': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            u'lg_push': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            u'md_col': ('django.db.models.fields.IntegerField', [], {'default': '1', 'null': 'True', 'blank': 'True'}),
            u'md_offset': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            u'md_pull': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            u'md_push': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            u'sm_col': ('django.db.models.fields.IntegerField', [], {'default': '1', 'null': 'True', 'blank': 'True'}),
            u'sm_offset': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            u'sm_pull': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            u'sm_push': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            u'xs_col': ('django.db.models.fields.IntegerField', [], {'default': '1', 'null': 'True', 'blank': 'True'}),
            u'xs_offset': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            u'xs_pull': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            u'xs_push': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'})
        },
        u'aldryn_bootstrap3.bootstrap3rowplugin': {
            'Meta': {'object_name': 'Bootstrap3RowPlugin', '_ormbases': ['cms.CMSPlugin']},
            'classes': (u'django.db.models.fields.TextField', [], {'default': "u''", 'blank': 'True'}),
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'})
        },
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.page': {
            'Meta': {'ordering': "('tree_id', 'lft')", 'unique_together': "(('publisher_is_draft', 'application_namespace'), ('reverse_id', 'site', 'publisher_is_draft'))", 'object_name': 'Page'},
            'application_namespace': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'application_urls': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'changed_by': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_navigation': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'is_home': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'languages': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'limit_visibility_in_menu': ('django.db.models.fields.SmallIntegerField', [], {'default': 'None', 'null': 'True', 'db_index': 'True', 'blank': 'True'}),
            'login_required': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'navigation_extenders': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '80', 'null': 'True', 'blank': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': "orm['cms.Page']"}),
            'placeholders': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['cms.Placeholder']", 'symmetrical': 'False'}),
            'publication_date': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'publication_end_date': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'publisher_is_draft': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'publisher_public': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'publisher_draft'", 'unique': 'True', 'null': 'True', 'to': "orm['cms.Page']"}),
            'reverse_id': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'revision_id': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'djangocms_pages'", 'to': u"orm['sites.Site']"}),
            'soft_root': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'template': ('django.db.models.fields.CharField', [], {'default': "'INHERIT'", 'max_length': '100'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'xframe_options': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'})
        },
        u'sites.site': {
            'Meta': {'ordering': "(u'domain',)", 'object_name': 'Site', 'db_table': "u'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['aldryn_bootstrap3']
