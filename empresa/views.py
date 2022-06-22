from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from app_juegos.models import Sucursal, Empleados, Juguete
from empresa.forms import User_registration_form


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

def logout_view(request):
    logout(request)
    return redirect('index')


def register_view(request):
    if request.method == 'POST':
        form = User_registration_form(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password = password)
            login(request, user)
            context = {'message':f'Hola, {username}, tu usuario fue creado correctamente.'}
            return render(request, 'index.html', context = context)
        else:
            errors = form.errors
            form = User_registration_form()
            context = {'errors':errors, 'form':form}
            return render(request, 'auth/register.html', context = context)
    else:
        form = User_registration_form()
        context = {'form':form}
        return render(request, 'auth/register.html', context =context)

def compra(request):
    return render(request, 'compra.html')
