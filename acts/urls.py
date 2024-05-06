from django.urls import path

from . import views

app_name = "acts"

urlpatterns = [
    path("", views.home_view, name="home"),
    path("create/", views.act_create, name="create"),
]
