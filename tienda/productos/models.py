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
