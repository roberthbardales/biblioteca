from atexit import register
from django.contrib import admin

# Register your models here.
from .models import Categoria
from .models import Libro

admin.site.register(Categoria)
admin.site.register(Libro)