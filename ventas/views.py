from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .serializers import ClienteSerializer
from .models import *


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def rf_cliente(request):
    if request.method == 'GET':
         cliente = Cliente.objects.all()
         serializer = ClienteSerializer(cliente, many=True)
         return JSONResponse(serializer.data)

    elif request.method == 'POST':
         data = JSONParser().parse(request)
         cliente = ClienteSerializer(data=data)
         if cliente.is_valid():
            cliente.save()
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