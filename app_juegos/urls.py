from django.urls import path
from app_juegos.views import listar_juguetes, crear_juguete_view, crear_sucursal_view, crear_empleado_view

urlpatterns = [
    path('', listar_juguetes, name = 'lista_juguetes'),
    path('crear-juguete/', crear_juguete_view, name = 'create-juguete'),
    path('crear-sucursal/', crear_sucursal_view, name = 'create-sucursal'),
    path('crear-empleado/', crear_empleado_view, name = 'create-empleado'),
]