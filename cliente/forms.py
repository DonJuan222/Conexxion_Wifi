from django import forms
from .models import Cliente,Factura


class ClienteFormulario(forms.ModelForm):
    tipoInsta =  [ ('Fibra Optica','Fibra'),('Radio Enlace','Radio')]

    tipo_instalacion = forms.CharField(
        label="Tipo de Instalacion",
        max_length=20,
        widget=forms.Select(choices=tipoInsta,attrs={'placeholder': 'Tipo de Instalacion',
        'id':'tipo_instalacion','class':'form-control'}
        )
        )

    class Meta:
        model = Cliente
        fields = ['ip','cedula','nombre','apellido','telefono_uno','telefonos_dos','mensualidad','fecha_instalacion','direccion','vereda',
                  'tipo_instalacion','status','descripcion','id_Pueblo','id_Estado']
        labels = {
        'ip': 'Ip del cliente',
        'cedula': 'Cedula del cliente',
        'nombre': 'Nombre del cliente',
        'apellido': 'Apellido del cliente',
        'telefono_uno': 'Telefono del cliente',
        'telefonos_dos': 'Segundo telefono (Opcional)',
        'mensualidad': 'Mensualidad cliente',
        'fecha_instalacion': 'Fecha de instalacion del cliente',
        'direccion': 'Dirección',
        'vereda': 'Vereda',
        'tipo_instalacion': 'Tipo de Instalacion',
        'status': 'Estado del Cliente',
        'descripcion': 'Detalles',
        'id_Pueblo': 'Pueblo',
        'id_Estado': 'Estado',
        }
        widgets = {
    
        'ip': forms.TextInput(attrs={'placeholder': 'Inserte la Ip del Cliente','id':'ip','class':'form-control'} ),
        'cedula': forms.TextInput(attrs={'placeholder': 'Inserte la cedula de identidad del cliente','id':'cedula','class':'form-control'} ),
        'nombre': forms.TextInput(attrs={'placeholder': 'Inserte el nombre del cliente','id':'nombre','class':'form-control'}),
        'apellido': forms.TextInput(attrs={'class':'form-control','id':'apellido','placeholder':'El apellido del cliente'}),
        'telefono_uno': forms.TextInput(attrs={'class':'form-control','id':'telefono_uno','placeholder':'Telefono del cliente'}), 
        'telefonos_dos': forms.TextInput(attrs={'class':'form-control','id':'telefonos_dos','placeholder':'Segundo telefono del cliente'}),                                                                       
        'mensualidad': forms.TextInput(attrs={'class':'form-control','id':'mensualidad','placeholder':'Mensualidad del cliente'}),                                                                                                     
        'fecha_instalacion':forms.DateInput(format=('%d-%m-%Y'),attrs={'id':'fecha_instalacion','class':'form-control','type':'date'} ),
        'direccion': forms.TextInput(attrs={'class':'form-control','id':'direccion','placeholder':'Direccion del cliente'}),                                                                       
        'vereda': forms.TextInput(attrs={'class':'form-control','id':'vereda','placeholder':'Vereda'}),                                                                       
        'tipo_instalacion': forms.TextInput(attrs={'class':'form-control','id':'tipo_instalacion','placeholder':'Tipo de instalacion'}),                                                                       
        'status': forms.TextInput(attrs={'class':'form-control','id':'status','placeholder':'Status'}),                                                                           
        'descripcion': forms.TextInput(attrs={'class':'form-control','id':'descripcion','placeholder':'Descripcion'}), 
        'id_Pueblo': forms.TextInput(attrs={'class':'form-control','id':'id_Pueblo','placeholder':'Pueblo'}),                                                                           
        'id_Estado': forms.TextInput(attrs={'class':'form-control','id':'id_Estado','placeholder':'Estado'}),                                                                                                                    

        }

        
class GenerarFactura(forms.ModelForm):
    
    class Meta:
        model = Factura
        fields = ['descripcion','valor_pago','fecha_pago','fecha_vencimiento']
        labels = {

        'descripcion': 'Detalle del pago',
        'valor_pago': 'Valor del Pago',
        'fecha_pago': 'Fecha del pago',
        'fecha_vencimiento': 'Pago valido hasta',
        
        }
        widgets = {
    
        'descripcion': forms.TextInput(attrs={'placeholder': 'Detalles del pago','id':'descripcion','class':'form-control'} ),
        'valor_pago': forms.TextInput(attrs={'placeholder': 'Valor de pago','id':'valor_pago','class':'form-control'}),
        'fecha_pago': forms.DateInput(format=('%d-%m-%Y'),attrs={'id':'fecha_pago','class':'form-control','type':'date'}),
        'fecha_vencimiento':forms.DateInput(format=('%d-%m-%Y'),attrs={'id':'fecha_instalacion','class':'form-control','type':'date'} ),
       
        }

# class GenerarFactura(forms.Form):
#     def __init__(self, *args, **kwargs):
#        elecciones = kwargs.pop('ip')
#        super(GenerarFactura, self).__init__(*args, **kwargs)

#        if(elecciones):
#             self.fields["cliente"] = forms.CharField(label="Cliente a facturar",max_length=50,
#             widget=forms.Select(choices=elecciones,
#             attrs={'placeholder': 'La cedula del cliente a facturar',
#             'id':'cliente','class':'form-control'}))
