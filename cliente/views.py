from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
# para redirigir a otras paginas
from django.http import HttpResponseRedirect, HttpResponse
#Mensajes de formulario
from django.contrib import messages

#Importando los modelos
from cliente.models import *
from core.models import *

from core.funciones import *

from django.views import View
from cliente.forms import *
# Create your views here.

#formularios dinamicos
from django.forms import formset_factory


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



#Muestra el mismo formulario del cliente pero con los datos a editar----------------------#
class EditarCliente(LoginRequiredMixin, View):
    login_url = '/login'
    redirect_field_name = None

    def post(self,request,p):
        # Crea una instancia del formulario y la llena con los datos:
        cliente = Cliente.objects.get(id=p)
        form = ClienteFormulario(request.POST, instance=cliente)
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


            cliente.ip=ip
            cliente.cedula=cedula
            cliente.nombre=nombre
            cliente.apellido=apellido 
            cliente.telefono_uno=telefono_uno
            cliente.telefonos_dos=telefonos_dos 
            cliente.mensualidad=mensualidad
            cliente.fecha_instalacion=fecha_instalacion
            cliente.direccion=direccion 
            cliente.vereda=vereda
            cliente.tipo_instalacion=tipo_instalacion 
            cliente.status=status
            cliente.descripcion=descripcion
            cliente.id_Pueblo=id_Pueblo
            cliente.id_Estado=id_Estado
            cliente.save()
            form = ClienteFormulario(instance=cliente)

            messages.success(request, 'Actualizado exitosamente el cliente de ID %s.' % p)
            request.session['clienteProcesado'] = 'editado'            
            return HttpResponseRedirect("/editarCliente/%s" % cliente.id)
        else:
            #De lo contrario lanzara el mismo formulario
            return render(request, 'cliente/agregarCliente.html', {'form': form})

    def get(self, request,p): 
        cliente = Cliente.objects.get(id=p)
        form = ClienteFormulario(instance=cliente)
        #Envia al usuario el formulario para que lo llene
        contexto = {'form':form , 'modo':request.session.get('clienteProcesado'),'editar':True} 
        contexto = complementarContexto(contexto,request.user)     
        return render(request, 'cliente/agregarCliente.html', contexto)  
#Fin de vista--------------------------------------------------------------------------------# 



#Elimina usuarios,clientes ----------------------------------------------------------------
class Eliminar(LoginRequiredMixin, View):
    login_url = '/login'
    redirect_field_name = None

    def get(self, request, modo, p):

        if modo == 'cliente':
            cliente = Cliente.objects.get(id=p)
            cliente.delete()
            messages.success(request, 'Cliente de ID %s borrado exitosamente.' % p)
            return HttpResponseRedirect("/listarClientes")            

        elif modo == 'usuario':
            if request.user.is_superuser == False:
                messages.error(request, 'No tienes permisos suficientes para borrar usuarios')  
                return HttpResponseRedirect('/listarUsuarios')

            elif p == 1:
                messages.error(request, 'No puedes eliminar al super-administrador.')
                return HttpResponseRedirect('/listarUsuarios')  

            elif request.user.id == p:
                messages.error(request, 'No puedes eliminar tu propio usuario.')
                return HttpResponseRedirect('/listarUsuarios')                 

            else:
                usuario = Usuario.objects.get(id=p)
                usuario.delete()
                messages.success(request, 'Usuario de ID %s borrado exitosamente.' % p)
                return HttpResponseRedirect("/listarUsuarios")        


#Fin de vista-------------------------------------------------------------------   


#Emite la primera parte de la factura------------------------------#
class EmitirFactura(LoginRequiredMixin, View):
    login_url = '/login'
    redirect_field_name = None

    def post(request):
        if request.method == 'GET':
            return render(request, 'factura/emitirFactura.html',{
            'form': GenerarFactura
        })
        else:
            try:
                form=GenerarFactura(request.POST)
                factura=form.save(commit=False)
                factura.save()
                return redirect('listarFacturas')

            except ValueError:
                return render (request, 'factura/emitirFactura.html',{
                    'form': GenerarFactura,
                    'error': 'Por favor proporciona los datos'
                })
    
#Fin de vista---------------------------------------------------------------------------------#


#Crea una lista de los clientes, 10 por pagina----------------------------------------#
class ListarFacturas(LoginRequiredMixin, View):
    login_url = '/login'
    redirect_field_name = None

    def get(self, request):
        from django.db import models
        #Saca una lista de todas las facturas de la BDD
        facturas = Factura.objects.all()                
        contexto = {'tabla': facturas}
        return render(request, 'factura/listarFacturas.html',contexto) 
#Fin de vista--------------------------------------------------------------------------#
