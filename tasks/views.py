from django.http import Http404
from .models import Task, Person
from django.shortcuts import render, redirect


def getTasks(request):
    taskList = Task.objects.all()
    return render(request, 'tasks/listTasks.html', {'taskList': taskList})

def getById(request, task_id):
    try:
        task = Task.objects.get(pk=task_id)
    except Task.DoesNotExist:
        raise Http404("a task que voce procura não existe")
    return render(request, 'tasks/taskDetail.html', {"task": task})

def taskAdd(request):
    person = Person.objects.all()

    if request.method == "POST":
        data = request.POST
        title = data.get("title")
        description = data.get("description")
        status = data.get("status")
        person_names = request.POST.getlist("person")

        new_task = Task.objects.create(
            title=title,
            description=description,
            status=status,
        )

        for person_name in person_names:
            person_instance = Person.objects.get(name=person_name)
            new_task.person.add(person_instance)
        
        return redirect("tasks:taskDetail", task_id=new_task.id)


    return render(request, 'tasks/taskAdd.html', {"person": person, "status": {0: "Pendente", 1: "Concluida"}})