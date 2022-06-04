from django.urls import path
from app_juegos.views import listar_juguetes

urlpatterns = [
    path('', listar_juguetes, name = 'lista_juguetes'),
]