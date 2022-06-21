from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
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

def login_view(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return render(request, 'index.html')
            else:
                context = {'errors':'El usuario no existe'}
                form = AuthenticationForm()
                return render(request, 'auth/login.html', context = context)
        else:
            errors = form.errors
            form = AuthenticationForm()
            context = {'errors':errors, 'form':form}
            return render(request, 'auth/login.html', context = context)

    else:
        form = AuthenticationForm()
        context = {'form':form}
        return render(request, 'auth/login.html', context = context)


