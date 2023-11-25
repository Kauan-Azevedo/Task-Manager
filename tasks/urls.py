from django.urls import path

from . import views

app_name = 'tasks'

urlpatterns = [
    path("", views.getTasks, name="taskList"),
    path("task/<int:task_id>", views.getById, name="taskDetail"),
    path("add//", views.taskAdd, name="taskAdd"),
]