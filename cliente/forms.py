from django import forms
from .models import Cliente


class ClienteFormulario(forms.ModelForm):
    tipoInsta =  [ ('Fibra Optica','Fibra'),('Radio Enlace','Radio')]
    tipo_instalacion = forms.ChoiceField(choices=tipoInsta)

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
