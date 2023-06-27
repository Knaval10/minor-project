from tracker.models import *
from django.db import models

class Location(models.Model):
    cur_lat = models.FloatField()
    cur_lon = models.FloatField()

    class Meta:
        abstract = True

class Help(TimeDateTracker,Location):
    driver = models.ForeignKey(Driver,on_delete=models.CASCADE)
    service = models.ForeignKey(VehicleService,on_delete=models.CASCADE)
    problem_desc = models.TextField()
    mechanic = models.ForeignKey(Mechanic,on_delete=models.CASCADE)
    vehicle_image = models.ImageField(upload_to="vehicle_image/")
    accept = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.driver} {self.mechanic}"