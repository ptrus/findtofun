from django.conf.urls import patterns, url
from django.views.generic import DetailView, ListView, TemplateView
from django.utils import timezone

from app import views
from app.models import Event
from app.models import Host

urlpatterns = patterns('',
    url(r'^$',
        ListView.as_view(
            queryset=Event.objects.order_by('-event_start_time')[:10],
            context_object_name='latest_events_list',
            template_name='events.html'),
        name='events'),
    url(r'^(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Event,
            template_name='details.html'),
        name='detail'),
)
