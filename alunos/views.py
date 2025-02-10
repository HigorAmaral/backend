from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from alunos.models import Estado
from alunos.serializers import EstadoSerializer

class EstadoViewSet(ModelViewSet):
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializer
