from django.contrib import admin
from events.models import FbEvent, Ticket


class TicketInline(admin.TabularInline):
    model = Ticket
    extra = 1


class EventInline(admin.StackedInline):
    #exclude = ['event_rated'] ce je null da ga ne izpise
    model = FbEvent
    extra = 1


class HostAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['host_name']}),
        #, 'classes': ['collapse']
    ]
    inlines = [EventInline]

#    list_display = ('host_name', 'event_start_time', 'legal_start_time')
#    list_filter = ['event_start_time']
    search_fields = ['host_name']
#    date_hierarchy = 'event_start_time'


class EventAdmin(admin.ModelAdmin):
    #fields = ['host', 'event_name', 'event_location', 'event_type']
    inlines = [TicketInline]

    #TO-DO show this function in true/false format
    #   'legal_start_time', 'legal_end_time'
    list_display = ('name', 'start_time', 'expired')
    list_filter = ['start_time']
    search_fields = ['name']
    date_hierarchy = 'start_time'


# admin.site.register(FbHost, HostAdmin)
# admin.site.register(FbEvent, EventAdmin)
