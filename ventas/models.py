from django.db import models
from rest_framework import serializers


class Color(models.Model): 
    id_color  = models.IntegerField(3,primary_key=True)
    nom_color = models.CharField(max_length=30, null=True)

class Pais(models.Model): 
    id_pais  = models.IntegerField(3, primary_key=True)
    nom_pais = models.CharField(max_length=15)

class Region(models.Model): 
    id_region  = models.IntegerField(3, primary_key=True)
    nom_region = models.CharField(max_length=15)
    id_pais    = models.ForeignKey(Pais, null=True, on_delete=models.CASCADE)

class Provincia(models.Model): 
    id_prov   = models.IntegerField(3, primary_key=True)
    nom_prov  = models.CharField(max_length=15)
    id_region = models.ForeignKey(Region, null=True, on_delete=models.CASCADE)

class Comuna(models.Model): 
    id_com  = models.IntegerField(3, primary_key=True ,)
    nom_com = models.CharField(max_length=15)
    id_prov = models.ForeignKey(Provincia, null=True, on_delete=models.CASCADE)

class Localizacion(models.Model): 
    id_localizacion = models.IntegerField(3, primary_key=True)
    direccion       = models.CharField(max_length=50)
    cod_postal      = models.CharField(max_length=15)
    id_com          = models.ForeignKey(Comuna, null=True, on_delete=models.CASCADE)

class Cliente(models.Model): 
    rut_cli         = models.IntegerField(10, primary_key=True)
    nom_cli         = models.CharField(max_length=30)
    app_cli         = models.CharField(max_length=30)
    raz_sol         = models.CharField(max_length=30)
    num_cel         = models.IntegerField(9)
    id_localizacion = models.ForeignKey(Localizacion, null=True, on_delete=models.CASCADE)

class Tipo_pago(models.Model): 
    id_tipo_pago  = models.IntegerField(2, primary_key=True)
    nom_tipo_pago = models.CharField(max_length=30)

class Temporada(models.Model): 
    id_temp   = models.IntegerField(2, primary_key=True)
    temporada = models.CharField(max_length=20)

class Especie(models.Model): 
    id_esp  = models.IntegerField(3, primary_key=True)
    nom_esp = models.CharField(max_length=15)

class TipoProducto(models.Model): 
    id_tipo        = models.IntegerField(3, primary_key=True)
    especificacion = models.CharField(max_length=200, null=True)

class Planta(models.Model): 
    id_planta  = models.IntegerField(3, primary_key=True)
    nom_planta = models.CharField(max_length=20)
    precio     = models.IntegerField(6)
    id_color   = models.ForeignKey(Color, null=True, on_delete=models.CASCADE)
    id_temp    = models.ForeignKey(Temporada, null=True, on_delete=models.CASCADE)
    id_esp     = models.ForeignKey(Especie, null=True, on_delete=models.CASCADE)

class Producto(models.Model): 
    id_prod  = models.IntegerField(3, primary_key=True)
    nom_prod = models.CharField(max_length=30, null=True)
    precio   = models.IntegerField(6, null=True)
    id_color = models.ForeignKey(Color, null=True, on_delete=models.CASCADE)
    id_tipo  = models.ForeignKey(TipoProducto, null=True, on_delete=models.CASCADE)

class Proveedor(models.Model): 
    id_prov            = models.IntegerField(3, primary_key=True)
    nom_prov           = models.CharField(max_length=20)
    fecha_ini_contrato = models.DateField
    id_prod            = models.ForeignKey(Producto, null=True, on_delete=models.CASCADE)          ####

class Macetero(models.Model): 
    id_macetero   = models.IntegerField(3, primary_key=True)
    tipo_macetero = models.CharField(max_length=15)
    tamanno       = models.CharField(max_length=20)
    precio        = models.IntegerField(6)
    id_color      = models.ForeignKey(Color, null=True, on_delete=models.CASCADE)

class TipoFer(models.Model): 
    id_tipo_Fer    = models.IntegerField(3, primary_key=True)
    tipo_fer       = models.CharField(max_length=30)
    especificacion = models.CharField(max_length=200)
    precio         = models.IntegerField(6)

class Fertilizante(models.Model): 
    id_fer   = models.IntegerField(3, primary_key=True)
    nom_fer  = models.CharField(max_length=20)
    Tipo_fer = models.ForeignKey(TipoFer, null=True, on_delete=models.CASCADE)

class Sucursal(models.Model): 
    id_sucursal     = models.IntegerField(3, primary_key=True)
    nom_sucursal    = models.CharField(max_length=20)
    direccion       = models.CharField(max_length=20)
    id_localizacion = models.ForeignKey(Localizacion, null=True, on_delete=models.CASCADE)

class Cargo(models.Model): 
    id_cargo    = models.IntegerField(3, primary_key=True)
    nom_cargo   = models.CharField(max_length=30)
    min_salario = models.IntegerField(4)
    max_salario = models.IntegerField(7)

class Empleado(models.Model): 
    id_emp             = models.IntegerField(10, primary_key=True)
    rut                = models.CharField(max_length=10)
    nom                = models.CharField(max_length=30)
    app                = models.CharField(max_length=30)
    apm                = models.CharField(max_length=30)
    num_celu           = models.CharField(max_length=12)
    salario            = models.IntegerField(7)
    fecha_ini_contrato = models.DateField
    id_sucursal        = models.ForeignKey(Sucursal, null=True, on_delete=models.CASCADE)
    id_localizacion    = models.ForeignKey(Localizacion, null=True, on_delete=models.CASCADE)
    id_cargo           = models.ForeignKey(Cargo, null=True, on_delete=models.CASCADE)

class Espacio_Bodega(models.Model): 
    id_espacio     = models.IntegerField(3, primary_key=True)
    fila           = models.IntegerField(7)
    columna        = models.CharField(max_length=7)
    stock          = models.IntegerField(7)
    especificacion = models.CharField(max_length=200, null=True)
    id_prod        = models.ForeignKey(Producto, null=True, on_delete=models.CASCADE)

class Bodega(models.Model): 
    id_prod         = models.IntegerField(3, primary_key=True )
    id_espacio      = models.ForeignKey(Espacio_Bodega, null=True, on_delete=models.CASCADE)
    id_tipo         = models.ForeignKey(TipoProducto, null=True, on_delete=models.CASCADE)
    id_com          = models.ForeignKey(Comuna, null=True, on_delete=models.CASCADE)
    id_localizacion = models.ForeignKey(Localizacion, null=True, on_delete=models.CASCADE)
    
class Boleta(models.Model): 
    id_boleta    = models.IntegerField(3, primary_key=True)
    id_tipo_pago = models.ForeignKey(Tipo_pago, null=True, on_delete=models.CASCADE)
    rut_cli      = models.ForeignKey(Cliente, null=True, on_delete=models.CASCADE)
    total_pago   = models.IntegerField(8)
    fecha        = models.DateField
    id_emp       = models.ForeignKey(Empleado, null=True, on_delete=models.CASCADE)
    id_sucursal  = models.ForeignKey(Sucursal, null=True, on_delete=models.CASCADE)
    
class Boleta_Detalle(models.Model): 
    id_boleta_det = models.IntegerField(3, primary_key=True)
    id_prod       = models.ForeignKey(Producto, null=True, on_delete=models.CASCADE)
    precio        = models.IntegerField(12)
    cantidad      = models.IntegerField(3)
    total         = models.IntegerField(12)

class Compra(models.Model): 
    id_compra    = models.IntegerField(3, primary_key=True)
    id_tipo_pago = models.ForeignKey(Tipo_pago, null=True, on_delete=models.CASCADE)
    rut_cli      = models.ForeignKey(Cliente, null=True, on_delete=models.CASCADE)
    total_pago   = models.IntegerField(8)
    fecha        = models.DateField
    id_emp       = models.ForeignKey(Empleado, null=True, on_delete=models.CASCADE)
    id_sucursal  = models.ForeignKey(Sucursal, null=True, on_delete=models.CASCADE)
    
class Compra_det(models.Model): 
    id_compra = models.IntegerField(3, primary_key=True)
    id_prod   = models.ForeignKey(Producto, null=True, on_delete=models.CASCADE)
    precio    = models.IntegerField(6, null=True)
    cantidad  = models.IntegerField(3)
    total     = models.IntegerField(12)

class Guia_Despacho(models.Model): #guia despacho
    id_gd        = models.IntegerField(3, primary_key=True)
    id_tipo_pago = models.ForeignKey(Tipo_pago, null=True, on_delete=models.CASCADE)
    rut_cli      = models.ForeignKey(Cliente, null=True, on_delete=models.CASCADE)
    total_pago   = models.IntegerField(8)
    fecha        = models.DateField
    id_emp       = models.ForeignKey(Empleado, null=True, on_delete=models.CASCADE)
    id_sucursal  = models.ForeignKey(Sucursal, null=True, on_delete=models.CASCADE)
    
class Gd_detalle(models.Model): 
    id_gd    = models.IntegerField(3, primary_key=True)
    id_prod  = models.ForeignKey(Producto, null=True, on_delete=models.CASCADE)
    precio   = models.IntegerField(6, null=True)
    cantidad = models.IntegerField(3)
    total    = models.IntegerField(12)
    #para mover de un lado a otro se necesita guia de despacho: c

class Conductor(models.Model): 
    id_conduc    = models.IntegerField(3, primary_key=True)
    nom_con      = models.CharField(max_length=30, null= True)
    apellido_con = models.CharField(max_length=30, null=True)
    rut_con      = models.IntegerField(10, null=True)

class Ruta(models.Model): 
    id_ruta         = models.IntegerField(3,primary_key=True)
    id_localizacion = models.ForeignKey(Localizacion, null=True, on_delete=models.CASCADE)

class Camion(models.Model): 
    id_camion     = models.IntegerField(3,primary_key=True)
    patente       = models.CharField(max_length=8,null=True)
    id_conduc     = models.ForeignKey(Conductor, null=True, on_delete=models.CASCADE)
    cantidad_prod = models.IntegerField(7, null=True)
    id_ruta       = models.ForeignKey(Localizacion, null=True, on_delete=models.CASCADE)














































### bodega😡                                      ###
### sucursales😡                                    ###
### cargo de empleados😡
### id especie aparte
### temporada en otra😡                         ###
### color otra😡                                  ###
### tipo fertilizante otra😡                        ###
### cambiar tablas a de tipos a otras tablas y ahi especificar (eje: iluminacion automovil)😡         ###
### trabajo cambiar a cargo😡
### sacar his_trabajo /cambiar pk de rut a un cod y poner inicio de contrato y final😡
### cambiar localizacion a comuna (siempre el menor en la tabla q tenga una foranea)😡               ###
### tabla region lleva el id_pais😡                                                                   ###
### una tabla de comuna 😡                                                                            ###
###  poner los null true  :(
###
###
###

