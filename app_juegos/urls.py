from django.urls import path
from app_juegos.views import ListView,listar_juguetes, crear_juguete_view, crear_sucursal_view, crear_empleado_view, Detail_juguete, Detail_empleados,Detail_sucursal,detail_juguete, delete_juguete


urlpatterns = [
    path('', listar_juguetes.as_view(), name = 'lista_juguetes'),
    path('crear-juguete/', crear_juguete_view, name = 'create-juguete'),
    path('crear-sucursal/', crear_sucursal_view, name = 'create-sucursal'),
    path('crear-empleado/', crear_empleado_view, name = 'create-empleado'),
    path('vermas/<int:pk>/', Detail_juguete.as_view(), name = 'vermas'),
    path('vermasE/<int:pk>/', Detail_empleados.as_view(), name = 'vermasE'),
    path('vermasS/<int:pk>/', Detail_sucursal.as_view(), name = 'vermasS'),
    path('detail-juguete/<int:pk>/', detail_juguete, name = 'detail_juguete'),
    path('delete-juguete/<int:pk>/', delete_juguete, name = 'delete_juguete'),
]