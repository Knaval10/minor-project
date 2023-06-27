from django.urls import path,include
# from tracker.views.driver_view import *

urlpatterns = [
    path("driver/",include("tracker.nested_urls.driver_urls")),
    path("mechanic/",include("tracker.nested_urls.mechanic_urls")),
]
