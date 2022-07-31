from atexit import register
from django.contrib import admin

# Register your models here.
from .models import Lector
from .models import Prestamo

admin.site.register(Lector)
admin.site.register(Prestamo)