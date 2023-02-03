from django.contrib import admin

from .models import Cliente, Factura, Municipio, Estado

# Register your models here.

admin.site.register(Cliente)
admin.site.register(Factura)
admin.site.register(Municipio)
admin.site.register(Estado)
