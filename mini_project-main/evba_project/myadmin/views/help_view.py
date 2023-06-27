from django.views import View
from django.shortcuts import render,redirect
from tracker.models import *

from django.contrib import messages
from myadmin.decorators import staff_login_required
from django.utils.decorators import method_decorator



class HelpIndexView(View):
    @method_decorator(staff_login_required)
    def get(self,request):
        helps = Help.objects.all()
        context = {
            'helps':helps
        }
        return render(request,"myadmin/help/index.html",context)