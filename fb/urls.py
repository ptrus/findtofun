from django.conf.urls import patterns, include, url

from fb.views import home, done, logout, error
from fb.facebook import facebook_view

urlpatterns = patterns('',
    url(r'^$', home, name='home'),
    url(r'^done/$', done, name='done'),
    url(r'^error/$', error, name='error'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^fb/', facebook_view, name='fb_app'),
    url(r'', include('social_auth.urls')),
)
