from django.db import models
from .person import Person
from .vehicle_service import *
from django.contrib.auth.hashers import make_password



class Mechanic(Person):
    
    mechanicId = models.AutoField(primary_key=True,unique=True)
    pan_no = models.CharField(max_length=20,unique=True,blank=False)
    services = models.ManyToManyField(VehicleService,related_name="provide_services")


    def save(self,*args,**kwargs):
        if self.mechanicId is None:
            self.password = make_password(self.password)
        super(Mechanic,self).save(*args,**kwargs)