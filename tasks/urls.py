from django.urls import path

from . import views

app_name = 'tasks'

urlpatterns = [
    path("", views.getTasks, name="taskList"),
    path("task/<int:task_id>", views.getById, name="taskDetail"),
    path("task/add/", views.taskAdd, name="taskAdd"),
    path("task/<int:task_id>/update/", views.taskUpdate, name="taskUpdate"),
    path("task/<int:task_id>/delete/", views.taskDelete, name="taskDelete")
]