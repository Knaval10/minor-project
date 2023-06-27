from django.views import View
from django.shortcuts import render,redirect
from tracker.models import *
from myadmin.forms.driver import *
from django.contrib import messages
from myadmin.decorators import staff_login_required
from django.utils.decorators import method_decorator


class DriverHomeView(View):
    @method_decorator(staff_login_required)
    def get(self,request):
        # staff = Staff.objects.filter(staffId=request.session['staff_id']).first()
        dirvers = Driver.objects.all()
        context = {
            'drivers':dirvers,
          
        }
        return render(request,"myadmin/driver/index.html",context)


class DriverAddView(View):
    @method_decorator(staff_login_required)
    def get(self,request):
        form = DriverAddForm()
        context = {
            'form':form
        }
        return render(request,"myadmin/driver/add.html",context)
    @method_decorator(staff_login_required)
    def post(self,request):
        form = DriverAddForm(request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"New Driver Registration")
        
        return redirect("admin_driver_add")


class DriverUpdateView(View):
    @method_decorator(staff_login_required)
    def get(self,request,driver_id):
        driver = Driver.objects.filter(driverId=driver_id).first()
        if driver:
            form = DriverUpdateForm(instance=driver)
            context = {
                'form':form,
                'driver':driver
            }
            return render(request,"myadmin/driver/edit.html",context)
    @method_decorator(staff_login_required)
    def post(self,request,driver_id):
        driver = Driver.objects.filter(driverId=driver_id).first()
        if driver:
            form = DriverUpdateForm(instance=driver,data=request.POST,files=request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request,f"{driver} successfully updated details")
            else:
                print(form.errors)
            return redirect(f"/myadmin/driver_mngt/update/{driver_id}/")
            

    