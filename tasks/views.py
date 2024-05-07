from django.shortcuts import redirect, render

from .forms import TaskForm
from .models import Task


def index(request):
    tasks = Task.objects.all()
    return render(request, "tasks/index.html", {"tasks": tasks})


def detail(request, pk):
    task = Task.objects.get(pk=pk)
    return render(request, "tasks/detail.html", {"task": task})


def new(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("tasks:index")
    else:
        form = TaskForm()
    return render(request, "tasks/new.html", {"form": form})


def edit(request, pk):
    task = Task.objects.get(pk=pk)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("tasks:detail", pk=pk)
    else:
        form = TaskForm(instance=task)
    return render(request, "tasks/edit.html", {"task": task, "form": form})


def delete(request, pk):
    task = Task.objects.get(pk=pk)
    task.delete()
    return redirect("tasks:index")
