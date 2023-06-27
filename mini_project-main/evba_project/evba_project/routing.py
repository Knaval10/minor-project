from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from tracker.consumers import *
from channels.sessions import SessionMiddlewareStack
from myadmin.consumers import *


application = ProtocolTypeRouter({
    'websocket':AuthMiddlewareStack(
        URLRouter([
            path("ws/mechanic/notifications/",MechanicNotificationConsumer.as_asgi()),
            path("ws/driver/notifications/",DriverNotificationConsumer.as_asgi()),
            path("ws/staff/notifications/",StaffNotificationConsumer.as_asgi()),
        ]),
    )
})