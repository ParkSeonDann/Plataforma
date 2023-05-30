from django.db import models
from rest_framework import serializers


class Color(models.Model): 
    id_color  = models.IntegerField(3,primary_key=True)
    nom_color = models.CharField(max_length=30, null=True)

class Pais(models.Model): 
    id_pais  = models.IntegerField(3, primary_key=True)
    nom_pais = models.CharField(null=True, max_length=15)

class Region(models.Model): 
    id_region  = models.IntegerField(3, primary_key=True)
    nom_region = models.CharField(null=True, max_length=15)
    id_pais    = models.ForeignKey(Pais, null=True, on_delete=models.CASCADE)

class Provincia(models.Model): 
    id_prov   = models.IntegerField(3, primary_key=True)
    nom_prov  = models.CharField(null=True, max_length=15)
    id_region = models.ForeignKey(Region, null=True, on_delete=models.CASCADE)


class Comuna(models.Model): 
    id_com  = models.IntegerField(3, primary_key=True ,)
    nom_com = models.CharField(null=True, max_length=15)
    id_prov = models.ForeignKey(Provincia, null=True, on_delete=models.CASCADE)

class Localizacion(models.Model): 
    id_localizacion = models.IntegerField(3, primary_key=True)
    direccion       = models.CharField(null=True, max_length=50)
    cod_postal      = models.CharField(null=True, max_length=15)
    id_com          = models.ForeignKey(Comuna, null=True, on_delete=models.CASCADE)

class Cliente(models.Model): 
    rut_cli         = models.IntegerField(10, primary_key=True)
    nom_cli         = models.CharField(null=True, max_length=30)
    app_cli         = models.CharField(null=True, max_length=30)
    raz_sol         = models.CharField(null=True, max_length=30)
    num_cel         = models.IntegerField(9)
    id_localizacion = models.ForeignKey(Localizacion, null=True, on_delete=models.CASCADE)

class Tipo_pago(models.Model): 
    id_tipo_pago  = models.IntegerField(2, primary_key=True)
    nom_tipo_pago = models.CharField(null=True, max_length=30)

class Temporada(models.Model): 
    id_temp   = models.IntegerField(2, primary_key=True)
    temporada = models.CharField(null=True, max_length=20)

class Especie(models.Model): 
    id_esp  = models.IntegerField(3, primary_key=True)
    nom_esp = models.CharField(null=True, max_length=15)

class TipoProducto(models.Model): 
    id_tipo        = models.IntegerField(3, primary_key=True)
    especificacion = models.CharField(max_length=200, null=True)

class Planta(models.Model): 
    id_planta  = models.IntegerField(3, primary_key=True)
    nom_planta = models.CharField(null=True, max_length=20)
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
    nom_prov           = models.CharField(null=True, max_length=20)
    fecha_ini_contrato = models.DateField
    id_prod            = models.ForeignKey(Producto, null=True, on_delete=models.CASCADE)          ####

class Macetero(models.Model): 
    id_macetero   = models.IntegerField(3, primary_key=True)
    tipo_macetero = models.CharField(null=True, max_length=15)
    tamanno       = models.CharField(null=True, max_length=20)
    precio        = models.IntegerField(6)
    id_color      = models.ForeignKey(Color, null=True, on_delete=models.CASCADE)

class TipoFer(models.Model): 
    id_tipo_Fer    = models.IntegerField(3, primary_key=True)
    tipo_fer       = models.CharField(null=True, max_length=30)
    especificacion = models.CharField(null=True, max_length=200)
    precio         = models.IntegerField(6)

class Fertilizante(models.Model): 
    id_fer   = models.IntegerField(3, primary_key=True)
    nom_fer  = models.CharField(null=True, max_length=20)
    Tipo_fer = models.ForeignKey(TipoFer, null=True, on_delete=models.CASCADE)

class Sucursal(models.Model): 
    id_sucursal     = models.IntegerField(3, primary_key=True)
    nom_sucursal    = models.CharField(null=True, max_length=20)
    direccion       = models.CharField(null=True, max_length=20)
    id_localizacion = models.ForeignKey(Localizacion, null=True, on_delete=models.CASCADE)

class Cargo(models.Model): 
    id_cargo    = models.IntegerField(3, primary_key=True)
    nom_cargo   = models.CharField(null=True, max_length=30)
    min_salario = models.IntegerField(4)
    max_salario = models.IntegerField(7)

class Empleado(models.Model): 
    id_emp             = models.IntegerField(10, primary_key=True)
    rut                = models.CharField(null=True, max_length=10)
    nom                = models.CharField(null=True, max_length=30)
    app                = models.CharField(null=True, max_length=30)
    apm                = models.CharField(null=True, max_length=30)
    num_celu           = models.CharField(null=True, max_length=12)
    salario            = models.IntegerField(7)
    id_sucursal        = models.ForeignKey(Sucursal, null=True, on_delete=models.CASCADE)
    id_localizacion    = models.ForeignKey(Localizacion, null=True, on_delete=models.CASCADE)
    id_cargo           = models.ForeignKey(Cargo, null=True, on_delete=models.CASCADE)

class Espacio_Bodega(models.Model): 
    id_espacio     = models.IntegerField(3, primary_key=True)
    fila           = models.IntegerField(7)
    columna        = models.CharField(null=True, max_length=7)
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
    fecha        = models.DateField()
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


### insertar datos 
new_color = Color(id_color=1, nom_color='Verde')
new_color.save()

nuevo_pais = Pais(id_pais=1, nom_pais='Chile')
nuevo_pais.save()

pais_chile = Pais.objects.get(id_pais=1)

nueva_region1 = Region(id_region=1, nom_region='Magallanes', id_pais=pais_chile)
nueva_region1.save()
nueva_region2 = Region(id_region=2, nom_region='Valparaíso', id_pais=pais_chile)
nueva_region2.save()
nueva_region3 = Region(id_region=3, nom_region='Maule', id_pais=pais_chile)
nueva_region3.save()

region1 = Region.objects.get(id_region=1)
region2 = Region.objects.get(id_region=2)
region3 = Region.objects.get(id_region=3)

nueva_provincia1 = Provincia(id_prov=1, nom_prov='Tierra del Fuego', id_region=region1)
nueva_provincia1.save()
nueva_provincia2 = Provincia(id_prov=2, nom_prov='San Antonio', id_region=region2)
nueva_provincia2.save()
nueva_provincia3 = Provincia(id_prov=3, nom_prov='Talca', id_region=region3)
nueva_provincia3.save()

provincia1 = Provincia.objects.get(id_prov=1)  
provincia2 = Provincia.objects.get(id_prov=2)  
provincia3 = Provincia.objects.get(id_prov=3)  

nueva_comuna1 = Comuna(id_com=1, nom_com=' Ushuaia', id_prov=provincia1)
nueva_comuna1.save()
nueva_comuna2 = Comuna(id_com=2, nom_com='Cartagena.', id_prov=provincia2)
nueva_comuna2.save()
nueva_comuna3 = Comuna(id_com=3, nom_com='San Clemente', id_prov=provincia3)
nueva_comuna3.save()

comuna1 = Comuna.objects.get(id_com=1) 
comuna2 = Comuna.objects.get(id_com=2) 
comuna3 = Comuna.objects.get(id_com=3) 

nueva_localizacion1 = Localizacion(id_localizacion=1, direccion='Calle 1', cod_postal='12345', id_com=comuna1)
nueva_localizacion1.save()
nueva_localizacion2 = Localizacion(id_localizacion=2, direccion='Calle 2', cod_postal='23456', id_com=comuna2)
nueva_localizacion2.save()
nueva_localizacion3 = Localizacion(id_localizacion=3, direccion='Calle 3', cod_postal='34567', id_com=comuna3)
nueva_localizacion3.save()

localizacion1 = Localizacion.objects.get(id_localizacion=1) 
localizacion2 = Localizacion.objects.get(id_localizacion=2) 
localizacion3 = Localizacion.objects.get(id_localizacion=3) 

nueva_sucursal1 = Sucursal(id_sucursal=1,nom_sucursal='Sucursal A',direccion='Calle 123',id_localizacion=localizacion1)
nueva_sucursal1.save()
nueva_sucursal2 = Sucursal(id_sucursal=2,nom_sucursal='Sucursal B',direccion='Calle 234',id_localizacion=localizacion2)
nueva_sucursal2.save()
nueva_sucursal3 = Sucursal(id_sucursal=3,nom_sucursal='Sucursal C',direccion='Calle 567',id_localizacion=localizacion3)
nueva_sucursal3.save()

sucursal1 = Sucursal.objects.get(id_sucursal=1) 
sucursal2 = Sucursal.objects.get(id_sucursal=2) 
sucursal3 = Sucursal.objects.get(id_sucursal=3) 

nuevo_cargo1 = Cargo(id_cargo=1, nom_cargo='Gerente', min_salario=500000, max_salario=1000000)
nuevo_cargo1.save()
nuevo_cargo2 = Cargo(id_cargo=2, nom_cargo='Jefe de area', min_salario=400000, max_salario=2000000)
nuevo_cargo2.save()
nuevo_cargo3 = Cargo(id_cargo=3, nom_cargo='Ayudante', min_salario=500000, max_salario=1000000)
nuevo_cargo3.save()


cargo1 = Cargo.objects.get(id_cargo=1) 
cargo2 = Cargo.objects.get(id_cargo=2) 
cargo3 = Cargo.objects.get(id_cargo=3) 


nuevo_empleado1 = Empleado(id_emp=1,rut='12345678-9',nom='Juan',app='Pérez',apm='Gómez',num_celu='987654321',salario=500000,id_sucursal=sucursal1,id_localizacion=localizacion1,id_cargo=cargo1)
nuevo_empleado1.save()
nuevo_empleado2 = Empleado(id_emp=2,rut='12312378-4',nom='pedro',app='cantillana',apm='alvaro',num_celu='123456789',salario=500000,id_sucursal=sucursal2,id_localizacion=localizacion2,id_cargo=cargo2)
nuevo_empleado2.save()
nuevo_empleado3 = Empleado(id_emp=3,rut='12345665-1',nom='almendra',app='henriquez',apm='lucho',num_celu='345678912',salario=500000,id_sucursal=sucursal3,id_localizacion=localizacion3,id_cargo=cargo3)
nuevo_empleado3.save()

empleado1 = Empleado.objects.get(id_emp=1) 
empleado2 = Empleado.objects.get(id_emp=2) 
empleado3 = Empleado.objects.get(id_emp=3) 

nuevo_tipo_producto = TipoProducto(id_tipo=1,especificacion='Especificación del tipo de producto')
nuevo_tipo_producto.save()
 
tipo_producto1 = TipoProducto.objects.get(id_tipo=1)  

nuevo_producto = Producto(id_prod=1,nom_prod='Producto A',precio=1000,id_color=new_color,id_tipo=tipo_producto1)
nuevo_producto.save()

producto1 = Producto.objects.get(id_prod=1) #ejemplo

nuevo_espacio1 = Espacio_Bodega(id_espacio=1,fila=1,columna='A',stock=100,especificacion='Especificación del espacio',id_prod=producto1)
nuevo_espacio1.save()
nuevo_espacio2 = Espacio_Bodega(id_espacio=2,fila=1,columna='b',stock=100,especificacion='Especificación del espacio',id_prod=producto1)
nuevo_espacio2.save()
nuevo_espacio3 = Espacio_Bodega(id_espacio=3,fila=1,columna='c',stock=100,especificacion='Especificación del espacio',id_prod=producto1)
nuevo_espacio3.save()

nueva_bodega1 = Bodega(id_prod=1,id_espacio=nuevo_espacio1,id_tipo=nuevo_tipo_producto,id_com=comuna1,id_localizacion=localizacion1)
nueva_bodega1.save()
nueva_bodega2 = Bodega(id_prod=1,id_espacio=nuevo_espacio2,id_tipo=nuevo_tipo_producto,id_com=comuna2,id_localizacion=localizacion2)
nueva_bodega2.save()
nueva_bodega3 = Bodega(id_prod=1,id_espacio=nuevo_espacio3,id_tipo=nuevo_tipo_producto,id_com=comuna3,id_localizacion=localizacion3)
nueva_bodega3.save()


