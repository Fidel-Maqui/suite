from django.db import models

# Create your models here.


class Area(models.Model):
    nombre = models.CharField(
        max_length=50, help_text="Nombre del área", unique=True)
    cant_trabs = models.PositiveSmallIntegerField(
        null=True, blank=True, default=0)

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ["nombre"]


class Trabajador(models.Model):
    nombre = models.CharField(
        max_length=50, unique=True, help_text="Nombre del Trabajador")
    cargo = models.CharField(max_length=50, help_text="Cargo del Trabajador")
    area = models.ForeignKey(
        Area, on_delete=models.CASCADE, default=0, null=True, blank=True)
    jefe = models.BooleanField(default=False)
    director = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ["nombre"]
