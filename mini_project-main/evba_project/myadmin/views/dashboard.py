from django.views import View
from django.shortcuts import render,redirect
from myadmin.decorators import staff_login_required
from django.utils.decorators import method_decorator
from tracker.models import *



class DashboardHome(View):
    @method_decorator(staff_login_required)
    def get(self,request):
        
        return render(request,"myadmin/base/dashboard.html")