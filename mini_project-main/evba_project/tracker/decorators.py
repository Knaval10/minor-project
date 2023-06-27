
from django.shortcuts import redirect
from django.contrib import messages
from tracker.models import *


def driver_login_required(func):
    def wrapper(request,*args,**kwargs):
        try:
            request.session['driver_id']
        except:
            messages.error(request,"Driver First Login Required !!!")
            return redirect("driver_login")
        return func(request,*args,**kwargs)
    return wrapper

def driver_approve_required(func):
    def wrapper(request,*args,**kwargs):
        driver = Driver.objects.filter(driverId=request.session['driver_id']).first()
        print(driver.status)
        if driver.status=='approve':
            return func(request,*args,**kwargs)
        else:
            messages.error(request,"Driver First Approval Required !!!")
            return redirect("driver_login")
    return wrapper



def mechanic_login_required(func):
    def wrapper(request,*args,**kwargs):
        try:
            request.session['mechanic_id']
        except:
            messages.error(request,"Mechanic First Login Required !!!")
            return redirect("mechanic_login")
        return func(request,*args,**kwargs)
    return wrapper

def mechanic_approve_required(func):
    def wrapper(request,*args,**kwargs):
        mechanic = Mechanic.objects.filter(mechanicId=request.session['mechanic_id']).first()
        if mechanic.status=='approve':
            return func(request,*args,**kwargs)
        else:
            messages.error(request,"Mechanic First Approval Required !!!")
            return redirect("mechanic_login")
    return wrapper


