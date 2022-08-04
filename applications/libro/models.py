from pickletools import optimize
from django.db import models
from django.db.models.signals import post_save

#apps de tercero

from PIL import Image

from applications.autor.models import Autor

from .managers import LibroManager,CategoriaManager
# Create your models here.


class Categoria(models.Model):
    nombre = models.CharField(max_length=30)

    objects=CategoriaManager()

    def __str__(self):
        return str(self.id) + ' - '+ self.nombre


class Libro(models.Model):
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        related_name='categoria_libro'
    )
    autores = models.ManyToManyField(Autor)
    titulo = models.CharField(
        max_length=50
    )
    fecha = models.DateField('Fecha de Lanzamiento')
    portada = models.ImageField(upload_to='portada')
    visitas = models.PositiveIntegerField()
    stok=models.PositiveIntegerField(default=0)

    objects = LibroManager()

    class Meta:
        verbose_name='Libro'
        verbose_name_plural='Libros'
        ordering=['titulo','fecha']


    def __str__(self):
        return str(self.id) + '-'+ self.titulo

    def listar_libros_categoria(self,categoria):

        return self.filter(
            categoria__id=categoria
        ).order_by('titulo')

def optimize_image(sender,instance,**kwargs):
    print("========")
    print(instance)
    if instance.portada:
        portada= Image.open(instance.portada.path)
        portada.save(instance.portada.path,quality=20,optimize=True)

post_save.connect(optimize_image,sender=Libro)
