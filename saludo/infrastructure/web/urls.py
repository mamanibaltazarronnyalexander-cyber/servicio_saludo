from django.urls import path

from .views import saludar_view

urlpatterns = [
    path("saludar/", saludar_view, name="saludar"),
]
