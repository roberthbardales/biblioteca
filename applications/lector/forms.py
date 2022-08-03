from dataclasses import fields
from django import forms

from .models import Prestamo

class PrestamoForm(forms.ModelForm):
    class Meta:
        model=Prestamo
        fields= (
            'lector',
            'libro',
        )