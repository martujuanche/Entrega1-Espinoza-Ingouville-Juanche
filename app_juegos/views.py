from django.shortcuts import render
from app_juegos.models import Juguete
from app_juegos.forms import Juguete_form

def listar_juguetes(request):
    lista_juguetes = Juguete.objects.all()
    context = {'lista_juguetes':lista_juguetes}
    return render(request, 'lista_juguetes.html', context=context)


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

