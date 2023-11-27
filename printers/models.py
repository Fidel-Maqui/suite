from django.db import models
from entidades.models import Trabajador
# Create your models here.
class PrinterStack(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    toner = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre
    
class PrinterOwner(models.Model):
    owner = models.ForeignKey(Trabajador, verbose_name="Responsable",  on_delete=models.CASCADE)
    printer = models.ForeignKey(PrinterStack, verbose_name="Impresora", on_delete=models.CASCADE)
    inv = models.CharField(max_length=6, unique=True)
    serial = models.CharField(max_length=6, unique=True)

    def __str__(self):
        return f"{self.owner} -- {self.printer}"
