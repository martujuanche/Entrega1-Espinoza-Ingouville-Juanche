from django import forms
from app_juegos.models import Juguete,Sucursal,Empleados

class Juguete_form(forms.ModelForm):
    # name = forms.CharField(max_length=100)
    # year = forms.DateField()
    # price = forms.FloatField()
    # image = forms.ImageField()
    # active = forms.BooleanField()
    class Meta:
        model = Juguete
        fields = '__all__'

class Sucursal_form(forms.ModelForm):
    # adress = forms.CharField(max_length=200)
    # phone = forms.IntegerField()
    # email = forms.CharField(max_length=50)
    # image = forms.ImageField()
    class Meta:
        model = Sucursal
        fields = '__all__'

class Empleados_form(forms.ModelForm):
    # nombre = forms.CharField(max_length=50)
    # puesto = forms.CharField(max_length=100)
    # email = forms.CharField(max_length=100)
    # image = forms.ImageField()
    class Meta:
        model = Empleados
        fields = '__all__'