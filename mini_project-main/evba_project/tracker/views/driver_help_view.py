import json
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .measure_dist import distance
from tracker.models import *




@csrf_exempt
def driverSendHelp(request):
    service_id=request.POST['service_id']
    service = VehicleService.objects.filter(serviceId=service_id).first()
    problem_desc = request.POST['problem_desc']
    vehicle_image = request.FILES['vehicle_image']
    driver = Driver.objects.filter(driverId=request.session['driver_id']).first()
    mechanic = Mechanic.objects.all().first()
    cur_lat = float(request.POST['lat'])
    cur_lon = float(request.POST['lon'])
    
    
    curr_loc = {
        'lat':cur_lat,
        'lon':cur_lon
    }
    data = return_driver_list(curr_loc)
    print(data)
    if len(data):
        request.session['mechanic_list'] ={
            'data':data,
            'index':1
        }
        mechanic = Mechanic.objects.filter(mechanicId=data[0]['mechanic_id']).first()
    
        resp = {
            'status':True,
            'data':{
                'id':mechanic.mechanicId,
                'name':f"{mechanic.fname} {mechanic.lname}",
                'lat':mechanic.latitude,
                'lon':mechanic.longitude,
                'distance':data[0]['distance'],
                'service':service.name,
                'problem_desc':problem_desc
            }
        }
        help = Help(driver=driver,mechanic=mechanic,service=service,problem_desc=problem_desc,vehicle_image=vehicle_image,cur_lat=cur_lat,cur_lon=cur_lon)
        help.save()
        send_notifications(mechanic_id=mechanic.mechanicId,distance=data[0]['distance'],help=help)
    else:
        resp = {
            'status':False,
            "message":"Not anyone available"
        }


    return JsonResponse(resp)


def return_driver_list(curr_loc):
    data = []
    for mechanic in Mechanic.objects.filter(online=True):
        
        loc = {
            'lat':mechanic.latitude,
            'lon':mechanic.longitude
        }
        d = distance(curr_loc,loc)
        print(d)
        t = {
            'mechanic_id':mechanic.mechanicId,
            'distance':d
        }
        data.append(t)
    data = bubbleSort(data)
    return data


def bubbleSort(data):
    for i in range(len(data)):
        for j in range(i,len(data)-1):
            if data[j]['distance']>data[j+1]['distance']:
                t = data[j]
                data[j]=data[j+1]
                data[j+1] = t
    return data


def send_notifications(mechanic_id,distance,help):
    from channels.layers import get_channel_layer
    from asgiref.sync import async_to_sync
    channel_layer = get_channel_layer()
    room_name = f"mechanic_{mechanic_id}"
    print(room_name)
    mechanic = Mechanic.objects.filter(mechanicId=mechanic_id).first()

    data = {
        'help_id':help.id,
        'driver_id':help.driver.driverId,
        'driver_name':f"{help.driver.fname} {help.driver.lname}",
        'distance':distance,
        'vehicle_image':help.vehicle_image.url,
        'problem_desc':help.problem_desc,
        'service':help.service.name,
        'm_lat':mechanic.latitude,
        'm_lon':mechanic.longitude,
        'd_lat':help.cur_lat,
        'd_lon':help.cur_lon,
    }
    
    async_to_sync(channel_layer.group_send)(
        room_name,
        {
            'type':'send_message',
            'text':data
        }

    )

@csrf_exempt
def send_again_help_request(request):
    data = request.session['mechanic_list']['data']
    index = request.session['mechanic_list']['index']
    service_id=request.POST['service_id']
    service = VehicleService.objects.filter(serviceId=service_id).first()
    problem_desc = request.POST['problem_desc']
    vehicle_image = request.FILES['vehicle_image']
    driver = Driver.objects.filter(driverId=request.session['driver_id']).first()
    mechanic = Mechanic.objects.all().first()
    cur_lat = float(request.POST['lat'])
    cur_lon = float(request.POST['lon'])
    print(data)
    if len(data)>index:
        mechanic = Mechanic.objects.filter(mechanicId=data[index]['mechanic_id']).first()
        help = Help(driver=driver,mechanic=mechanic,service=service,problem_desc=problem_desc,vehicle_image=vehicle_image,cur_lat=cur_lat,cur_lon=cur_lon)
        help.save()
        send_notifications(mechanic_id=data[index]['mechanic_id'],distance=data[index]['distance'],help=help)
        request.session['mechanic_list'] ={
            'data':data,
            'index':index+1
        }
        resp = {
            'status':True,
            'data':{
                'id':mechanic.mechanicId,
                'name':f"{mechanic.fname} {mechanic.lname}",
                'lat':mechanic.latitude,
                'lon':mechanic.longitude,
                'distance':data[index]['distance'],
                'service':service.name,
                'problem_desc':problem_desc
            }
        }
        
    else:
        resp = {
            'status':False,
            'message':"No other Mechanic Available"
        }
    
    return JsonResponse(resp)