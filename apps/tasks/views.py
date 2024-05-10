from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from .forms import TaskForm
from .models import Task


def index(request):
    tasks = Task.objects.all()
    return render(request, "tasks/tasks.html", {"tasks": tasks})


@require_http_methods(["POST"])
def add(request):
    form = TaskForm(request.POST)
    if form.is_valid():
        form.save()
        return render(
            request, "tasks/partials/task.html", {"form": form, "task": form.instance}
        )
    else:
        messages.error(request, form.errors.as_text())
        return render(request, "tasks/partials/task.html", {"form": form})


@require_http_methods(["GET", "POST"])
def edit(request, pk):
    task = Task.objects.get(pk=pk)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return render(request, "tasks/partials/task.html", {"task": task})
    else:
        form = TaskForm(instance=task)
    return render(request, "tasks/partials/edit.html", {"task": task, "form": form})


@require_http_methods(["PUT"])
def update(request, pk):
    task = Task.objects.get(pk=pk)
    task.is_done = True
    task.save()
    return render(request, "tasks/partials/task.html", {"task": task})


@require_http_methods(["DELETE"])
def delete(request, pk):
    task = Task.objects.get(pk=pk)
    task.delete()
    return HttpResponse()
