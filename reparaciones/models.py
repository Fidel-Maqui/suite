from django.db import models
from computadoras.models import Computadora, Trabajador
# Create your models here.
class Reparacion(models.Model):
    recurso = models.ForeignKey(Computadora, on_delete=models.CASCADE)
    sello_1 = models.CharField(max_length=6, default="000000", unique=True)
    sello_2 = models.CharField(max_length=6, default="000000", unique=True)
    tenico = models.ForeignKey(Trabajador, on_delete=models.CASCADE)
    descripcion = models.TextField()
    modified = models.DateTimeField(auto_now=True, auto_now_add=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)