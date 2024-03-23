from django.contrib import admin
from django.urls import path


from .import views


app_name = "lector_app"

urlpatterns = [
    # lector
    path(
        'listar-lectores/',
        views.ListLectores.as_view(),
        name="listar-lectores"
    ),
    path(
        'detalle-lectores/<pk>/',
        views.LectorDetailView.as_view(),
        name="detalle-lectores"
    ),
    path(
        'modificar-lectores/<pk>',
        views.LectorUpdateView.as_view(),
        name="modificar-lectores"
    ),
    path(
        'eliminar-lectores/<pk>',
        views.LectorDeleteView.as_view(),
        name="eliminar-lectores"
    ),
    path(
        'agregar-lectores/',
        views.LectorCreateView.as_view(),
        name="agregar-lectores"
    ),
    # Prestamo
    path(
        'prestamo/add/',
        views.AddPrestamo.as_view(),
        name="prestamo-add"
    ),
    path(
        'prestamo/multiple-add/',
        views.AddMultiplePrestamo.as_view(),
        name="prestamo-add_multiple"
    ),
]
