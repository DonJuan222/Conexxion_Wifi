from django.urls import path
from . import views

urlpatterns = [

    path('listarClientes', views.ListarClientes.as_view(), name='listarClientes'),
    path('agregarCliente', views.AgregarCliente.as_view(), name='agregarCliente'),
    # path('importarClientes', views.ImportarClientes.as_view(), name='importarClientes'),
    # path('exportarClientes', views.ExportarClientes.as_view(), name='exportarClientes'),
    path('editarCliente/<int:p>', views.EditarCliente.as_view(), name='editarCliente'),
    path('eliminar/<str:modo>/<int:p>', views.Eliminar.as_view(), name='eliminar'),
        
    path('emitirFactura/<int:id>', views.EmitirFactura.as_view(), name='emitirFactura'),
    path('listarFacturas',views.ListarFacturas.as_view(), name='listarFacturas'),
    # path('verFactura/<int:p>',views.VerFactura.as_view(), name='verFactura'),
    # path('generarFactura/<int:p>',views.GenerarFactura.as_view(), name='generarFactura'),
    # path('generarFacturaPDF/<int:p>',views.GenerarFacturaPDF.as_view(), name='generarFacturaPDF'),

]

