from datetime import date

from django.shortcuts import render

from django.http import HttpResponseRedirect

from django.views.generic import ListView,DetailView,UpdateView,DeleteView,CreateView
from django.views.generic.edit import FormView

from .models import Prestamo,Lector
from .forms import PrestamoForm, MultiplePrestamoForm
from django.urls import reverse_lazy


""" Modelo Lector """
class ListLectores(ListView):

    template_name ="lector/lista.html"
    # model = Lector
    paginate_by = 4
    ordering='id'
    context_object_name = 'lectores'

    def get_queryset(self):

        palabra_clave = self.request.GET.get("kword", '')
        lista = Lector.objects.filter(
            nombre__icontains=palabra_clave
        ).order_by('id')
        return lista


class LectorDetailView(DetailView):
    model = Lector
    template_name = "lector/detalle.html"

    def get_context_data(self, **kwargs):
        context = super(LectorDetailView, self).get_context_data(**kwargs)
        #toot un proceso
        context['ejemplo'] = 'contexto ejemplo'
        return context


class LectorUpdateView(UpdateView):
    template_name = "libro/modificar.html"
    model = Lector
    fields =('__all__')
    success_url=reverse_lazy('lector_app:listar-lectores')

class LectorDeleteView(DeleteView):
    model = Lector
    template_name = "lector/eliminar.html"

    success_url=reverse_lazy('lector_app:listar-lectores')

class LectorCreateView(CreateView):
    model = Lector
    template_name = "lector/agregar.html"

    fields = [
        'nombre',
        'apellidos',
        'nacionalidad',
        'edad',
    ]

    success_url=reverse_lazy('lector_app:listar-lectores')

""" Modelo Prestamo """

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

        libro=form.cleaned_data['libro']
        libro.stok=libro.stok-1
        libro.save()

        return super(RegistrarPrestamo,self).form_valid(form)


class AddPrestamo(FormView):
    template_name='lector/add_prestamo.html'
    form_class =PrestamoForm
    success_url= '.'

    def form_valid(self,form):

        obj, created= Prestamo.objects.get_or_create(
            lector=form.cleaned_data['lector'],
            libro=form.cleaned_data['libro'],
            devuelto=False,
            defaults={
            'fecha_prestamo':date.today()
            }

        )

        if created:
            return super(AddPrestamo,self).form_valid(form)
        else:
            return HttpResponseRedirect('/')

class AddMultiplePrestamo(FormView):
    template_name='lector/add_multiple_prestamo.html'
    form_class =MultiplePrestamoForm
    success_url= '.'

    def form_valid(self,form):

        print(form.cleaned_data['lector'])
        print(form.cleaned_data['libros'])

        prestamos= []
        for l in form.cleaned_data['libros']:
            prestamo= Prestamo(
            lector=form.cleaned_data['lector'],
            libro=l,
            fecha_prestamo=date.today(),
            devuelto=False
            )
            prestamos.append(prestamo)

        Prestamo.objects.bulk_create(
            prestamos
        )


        return super(AddMultiplePrestamo,self).form_valid(form)
