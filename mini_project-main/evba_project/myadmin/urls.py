from django.urls import path,include
# from django.urls import path
from myadmin.views.myadmin_view import *


urlpatterns = [
    path("",include("myadmin.nested_urls.index_urls")),
    path("driver_mngt/",include("myadmin.nested_urls.driver_urls")),
    path("mechanic_mngt/",include("myadmin.nested_urls.mechanic_urls")),
    path("service_mngt/",include("myadmin.nested_urls.service_urls")),
    path("help_mngt/",include("myadmin.nested_urls.help_urls")),

    path("staff_mngt/",include("myadmin.nested_urls.staff_urls")),
    path("login/",MyAdminLoginView.as_view(),name="myadmin_login"),
    path("logout/",adminLogout,name="myadmin_logout"),
    path("fetch_notifications/",fetch_notifications,name="fetch_notifications"),
    path("watch_notifications/",watch_notifications,name="watch_notifications"),

]
