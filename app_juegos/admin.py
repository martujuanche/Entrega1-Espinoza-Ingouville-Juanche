from django.contrib import admin
from app_juegos.models import Juguete, Sucursal, Empleados

@admin.register(Juguete)
class JugueteAdmin(admin.ModelAdmin):
    list_display = ['name', 'year', 'price', 'is_active']
@admin.register(Sucursal)
class SucursalAdmin(admin.ModelAdmin):
    list_display = ['adress', 'phone', 'email', 'is_active']
@admin.register(Empleados)
class EmpleadosAdmin(admin.ModelAdmin):
    list_display = ['nombre','puesto','email','is_active']