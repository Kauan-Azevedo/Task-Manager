from django.db import models


class Person(models.Model):

    def __str__(self) -> str:
        return self.name

    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    role = models.IntegerField(choices=((0, ("Cliente")),
                                        (1, ("Colaborador"))),
                                default=0)




class Task(models.Model):

    def __str__(self) -> str:
        return self.title

    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    status = models.IntegerField(choices=((0, ("Pendente")),
                                        (1, ("Concluida"))),
                                default=0)
    person = models.ManyToManyField(Person)