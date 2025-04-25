from django.shortcuts import render
from .models import Producto


def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos/lista_productos.html', {'productos': productos})

def inicio(request):
    return render(request, 'productos/inicio.html')

