from django.shortcuts import render, redirect
from django.urls import reverse
from app_juegos.models import Juguete, Sucursal, Empleados
from app_juegos.forms import Juguete_form, Sucursal_form, Empleados_form
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView,ListView,CreateView




def listar_juguetes(request):
    lista_juguetes = Juguete.objects.all()
    context = {'lista_juguetes':lista_juguetes}
    return render(request, 'lista_juguetes.html', context=context)

def detail_juguete(request, pk):
    try:
        juguete = Juguete.objects.get(id=pk)
        context = {'juguete':juguete}
        return render(request, 'juguete_detail.html', context = context)

    except:

        context = {'error':'El juguete no existe'}
        return render(request, 'juguete.html',context = context)


def delete_juguete(request, pk):
    try:
        if request.method == "GET":
            juguete = Juguete.objects.get(id=pk)
            juguete = {'juguete':juguete}
        
        else:
            juguete = Juguete.objects.get(id=pk)
            juguete.delete()
            context = {'message':'Juguete eliminado correctamente'}
        return render(request, 'delete_juguete.html', context = context)

    except: 
        context = {'error':'El juguete no existe'}
        return render(request, 'delete_juguete.html', context = context)
        

@login_required
def crear_juguete_view(request):
    if request.method == 'GET':
        form = Juguete_form()
        context = {'form':form}
        return render(request, 'crear_juguete.html', context=context)
    else:
        form = Juguete_form(request.POST)
        if form.is_valid():
            new_product = Juguete.objects.create(
                  name = form.cleaned_data['name'],
                  year = form.cleaned_data['year'],
                  price = form.cleaned_data['price'],
                  image = form.cleaned_data['image'],
            )
            context ={'new_product':new_product}
        return render(request, 'crear_juguete.html', context=context)

def crear_sucursal_view(request):
    if request.user.is_authenticated and request.user.is_superuser:
        if request.method == 'GET':
            form = Sucursal_form()
            context = {'form':form}
            return render(request, 'crear_sucursal.html',context=context )
        else:
            form = Sucursal_form(request.POST)
            if form.is_valid():
                new_sucursal = Sucursal.objects.create(
                    adress = form.cleaned_data['adress'],
                    phone = form.cleaned_data['phone'],
                    email = form.cleaned_data['email'],
                    image = form.cleaned_data['image'],
                )
                context ={'new_sucursal':new_sucursal}
            return render(request, 'crear_sucursal.html',context=context )
    else:
        return redirect('login')



def crear_empleado_view(request):
    if request.user.is_authenticated and request.user.is_superuser:
        if request.method == 'GET':
            form = Empleados_form()
            context = {'form':form}
            return render(request, 'crear_empleado.html',context=context )
        else:
            form = Empleados_form(request.POST)
            if form.is_valid():
                new_empleado = Empleados.objects.create(
                    nombre = form.cleaned_data['nombre'],
                    puesto = form.cleaned_data['puesto'],
                    email = form.cleaned_data['email'],
                    image = form.cleaned_data['image'],
                )
                context ={'new_empleado':new_empleado}
            return render(request, 'crear_empleado.html',context=context )
    else:
        return redirect('login')

class listar_juguetes(ListView):
    model = Juguete
    template_name= 'juguete.html'



class Detail_juguete(DetailView):
    model = Juguete
    template_name= 'vermas.html'

class Detail_sucursal(DetailView):
    model= Sucursal
    template_name= 'vermasS.html'

class Detail_empleados(DetailView):
    model= Empleados
    template_name= 'vermasE.html'

class Create_Juguete(CreateView):
    model= Juguete
    template_name= 'crear_juguete.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('detail_juguete',kwargs={'pk':self.object.pk})

class Delete_juguete(DetailView):
    model= Juguete
    template_name= 'delete_juguete.html'

    def get_success_url(self):
        return reverse('lista_juguetes')
