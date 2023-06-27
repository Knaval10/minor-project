from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json

class StaffNotificationConsumer(WebsocketConsumer):

    def connect(self):
        self.accept()
        staff_id = self.scope['session']['staff_id']
        self.room_name = f"staff_{staff_id}"
        async_to_sync(self.channel_layer.group_add)(self.room_name,self.channel_name)
    
    def receive(self,event):
        pass

    def disconnect(self,close_code):
        async_to_sync(self.channel_layer.group_discard)(self.room_name,self.channel_name)
    

    def send_notification(self,event):
        self.send(text_data=json.dumps(event.get('text')))