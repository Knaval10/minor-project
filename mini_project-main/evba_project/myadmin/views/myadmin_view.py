from django.views import View
from django.shortcuts import render,redirect
from tracker.models import *
from django.contrib.auth.hashers import check_password
from django.contrib import messages
from myadmin.decorators import staff_login_required
from django.utils.decorators import method_decorator
import json
from django.http import JsonResponse


class MyAdminLoginView(View):
    
    def get(self,request):


        return render(request,"myadmin/base/login.html")
    
    def post(self,request):
        email = request.POST['email']
        password = request.POST['password']
        staff = Staff.objects.filter(email=email).first()
        if staff:
            if check_password(password,staff.password):
                if staff.admin:
                    request.session['staff_id'] = staff.staffId
                    request.session['avatar_url'] = staff.avatar.url
                    staff.online = True
                    staff.save()
                    return redirect("admin_dashboard")
                else:
                    messages.error(request,"Only Admin can Login")
            else:
                messages.error(request,"Password is doesn't exist")
        else:
            messages.error(request,"This email id doesn't exists")
        return redirect("myadmin_login")


@staff_login_required
def adminLogout(request):
    staff = Staff.objects.filter(staffId=request.session['staff_id']).first()
    staff.online =False
    staff.save()
    del request.session['staff_id']
    del request.session['avatar_url']
    messages.info(request,"successfully logout admin")
    return redirect("myadmin_login")


def fetch_notifications(request):
    notifications = StaffNotification.objects.all().order_by('-created_at')
    data = []
    for notification in notifications:
        
        t = {
            'notification_id':notification.id,
            'notification':json.loads(notification.notification)
        }
        data.append(t)
    
    resp = {
        'status':True,
        'data':data,
        'not_seen':StaffNotification.objects.filter(watch=False).count()
    }
    return JsonResponse(resp)


def watch_notifications(request):
    notifications = StaffNotification.objects.filter(watch=False)
    for notification in notifications:
        notification.watch = True
        notification.save()

    resp = {
        'status':True
    }
    return JsonResponse(resp)
