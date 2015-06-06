# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Boostrap3BlockquotePlugin.context'
        db.delete_column(u'aldryn_bootstrap3_boostrap3blockquoteplugin', 'context')

        # Adding field 'Boostrap3BlockquotePlugin.reverse'
        db.add_column(u'aldryn_bootstrap3_boostrap3blockquoteplugin', 'reverse',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Boostrap3BlockquotePlugin.classes'
        db.add_column(u'aldryn_bootstrap3_boostrap3blockquoteplugin', 'classes',
                      self.gf(u'django.db.models.fields.TextField')(default=u'', blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Boostrap3BlockquotePlugin.context'
        db.add_column(u'aldryn_bootstrap3_boostrap3blockquoteplugin', 'context',
                      self.gf('django.db.models.fields.CharField')(default=u'', max_length=255, blank=True),
                      keep_default=False)

        # Deleting field 'Boostrap3BlockquotePlugin.reverse'
        db.delete_column(u'aldryn_bootstrap3_boostrap3blockquoteplugin', 'reverse')

        # Deleting field 'Boostrap3BlockquotePlugin.classes'
        db.delete_column(u'aldryn_bootstrap3_boostrap3blockquoteplugin', 'classes')


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
            'label': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '256', 'blank': 'True'}),
            'size': (u'django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '255', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'default': "u''", 'max_length': '200', 'blank': 'True'})
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