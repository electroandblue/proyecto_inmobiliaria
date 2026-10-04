from django.contrib import admin
from .models import Inmueble, Region, Comuna


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('nombre',)


@admin.register(Comuna)
class ComunaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'region')
    list_filter = ('region',)
    search_fields = ('nombre', 'region__nombre')


@admin.register(Inmueble)
class InmuebleAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'tipo_inmueble', 'comuna', 'precio')
    list_filter = ('tipo_inmueble', 'comuna__region', 'comuna')
    search_fields = ('nombre', 'direccion', 'descripcion')