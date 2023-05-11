from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status
from .models import *

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ('rut_cli', 'nom_cli','app_cli','raz_sol','num_cel','id_localizacion')
