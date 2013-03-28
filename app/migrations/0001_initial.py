# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Host'
        db.create_table(u'app_host', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('host_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'app', ['Host'])

        # Adding model 'Event'
        db.create_table(u'app_event', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('host', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.Host'], null=True)),
            ('event_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('event_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('event_start_time', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 3, 28, 0, 0))),
            ('event_end_time', self.gf('django.db.models.fields.DateTimeField')()),
            ('male_guests', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('female_guests', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('event_location', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('event_rated', self.gf('django.db.models.fields.CharField')(max_length=2, null=True)),
        ))
        db.send_create_signal(u'app', ['Event'])

        # Adding model 'Ticket'
        db.create_table(u'app_ticket', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.Event'], null=True)),
            ('ticket_place', self.gf('django.db.models.fields.CharField')(max_length=200, null=True)),
        ))
        db.send_create_signal(u'app', ['Ticket'])


    def backwards(self, orm):
        # Deleting model 'Host'
        db.delete_table(u'app_host')

        # Deleting model 'Event'
        db.delete_table(u'app_event')

        # Deleting model 'Ticket'
        db.delete_table(u'app_ticket')


    models = {
        u'app.event': {
            'Meta': {'object_name': 'Event'},
            'event_end_time': ('django.db.models.fields.DateTimeField', [], {}),
            'event_location': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'event_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'event_rated': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True'}),
            'event_start_time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 3, 28, 0, 0)'}),
            'event_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'female_guests': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'host': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Host']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'male_guests': ('django.db.models.fields.IntegerField', [], {'default': '0'})
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