from django.views import View
from tracker.models import *
from django.contrib import messages
from django.shortcuts import redirect,render
from myadmin.forms.service import *
from myadmin.decorators import staff_login_required
from django.utils.decorators import method_decorator


class ServiceHomeView(View):
    @method_decorator(staff_login_required)
    def get(self,request):
        services = VehicleService.objects.all()
        context = {
            'services':services
        }
        return render(request,"myadmin/service/index.html",context)


class ServiceAddView(View):
    @method_decorator(staff_login_required)
    def get(self,request):
        form = ServiceForm()
        context = {
            'form':form
        }
        return render(request,"myadmin/service/add.html",context)
    
    @method_decorator(staff_login_required)
    def post(self,request):
        form = ServiceForm(request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"added new survice successfully")
        return redirect("admin_service_add")


class ServiceEditView(View):
    @method_decorator(staff_login_required)
    def get(self,request,service_id):
        service = VehicleService.objects.filter(serviceId=service_id).first()
        form = ServiceForm(instance=service)
        context = {
            'form':form
        }
        return render(request,"myadmin/service/update.html",context)
    @method_decorator(staff_login_required)
    def post(self,request,service_id):
        service = VehicleService.objects.filter(serviceId=service_id).first()
        form = ServiceForm(instance=service,data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"update survice successfully")
        return redirect(f"/myadmin/service_mngt/update/{service_id}/")
