from django.db import models
from .person import *
from django.contrib.auth.hashers import make_password


class Staff(Person):
    staffId = models.AutoField(unique=True,primary_key=True)
    admin = models.BooleanField(default=False)


    def save(self,*args,**kwargs):
        if self.staffId is None:
            self.password = make_password(self.password)
        super(Staff,self).save(*args,**kwargs)



class StaffNotification(TimeDateTracker):
    notification = models.TextField()
    watch = models.BooleanField(default=False)


    def __str__(self):
        return self.notification
    