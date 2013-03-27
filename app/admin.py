__author__ = 'Nejc'

from django.contrib import admin
from app.models import Host, Event, Ticket


class TicketInline(admin.TabularInline):
    model = Ticket
    extra = 1

class EventInline(admin.StackedInline):
    exclude = ['event_rated']
    model = Event
    extra = 1


class HostAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['host_name']}), #, 'classes': ['collapse']
    ]
    inlines = [EventInline]

admin.site.register(Host, HostAdmin)

#admin.site.register(Host)
#admin.site.register(Event)