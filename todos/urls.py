from django.urls import path

from . import views

app_name = "todos"

urlpatterns = [
    path("", views.todos_list, name="list"),
    path("add/", views.add_todo, name="add"),
    path("edit/<int:pk>/", views.edit_todo, name="edit"),
    path("update/<int:pk>/", views.update_todo, name="update"),
    path("delete/<int:pk>/", views.delete_todo, name="delete"),
]
