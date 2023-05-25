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

def mostrar_carrito(request):
    return render(request,'carro-compras.html')

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
