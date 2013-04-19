from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin

from tastypie.api import Api
from events import resources

import views

v1_api = Api(api_name='v1')
v1_api.register(resources.EventResource())

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(v1_api.urls)),

    url(r'^$', views.index, name='index'),
    url(r'^contact',
        'django.contrib.auth.views.login',
        {'template_name': 'contact.html'}),

    url(r'^signup',
        TemplateView.as_view(template_name='signup.html'),
        name='signup'),
    url(r'^$',
        'django.contrib.auth.views.login',
        {'template_name': 'home.html'}),

    url(r'^events', include('events.urls')),
    url(r'', include('social_custom.urls')),
)
