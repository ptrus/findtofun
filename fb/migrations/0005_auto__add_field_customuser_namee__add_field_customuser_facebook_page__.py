# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'CustomUser.namee'
        db.add_column(u'fb_customuser', 'namee',
                      self.gf('django.db.models.fields.TextField')(null=True),
                      keep_default=False)

        # Adding field 'CustomUser.facebook_page__id'
        db.add_column(u'fb_customuser', 'facebook_page__id',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'CustomUser.namee'
        db.delete_column(u'fb_customuser', 'namee')

        # Deleting field 'CustomUser.facebook_page__id'
        db.delete_column(u'fb_customuser', 'facebook_page__id')


    models = {
        u'fb.customuser': {
            'Meta': {'object_name': 'CustomUser'},
            'dances_whenever_able': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'facebook_page__id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'namee': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'shrubberies': ('django.db.models.fields.IntegerField', [], {}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'})
        }
    }

    complete_apps = ['fb']