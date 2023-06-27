from django.db import models
from tracker.models import *
from django.contrib.auth.hashers import make_password


class Driver(Person):
    driverId = models.AutoField(primary_key=True,unique=True)
    liscence_no = models.CharField(max_length=20,unique=True)

    def save(self,*args,**kwargs):
        if self.driverId is None:
            self.password = make_password(self.password)
        super(Driver,self).save(*args,**kwargs)


