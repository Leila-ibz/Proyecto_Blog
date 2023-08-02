from django import forms
from .models import Articulo   

class ArticuloForm(forms.ModelForm):
    class Meta: 
        model = Articulo
        fields = ['titulo', 'resumen', 'contenido', 'imagen', 'categoria']