from django.http import HttpResponse
from .models import Task, Person
from django.shortcuts import render


def getTasks(request):
    taskList = Task.objects.all()
    return render(request, 'task_manager/index.html', {'taskList': taskList})

def getById(request, task_id):
    return HttpResponse(f"Getting task {task_id}")