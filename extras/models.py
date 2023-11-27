from django.db import models
from entidades.models import Trabajador
# Create your models here.
class Banco(models.Model):
    responsable = models.ForeignKey(Trabajador, on_delete=models.CASCADE)
    description = models.TextField("Descripción")
    created = models.DateField("Creado", auto_now_add=True)
    modified = models.DateField("Editado", auto_now=True)

    def __str__(self):
        return f"{self.responsable} - {self.description} - {self.created}"