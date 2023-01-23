from django.urls import path
from . import views

urlpatterns = [

    path('listarClientes', views.ListarClientes.as_view(), name='listarClientes'),
    path('agregarCliente', views.AgregarCliente.as_view(), name='agregarCliente'),
    path('editarCliente/<int:p>', views.EditarCliente.as_view(), name='editarCliente'),
    path('eliminar/<str:modo>/<int:p>', views.Eliminar.as_view(), name='eliminar'),

]
