
from pyexpat import model
from django.db import models
# managers
from .managers import AutorManager

class Persona(models.Model):
    nombre = models.CharField(
        max_length=50
    )
    apellidos = models.CharField(
        max_length=50
    )
    nacionalidad = models.CharField(
        max_length=20
    )
    edad = models.PositiveIntegerField()

    def __str__(self):
        return str(self.id)+'-'+ self.nombre + '-'+ self.apellidos

    class Meta:
        abstract=True


class Autor(Persona):
    seudonimo = models.CharField(
        'seudonimo',
        max_length=50,
        blank= True
        )
    objects=AutorManager()
