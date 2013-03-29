from django.conf.urls import patterns, include, url

from fb.views import home, done, logout, error

urlpatterns = patterns('',
    url(r'', include('social_auth.urls')),
    url(r'^$', home, name='home'),
    url(r'^done$', done, name='done'),
    url(r'^error$', error, name='error'),
    url(r'^logout$', logout, name='logout'),
)
