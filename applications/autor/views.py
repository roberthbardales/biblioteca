from enum import auto
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
        
    