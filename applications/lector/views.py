from datetime import date

from django.shortcuts import render

# Create your views here.
from django.views.generic.edit import FormView

from .models import Prestamo
from .forms import PrestamoForm

class RegistrarPrestamo(FormView):
    template_name='lector/add_prestamo.html'
    form_class =PrestamoForm
    success_url= '.'
    
    def form_valid(self,form):
        
        # Prestamo.objects.create(
        #     lector=form.cleaned_data['lector'],
        #     libro=form.cleaned_data['libro'],
        #     fecha_prestamo=date.today(),
        #     devuelto=False,
        # )
        prestamo= Prestamo(
            lector=form.cleaned_data['lector'],
            libro=form.cleaned_data['libro'],
            fecha_prestamo=date.today(),
            devuelto=False,

        )

        prestamo.save()

        return super(RegistrarPrestamo,self).form_valid(form)

