# from django.db import models

# # Create your models here.

# #--------------------------------Antena-----------------------------------------------
# class AntenaImg(models.Model):
#     nombre_antena = models.CharField(max_length=100, null=True, blank=True, verbose_name='Nombre de la Antena')
#     imagen_instalacion1 = models.ImageField(null=True, blank=True)
#     imagen_instalacion2 = models.ImageField(null=True, blank=True)
#     imagen_instalacion3 = models.ImageField(null=True, blank=True)

#     def __str__(self):
#         return self.nombre

#     class Meta:
#         db_table = 'Antenas'
#         verbose_name = 'Antena'
#         verbose_name_plural = 'Antenas'
#         ordering = ['id']
# #-------------------------------------------------------------------------------------


# #--------------------------------Antena-----------------------------------------------
# class Antena(models.Model):
#     nombre = models.CharField(max_length=100, null=True, blank=True, verbose_name='Nombre de la Antena')

#     def __str__(self):
#         return self.nombre

#     class Meta:
#         db_table = 'Antenas'
#         verbose_name = 'Antena'
#         verbose_name_plural = 'Antenas'
#         ordering = ['id']
# #-------------------------------------------------------------------------------------


# #--------------------------------Municipio-----------------------------------------------
# class Municipio(models.Model):
#     nombre = models.CharField(
#         max_length=100, null=False, verbose_name='Nombre del Municipio')

#     def __str__(self):
#         return self.nombre

#     class Meta:
#         db_table = 'municipio'
#         verbose_name = 'Municipio'
#         verbose_name_plural = 'Municipios'
#         ordering = ['id']
# #-------------------------------------------------------------------------------------


# #--------------------------------Radios-----------------------------------------------
# class Radios(models.Model):
#     ip1 = models.CharField(max_length=15, null=False,unique=True, verbose_name='Ip 1 del Radio')
#     ip2 = models.CharField(max_length=15, null=False,unique=True, verbose_name='Ip 2 del Radio')
#     nombre = models.CharField(max_length=100, null=True, blank=True, verbose_name='Nombre')
#     id_municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE, null=True, blank=True, related_name='Municipios')
#     id_antena = models.ForeignKey(Antena, on_delete=models.CASCADE, null=True, blank=True, related_name='Antenas')
    
#     def __str__(self):
#         return self.nombre

#     @property
#     def imagenUrl1(self):
#         try:
#             url = self.imagen_instalacion1.url
#         except:
#             url = ''

#         return url

#     @property
#     def imagenUrl2(self):
#         try:
#             url = self.imagen_instalacion2.url
#         except:
#             url = ''

#         return url

#     @property
#     def imagenUrl3(self):
#         try:
#             url = self.imagen_instalacion3.url
#         except:
#             url = ''

#         return url

#     class Meta:
#         db_table = 'Radios'
#         verbose_name = 'Radio'
#         verbose_name_plural = 'Radios'
#         ordering = ['id']
# #-------------------------------------------------------------------------------------