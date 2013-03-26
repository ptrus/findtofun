from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^events/', include('app.urls', namespace="events")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^contact',
        TemplateView.as_view(template_name='events/contact.html'),
        name='contact'),
    url(r'^$',
        TemplateView.as_view(template_name='events/signup.html'),
        name='sign_up'),
    url(r'', include('fb.urls')),
)