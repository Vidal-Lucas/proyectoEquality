from datetime import datetime
from django.db import models
from django.forms import CharField
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class Paciente(models.Model):
    nombre=models.CharField(max_length=150)
    apellido=models.CharField(max_length=150)
    dni=models.IntegerField(validators=[MinValueValidator(5000),MaxValueValidator(99999999)])
    nacimiento=models.DateField()
    telefono=models.CharField(max_length=50,blank=True,null=True)
    obra_soc=models.CharField(max_length=150)
    localidad=models.CharField(max_length=150,blank=True,null=True)
    direccion=models.CharField(max_length=150)

    def __str__(self):
        return 'Nombre Paciente: %s %s'%(self.nombre, self.apellido) 
