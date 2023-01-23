from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
# para redirigir a otras paginas
from django.http import HttpResponseRedirect, HttpResponse
#Mensajes de formulario
from django.contrib import messages

from core.funciones import *
from cliente.models import *
from django.views import View
from cliente.forms import *
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


#Crea y procesa un formulario para agregar a un cliente---------------------------------#
class AgregarCliente(LoginRequiredMixin, View):
    login_url = '/login'
    redirect_field_name = None

    def post(self, request):
        # Crea una instancia del formulario y la llena con los datos:
        form = ClienteFormulario(request.POST)
        # Revisa si es valido:

        if form.is_valid():
            # Procesa y asigna los datos con form.cleaned_data como se requiere
            ip = form.cleaned_data['ip']
            cedula = form.cleaned_data['cedula']
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            telefono_uno = form.cleaned_data['telefono_uno']
            telefonos_dos = form.cleaned_data['telefonos_dos']
            mensualidad = form.cleaned_data['mensualidad']
            fecha_instalacion = form.cleaned_data['fecha_instalacion']
            direccion = form.cleaned_data['direccion']
            vereda = form.cleaned_data['vereda']
            tipo_instalacion = form.cleaned_data['tipo_instalacion']
            status = form.cleaned_data['status']
            descripcion = form.cleaned_data['descripcion']
            id_Pueblo = form.cleaned_data['id_Pueblo']
            id_Estado = form.cleaned_data['id_Estado']

            cliente = Cliente(ip=ip,cedula=cedula,nombre=nombre,apellido=apellido,telefono_uno=telefono_uno,
                telefonos_dos=telefonos_dos, mensualidad=mensualidad,fecha_instalacion=fecha_instalacion,
                direccion=direccion,vereda=vereda,tipo_instalacion=tipo_instalacion,
                status=status,descripcion=descripcion,id_Pueblo=id_Pueblo,id_Estado=id_Estado)
            cliente.save()
            form = ClienteFormulario()

            messages.success(request, 'Ingresado exitosamente bajo la ID %s.' % cliente.id)
            request.session['clienteProcesado'] = 'agregado'
            return HttpResponseRedirect("/agregarCliente")
        else:
            #De lo contrario lanzara el mismo formulario
           
            return render(request, 'cliente/agregarCliente.html', {'form': form})        

    def get(self,request):
      
        form = ClienteFormulario()
        #Envia al usuario el formulario para que lo llene
        contexto = {'form':form , 'modo':request.session.get('clienteProcesado')} 
        contexto = complementarContexto(contexto,request.user)         
        return render(request, 'cliente/agregarCliente.html', contexto)
#Fin de vista-----------------------------------------------------------------------------#        
