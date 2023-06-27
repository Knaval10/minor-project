from django.views import View
from django.shortcuts import render,redirect
from tracker.forms import *
from myadmin.forms.driver import *
from django.contrib import messages
from django.contrib.auth.hashers import check_password,make_password
from django.utils.decorators import method_decorator
from tracker.decorators import *
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from myadmin.forms.mechanic import *


class MechanicHomeView(View):
    @method_decorator([mechanic_login_required,mechanic_approve_required])
    def get(self,request):
        
        return render(request,"tracker/mechanic/index.html")


class MechanicLoginView(View):
    def get(self,request):
        
        return render(request,"tracker/mechanic/login.html")
    
    def post(self,request):
        email = request.POST['email']
        password = request.POST['password']
        mechanic = Mechanic.objects.filter(email=email).first()
        # print(mechanic)
        if mechanic:
            if check_password(password,mechanic.password):
                mechanic.online = True
                mechanic.save()
                request.session['mechanic_id'] = mechanic.mechanicId
                request.session['mechanic_email'] = mechanic.email
                return redirect("mechanic_home")
            else:
                messages.error(request,"password is doesn't match")
        else:
        
            messages.error(request,"This Email id is doesn't exist")
        return redirect("mechanic_login")


class MechanicSignUpView(View):
    def get(self,request):
        form = MechanicAddForm()

        context = {
        'form':form,
        }
        return render(request,"tracker/mechanic/signup.html",context)

    def post(self,request):
        form = MechanicAddForm(request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            messages.info(request,"New Mechanic successfully registered")
        else:
            print(form.errors)

        return redirect("mechanic_signup")


@mechanic_login_required
def mechanicLogout(request):
    mechanic = Mechanic.objects.filter(mechanicId=request.session['mechanic_id']).first()
    mechanic.online = False
    mechanic.save()
    del request.session["mechanic_id"]
    del request.session["mechanic_email"]
    messages.info(request,"Mechanic Successufully logout")
    return redirect("mechanic_login")




@csrf_exempt
def mechanic_response(request):
    if request.method == "POST":
        data = json.loads(request.body)
        print(data)
        data['mechanic_id'] = request.session['mechanic_id']

        send_response_back_to_driver(data)
        if data['accept']:
            help = Help.objects.filter(id=data['help_id']).first()
            data['distance'] = data['distance']
            data['mechanic_name'] = f"{help.mechanic.fname} {help.mechanic.lname}"

            help.accept =True
            help.save()
        resp = {
            'status':True
        }


    else:
        resp = {
            'status':False
        }
    return JsonResponse(resp)


def send_response_back_to_driver(data):
    channel_layer = get_channel_layer()
    room_name = f"driver_{data['driver_id']}"
    print(room_name)

    async_to_sync(channel_layer.group_send)(
        room_name,
        {
            'type':'reply_message',
            'text':data
        }
    )

