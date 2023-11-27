from django.db import models

# Create your models here.
class pdfConf(models.Model):
    logo = models.CharField(max_length=200)
    empresa = models.CharField(max_length=50)
    aprobador = models.CharField(max_length=50)
    responsable_seg = models.CharField(max_length=50)
    responsable_tec = models.CharField(max_length=50)

    def __str__(self):
        return self.responsable_tec