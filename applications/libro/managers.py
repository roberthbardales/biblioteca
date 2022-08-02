import datetime
from itertools import count
from django.db import models
from django.db.models import Q, Count


class LibroManager(models.Manager):

    def listar_libros(self, kword):

        resultado = self.filter(
            titulo__icontains=kword,
            fecha__range=('2000-01-01', '2010-01-01')
        )
        return resultado

    def listar_libros3(self, kword, fecha1, fecha2):

        date1 = datetime.datetime.strptime(fecha1, "%Y-%m-%d").date()
        date2 = datetime.datetime.strptime(fecha2, "%Y-%m-%d").date()

        resultado = self.filter(
            titulo__icontains=kword,
            fecha__range=(date1, date2)
        )
        return resultado

    def listar_libros_categoria(self, categoria):
        return self.filter(
            categoria__id=categoria
        ).order_by('titulo')

    def add_autor_libro(self,libro_id,autor):

        libro = self.get(id=libro_id)
        libro.autores.add(autor)
        #   from applications.libro.models import *
        #   Libro.objects.add_autor_libro('2','4')
        return libro

    def libros_num_prestamos(self):
        resultado= self.aggregate(
            num_prestamos=Count('libro_prestamo')
        )
        #   from applications.libro.models import *
        #   Libro.objects.libros_num_prestamos()
        return resultado

class CategoriaManager(models.Manager):

    def categoria_por_autor(self, autor):

        return self.filter(
            categoria_libro__autores__id=autor
        ).distinct()

    def listar_categoria_libros(self):
        resultado= self.annotate(
            num_libros=Count('categoria_libro')
        )
        #   from applications.libro.models import *
        #   Categoria.objects.listar_categoria_libros()
        for r in resultado:
            print('***********')
            print(r,r.num_libros)    
        return resultado
