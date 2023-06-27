from django.urls import path
from tracker.views.driver_view import *
from tracker.views.driver_help_view import *

urlpatterns = [
    path("",DriverHomeView.as_view(),name="driver_home"),
    path("profile/",DriverProfileView.as_view(),name="driver_profile"),
    path("signup/",DriverSignUpView.as_view(),name="driver_signup"),
    path('login/',DriverLoginView.as_view(),name="driver_login"),
    path("logout/",driverLogout,name="driver_logout"),
    path("send_help/",driverSendHelp,name="send_help"),
    path("send_help_again/",send_again_help_request,name="send_help_again"),
    path('driver_helps/',DriverHelpView.as_view(),name="driver_helps"),
]