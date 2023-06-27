from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json



class MechanicNotificationConsumer(WebsocketConsumer):

    def connect(self):
        self.accept()
        mechanic_id = self.scope['session']['mechanic_id']
        self.room_name = f"mechanic_{mechanic_id}"
        async_to_sync(self.channel_layer.group_add)(self.room_name,self.channel_name)
    
    def receive(self,event):
        pass

    def disconnect(self,close_code):
        async_to_sync(self.channel_layer.group_discard)(self.room_name,self.channel_name)
    

    def send_message(self,event):
        self.send(text_data=json.dumps(event.get('text')))


class DriverNotificationConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        driver_id = self.scope['session']['driver_id']
        self.room_name = f"driver_{driver_id}"
        print(self.room_name)
        async_to_sync(self.channel_layer.group_add)(self.room_name,self.channel_name)
    
    def receive(self,event):
        pass

    def disconnect(self,close_code):
        async_to_sync(self.channel_layer.group_discard)(self.room_name,self.channel_name)
    

    def reply_message(self,event):
        
        self.send(text_data=json.dumps(event.get('text')))
    


