# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding unique constraint on 'CustomUser', fields ['username']
        db.create_unique(u'fb_customuser', ['username'])


    def backwards(self, orm):
        # Removing unique constraint on 'CustomUser', fields ['username']
        db.delete_unique(u'fb_customuser', ['username'])


    models = {
        u'fb.customuser': {
            'Meta': {'object_name': 'CustomUser'},
            'dances_whenever_able': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'shrubberies': ('django.db.models.fields.IntegerField', [], {}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'})
        }
    }

    complete_apps = ['fb']