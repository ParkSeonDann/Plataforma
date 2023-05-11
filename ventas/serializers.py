from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status
from .models import *

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ('rut_cli', 'nom_cli','app_cli','raz_sol','num_cel')


class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = ('id_prov', 'nom_prov','fecha_ini_contrato','id_prod')