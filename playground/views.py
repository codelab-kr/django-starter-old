# from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# 뷰 또는 뷰 함수 정의
# request -> response
# request handler
# action
# view function


def calcurate():
    x = 1
    # y = 2
    return x


def say_hello(request):
    calcurate()
    # return HttpResponse("Hello World")
    return render(request, "hello.html", {"name": "Mosh"})
