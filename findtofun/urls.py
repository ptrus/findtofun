from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^app/', include('app.urls', namespace='app')),
    url(r'^admin/', include(admin.site.urls))
)
