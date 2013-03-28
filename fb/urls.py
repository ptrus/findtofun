from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from social_auth.views import auth, complete, disconnect

from fb.views import home, done, logout, error
from fb.facebook import facebook_view

urlpatterns = patterns('',
    url(r'^$', home, name='home'),
    url(r'^done/$', done, name='done'),
    url(r'^error/$', error, name='error'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^fb/', facebook_view, name='fb_app'),
    
    url(r'^associate/(?P<backend>[^/]+)/$',
        login_required(auth),
        name='socialauth_begin'),
    url(r'^associate/complete/(?P<backend>[^/]+)/$',
        login_required(complete),
        name='socialauth_complete'),

    url(r'^disconnect/(?P<backend>[^/]+)/$',
        disconnect,
        name='socialauth_disconnect'),
    url(r'^disconnect/(?P<backend>[^/]+)/(?P<association_id>[^/]+)/$',
        disconnect,
        name='socialauth_disconnect_individual'),
                       
    url(r'', include('social_auth.urls')),
)
