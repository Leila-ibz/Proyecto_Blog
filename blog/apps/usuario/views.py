from django.shortcuts import render
from .forms import RegistroUsuarioForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse

# Create your views here.


class RegistrarUsuario(CreateView):
    template_name = 'registration/registrar.html'
    form_class = RegistroUsuarioForm

    def form_valid(self, form):
        messages.success(self.request, 'REGISTRO EXITOSO. POR FAVOR INICIA SESIÓN.')
        form.save()

        return redirect('usuario:login')
    

class LoginUsuario(LoginView):
    template_name = 'registration/login.html'
    

    def get_success_url(self):
        messages.success(self.request, 'INICIO DE SESIÓN EXITOSO. ¡BIENVENID@!')
        return reverse('posts:articulos') 

class LogoutUsuario(LogoutView):
    # template_name = 'registration/logout.html'

    def get_success_url(self):
        messages.success(self.request, '¡SU CUENTA HA SIDO CERRADA CORRECTAMENTE! ¡HASTA LUEGO!')

        return reverse('usuario:login')