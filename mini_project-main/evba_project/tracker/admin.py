from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Staff)
admin.site.register(Driver)
admin.site.register(Mechanic)
admin.site.register(VehicleService)
admin.site.register(Help)
admin.site.register(StaffNotification)