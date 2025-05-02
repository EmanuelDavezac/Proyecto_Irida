from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import detalle_producto, about, contacto, ProductoCreateView, ProductoUpdateView, ProductoDeleteView





urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('productos/', views.lista_productos, name='lista_productos'),
    path('producto/agregar/', ProductoCreateView.as_view(), name='agregar_producto'),
    path('producto/editar/<int:pk>/', ProductoUpdateView.as_view(), name='editar_producto'),
    path('producto/eliminar/<int:pk>/', ProductoDeleteView.as_view(), name='borrar_producto'),
    path('producto/<int:pk>/', detalle_producto, name='detalle_producto'),
    path('about/', about, name='about'),
    path('contacto/', contacto, name='contacto'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)