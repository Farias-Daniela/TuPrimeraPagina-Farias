# TuPrimeraPagina-farias
#crear entorno virtual - en terminal poner: python -m venv venv (el ultimo venv es el nombre del entorno)

#activar el entorno virtual - en terminal: .\venv\Scripts\activate

#instalar request - en terminal: pip install requests

#Configurar el intérprete de Python en VS Code: Asegúrate de que Visual Studio Code use el intérprete de Python dentro del entorno virtual. Haz lo siguiente:

Abre el Command Palette (Ctrl + Shift + P o Cmd + Shift + P).

Escribe Python: Select Interpreter y selecciona el intérprete de tu entorno virtual (debería aparecer algo como .venv/bin/python o similar).

Istalar django - en terminal poner: pip install django 

crear el proyecto Django - en terminal: django-admin startproject tienda (tienda es el nombre de mi proyecto)
en terminal pongo "cd tienda" que ahi me estoy parando 

crear una aplicacion dentro de mi proyecto llamada producto. en terminal: python manage.py startapp productos

Configurar la Base de Datos y el Modelo - en el archivo tienda/settings.py, agrega la aplicación productos a la lista INSTALLED_APPS:
INSTALLED_APPS = [
    ...
    'productos',
]

Ahora vamos a crear los modelos en el archivo productos/models.py. Imaginemos que quieres una tienda que tiene Productos, Categorías y Marcas.

from django.db import models

# Modelo para Categoría
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

# Modelo para Marca
class Marca(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

# Modelo para Producto
class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


Después de definir tus modelos, ejecuta las migraciones:
python manage.py makemigrations
python manage.py migrate

Ahora, crea los formularios para agregar productos, categorías y marcas en productos/forms.py.from django import forms
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

Ahora, vamos a crear las vistas para insertar datos y para buscar productos en productos/views.py.

from django.shortcuts import render, redirect
from .models import Producto
from .forms import ProductoForm, CategoriaForm, MarcaForm
from django.db.models import Q

# Vista para el formulario de Producto
def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agregar_producto')
    else:
        form = ProductoForm()
    return render(request, 'productos/agregar_producto.html', {'form': form})

# Vista para buscar productos
def buscar_producto(request):
    productos = Producto.objects.all()

    if 'q' in request.GET:
        query = request.GET['q']
        productos = productos.filter(Q(nombre__icontains=query) | Q(descripcion__icontains=query))
    
    return render(request, 'productos/buscar_producto.html', {'productos': productos})


Crear Plantillas con Herencia- Ahora creamos las plantillas. Primero, crea una carpeta llamada templates dentro de la carpeta de tu aplicación productos

Base (herencia):
Crea un archivo base en productos/templates/base.html:
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mi Tienda</title>
</head>
<body>
    <header>
        <h1>Bienvenido a la tienda</h1>
        <nav>
            <a href="{% url 'agregar_producto' %}">Agregar Producto</a> |
            <a href="{% url 'buscar_producto' %}">Buscar Producto</a>
        </nav>
    </header>
    
    <main>
        {% block content %}
        {% endblock %}
    </main>
    
    <footer>
        <p>&copy; 2025 Mi Tienda</p>
    </footer>
</body>
</html>




Crea la plantilla productos/templates/productos/agregar_producto.html para agregar productos:{% extends 'base.html' %}

{% block content %}
<h2>Agregar Producto</h2>
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Guardar</button>
</form>
{% endblock %}





Crea la plantilla productos/templates/productos/buscar_producto.html para buscar productos:



{% extends 'base.html' %}

{% block content %}
<h2>Buscar Producto</h2>
<form method="get">
    <input type="text" name="q" placeholder="Buscar..." value="{{ request.GET.q }}">
    <button type="submit">Buscar</button>
</form>

<h3>Resultados:</h3>
<ul>
    {% for producto in productos %}
        <li>{{ producto.nombre }} - {{ producto.precio }} EUR</li>
    {% empty %}
        <li>No se encontraron productos.</li>
    {% endfor %}
</ul>
{% endblock %}




Configura las URLs para las vistas en productos/urls.py:

from django.urls import path
from . import views

urlpatterns = [
    path('agregar/', views.agregar_producto, name='agregar_producto'),
    path('buscar/', views.buscar_producto, name='buscar_producto'),
]



Y en tienda/urls.py, incluye las URLs de la aplicación productos:
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('productos/', include('productos.urls')),
]



Finalmente, ejecuta el servidor para ver tu tienda en acción:

python manage.py runserver

Subir el Proyecto a GitHubgit init
git add .
git commit -m "Primer commit"

