from django.urls import path
from app_juegos.views import listar_juguetes, crear_juguete_view, crear_sucursal_view, crear_empleado_view, Detail_juguete, Detail_empleados,Detail_sucursal

urlpatterns = [
    path('', listar_juguetes, name = 'lista_juguetes'),
    path('crear-juguete/', crear_juguete_view, name = 'create-juguete'),
    path('crear-sucursal/', crear_sucursal_view, name = 'create-sucursal'),
    path('crear-empleado/', crear_empleado_view, name = 'create-empleado'),
    path('detail-juguete/<int:pk>/', Detail_juguete.as_view(), name = 'detail_juguete'),
    path('detail-empleado/<int:pk>/', Detail_empleados.as_view(), name = 'detail_empleado'),
    path('detail-sucursal/<int:pk>/', Detail_sucursal.as_view(), name = 'detail_sucursal'),
]