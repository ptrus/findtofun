__author__ = 'Nejc'
#info:
#https://docs.djangoproject.com/en/1.5/ref/models/instances/#django.db.models.Model
#https://docs.djangoproject.com/en/dev/ref/forms/fields/
from django.db import models
from django.utils import timezone

class Host(models.Model):
    host_name = models.CharField(max_length=200)
    def __unicode__(self):
        return self.host_name

class Event(models.Model):
    EVENT_RATE = (
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
    event_start_time = models.DateTimeField(default=timezone.now()) #'%m/%d/%Y %H:%M' '10/25/2006 14:30'
    event_end_time = models.DateTimeField()   #TO-DO default = start time
#    event_created_time = models.DateField(auto_now_add=True) #TO-DO
    male_guests = models.IntegerField(default=0)
    female_guests = models.IntegerField(default=0)
    event_location = models.CharField(max_length=200)
    event_rated = models.CharField(max_length=2, choices=EVENT_RATE, null=True)
    def __unicode__(self):
        return u'%s %s' % (self.event_name, self.get_event_type_display())
    def legal_start_time(self):  #TO-DO pravilnost vnosa
        return self.event_start_time > self.event_created_time
    def legal_end_time(self):
        return self.event_start_time < self.event_end_time
    def expired(self):
        return self.event_end_time < timezone.now()
    expired.admin_order_field = 'event_end_time'
    expired.boolean = True
    expired.short_description = 'Event expired ?'


class Ticket(models.Model):
    event = models.ForeignKey(Event, null=True)
    ticket_place = models.CharField(max_length=200, null=True)
    def __unicode__(self):
        return self.ticket_place

