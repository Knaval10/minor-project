from django.urls import path
from myadmin.views.mechanic_view import *


urlpatterns = [
    path("",MechanicHomeView.as_view(),name="admin_mechanic_index"),
    path("add_new/",MechanicAddView.as_view(),name="admin_mechanic_add"),
    path("update/<int:mechanic_id>/",MechanicEditView.as_view(),name="admin_mechanic_edit"),
]
