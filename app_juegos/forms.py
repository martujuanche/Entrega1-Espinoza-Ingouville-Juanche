from django import forms
from app_juegos.models import Juguete

class Juguete_form(forms.ModelForm):
    class Meta:
        model = Juguete
        fields = '__all__'