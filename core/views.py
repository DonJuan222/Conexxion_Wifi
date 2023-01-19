#renderiza las vistas al usuario
from django.shortcuts import render
# para redirigir a otras paginas
from django.http import HttpResponseRedirect, HttpResponse,FileResponse
#el formulario de login
from .forms import *
# clase para crear vistas basadas en sub-clases
from django.views import View
#autentificacion de usuario e inicio de sesion
from django.contrib.auth import authenticate, login, logout
#verifica si el usuario esta logeado
from django.contrib.auth.mixins import LoginRequiredMixin

#modelos
from .models import *

#Mensajes de formulario
from django.contrib import messages
#Ejecuta un comando en la terminal externa
from django.core.management import call_command
#procesa archivos en .json
from django.core import serializers

# Create your views here.

#Interfaz de inicio de sesion----------------------------------------------------#
class Login(View):
    #Si el usuario ya envio el formulario por metodo post
    def post(self,request):
        # Crea una instancia del formulario y la llena con los datos:
        form = LoginFormulario(request.POST)
        # Revisa si es valido:
        if form.is_valid():
            # Procesa y asigna los datos con form.cleaned_data como se requiere
            usuario = form.cleaned_data['username']
            clave = form.cleaned_data['password']
            # Se verifica que el usuario y su clave existan
            logeado = authenticate(request, username=usuario, password=clave)
            if logeado is not None:
                login(request,logeado)
                #Si el login es correcto lo redirige al panel del sistema:
                return HttpResponseRedirect('/panel')
            else:
                #De lo contrario lanzara el mismo formulario
                return render(request, '/login.html', {'form': form})

    # Si se llega por GET crearemos un formulario en blanco
    def get(self,request):
        if request.user.is_authenticated == True:
            return HttpResponseRedirect('/panel')

        form = LoginFormulario()
        #Envia al usuario el formulario para que lo llene
        return render(request, 'login.html', {'form': form})
#Fin de vista---------------------------------------------------------------------#        


#Panel de inicio y vista principal------------------------------------------------#
class Panel(LoginRequiredMixin, View):
    #De no estar logeado, el usuario sera redirigido a la pagina de Login
    #Las dos variables son la pagina a redirigir y el campo adicional, respectivamente
    login_url = '/login'
    redirect_field_name = None

    def get(self, request):
        from datetime import date
        #Recupera los datos del usuario despues del login
        contexto = {'usuario': request.user.username,
                    'id_usuario':request.user.id,
                   'nombre': request.user.first_name,
                   'apellido': request.user.last_name,
                   'correo': request.user.email,
                   'fecha':  date.today(),
                   'usuariosRegistrados' : Usuario.numeroRegistrados(),
                   'administradores': Usuario.numeroUsuarios('administrador'),
                   'usuarios': Usuario.numeroUsuarios('usuario')
        }
        return render(request, 'panel.html',contexto)
#Fin de vista----------------------------------------------------------------------#

