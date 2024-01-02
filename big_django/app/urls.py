from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello),
    path('tasks/', views.task_list, name="task_list")
]
