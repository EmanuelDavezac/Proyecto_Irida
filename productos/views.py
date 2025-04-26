from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ProductoForm, CategoriaForm, ClienteForm, BuscarProductoForm

def inicio(request):
    return render(request, 'productos/inicio.html')

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos/lista_productos.html', {'productos': productos})


def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProductoForm()
    return render(request, 'formulario_producto.html', {'form': form})

def agregar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CategoriaForm()
    return render(request, 'formulario_categoria.html', {'form': form})

def agregar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ClienteForm()
    return render(request, 'formulario_cliente.html', {'form': form})

def buscar_producto(request):
    if request.method == 'GET':
        form = BuscarProductoForm(request.GET)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            productos = Producto.objects.filter(nombre__icontains=nombre)
            return render(request, 'resultados_busqueda.html', {'productos': productos, 'form': form})
    else:
        form = BuscarProductoForm()
    return render(request, 'buscar_producto.html', {'form': form})

def editar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    form = ProductoForm(request.POST or None, request.FILES or None, instance=producto)
    if form.is_valid():
        form.save()
        return redirect('lista_productos')
    return render(request, 'editar_producto.html', {'form': form})

def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('lista_productos')
    return render(request, 'eliminar_producto.html', {'producto': producto})