from django.shortcuts import render, redirect
from .models import Producto
from .forms import ProductoForm
from django.db.models import Q


# Vista de Bienvenida
def bienvenida(request):
    return render(request, 'productos/bienvenida.html')

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

# Create your views here.
