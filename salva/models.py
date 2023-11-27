from django.db import models

# Create your models here.


class SArea(models.Model):

    nombre = models.CharField(
        max_length=50, help_text="Nombre del área", unique=True)
    cant_trabs = models.PositiveSmallIntegerField(
        null=True, blank=True, default=0)

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ["nombre"]


class STrabajador(models.Model):

    nombre = models.CharField(
        max_length=50, unique=True, help_text="Nombre del Trabajador")
    cargo = models.CharField(max_length=50, help_text="Cargo del Trabajador")
    area = models.ForeignKey(
        SArea, on_delete=models.CASCADE, default=0, null=True, blank=True)
    jefe = models.BooleanField(default=False)
    director = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ["nombre"]


class SComputadora(models.Model):

    responsable = models.ForeignKey(
        STrabajador, on_delete=models.CASCADE, null=True, blank=True)
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


class SHardware(models.Model):
    PIEZAS = [
        ("CPU", "CPU"),
        ("RAM", "RAM"),
        ("BOARD", "BOARD"),
        ("DISCO", "DISCO"),
        ("CD-ROM", "CD-ROM"),
    ]

    computadora = models.ForeignKey(SComputadora, on_delete=models.CASCADE)
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


class SPeriferico(models.Model):
    PERI = [
        ("Monitor", "Monitor"),
        ("Teclado", "Teclado"),
        ("Ups", "Ups"),
        ("Mouse", "Mouse"),
    ]

    computadora = models.ForeignKey(SComputadora, on_delete=models.CASCADE)
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


class SDiferencias(models.Model):

    computadora = models.ForeignKey(SComputadora, on_delete=models.CASCADE)
    campo = models.CharField(max_length=50)
    cambio = models.CharField(max_length=50)
    fecha = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.computadora} - {self.campo}, nuevo valor: {self.cambio}"


class SPrograms(models.Model):

    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre


class SSoftwares(models.Model):

    computadora = models.ForeignKey(SComputadora, on_delete=models.CASCADE)
    nombre = models.ForeignKey(SPrograms, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.computadora.responsable}--{self.computadora}: {self.nombre}"
