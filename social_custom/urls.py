from django.conf.urls import url, patterns
from django.views.generic import RedirectView

from views import logout

urlpatterns = patterns(
    '',
    url(r'^logout', logout, name='logout'),
    url(r'', RedirectView.as_view(url='/')),
)
