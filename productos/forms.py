from django import forms
from .models import Producto, Categoria, Cliente

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

class BuscarProductoForm(forms.Form):
    nombre = forms.CharField(label='Buscar producto por nombre', max_length=100)
