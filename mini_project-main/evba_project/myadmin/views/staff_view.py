from django.views import View
from django.shortcuts import render,redirect
from tracker.models import *
from myadmin.forms.driver import *
from django.contrib import messages
from myadmin.decorators import staff_login_required
from django.utils.decorators import method_decorator


class StaffIndexView(View):
    def get(self,request):
        staffs = Staff.objects.all()
        context = {
            'staffs':staffs
        }

        return render(request,"myadmin/staff/index.html",context)


