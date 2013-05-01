from django.http import HttpResponseRedirect
from django.contrib.auth import logout as auth_logout


def logout(request):
    """Logs out user"""
    auth_logout(request)
    return HttpResponseRedirect('/')
