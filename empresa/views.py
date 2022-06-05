from django.shortcuts import render
from app_juegos.models import Sucursal, Empleados, Juguete

def index(request):
    return render(request, 'index.html')

def listar_sucursales(request):
    lista_sucursales = Sucursal.objects.all()
    context = {'lista_sucursales':lista_sucursales}
    return render(request, 'sucursales.html', context=context)

def listar_empleados(request):
    lista_empleados = Empleados.objects.all()
    context = {'lista_empleados':lista_empleados}
    return render(request, 'quienes_somos.html', context=context)

def contacto(request):
    return render(request, 'contacto.html')

def buscar_juguetes(request):
    print(request.GET)
    juguetes = Juguete.objects.filter(name__icontains = request.GET['search'])
    context = {'juguetes':juguetes}
    return render(request, 'buscar_juguetes.html', context = context)


