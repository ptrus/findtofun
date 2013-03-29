from django.contrib.auth import logout as auth_logout
from django.http import HttpResponseRedirect


def logout(request):
    """Logs out user"""
    auth_logout(request)
    return HttpResponseRedirect('/')