#!/user/bin/env python
# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.shortcuts import reverse


# Go to login page if not logged in
def login(func):
    def login_fun(request, *args, **kwargs):
        if 'user_id' in request.session:
            return func(request, *args, **kwargs)
        else:
            red = HttpResponseRedirect(reverse("df_user:login"))
            red.set_cookie('url', request.get_full_path())
            # Ensure that the user still clicks to the desired page after logging in and verifying
            return red
    return login_fun

"""
http://127.0.0.1:8000/200/?type=10
request.path :Indicates the current path，for /200/
request.get_full_path():Indicates the full path, for /200/?type=10
"""
