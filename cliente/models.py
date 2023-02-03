from django.db import models

# Create your models here.

#------------------------------------------Estado--------------------------------------
class Estado(models.Model):
    tipo=models.CharField(max_length=100, null=False, verbose_name='tipo')

    def __str__(self):
        return self.tipo

    class Meta:
        db_table='estado'
        verbose_name='Estado'
        verbose_name_plural='Estados'
        ordering=['id']
#-----------------------------------------------------------------------------------------        


#------------------------------------------Municipio--------------------------------------
class Municipio(models.Model):
    nombreMunicipio=models.CharField(max_length=100, null=False, verbose_name='Nombre del Municipio')

    def __str__(self):
        return self.nombreMunicipio

    class Meta:
        db_table='municipio'
        verbose_name='Municipio'
        verbose_name_plural='Municipios'
        ordering=['id']
#-----------------------------------------------------------------------------------------        


#------------------------------------------Cliente--------------------------------------
class Cliente(models.Model):
    
    ESTADO_CHOICES = (
        ('arriba', 'Activo'),
        ('abajo', 'Sin servicio'),
    )
    TIPOS_CHOICES = (
        ('------','------'),
        ('Fibra Optica','Fibra'),
        ('Radio Enlace','Radio'),
    )

    ip= models.CharField(max_length=15,null=False, unique=True, verbose_name='Ip del Cliente' ) 
    cedula=models.CharField(max_length=12, null=False, unique=True, verbose_name='Cedula del Cliente')
    nombre=models.CharField(max_length=100, null=False, verbose_name='Nombre del Cliente')
    apellido=models.CharField(max_length=100, null=False, verbose_name='Apellido del Cliente')
    telefono_uno=models.CharField(max_length=12, null=True,blank=True, verbose_name='Primer Telefono ')
    telefonos_dos=models.CharField(max_length=12, null=True,blank=True, verbose_name='Segundo Telefono')
    mensualidad=models.PositiveIntegerField(null=True,blank=True, verbose_name='Mensualidad')
    fecha_instalacion = models.DateField(null=True,blank=True, verbose_name='Fecha de Instalacion')
    direccion=models.CharField(max_length=100,null=True,blank=True,verbose_name='Direccion')
    tipo_instalacion=models.CharField(max_length=20, choices=TIPOS_CHOICES, null=True,blank=True,  verbose_name='Tipo de Instalacion')
    status=models.CharField(max_length=20, choices=ESTADO_CHOICES, null=True,blank=True,  verbose_name='Estado')
    descripcion=models.TextField( null=True,blank=True, verbose_name='Descripcion')
    id_Municipio=models.ForeignKey(Municipio, on_delete=models.CASCADE,null=True,blank=True, related_name='Municipio')
    id_Estado=models.ForeignKey(Estado, on_delete=models.CASCADE, null=True,blank=True, related_name='Estado')
    
    class Meta:
        db_table='cliente'
        verbose_name='Cliente'
        verbose_name_plural='Clientes'
        ordering=['ip']
    
    def __str__(self):
        return self.nombre + ' ' + self.apellido


    @classmethod
    def numeroRegistrados(self):
        return int(self.objects.all().count() )
    
    @classmethod
    def ipRegistradas(self):
        objetos = self.objects.all().order_by('ip')
        arreglo = []
        for indice,objeto in enumerate(objetos):
            arreglo.append([])
            arreglo[indice].append(objeto.ip)
            nombre_cliente = objeto.nombre + " " + objeto.apellido
            arreglo[indice].append("%s. I.P: %s" % (nombre_cliente,self.formatearIp(objeto.ip)) )
        return arreglo   

    @staticmethod
    def formatearIp(ip):
        return str.format((ip), '.d') 
      
#-----------------------------------------------------------------------------------------        


#-------------------------------------FACTURA---------------------------------------------
class Factura(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=100, null=True,blank=True, verbose_name='Descripcion')
    valor_pago =  models.PositiveIntegerField( null=True,blank=True, verbose_name='Valor del Pago')
    fecha_pago = models.DateField(null=True,verbose_name='Fecha de pago')
    fecha_vencimiento = models.DateField(null=True,blank=True,verbose_name='Valido Hasta')
#-----------------------------------------------------------------------------------------
