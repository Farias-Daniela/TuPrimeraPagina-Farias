from django.urls import path
from . import views

urlpatterns = [
    path('', views.bienvenida, name='bienvenida'),  # Página de bienvenida
    path('agregar/', views.agregar_producto, name='agregar_producto'),
    path('buscar/', views.buscar_producto, name='buscar_producto'),
]
