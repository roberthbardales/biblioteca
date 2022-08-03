from django.shortcuts import render

# Create your views here.
from django.views.generic.edit import FormView

from .forms import PrestamoForm

class RegistrarPrestamo(FormView):
    template_name='lector/add_prestamo.html'
    form_class =PrestamoForm
    success_url= '.'
    
    def form_valid(self,form):
        
        

        return super(RegistrarPrestamo,self).form_valid(form)

