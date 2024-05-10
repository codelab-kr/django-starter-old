from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods

from . import forms
from .models import Act


def home_view(request):
    acts = Act.objects.all()
    return render(request, "acts/home.html", {"acts": acts})


@require_http_methods(["GET", "POST"])
def act_create(request):
    if request.method == "POST":
        form = forms.CreateAct(request.POST)
        if form.is_valid():
            new_act = form.save(commit=False)
            # new_act.author = request.user
            new_act.save()
            return redirect("acts:home")
    form = forms.CreateAct()
    return render(request, "acts/act_create.html", {"form": form})


def act_test(request):
    return render(request, "test.html")


def act_index(request):
    return render(request, "index.html")
