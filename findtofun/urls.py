from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.shortcuts import render

from tastypie.api import Api
from events import api as eventApi

admin.autodiscover()


def angular(request):
    return render(request, 'base-ang.html')

v1_api = Api(api_name='v1')
v1_api.register(eventApi.FbEventResource())
v1_api.register(eventApi.FbUserResource())
v1_api.register(eventApi.FbEventFbUserResource())

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(v1_api.urls)),
    url(r'^account/', include('social_custom.urls')),
    url(r'', include('social_auth.urls')),
    url(r'^$', angular),
)
