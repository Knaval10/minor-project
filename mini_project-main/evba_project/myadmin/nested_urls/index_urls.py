from django.urls import path
from myadmin.views import *

urlpatterns = [
    path("",DashboardHome.as_view(),name="admin_dashboard"),
]
