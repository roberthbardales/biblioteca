import datetime
from itertools import count
from django.db import models
from django.db.models import Q, Count, Avg, Sum

class PrestamoManager(models.Manager):
    """Procesdimientos para manager"""

    def libros_promedio_edades(self):
        resultado=self.filter(
            libro__id='1'

        ).aggregate(
            promedio_edad=Avg('lector__edad'),
            suma_edad=Sum('lector__edad')
        )
        #   from applications.lector.models import * 
        #   Prestamo.objects.libros_promedio_edades()
        return resultado
    def num_libros_prestados(self):
        resultado=self.values(
            'libro'
        ).annotate(
            num_prestados=Count('libro')
        )
        for r in resultado:
            print('=========')
            print(r,r['num_prestados'])

        #   from applications.lector.models import * 
        #   Prestamo.objects.num_libros_prestados()

        return resultado

