from django.db import models


class Fisica(models.Model):
    
    """ Tabla para personas fisicas """

    nombre = models.CharField(max_length=80)
    apellido = models.CharField(max_length=250)
    dni = models.IntegerField()
    cuit = models.IntegerField(unique=True,blank=False, null=False)
   

    class Meta:
        verbose_name = "Fisica"
        verbose_name_plural = "Fisicas"

    def __str__(self):
        return self.nombre


class Juridica(models.Model):

    """ Tabla para personas juridicas """

    razon = models.CharField(max_length=100)
    año = models.IntegerField()
    cuit = models.IntegerField(unique=True,blank=False, null=False)
    
    
    

    class Meta:
        verbose_name = "juridica"
        verbose_name_plural = "juridicas"

    def __str__(self):
        return self.razon


  

