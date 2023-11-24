from django.db import models


class Person(models.Model):

    def __str__(self) -> str:
        return self.name

    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    role = models.IntegerField(choices=((1, ("Cliente")),
                                        (2, ("Colaborador"))),
                                default=1)




class Task(models.Model):

    def __str__(self) -> str:
        return self.title

    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    status = models.BooleanField(default=False)
    person = models.ManyToManyField(Person)