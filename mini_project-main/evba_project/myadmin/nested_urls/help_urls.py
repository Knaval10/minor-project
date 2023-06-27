from django.urls import path
from myadmin.views.help_view import *


urlpatterns = [
    path("",HelpIndexView.as_view(),name="admin_help_index"),
]