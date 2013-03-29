from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^contact', 'django.contrib.auth.views.login', {'template_name': 'contact.html'}),
    url(r'^signup',
        TemplateView.as_view(template_name='signup.html'),
        name='signup'),
    url(r'^$', 'django.contrib.auth.views.login', {'template_name': 'home.html'}),
    url(r'', include('events.urls', namespace="events")),
    url(r'', include('fb.urls')),
)