# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'CustomUser', fields ['username']
        db.delete_unique(u'fb_customuser', ['username'])

        # Deleting field 'CustomUser.dances_whenever_able'
        db.delete_column(u'fb_customuser', 'dances_whenever_able')

        # Deleting field 'CustomUser.last_login'
        db.delete_column(u'fb_customuser', 'last_login')

        # Deleting field 'CustomUser.namee'
        db.delete_column(u'fb_customuser', 'namee')

        # Deleting field 'CustomUser.facebook_page_id'
        db.delete_column(u'fb_customuser', 'facebook_page_id')

        # Deleting field 'CustomUser.shrubberies'
        db.delete_column(u'fb_customuser', 'shrubberies')

        # Adding field 'CustomUser.password'
        db.add_column(u'fb_customuser', 'password',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=60),
                      keep_default=False)

        # Adding field 'CustomUser.name'
        db.add_column(u'fb_customuser', 'name',
                      self.gf('django.db.models.fields.TextField')(default=0),
                      keep_default=False)


        # Changing field 'CustomUser.username'
        db.alter_column(u'fb_customuser', 'username', self.gf('django.db.models.fields.CharField')(max_length=255))

    def backwards(self, orm):
        # Adding field 'CustomUser.dances_whenever_able'
        db.add_column(u'fb_customuser', 'dances_whenever_able',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'CustomUser.last_login'
        db.add_column(u'fb_customuser', 'last_login',
                      self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'CustomUser.namee'
        db.add_column(u'fb_customuser', 'namee',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True),
                      keep_default=False)

        # Adding field 'CustomUser.facebook_page_id'
        db.add_column(u'fb_customuser', 'facebook_page_id',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'CustomUser.shrubberies'
        raise RuntimeError("Cannot reverse this migration. 'CustomUser.shrubberies' and its values cannot be restored.")
        # Deleting field 'CustomUser.password'
        db.delete_column(u'fb_customuser', 'password')

        # Deleting field 'CustomUser.name'
        db.delete_column(u'fb_customuser', 'name')


        # Changing field 'CustomUser.username'
        db.alter_column(u'fb_customuser', 'username', self.gf('django.db.models.fields.CharField')(max_length=128, unique=True))
        # Adding unique constraint on 'CustomUser', fields ['username']
        db.create_unique(u'fb_customuser', ['username'])


    models = {
        u'fb.customuser': {
            'Meta': {'object_name': 'CustomUser'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['fb']