from django.http import Http404
from .models import Task, Person
from django.shortcuts import render, redirect


def getTasks(request):
    taskList = Task.objects.all().order_by('-id')
    return render(request, 'tasks/taskList.html', {'taskList': taskList})

def getTaskById(request, task_id):
    try:
        person = Person.objects.all()
        task = Task.objects.get(pk=task_id)
    except Task.DoesNotExist:
        raise Http404("a task que voce procura não existe")
    return render(request, 'tasks/taskDetail.html', {"task": task, "person": person})

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
        
        new_task.save()
        return redirect("tasks:taskDetail", task_id=new_task.id)


    return render(request, 'tasks/taskAdd.html', {"person": person, "status": {0: "Pendente", 1: "Concluida"}})

def taskUpdate(request, task_id):
    try:
        task = Task.objects.get(pk=task_id)
    except Task.DoesNotExist:
        raise Http404("Tarefa inexistente!")

    if request.method == "POST":
        data = request.POST
        task.title = data.get("title")
        task.description = data.get("description")
        task.status = data.get("status")
        task.person.clear()
        
        person_names = request.POST.getlist("person")
        for person_name in person_names:
            person_instance = Person.objects.get(name=person_name)
            task.person.add(person_instance)
        
        task.save()
        return redirect("tasks:taskDetail", task_id=task.id)

    person = Person.objects.all()
    return render(request, 'tasks/taskUpdate.html', {"task": task, "person": person, "status": {0: "Pendente", 1: "Concluída"}})

def taskDelete(request, task_id):
    try:
        task = Task.objects.get(pk=task_id)
    except Task.DoesNotExist:
        raise Http404("Tarefa inexistente!")

    if request.method == "POST":
        task.delete()
        return redirect("tasks:taskList")

    return render(request, 'tasks/taskDelete.html', {"task": task})

# CRUD PESSOAS

def getPersons(request):
    personList = Person.objects.all().order_by('-id')
    return render(request, 'persons/personList.html', {'personList': personList})

def getPersonById(request, person_id):
    try:
        person = Person.objects.get(pk=person_id)
    except Person.DoesNotExist:
        raise Http404("a pessoa que voce procura não existe")
    return render(request, 'persons/personDetail.html', {"person": person})

def personAdd(request):
    if request.method == "POST":
        data = request.POST
        
        name = data.get("name")
        role = data.get("role")
        
        new_person = Person.objects.create(
            name=name,
            role=role
        )

        new_person.save()
        return redirect("tasks:personDetail", person_id=new_person.id)


    return render(request, 'persons/personAdd.html', {"roles": {0: "Cliente", 1: "Colaborador"}})

def personUpdate(request, person_id):
    try:
        person = Person.objects.get(pk=person_id)
    except Person.DoesNotExist:
        raise Http404("Pessoa inexistente!")

    if request.method == "POST":
        data = request.POST
        person.name = data.get("name")
        person.role = data.get("role")
        
        person.save()
        return redirect("tasks:personDetail", person_id=person.id)

    return render(request, 'tasks/taskUpdate.html', {"person": person, "status": {0: "Cliente", 1: "Colaborador"}})

def personDelete(request, person_id):
    try:
        person = Person.objects.get(pk=person_id)
    except Person.DoesNotExist:
        raise Http404("Pessoa inexistente!")

    if request.method == "POST":
        person.delete()
        return redirect("tasks:personList")

    return render(request, 'tasks/personDelete.html', {"person": person})