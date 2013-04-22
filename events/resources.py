# myapp/api.py
from tastypie.resources import ModelResource
from tastypie.authentication import SessionAuthentication
from events import models


class EventResource(ModelResource):
    class Meta:
        queryset = models.Event.objects.order_by('-start_time')[:10]
        resource_name = 'event'
        allowed_methods = ['get']
        # authentication = SessionAuthentication()
