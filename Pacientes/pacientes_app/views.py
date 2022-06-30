from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Paciente
from .serializers import PacienteSerializer

class PacienteListApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self,request, *args, **kwargs):

        pacientes= Paciente.objects.all()
        serializer=PacienteSerializer(pacientes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

   

# Create your views here.
