from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    # # TASKS
    path("", views.getTasks, name="taskList"),
    path("task/<int:task_id>", views.getTaskById, name="taskDetail"),
    path("task/add/", views.taskAdd, name="taskAdd"),
    path("task/<int:task_id>/update/", views.taskUpdate, name="taskUpdate"),
    path("task/<int:task_id>/delete/", views.taskDelete, name="taskDelete"),

    # PERSONS
    path("person/", views.getPersons, name="personList"),
    path("person/<int:person_id>", views.getPersonById, name="personDetail"),
    path("person/add/", views.personAdd, name="personAdd"),
    path("person/<int:person_id>/update/", views.personUpdate, name="personUpdate"),
    path("person/<int:person_id>/delete/", views.personDelete, name="personDelete"),
    

    # API TASKS
    path("api/", views.TaskListView.as_view(), name="taskListApi"),
    path("api/task/<int:pk>/", views.TaskDetailView.as_view(), name="taskDetailApi"),
    path("api/task/add/", views.TaskCreateView.as_view(), name="taskAddApi"),
    path("api/task/<int:pk>/update/", views.TaskUpdateView.as_view(), name="taskUpdateApi"),
    path("api/task/<int:pk>/delete/", views.TaskDeleteView.as_view(), name="taskDeleteApi"),

    # API PERSONS
    path("api/person/", views.PersonListView.as_view(), name="personListApi"),
    path("api/person/<int:pk>/", views.PersonDetailView.as_view(), name="personDetailApi"),
    path("api/person/add/", views.PersonCreateView.as_view(), name="personAddApi"),
    path("api/person/<int:pk>/update/", views.PersonUpdateView.as_view(), name="personUpdateApi"),
    path("api/person/<int:pk>/delete/", views.PersonDeleteView.as_view(), name="personDeleteApi"),
]