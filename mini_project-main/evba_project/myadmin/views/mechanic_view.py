from django.views import View
from django.shortcuts import render,redirect
from tracker.models import *
from django.contrib import messages
from myadmin.forms.mechanic import *
from django.contrib.auth.hashers import make_password
from myadmin.decorators import *
from myadmin.decorators import staff_login_required
from django.utils.decorators import method_decorator


class MechanicHomeView(View):
    @method_decorator(staff_login_required)
    def get(self,request):
        mechanics = Mechanic.objects.all()
        context = {
            'mechanics':mechanics
        }
        return render(request,"myadmin/mechanic/index.html",context)


class MechanicAddView(View):
    @method_decorator(staff_login_required)
    def get(self,request):
        form = MechanicAddForm()
        context = {
            'form':form
        }
        return render(request,"myadmin/mechanic/add.html",context)
    @method_decorator(staff_login_required)
    def post(self,request):

        form = MechanicAddForm(request.POST,files=request.FILES)
        if form.is_valid():
            mechanic = form.save()
            # mechanic.password = make_password(mechanic.password)
            # mechanic.save()
            messages.success(request,"added new mechanic successfully")
        else:
            print(form.errors)
        
        return redirect("admin_mechanic_add")

class MechanicEditView(View):
    @method_decorator(staff_login_required)
    def get(self,request,mechanic_id):
        mechanic = Mechanic.objects.filter(mechanicId=mechanic_id).first()
        form = MechanicUpdateForm(instance=mechanic)
        context = {
            'form':form,
            'mechanic':mechanic
        }
        return render(request,"myadmin/mechanic/edit.html",context)
    @method_decorator(staff_login_required)
    def post(self,request,mechanic_id):
        mechanic = Mechanic.objects.filter(mechanicId = mechanic_id).first()
        form = MechanicUpdateForm(instance=mechanic,files=request.FILES,data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"successfully updated the mechanic")
        else:
            print(form.errors)
        return redirect(f"/myadmin/mechanic_mngt/update/{mechanic_id}/")