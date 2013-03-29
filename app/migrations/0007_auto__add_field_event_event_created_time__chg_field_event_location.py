# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Event.event_created_time'
        db.add_column(u'app_event', 'event_created_time',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2013, 3, 29, 0, 0)),
                      keep_default=False)


        # Changing field 'Event.location'
        db.alter_column(u'app_event', 'location', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

    def backwards(self, orm):
        # Deleting field 'Event.event_created_time'
        db.delete_column(u'app_event', 'event_created_time')


        # User chose to not deal with backwards NULL issues for 'Event.location'
        raise RuntimeError("Cannot reverse this migration. 'Event.location' and its values cannot be restored.")

    models = {
        u'app.event': {
            'Meta': {'object_name': 'Event'},
            'end_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'event_created_time': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2013, 3, 29, 0, 0)'}),
            'females': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'host': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Host']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'males': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'rated': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True'}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 3, 29, 0, 0)'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'update_time': ('django.db.models.fields.DateField', [], {'null': 'True'})
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