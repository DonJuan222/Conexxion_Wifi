from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from core.funciones import *
from cliente.models import *
from django.views import View
# Create your views here.


#Crea una lista de los clientes, 10 por pagina----------------------------------------#
class ListarClientes(LoginRequiredMixin, View):
    login_url = '/login'
    redirect_field_name = None

    def get(self, request):
        from django.db import models
        #Saca una lista de todos los clientes de la BDD
        clientes = Cliente.objects.all()                
        contexto = {'tabla': clientes}
        contexto = complementarContexto(contexto,request.user)         

        return render(request, 'cliente/listarClientes.html',contexto) 
#Fin de vista--------------------------------------------------------------------------#
