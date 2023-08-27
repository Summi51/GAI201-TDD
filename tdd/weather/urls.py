from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("weather/<str:city>/", views.get_weather, name="get-weather"),
    path("weather/", views.create_weather, name="create-weather"),
    path("weather/<str:city>/update/", views.update_weather, name="update-weather"),
    path("weather/<str:city>/delete/", views.del_weather, name="del-weather"),
]