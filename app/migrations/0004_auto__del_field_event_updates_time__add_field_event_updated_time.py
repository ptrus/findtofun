# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Event.updates_time'
        db.delete_column(u'app_event', 'updates_time')

        # Adding field 'Event.updated_time'
        db.add_column(u'app_event', 'updated_time',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2013, 3, 29, 0, 0), blank=True),
                      keep_default=False)


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Event.updates_time'
        raise RuntimeError("Cannot reverse this migration. 'Event.updates_time' and its values cannot be restored.")
        # Deleting field 'Event.updated_time'
        db.delete_column(u'app_event', 'updated_time')


    models = {
        u'app.event': {
            'Meta': {'object_name': 'Event'},
            'end_time': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            'females': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'host': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Host']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'males': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'rated': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True'}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 3, 29, 0, 0)'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'updated_time': ('django.db.models.fields.DateField', [], {'blank': 'True'})
        },
        u'app.host': {
            'Meta': {'object_name': 'Host'},
            'host_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'app.ticket': {
            'Meta': {'object_name': 'Ticket'},
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Event']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ticket_place': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'})
        }
    }

    complete_apps = ['app']