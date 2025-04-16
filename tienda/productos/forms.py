from django import forms
from .models import Categoria, Marca, Producto

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']

class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = ['nombre']

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'categoria', 'marca']
