from django.urls import path

from . import views

app_name = 'tasks'

urlpatterns = [
    path("", views.getTasks, name="taskList"),
    path("task/<int:task_id>", views.getTaskById, name="taskDetail"),
    path("task/add/", views.taskAdd, name="taskAdd"),
    path("task/<int:task_id>/update/", views.taskUpdate, name="taskUpdate"),
    path("task/<int:task_id>/delete/", views.taskDelete, name="taskDelete"),

    path("person/", views.getPersons, name="personList"),
    path("person/<int:person_id>", views.getPersonById, name="personDetail"),
    path("person/add/", views.personAdd, name="personAdd"),
    path("person/<int:person_id>/update/", views.personUpdate, name="personUpdate"),
    path("person/<int:person_id>/delete/", views.personDelete, name="personDelete"),

]