from django.contrib import admin

# Register your models here.
from .models import Persona,Empleados


admin.site.register(Persona)
admin.site.register(Empleados)