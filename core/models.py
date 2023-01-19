from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


#--------------------------------USUARIO------------------------------------------------
class Usuario(AbstractUser):

    username = models.CharField(max_length=80, unique=True)
    password = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=60)
    nivel = models.IntegerField(null=True) 

    @classmethod
    def numeroRegistrados(self):
        return int(self.objects.all().count() )   

    @classmethod
    def numeroUsuarios(self,tipo):
        if tipo == 'administrador':
            return int(self.objects.filter(is_superuser = True).count() )
        elif tipo == 'usuario':
            return int(self.objects.filter(is_superuser = False).count() )


#---------------------------------------------------------------------------------------
