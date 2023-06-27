from django.db import models
from django.contrib.auth.hashers import make_password


class TimeDateTracker(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Person(TimeDateTracker):
    gender_choices = (
        ('male','male'),
        ('female','female')
    )
    status_choices = (
        ('pending','pending'),
        ('approve','approve')
    )
    fname=models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    gender = models.CharField(max_length=15,choices=gender_choices,default='male')
    birth_date = models.DateField()
    email = models.EmailField(max_length=120,unique=True,blank=False)
    contact_no = models.CharField(max_length=15)
    avatar = models.ImageField(upload_to="avatar/")
    status = models.CharField(max_length=20,choices=status_choices,default='pending')
    online = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    password = models.CharField(max_length=100)
    address = models.CharField(max_length=150)
    latitude = models.FloatField()
    longitude = models.FloatField()
    def __str__(self):
        return f"{self.fname} {self.lname}"
    
    class Meta:
        abstract = True



        
