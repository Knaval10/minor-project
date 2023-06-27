from django.urls import path
from myadmin.views.staff_view import *


urlpatterns = [
    path("",StaffIndexView.as_view(),name="staff_index"),
    # path("",Staff)
]
