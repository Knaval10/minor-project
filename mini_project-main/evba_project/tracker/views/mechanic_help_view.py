
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from tracker.models import *








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
