from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required

def anonymous_required(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseForbidden()
        else:
            return view_func(request, *args, **kwargs)
    return wrapper

def sponsor_required(view_func):
    @login_required
    def wrapper(request, *args, **kwargs):
        if request.user.user_type != 'sponsor':
            return HttpResponseForbidden()
        else:
            return view_func(request, *args, **kwargs)
    return wrapper

def influencer_required(view_func):
    @login_required
    def wrapper(request, *args, **kwargs):
        if request.user.user_type != 'influencer':
            return HttpResponseForbidden()
        else:
            return view_func(request, *args, **kwargs)
    return wrapper
