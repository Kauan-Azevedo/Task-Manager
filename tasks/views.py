from django.http import Http404
from .models import Task, Person
from django.shortcuts import render


def getTasks(request):
    taskList = Task.objects.all()
    return render(request, 'tasks/index.html', {'taskList': taskList})

def getById(request, task_id):
    try:
        task = Task.objects.get(pk=task_id)
    except Task.DoesNotExist:
        raise Http404("a task que voce procura não existe")
    return render(request, 'tasks/taskDetail.html', {"task": task})