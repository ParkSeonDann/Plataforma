from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .serializers import *
from .models import *


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)
                                                                    # RESTFULL COLOR

@csrf_exempt
def rf_color(request):
    if request.method == 'GET':
         color = Color.objects.all()
         serializer = ColorSerializer(color, many=True)
         return JSONResponse(serializer.data)
    
    elif request.method == 'POST':
         print("******************",request)
         data = JSONParser().parse(request)
         print("******************data:",data)
         color = ColorSerializer(data=data)
         print("******************color:",data)
         if color.is_valid():
            color.save()
            ##code para enviar data el server
            return JSONResponse(color.data, status=201)
    
@csrf_exempt
def rf_color_pk(request,id_color):
    try:
        color = Color.objects.get(pk=id_color)
    except Color.DoesNotExist:
        return HttpResponse(status=408)

    ##   Ya lei el registros
    if request.method == 'GET':
        color = ColorSerializer(color)
        return JSONResponse(color.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        color = ColorSerializer(color, data=data)
        if color.is_valid():
            color.save()
            return JSONResponse(color.data)

    elif request.method == 'DELETE':
        color.delete()
        return HttpResponse(status=204)
        

    return JSONResponse(color.errors, status=400) 

                                                                    # RESTFULL CLIENTE
@csrf_exempt
def rf_cliente(request):
    if request.method == 'GET':
         cliente = Cliente.objects.all()
         serializer = ClienteSerializer(cliente, many=True)
         return JSONResponse(serializer.data)

    elif request.method == 'POST':
         print("******************",request)
         data = JSONParser().parse(request)
         print("******************data:",data)
         cliente = ClienteSerializer(data=data)
         print("******************cliente:",data)
         if cliente.is_valid():
            cliente.save()
            ##code para enviar data el server
            return JSONResponse(cliente.data, status=201)
         
@csrf_exempt
def rf_cliente_pk(request,rut_cli):
    try:
        cliente = Cliente.objects.get(pk=rut_cli)
    except Cliente.DoesNotExist:
        return HttpResponse(status=408)

    ##   Ya lei el registros
    if request.method == 'GET':
        cliente = ClienteSerializer(cliente)
        return JSONResponse(cliente.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        cliente = ClienteSerializer(cliente, data=data)
        if cliente.is_valid():
            cliente.save()
            return JSONResponse(cliente.data)

    elif request.method == 'DELETE':
        cliente.delete()
        return HttpResponse(status=204)
        
    return JSONResponse(cliente.errors, status=400) 

                                                                    # RESTFULL PROVEEDOR
@csrf_exempt
def rf_proveedor(request):
    if request.method == 'GET':
         proveedor = proveedor.objects.all()
         serializer = ProveedorSerializer(proveedor, many=True)
         return JSONResponse(serializer.data)

    elif request.method == 'POST':
         data = JSONParser().parse(request)
         proveedor = ProveedorSerializer(data=data)
         if proveedor.is_valid():
            proveedor.save()
            return JSONResponse(proveedor.data, status=201)
         
@csrf_exempt
def rf_proveedor_pk(request,rut_cli):
    try:
        proveedor = Proveedor.objects.get(pk=rut_cli)
    except Proveedor.DoesNotExist:
        return HttpResponse(status=408)

    ##   Ya lei el registros
    if request.method == 'GET':
        proveedor = ProveedorSerializer(proveedor)
        return JSONResponse(proveedor.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        proveedor = ProveedorSerializer(proveedor, data=data)
        if proveedor.is_valid():
            proveedor.save()
            return JSONResponse(proveedor.data)

    elif request.method == 'DELETE':
        proveedor.delete()
        return HttpResponse(status=204)
        
    return JSONResponse(proveedor.errors, status=400)

                                                                    # RESTFULL TIPO PRODUCTO

@csrf_exempt
def rf_tipoProducto(request):
    if request.method == 'GET':
         tp = TipoProducto.objects.all()
         serializer = TipoProductoSerializer(tp, many=True)
         return JSONResponse(serializer.data)

    elif request.method == 'POST':
         data = JSONParser().parse(request)
         tp = TipoProductoSerializer(data=data)
         if tp.is_valid():
            tp.save()
            return JSONResponse(tp.data, status=201)
         
@csrf_exempt
def rf_tipoProducto_pk(request,id_tipo):
    try:
        tp = TipoProducto.objects.get(pk=id_tipo)
    except TipoProducto.DoesNotExist:
        return HttpResponse(status=408)

    ##   Ya lei el registros
    if request.method == 'GET':
        tp = TipoProductoSerializer(tp)
        return JSONResponse(tp.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        tp = TipoProductoSerializer(tp, data=data)
        if tp.is_valid():
            tp.save()
            return JSONResponse(tp.data)

    elif request.method == 'DELETE':
        tp.delete()
        return HttpResponse(status=204)
        
    return JSONResponse(tp.errors, status=400)  
                                                                    # RESTFULL PRODUCTO
@csrf_exempt
def rf_producto(request):
    if request.method == 'GET':
         p = Producto.objects.all()
         serializer = ProductoSerializer(p, many=True)
         return JSONResponse(serializer.data)

    elif request.method == 'POST':
         data = JSONParser().parse(request)
         p = ProductoSerializer(data=data)
         if p.is_valid():
            p.save()
            return JSONResponse(p.data, status=201)
         
@csrf_exempt
def rf_producto_pk(request,id_prod):
    try:
        p = Producto.objects.get(pk=id_prod)
    except Producto.DoesNotExist:
        return HttpResponse(status=408)

    ##   Ya lei el registros
    if request.method == 'GET':
        p = ProductoSerializer(p)
        return JSONResponse(p.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        p = ProductoSerializer(p, data=data)
        if p.is_valid():
            p.save()
            return JSONResponse(p.data)

    elif request.method == 'DELETE':
        p.delete()
        return HttpResponse(status=204)
        
    return JSONResponse(p.errors, status=400) 

                                                                    # RESTFULL sucursal 

@csrf_exempt
def rf_sucursal(request):
    if request.method == 'GET':
         sucursal = sucursal.objects.all()
         serializer = SucursalSerializer(sucursal, many=True)
         return JSONResponse(serializer.data)

    elif request.method == 'POST':
         data = JSONParser().parse(request)
         sucursal = SucursalSerializer(data=data)
         if sucursal.is_valid():
            sucursal.save()
            return JSONResponse(sucursal.data, status=201)
         
@csrf_exempt
def rf_sucursal_pk(request,id_sucursal):
    try:
        sucursal = Sucursal.objects.get(pk=id_sucursal)
    except Sucursal.DoesNotExist:
        return Sucursal(status=408)

    ##   Ya lei el registros
    if request.method == 'GET':
        sucursal = SucursalSerializer(sucursal)
        return JSONResponse(sucursal.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        sucursal = SucursalSerializer(sucursal, data=data)
        if sucursal.is_valid():
            sucursal.save()
            return JSONResponse(sucursal.data)

    elif request.method == 'DELETE':
        sucursal.delete()
        return HttpResponse(status=204)
        
    return JSONResponse(sucursal.errors, status=400)                           

                                                                    # RESTFULL sucursal 

@csrf_exempt
def rf_Empleado(request):
    if request.method == 'GET':
         empleado = empleado.objects.all()
         serializer = EmpleadoSerializer(empleado, many=True)
         return JSONResponse(serializer.data)

    elif request.method == 'POST':
         data = JSONParser().parse(request)
         empleado = EmpleadoSerializer(data=data)
         if empleado.is_valid():
            empleado.save()
            return JSONResponse(empleado.data, status=201)
         
@csrf_exempt
def rf_Empleado_pk(request,id_emp):
    try:
        empleado = Empleado.objects.get(pk=id_emp)
    except Sucursal.DoesNotExist:
        return Sucursal(status=408)

    ##   Ya lei el registros
    if request.method == 'GET':
        empleado = EmpleadoSerializer(empleado)
        return JSONResponse(empleado.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        empleado = EmpleadoSerializer(empleado, data=data)
        if empleado.is_valid():
            empleado.save()
            return JSONResponse(empleado.data)

    elif request.method == 'DELETE':
        empleado.delete()
        return HttpResponse(status=204)
        
    return JSONResponse(empleado.errors, status=400)  
                                                           
### Soap

from django.views.decorators.csrf import csrf_exempt
from spyne.application import Application
from spyne.decorator import rpc
from spyne.model.primitive import Unicode, Integer
from spyne.protocol.soap import Soap11
from spyne.server.django import DjangoApplication
from spyne.service import ServiceBase

# http://127.0.0.1:9010/ventas/soap_service/
# http://127.0.0.1:9010/ventas/soap_service/?WSDL
class SoapService(ServiceBase):
    @rpc(Unicode(nillable=False), _returns=Unicode)
    def hello(ctx, name):
        return 'Hello, {}'.format(name)

    @rpc(Integer(nillable=False), Integer(nillable=False), _returns=Integer)
    def sum(ctx, a, b):
        return int(a + b)


soap_app = Application(
    [SoapService],
    tns='django.soap.example',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11(),
)

django_soap_application = DjangoApplication(soap_app)
my_soap_application = csrf_exempt(django_soap_application)


def compra_view(request):
    if request.method == 'POST':
        producto_id = request.POST.get('producto')
        cantidad = request.POST.get('cantidad')
        
        producto = Producto.objects.get(id=producto_id)
        
        # Realizar las operaciones necesarias para registrar la compra en la base de datos
        compra = Compra(producto=producto, cantidad=cantidad)
        compra.save()
        
        return redirect('compra_exitosa')  # Redirigir a una página de confirmación de compra exitosa
    else:
        productos = Producto.objects.all()
        return render(request, 'compra.html', {'productos': productos})


# pruebas Soap 222
class SoapServiceFerreteria(ServiceBase):
    @rpc(Unicode(nillable=False), _returns=Unicode)
    def mandarHola(ctx, nombre):
        return 'Hola Profesor, {}'.format(nombre)

    @rpc(Integer(nillable=False), Integer(nillable=False), Integer(nillable=False), _returns=Integer)
    def ejeSumar(ctx, a, b, c):
        return int(a + b + c)
soap_app_ferreteria = Application(
    [SoapServiceFerreteria],
    tns='django.soap.example',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11(),
)

django_soap_ferreteria = DjangoApplication(soap_app_ferreteria)
pruebaFerreteria = csrf_exempt(django_soap_ferreteria)


####  Consumir
###from suds.client import Client
###from suds.cache import NoCache
###class SoapList(APIView):
   ### def get(self, request, format=None):
      ###  my_client = Client('http://127.0.0.1:8000/ventas/soap_service/?WSDL', cache=NoCache())
        ###print("WSDL Metodos : ", my_client)
        ###stResult = 'Function hello: ' +  str(my_client.service.hello('Harrys el magnifico'))
        ###stResult = stResult + '<br>'+ 'Function sum: ' + str(my_client.service.sum(10, 25))
        ###return HttpResponse(stResult)
