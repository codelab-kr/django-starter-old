from django.shortcuts import render


# Create your views here.
def todos_list(request):
    return render(request, "todos/todos.html")
