__author__ = 'Nejc'
#info:
#https://docs.djangoproject.com/en/1.5/ref/models/instances/#django.db.models.Model

from django.db import models
from django.utils import timezone

class User(models.Model):
    user_name = models.CharField(max_length=200)
    def __unicode__(self):
        return self.user_name

class Host(models.Model):
    host_name = models.CharField(max_length=200)
    def __unicode__(self):
        return self.host_name

class Event(models.Model):
    EVENT_REATE = (
        (u'1', u'Not interesting'),
        (u'2', u'Not bad'),
        (u'3', u'Interesting'),
        (u'4', u'Tempting'), #mammljivo :D
        (u'5', u'You can not miss'),
    )

    EVENT_TYPES = (
        (u'1', u'Party'),
        (u'2', u'Causes'),
        (u'3', u'Education'),
        (u'4', u'Meetings'),
        (u'5', u'Music/Arts'),
        (u'6', u'Sports'),
        (u'7', u'Trips'),
        (u'8', u'Other'),
    )

    host = models.ForeignKey(Host, null=True)
    event_name = models.CharField(max_length=200)
    event_type = models.CharField(max_length=1, choices=EVENT_TYPES)
    event_start_time = models.DateTimeField(default=timezone.now())
    event_end_time = models.DateTimeField()
    male_guests = models.IntegerField(default=0)
    female_guests = models.IntegerField(default=0)
    event_location = models.CharField(max_length=200)
    #ticket_place = models.CharField(max_length=200)
    event_rated = models.CharField(max_length=2, choices=EVENT_REATE, null=True)
    def __unicode__(self):
        return u'%s %s' % (self.event_name, self.event_type)

class Ticket(models.Model):
    event = models.ForeignKey(Event, null=True)
    ticket_place = models.CharField(max_length=200, null=True)
    def __unicode__(self):
        return self.ticket_place

