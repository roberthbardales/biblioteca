from enum import auto
from html.entities import html5
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView


from .models import Autor


class ListAutores(ListView):
    model = Autor
    context_object_name = 'lista_autores'
    template_name = "autor/lista.html"
    
    def get_queryset(self):
        return Autor.objects.all()
        def get_queryset(self):
            queryset = super(CLASS_NAME, self).get_queryset()
            queryset = queryset # TODO
            return queryset