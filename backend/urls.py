from django.contrib import admin
from django.urls import path
from ventas import views
from ventas.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('carrito/', mostrar_carrito, name='carrito'),
    path('cliente/', views.rf_cliente),
    path('cliente/<int:rut_cli>', views.rf_cliente_pk),
    path('soap_service/', views.my_soap_application),
    path('soap_service_ferreteria/', views.pruebaFerreteria),
    

    ###path('soap_service_consumir/', views.SoapList.as_view()),
    
]
