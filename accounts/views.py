from django.shortcuts import render, get_object_or_404
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Perfil
from django.views.generic import UpdateView
from .forms import EditarPerfilForm



class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'

    def get_success_url(self):
        return reverse_lazy('inicio')

class CustomLogoutView(LogoutView):
    template_name = 'accounts/logout.html'
    next_page = reverse_lazy('inicio')


class RegistroView(CreateView):
    template_name = 'accounts/registro.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('inicio')

@login_required
def perfil_usuario(request):
    perfil, _ = Perfil.objects.get_or_create(user=request.user)  # Si no existe, lo crea automáticamente
    return render(request, 'accounts/perfil.html', {'perfil': perfil})



class EditarPerfilView(UpdateView):
    model = Perfil
    form_class = EditarPerfilForm
    template_name = 'accounts/editar_perfil.html'
    success_url = reverse_lazy('perfil_usuario')

    def get_initial(self):
        initial = super().get_initial()
        initial['first_name'] = self.request.user.first_name
        initial['last_name'] = self.request.user.last_name
        initial['email'] = self.request.user.email
        return initial
