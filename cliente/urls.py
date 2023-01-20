from django.urls import path
from . import views

urlpatterns = [

path('listarClientes', views.ListarClientes.as_view(), name='listarClientes'),
# path('agregarCliente', views.AgregarCliente.as_view(), name='agregarCliente'),
# path('importarClientes', views.ImportarClientes.as_view(), name='importarClientes'),
# path('exportarClientes', views.ExportarClientes.as_view(), name='exportarClientes'),
# path('editarCliente/<int:p>', views.EditarCliente.as_view(), name='editarCliente'),

]

