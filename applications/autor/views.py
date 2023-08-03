
from django.shortcuts import render

# Create your views here.
from django.views.generic import (
    ListView,
    TemplateView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView
)
from django.urls import reverse_lazy

from .models import Autor


class PaginaInicio(TemplateView):
    template_name = "inicio.html"


class BuscarAutor(ListView):
    model:Autor
    template_name = "autor/buscar_autor.html"

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword",'')
        return Autor.objects.buscar_autor2(palabra_clave)


class ListarAutores(ListView):
    # context_object_name='lista_autores'
    # template_name='autor/lista.html'
    # def get_queryset(self):
    #     return  Autor.objects.all()
    template_name ="autor/lista.html"
    # model = Autor
    paginate_by = 4
    ordering='id'
    context_object_name = 'autores'

    def get_queryset(self):

        palabra_clave = self.request.GET.get("kword", '')
        lista = Autor.objects.filter(
            nombre__icontains=palabra_clave
        ).order_by('id')
        return lista

class ListarAutores2(ListView):

    context_object_name='lista_autores2'
    template_name='autor/lista2.html'

    def get_queryset(self):
        palabra_clave=self.request.GET.get('kword','')
        return  Autor.objects.buscar_autor(palabra_clave)

class AutorDetailView(DetailView):
    model = Autor
    template_name = "autor/detalle.html"

    def get_context_data(self, **kwargs):
        context = super(AutorDetailView, self).get_context_data(**kwargs)
        #toot un proceso
        context['ejemplo'] = 'contexto ejemplo'
        return context


class AutorCreateView(CreateView):
    model = Autor
    template_name = "autor/agregar.html"

    fields=[
        'nombre',
        'apellidos',
        'nacionalidad',
        'edad',
        'seudonimo',
    ]

    success_url=reverse_lazy('autor_app:listar-autores')

class AutorUpdateView(UpdateView):
    template_name = "autor/modificar.html"
    model = Autor
    fields =('__all__')
    success_url=reverse_lazy('autor_app:listar-autores')

class AutorDeleteView(DeleteView):
    model = Autor
    template_name = "autor/eliminar.html"
    success_url=reverse_lazy('autor_app:listar-autores')


