from django.conf.urls import patterns, url
from django.views.generic import DetailView, ListView
from app.models import Event

urlpatterns = patterns('',
    url(r'^$',
        ListView.as_view(
            queryset=Event.objects.order_by('-event_start_time')[:10],
            context_object_name='latest_events_list',
            template_name='events/events.html'),
        name='events'),
    url(r'^(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Event,
            template_name='events/details.html'),
        name='detail'),
    )
