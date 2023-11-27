from django.http import Http404
from .models import Task, Person
from .models import Task, Person
from django.shortcuts import render, redirect

from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from .serializers import TaskSerializer, PersonSerializer



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

# Django rest Framework API

class TaskListView(ListAPIView):
    """
    API endpoint that shows all tasks created in descending order.
    """
    queryset = Task.objects.all().order_by('-id')
    serializer_class = TaskSerializer

class TaskDetailView(RetrieveAPIView):
    """
    API endpoint that allows viewing a task by its ID.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskCreateView(CreateAPIView):
    """
    API endpoint that allows creating a task.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskUpdateView(UpdateAPIView):
    """
    API endpoint that allows updating task data.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskDeleteView(DestroyAPIView):
    """
    API endpoint that allows deleting a task.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class PersonListView(ListAPIView):
    """
    API endpoint that shows all persons.
    """
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class PersonDetailView(RetrieveAPIView):
    """
    API endpoint that allows viewing a person by their ID.
    """
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class PersonCreateView(CreateAPIView):
    """
    API endpoint that allows creating a person.
    """
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class PersonUpdateView(UpdateAPIView):
    """
    API endpoint that allows updating person data.
    """
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class PersonDeleteView(DestroyAPIView):
    """
    API endpoint that allows deleting a person.
    """
    queryset = Person.objects.all()
    serializer_class = PersonSerializer