from django.db import models

class Juguete(models.Model):
    name = models.CharField(max_length=100)
    year = models.DateField()
    price = models.FloatField()
    image = models.ImageField(null=True, blank=True)
    class Meta:
        verbose_name = 'juguete'
        verbose_name_plural = 'juguetes'

class Sucursal(models.Model):
    adress = models.CharField(max_length=200)
    phone = models.IntegerField()
    email = models.CharField(max_length=50)
    image = models.ImageField(null=True, blank=True)
    class Meta:
        verbose_name = 'sucursal'
        verbose_name_plural = 'sucursales'


class Empleados(models.Model):
    nombre = models.CharField(max_length=50)
    puesto = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True)
    class Meta:
        verbose_name = 'empleado'
        verbose_name_plural = 'empleados'

