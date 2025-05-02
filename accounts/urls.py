from django.urls import path
from .views import CustomLoginView, CustomLogoutView, RegistroView, perfil_usuario, EditarPerfilView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('registro/', RegistroView.as_view(), name='registro'),
    path('perfil/', perfil_usuario, name='perfil_usuario'),
    path('perfil/editar/<int:pk>/', EditarPerfilView.as_view(), name='editar_perfil'),

]