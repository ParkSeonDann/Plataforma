from django import forms
from .models import *

class ActualizarStockForm(forms.Form):
    nuevo_stock = forms.IntegerField(label='Nuevo Stock')

"""class CompraForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['id_prod','cantidad_prod'] """   

class CompraForm(forms.ModelForm):
    opcion_entrega = forms.ChoiceField(choices=[('despacho', 'Despacho'), ('retiro', 'Retiro')], widget=forms.RadioSelect)

    class Meta:
        model = Producto
        fields = ['id_prod', 'cantidad_prod', 'opcion_entrega']