#info:
#https://docs.djangoproject.com/en/1.5/ref/models/instances/#django.db.models.Model
#https://docs.djangoproject.com/en/dev/ref/forms/fields/
from django.db import models
from django.utils import timezone

class Host(models.Model):
    host_name = models.CharField(max_length=200)
    def __unicode__(self):
        return self.host_name

class EventManager(models.Manager):
    def create_event(self, host, name, location, start_time, end_time):
        event = self.model(
            host=host,
            name=name,
            location=location,
            start_time=start_time,
            end_time=end_time,
        )
        
        return event
        
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
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=1, choices=EVENT_TYPES)
    start_time = models.DateTimeField(default=timezone.now()) #'%m/%d/%Y %H:%M' '10/25/2006 14:30'
    end_time = models.DateTimeField(null=True)
    update_time = models.DateField(null=True)
    event_created_time = models.DateField(default=timezone.now())
    males = models.IntegerField(default=0)
    females = models.IntegerField(default=0)
    location = models.CharField(max_length=200, null=True)
    rated = models.CharField(max_length=2, choices=EVENT_RATE, null=True)
#    def __unicode__(self):
#        return u'%s %s' % (self.name, self.get_event_type_display())
#    def legal_start_time(self):  #TO-DO pravilnost vnosa
#        return self.start_time > self.event_created_time
    def legal_end_time(self):
        return self.start_time < self.end_time
    def expired(self):
        return self.end_time < timezone.now()
    expired.admin_order_field = 'event_end_time'
    expired.boolean = True
    expired.short_description = 'Event expired ?'
    
    objects = EventManager()


class Ticket(models.Model):
    event = models.ForeignKey(Event, null=True)
    ticket_place = models.CharField(max_length=200, null=True)
    def __unicode__(self):
        return self.ticket_place

