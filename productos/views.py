from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Categoria, Cliente
from .forms import ProductoForm, CategoriaForm, ClienteForm, BuscarProductoForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator




def inicio(request):
    productos = Producto.objects.all() 
    return render(request, 'productos/inicio.html', {'productos': productos})

def lista_productos(request):
    query = request.GET.get("q")
    productos = Producto.objects.all()

    if query:
        productos = productos.filter(nombre__icontains=query)
    return render(request, "productos/lista_productos.html", {"productos": productos, "query": query})

def agregar_item(request, model_class, form_class, template_name, redirect_url):
    if request.method == 'POST':
        form = form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(redirect_url)
    else:
        form = form_class()
    return render(request, template_name, {'form': form})

# Vista para agregar productos (solo admins)

@method_decorator(staff_member_required, name='dispatch')
class ProductoCreateView(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'productos/formulario_producto.html'
    success_url = reverse_lazy('lista_productos')

def agregar_categoria(request):
    return agregar_item(request, Categoria, CategoriaForm, 'productos/formulario_categoria.html', 'inicio')

def agregar_cliente(request):
    return agregar_item(request, Cliente, ClienteForm, 'productos/formulario_cliente.html', 'inicio')

def buscar_producto(request):
    if request.method == 'GET':
        form = BuscarProductoForm(request.GET)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            productos = Producto.objects.filter(nombre__icontains=nombre)
            return render(request, 'productos/resultados_busqueda.html', {'productos': productos, 'form': form})
    else:
        form = BuscarProductoForm()
    return render(request, 'productos/buscar_producto.html', {'form': form})

# Vista para editar productos (solo admins)

@method_decorator(staff_member_required, name='dispatch')
class ProductoUpdateView(UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'productos/formulario_producto.html'
    success_url = reverse_lazy('lista_productos')

# Vista para eliminar productos (solo admins)

@method_decorator(staff_member_required, name='dispatch')
class ProductoDeleteView(DeleteView):
    model = Producto
    template_name = 'productos/eliminar_producto.html'
    success_url = reverse_lazy('lista_productos')


from django.shortcuts import render, get_object_or_404
from .models import Producto

@login_required
def detalle_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, 'productos/detalle_producto.html', {'producto': producto})

def about(request):
    foto_url = "/static/img/perfil.jpg"
    return render(request, "productos/about.html", {"foto_url": foto_url})

def contacto(request):
    return render(request, "productos/contacto.html")

class ProductoListView(LoginRequiredMixin, ListView):
    model = Producto
    template_name = "productos/lista_productos.html"
    context_object_name = "productos"
