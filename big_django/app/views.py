from django.shortcuts import render
from django.http import HttpResponse
from .models import Task

# Create your views here.

def hello(request):
    return HttpResponse("hello world!")


def task_list(request):
    tasks = Task.objects.all()
    return render(request, "task_list.html", {"tasks": tasks})
