from django.contrib import admin
from django.urls import path


from .import views

app_name = "autor_app"
urlpatterns = [

    path(
        '',
        views.PaginaInicio.as_view(),
        name="inicio"
    ),
    path(
        'listar-autores/',
        views.ListarAutores.as_view(),
        name="listar-autores"
    ),
    path(
        'autores',
        views.ListarAutores2.as_view(),
        name="autores"
    ),
    path(
        'detalle-autores/<pk>',
        views.AutorDetailView.as_view(),
        name="detalle-autores"
    ),
    path(
        'buscar-autores/',
        views.BuscarAutor.as_view(),
        name="buscar-autores"
    ),
    path(
        'agregar-autores/',
        views.AutorCreateView.as_view(),
        name="agregar-autores"
    ),
    path(
        'modificar-autores/<pk>',
        views.AutorUpdateView.as_view(),
        name="modificar-autores"
    ),
    path(
        'eliminar-autores/<pk>',
        views.AutorDeleteView.as_view(),
        name="eliminar-autores"
    ),
]
