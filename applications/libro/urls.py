from django.contrib import admin
from django.urls import path


from .import views

app_name = "libro_app"

urlpatterns = [
    path(
        'listar-libros/',
        views.ListLibrosZero.as_view(),
        name="listar-libros"
    ),
    path(
        'listar_libros2/',
        views.ListLibros2.as_view(),
        name="listar_libros2"
    ),
    path(
        'detalle-libros/<pk>/',
        views.LibroDetailView.as_view(),
        name="detalle-libros"
    ),
        path(
        'modificar-libros/<pk>',
        views.LibroUpdateView.as_view(),
        name="modificar-libros"
    ),
    path(
        'eliminar-libros/<pk>',
        views.AutorDeleteView.as_view(),
        name="eliminar-libros"
    ),
    path(
        'agregar-libros/',
        views.LibroCreateView.as_view(),
        name="agregar-libros"
    ),
    path(
        'libros-trg/',
        views.ListLibrosTrg.as_view(),
        name="libros-trg"
    ),

]
