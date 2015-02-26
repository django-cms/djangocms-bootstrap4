# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Boostrap3ButtonPlugin.icon_left'
        db.add_column(u'aldryn_bootstrap3_boostrap3buttonplugin', 'icon_left',
                      self.gf(u'django.db.models.fields.CharField')(default=u'', max_length=255, blank=True),
                      keep_default=False)

        # Adding field 'Boostrap3ButtonPlugin.icon_right'
        db.add_column(u'aldryn_bootstrap3_boostrap3buttonplugin', 'icon_right',
                      self.gf(u'django.db.models.fields.CharField')(default=u'', max_length=255, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Boostrap3ButtonPlugin.icon_left'
        db.delete_column(u'aldryn_bootstrap3_boostrap3buttonplugin', 'icon_left')

        # Deleting field 'Boostrap3ButtonPlugin.icon_right'
        db.delete_column(u'aldryn_bootstrap3_boostrap3buttonplugin', 'icon_right')


    models = {
        u'aldryn_bootstrap3.boostrap3blockquoteplugin': {
            'Meta': {'object_name': 'Boostrap3BlockquotePlugin', '_ormbases': ['cms.CMSPlugin']},
            'classes': (u'django.db.models.fields.TextField', [], {'default': "u''", 'blank': 'True'}),
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "u'+'", 'unique': 'True', 'primary_key': 'True', 'to': "orm['cms.CMSPlugin']"}),
            'reverse': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'aldryn_bootstrap3.boostrap3buttonplugin': {
            'Meta': {'object_name': 'Boostrap3ButtonPlugin', '_ormbases': ['cms.CMSPlugin']},
            'classes': (u'django.db.models.fields.TextField', [], {'default': "u''", 'blank': 'True'}),
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "u'+'", 'unique': 'True', 'primary_key': 'True', 'to': "orm['cms.CMSPlugin']"}),
            'context': (u'django.db.models.fields.CharField', [], {'default': "u'default'", 'max_length': '255'}),
            'icon_left': (u'django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '255', 'blank': 'True'}),
            'icon_right': (u'django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '255', 'blank': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '256', 'blank': 'True'}),
            'size': (u'django.db.models.fields.CharField', [], {'default': "u'md'", 'max_length': '255', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'default': "u''", 'max_length': '200', 'blank': 'True'})
        },
        u'aldryn_bootstrap3.bootstrap3columnplugin': {
            'Meta': {'object_name': 'Bootstrap3ColumnPlugin', '_ormbases': ['cms.CMSPlugin']},
            'classes': (u'django.db.models.fields.TextField', [], {'default': "u''", 'blank': 'True'}),
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            u'lg_offset': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            u'lg_size': ('django.db.models.fields.IntegerField', [], {'default': '1', 'null': 'True', 'blank': 'True'}),
            u'md_offset': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            u'md_size': ('django.db.models.fields.IntegerField', [], {'default': '1', 'null': 'True', 'blank': 'True'}),
            u'sm_offset': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            u'sm_size': ('django.db.models.fields.IntegerField', [], {'default': '1', 'null': 'True', 'blank': 'True'}),
            u'xs_offset': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            u'xs_size': ('django.db.models.fields.IntegerField', [], {'default': '1', 'null': 'True', 'blank': 'True'})
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
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'})
        }
    }

    complete_apps = ['aldryn_bootstrap3']