from django.db import models
from entidades.models import Area, Trabajador

# Create your models here.


class Computadora(models.Model):

    responsable = models.ForeignKey(
        Trabajador, on_delete=models.CASCADE, null=True, blank=True)
    nombre = models.CharField(
        max_length=50, help_text="Nombre de la computadora", unique=True)
    ip = models.CharField(max_length=15, default="172.19.250.000", unique=True)
    num_de_inventario = models.CharField(
        max_length=8, unique=True, null=True, blank=True)
    sello_1 = models.CharField(
        max_length=6, unique=True, null=True, blank=True)
    sello_2 = models.CharField(
        max_length=6, unique=True, null=True, blank=True)
    cambios = models.BooleanField(default=False)
    baja = models.BooleanField(default=0)

    def __str__(self):
        return self.nombre


class Hardware(models.Model):
    PIEZAS = [
        ("CPU", "CPU"),
        ("RAM", "RAM"),
        ("BOARD", "BOARD"),
        ("DISCO", "DISCO"),
        ("CD-ROM", "CD-ROM"),
    ]

    computadora = models.ForeignKey(Computadora, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=14, choices=PIEZAS, default="CPU")
    fabricante = models.CharField(
        max_length=50, help_text="Fabricante de la pieza", null=True,  blank=True)
    modelo = models.CharField(
        "módelo", max_length=50, help_text="Módelo de la pieza", null=True,  blank=True)
    capacidad_gb = models.CharField(
        "Capacidad", max_length=50, help_text="Cantidad", null=True,  blank=True)
    velocidad = models.CharField(
        max_length=50, help_text="Velocidad", null=True,  blank=True)
    num_de_serie = models.CharField(
        max_length=50, help_text="No. de serie", null=True, blank=True)
    baja = models.BooleanField(default=0)

    # class Meta:
    # unique_together = [['computadora', 'num_de_serie']]
    # unique_together = [['driver', 'restaurant']]
    def __str__(self):
        return self.nombre


class Periferico(models.Model):
    PERI = [
        ("Monitor", "Monitor"),
        ("Teclado", "Teclado"),
        ("Ups", "Ups"),
        ("Mouse", "Mouse"),
    ]

    computadora = models.ForeignKey(Computadora, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=7, choices=PERI, default="Monitor")
    fabricante = models.CharField(
        max_length=50, help_text="Fabricante del periférico", null=True, blank=True)
    modelo = models.CharField(
        "módelo", max_length=50, help_text="Módelo del periférico", null=True, blank=True)
    num_inventario = models.CharField(
        max_length=50, default="200000", null=True, blank=True)
    num_de_serie = models.CharField(
        max_length=50, help_text="No. de serie", null=True, blank=True)
    baja = models.BooleanField(default=0)

    def __str__(self):
        return self.nombre


class Diferencias(models.Model):

    computadora = models.ForeignKey(Computadora, on_delete=models.CASCADE)
    campo = models.CharField(max_length=50)
    cambio = models.CharField(max_length=50)
    fecha = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.computadora} - {self.campo}, nuevo valor: {self.cambio}"


class Programs(models.Model):

    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre


class Softwares(models.Model):

    computadora = models.ForeignKey(Computadora, on_delete=models.CASCADE)
    nombre = models.ForeignKey(Programs, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.computadora.responsable}--{self.computadora}: {self.nombre}"
