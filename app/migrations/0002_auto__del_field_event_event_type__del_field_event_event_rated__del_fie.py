# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Event.event_type'
        db.delete_column(u'app_event', 'event_type')

        # Deleting field 'Event.event_rated'
        db.delete_column(u'app_event', 'event_rated')

        # Deleting field 'Event.event_start_time'
        db.delete_column(u'app_event', 'event_start_time')

        # Deleting field 'Event.event_end_time'
        db.delete_column(u'app_event', 'event_end_time')

        # Deleting field 'Event.event_location'
        db.delete_column(u'app_event', 'event_location')

        # Deleting field 'Event.female_guests'
        db.delete_column(u'app_event', 'female_guests')

        # Deleting field 'Event.male_guests'
        db.delete_column(u'app_event', 'male_guests')

        # Deleting field 'Event.event_name'
        db.delete_column(u'app_event', 'event_name')

        # Adding field 'Event.name'
        db.add_column(u'app_event', 'name',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200),
                      keep_default=False)

        # Adding field 'Event.type'
        db.add_column(u'app_event', 'type',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=1),
                      keep_default=False)

        # Adding field 'Event.start_time'
        db.add_column(u'app_event', 'start_time',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 3, 29, 0, 0)),
                      keep_default=False)

        # Adding field 'Event.end_time'
        db.add_column(u'app_event', 'end_time',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 3, 29, 0, 0)),
                      keep_default=False)

        # Adding field 'Event.males'
        db.add_column(u'app_event', 'males',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Event.females'
        db.add_column(u'app_event', 'females',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Event.location'
        db.add_column(u'app_event', 'location',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200),
                      keep_default=False)

        # Adding field 'Event.rated'
        db.add_column(u'app_event', 'rated',
                      self.gf('django.db.models.fields.CharField')(max_length=2, null=True),
                      keep_default=False)


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Event.event_type'
        raise RuntimeError("Cannot reverse this migration. 'Event.event_type' and its values cannot be restored.")
        # Adding field 'Event.event_rated'
        db.add_column(u'app_event', 'event_rated',
                      self.gf('django.db.models.fields.CharField')(max_length=2, null=True),
                      keep_default=False)

        # Adding field 'Event.event_start_time'
        db.add_column(u'app_event', 'event_start_time',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 3, 28, 0, 0)),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Event.event_end_time'
        raise RuntimeError("Cannot reverse this migration. 'Event.event_end_time' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Event.event_location'
        raise RuntimeError("Cannot reverse this migration. 'Event.event_location' and its values cannot be restored.")
        # Adding field 'Event.female_guests'
        db.add_column(u'app_event', 'female_guests',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Event.male_guests'
        db.add_column(u'app_event', 'male_guests',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Event.event_name'
        raise RuntimeError("Cannot reverse this migration. 'Event.event_name' and its values cannot be restored.")
        # Deleting field 'Event.name'
        db.delete_column(u'app_event', 'name')

        # Deleting field 'Event.type'
        db.delete_column(u'app_event', 'type')

        # Deleting field 'Event.start_time'
        db.delete_column(u'app_event', 'start_time')

        # Deleting field 'Event.end_time'
        db.delete_column(u'app_event', 'end_time')

        # Deleting field 'Event.males'
        db.delete_column(u'app_event', 'males')

        # Deleting field 'Event.females'
        db.delete_column(u'app_event', 'females')

        # Deleting field 'Event.location'
        db.delete_column(u'app_event', 'location')

        # Deleting field 'Event.rated'
        db.delete_column(u'app_event', 'rated')


    models = {
        u'app.event': {
            'Meta': {'object_name': 'Event'},
            'end_time': ('django.db.models.fields.DateTimeField', [], {}),
            'females': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'host': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Host']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'males': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'rated': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True'}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 3, 29, 0, 0)'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '1'})
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