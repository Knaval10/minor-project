from django.urls import path
from myadmin.views.driver_view import *

urlpatterns = [
    path("",DriverHomeView.as_view(),name="admin_driver_index"),
    path("add_new/",DriverAddView.as_view(),name="admin_driver_add"),
    path("update/<int:driver_id>/",DriverUpdateView.as_view(),name="admin_driver_update"),
]

