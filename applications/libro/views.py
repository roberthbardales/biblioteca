
from django.shortcuts import render

from django.views.generic import ListView,DetailView,UpdateView,DeleteView,CreateView

from .models import Libro

from django.urls import reverse_lazy
class ListLibros(ListView):
    context_object_name = 'lista_libros'
    template_name = "libro/lista.html"

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword",'')

        #fecha1
        f1 = self.request.GET.get("fecha1",'')
        #fecha2
        f2 = self.request.GET.get("fecha2",'')

        if f1 and f2:
            return Libro.objects.listar_libros3(palabra_clave,f1,f2)
        else:
            return Libro.objects.listar_libros(palabra_clave)

class ListLibrosZero(ListView):

    template_name ="libro/lista.html"
    # model = Libro
    paginate_by = 4
    ordering='id'
    context_object_name = 'autores'

    def get_queryset(self):

        palabra_clave = self.request.GET.get("kword", '')
        lista = Libro.objects.filter(
            titulo__icontains=palabra_clave
        ).order_by('id')
        return lista

class LibroDetailView(DetailView):
    model = Libro
    template_name = "libro/detalle.html"

    def get_context_data(self, **kwargs):
        context = super(LibroDetailView, self).get_context_data(**kwargs)
        #toot un proceso
        context['ejemplo'] = 'contexto ejemplo'
        return context

class LibroUpdateView(UpdateView):
    template_name = "libro/modificar.html"
    model = Libro
    fields =('__all__')
    success_url=reverse_lazy('libro_app:listar-libros')

class AutorDeleteView(DeleteView):
    model = Libro
    template_name = "libro/eliminar.html"

    success_url=reverse_lazy('libro_app:listar-libros')

class LibroCreateView(CreateView):
    model = Libro
    template_name = "libro/agregar.html"

    fields=[
        'categoria',
        'autores',
        'titulo',
        'fecha',
        'visitas',
        'stok',
        'portada',
    ]

    success_url=reverse_lazy('libro_app:listar-libros')


class ListLibrosTrg(ListView):
    context_object_name = 'lista_libros'
    template_name = "libro/lista.html"

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword",'')

        return Libro.objects.listar_libros_trg(palabra_clave)

class ListLibros2(ListView):
    context_object_name = 'lista_libros'
    template_name = 'libro/lista2.html'

    def get_queryset(self):
        return Libro.objects.listar_libros_categoria('2')


# class LibroDetailView(DetailView):
#     model = Libro
#     template_name = "libro/detalle.html"
