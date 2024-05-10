from django.urls import path

from . import views

app_name = "acts"

urlpatterns = [
    path("home", views.home_view, name="home"),
    path("create", views.act_create, name="create"),
    path("test", views.act_test, name="test"),
    path("index", views.act_index, name="index"),
]
