from django.views import View
from django.shortcuts import render,redirect
from tracker.forms import *
from myadmin.forms.driver import *
from django.contrib import messages
from django.contrib.auth.hashers import check_password,make_password
from django.utils.decorators import method_decorator
from tracker.decorators import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .measure_dist import distance
import json
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.db import connection

class DriverHomeView(View):

    @method_decorator([driver_login_required,driver_approve_required])
    def get(self,request):
        form = HelpForm()
        context = {
            'form':form,
            
        }
        

        return render(request,"tracker/driver/index.html",context)


class DriverProfileView(View):
    @method_decorator([driver_login_required,driver_approve_required])
    def get(self,request):
        driver = Driver.objects.filter(driverId=request.session['driver_id']).first()
        form = DriverEditForm(instance=driver)
        context = {
            'driver':driver,
            'form':form,
        }
        return render(request,"tracker/driver/profile.html",context)


class DriverSignUpView(View):
    def get(self,request):
        form = DriverAddForm()
        context = {
            'form':form
        }
        return render(request,"tracker/driver/signup.html",context)
    
    def post(self,request):
        form = DriverAddForm(request.POST,files=request.FILES)
        if form.is_valid():
            driver = form.save()
            send_notifications_to_admin(driver)
            messages.info(request,"Driver Successfully Register His Account")
        
        return redirect("driver_signup")

def send_notifications_to_admin(driver):
    data = {
        'message':f"{driver.fname} {driver.lname} driver create an account and waiting for approval",
        'driver_id':driver.driverId
    }
    notification = StaffNotification(notification=json.dumps(data))
    notification.save()
    info = {
        'notification':data,
        'notification_id':notification.id
    }

    channel_layer = get_channel_layer()
    staff = Staff.objects.filter(admin=True).first()
    if staff.online:
        room_name = f"staff_{staff.staffId}"
        async_to_sync(channel_layer.group_send)(
            room_name,
            {
                'type':"send_notification",
                "text":info
            }
        )
    



class DriverLoginView(View):
    def get(self,request):
        
        return render(request,"tracker/driver/login.html")
    
    def post(self,request):
        email = request.POST['email']
        password = request.POST['password']
        driver = Driver.objects.filter(email=email).first()
        # print(driver)
        if driver:
            if check_password(password,driver.password):
                request.session['driver_id'] = driver.driverId
                driver.online=True
                driver.save()
                return redirect("driver_home")
            else:
                messages.error(request,"password is doesn't match")
        else:
        
            messages.error(request,"This Email id is doesn't exist")
        return redirect("driver_login")


@driver_login_required
def driverLogout(request):
    driver = Driver.objects.filter(driverId=request.session['driver_id']).first()
    driver.online = False
    driver.save()
    del request.session['driver_id']
    messages.info(request,"Driver Successfully logout")
    return redirect("driver_login")





class DriverHelpView(View):
    def get(self,request):
        driver = Driver.objects.filter(driverId=request.session['driver_id']).first()

        helps = Help.objects.filter(driver=driver)
        context = {
            'helps':helps
        }
        return render(request,"tracker/driver/help.html",context)