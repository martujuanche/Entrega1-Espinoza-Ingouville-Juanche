from django.shortcuts import render
from app_juegos.models import Juguete, Sucursal, Empleados

def listar_juguetes(request):
    lista_juguetes = Juguete.objects.all()
    context = {'lista_juguetes':lista_juguetes}
    return render(request, 'lista_juguetes.html', context=context)

