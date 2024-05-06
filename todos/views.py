from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from .models import Todo


# Create your views here.
def todos_list(request):
    todos = Todo.objects.all()
    return render(request, "todos/todos.html", {"todos": todos})


@require_http_methods(["POST"])
def add_todo(request):
    todo = None
    title = request.POST.get("title", "")

    if title:
        todo = Todo.objects.create(title=title)
    return render(request, "todos/partials/todo.html", {"todo": todo})


@require_http_methods(["GET", "POST"])
def edit_todo(request, pk):
    todo = Todo.objects.get(pk=pk)
    if request.method == "POST":
        todo.title = request.POST.get("title", "")
        todo.save()
        return render(request, "todos/partials/todo.html", {"todo": todo})
    return render(request, "todos/partials/edit.html", {"todo": todo})


@require_http_methods(["PUT"])
def update_todo(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.is_done = True
    todo.save()
    return render(request, "todos/partials/todo.html", {"todo": todo})


@require_http_methods(["DELETE"])
def delete_todo(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.delete()
    return HttpResponse()
