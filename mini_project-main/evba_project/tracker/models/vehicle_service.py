from django.db import models
# from .vehicle_repair import Mechanic
from tracker.models import *


class VehicleService(TimeDateTracker):
    serviceId = models.AutoField(primary_key=True,unique=True)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="vehicle_thumbnail/")

    def __str__(self):
        return self.name
    
    

