from django.urls import path
from app_juegos.views import listar_juguetes, crear_juguete_view

urlpatterns = [
    path('', listar_juguetes, name = 'lista_juguetes'),
    path('crear-juguete/', crear_juguete_view, name = 'create-product'),
]