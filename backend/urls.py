from django.contrib import admin
from django.urls import path
from ventas import views
from ventas.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cliente/', views.rf_cliente),
    path('cliente/<int:rut_cli>', views.rf_cliente_pk),
    path('producto/', views.rf_producto),
    path('producto/<int:id_prod>', views.rf_producto_pk),
    path('proveedor/', views.rf_proveedor),
    path('proveedor/<int:id_prov>', views.rf_proveedor_pk),
    path('color/', views.rf_color),
    path('color/<int:id_color>', views.rf_color_pk),
    path('TP/', views.rf_tipoProducto),
    path('TP/<int:id_tipo>', views.rf_tipoProducto_pk),
    path('sucursal/', views.rf_sucursal),
    path('sucursal/<int:id_sucursal>', views.rf_sucursal_pk),
    path('Empleado/', views.rf_Empleado),
    path('Empleado/<int:id_emp>', views.rf_Empleado_pk),
    path('soap_service/', views.my_soap_application),
    path('soap_service_ferreteria/', views.pruebaFerreteria),
    path('productos/<int:id_prod>/actualizar-stock/', views.actualizar_stock, name='actualizar_stock'),
    path('carga_exitosa/', carga_exitosa, name='carga_exitosa'),
    path('compra/', views.crear_compra, name='crear_compra'),
    path('compra_exitosa/', views.confirmacion_compra, name='confirmacion_compra'),
    

    ###path('soap_service_consumir/', views.SoapList.as_view()),
    
]