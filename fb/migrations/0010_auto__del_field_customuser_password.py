# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'CustomUser.password'
        db.delete_column(u'fb_customuser', 'password')


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'CustomUser.password'
        raise RuntimeError("Cannot reverse this migration. 'CustomUser.password' and its values cannot be restored.")

    models = {
        u'fb.customuser': {
            'Meta': {'object_name': 'CustomUser'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'password_hash': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True'}),
            'password_salt': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['fb']