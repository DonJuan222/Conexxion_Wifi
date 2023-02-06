from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Cliente, Factura, Municipio, Estado

# Register your models here.

class ClienteResource(resources.ModelResource):
    class Meta:
        model=Cliente


class ClienteAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display=('ip','cedula','nombre','apellido','telefono_uno','telefonos_dos','mensualidad','fecha_instalacion','direccion',
                  'tipo_instalacion','status','descripcion','id_Estado')
    resource_class=ClienteResource

admin.site.register(Cliente,ClienteAdmin)
admin.site.register(Factura)
admin.site.register(Municipio)
admin.site.register(Estado)
