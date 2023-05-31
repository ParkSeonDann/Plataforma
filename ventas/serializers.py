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

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ('id_color', 'nom_color')

class TipoProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoProducto
        fields = ('id_tipo', 'especificacion')

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ('id_prod', 'nom_prod','precio','cantidad_prod','id_tipo')

class SucursalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sucursal
        fields = ('id_sucursal', 'nom_sucursal','direccion','id_localizacion')

class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = ('id_emp', 'rut','nom','app', 'apm','num_celu', 'salario','fecha_ini_contrato', 'id_sucursal','id_localizacion','id_cargo')