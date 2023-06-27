from django.urls import path
from tracker.views.mechanic_view import *


urlpatterns = [
    path('', MechanicHomeView.as_view(),name="mechanic_home"),
    path("login/",MechanicLoginView.as_view(),name="mechanic_login"),
    path("logout/",mechanicLogout,name="mechanic_logout"),
    path("send_response/",mechanic_response,name="mechanic_response"),
    path("signup/",MechanicSignUpView.as_view(),name="mechanic_signup"),
]