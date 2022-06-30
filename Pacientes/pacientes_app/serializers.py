from dataclasses import field, fields
from pyexpat import model
from turtle import clear
from rest_framework import serializers
from .models import Paciente
from datetime import date

class PacienteSerializer(serializers.ModelSerializer):
    
    Nombre_Completo = serializers.SerializerMethodField(read_only=True)
    def get_Nombre_Completo(self, obj):
        return '%s %s' % (obj.nombre, obj.apellido)
        
    edad = serializers.SerializerMethodField(read_only=True)
    def get_edad(self, obj):
        fechahoy=date.today()
        if (fechahoy.month, fechahoy.day) > (obj.nacimiento.month, obj.nacimiento.day):
            return '%s años'%(fechahoy.year - obj.nacimiento.year)
        else:
            return '%s años'%(fechahoy.year - obj.nacimiento.year - 1)
    class Meta:
        model = Paciente
        fields = ["Nombre_Completo","dni","telefono","edad"]
