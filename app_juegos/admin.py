from django.contrib import admin
from app_juegos.models import Juguete, Sucursal, Empleados

@admin.register(Juguete)
class ProductsAmin(admin.ModelAdmin):
    list_display = ['name']
@admin.register(Sucursal)
class SucursalAmin(admin.ModelAdmin):
    list_display = ['adress']
@admin.register(Empleados)
class Empleados(admin.ModelAdmin):
    list_display = ['nombre']