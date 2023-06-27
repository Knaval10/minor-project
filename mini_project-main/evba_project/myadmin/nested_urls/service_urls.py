from django.urls import path
from myadmin.views.service_view import *


urlpatterns = [
    path("",ServiceHomeView.as_view(),name="admin_service_index"),
    path("add_new/",ServiceAddView.as_view(),name="admin_service_add"),
    path("update/<int:service_id>/",ServiceEditView.as_view(),name="admin_service_edit"),
]
