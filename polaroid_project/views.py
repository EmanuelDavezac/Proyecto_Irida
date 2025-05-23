from .forms import ProductoForm
from django.shortcuts import render, redirect
from productos.models import Producto


def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm()
    return render(request, 'agregar_producto.html', {'form': form})


def inicio(request):
    productos = Producto.objects.all()[:6]  # Muestra los primeros 6 productos
    return render(request, 'productos/inicio.html', {'productos': productos})


