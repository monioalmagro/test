from django.shortcuts import render
from rest_framework import viewsets

from .serializers import FisicaSerializer , JuridicaSerializer
from .models import Fisica , Juridica

class FisicaViewSet(viewsets.ModelViewSet):
    serializer_class = FisicaSerializer
    queryset = Fisica.objects.all()

class JuridicaViewSet(viewsets.ModelViewSet):
    serializer_class = JuridicaSerializer
    queryset = Juridica.objects.all()

