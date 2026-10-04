from django.db import models

class TipoInmueble(models.Model):
    """Modelo que representa la categoría del inmueble (Casa, Departamento, etc.)"""
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre


class Region(models.Model):
    """Modelo que representa una región geográfica"""
    nombre = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = "Región"
        verbose_name_plural = "Regiones"

    def __str__(self):
        return self.nombre

class Comuna(models.Model):
    """Modelo que representa una comuna asociada a una región"""
    nombre = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='comunas')

    def __str__(self):
        return f"{self.nombre} ({self.region.nombre})"


class Inmueble(models.Model):
    """Modelo que representa una propiedad disponible para arriendo"""
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    direccion = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    m2_construidos = models.IntegerField(default=50)
    habitaciones = models.IntegerField(default=1)
    banos = models.IntegerField(default=1)
    tipo_inmueble = models.ForeignKey(TipoInmueble, on_delete=models.CASCADE, related_name='inmuebles')
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE, related_name='inmuebles', null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} - ${self.precio}"