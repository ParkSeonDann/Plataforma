from django.contrib import admin
from django.urls import path
from ventas import views

urlpatterns = [
    path('cliente/', views.rf_cliente),
    path('cliente/<int:rut_cli>', views.rf_cliente_pk),
]
