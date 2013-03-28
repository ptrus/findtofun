from django.core.urlresolvers import reverse

from social_auth.exceptions import AuthAlreadyAssociated
from social_auth.middleware import SocialAuthExceptionMiddleware


class ExampleSocialAuthExceptionMiddleware(SocialAuthExceptionMiddleware):
    def raise_exception(self, request, exception):
        return False

    def get_message(self, request, exception):
        if isinstance(exception, AuthAlreadyAssociated):
            return 'Somebody is already using that account!'
        return super(ExampleSocialAuthExceptionMiddleware, self)\
                        .get_message(request, exception)

    def get_redirect_uri(self, request, exception):
        if request.user.is_authenticated():
            return reverse('done')
        else:
            return reverse('error')
        
import re

from django.conf import settings
from django.core import urlresolvers
from django.http import HttpResponse, HttpResponseRedirect


class SSLMiddleware(object):

    def process_request(self, request):
        if not any([settings.DEBUG, request.is_secure(), request.META.get("HTTP_X_FORWARDED_PROTO", "") == 'https']):
            url = request.build_absolute_uri(request.get_full_path())
            secure_url = url.replace("http://", "https://")
            return HttpResponseRedirect(secure_url)