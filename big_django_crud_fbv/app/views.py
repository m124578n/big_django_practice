from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from .models import Task
from .forms import TaskForm

# Create your views here.

def hello(request):
    return HttpResponse("hello world!")


def task_list(request):
    tasks = Task.objects.all()
    return render(request, "task_list.html", {"tasks": tasks})


def task_create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("tasks:task_list"))
    else:
        form = TaskForm
    return render(request, "task_form.html", {"form": form})


def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, "task_detail.html", {"task": task})


def task_update(request, pk):
    task_obj = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        form = TaskForm(instance=task_obj, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("tasks:task_detail", args=[pk, ]))
    else:
        form = TaskForm(instance=task_obj)
    return render(request, "task_form.html", {"form": form, "object": task_obj})


def task_delete(request, pk):
    task_obj = get_object_or_404(Task, pk=pk)
    task_obj.delete()
    return redirect(reverse("tasks:task_list"))
