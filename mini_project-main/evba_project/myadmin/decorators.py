
from django.shortcuts import redirect
from django.contrib import messages
from tracker.models import *

def staff_login_required(func):
    def wrapper(request,*args,**kwargs):
        try:
            request.session['staff_id']
        except:
            messages.error(request,"Staff First Login Required !!!")
            return redirect("myadmin_login")
        return func(request,*args,**kwargs)
    return wrapper