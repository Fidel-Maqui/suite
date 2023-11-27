from django.http import HttpResponse
from django.shortcuts import render, redirect
# from django.views.generic import ListView, View

from .utils import render_to_pdf

from computadoras import models
from .models import pdfConf
# from .forms import *
# Create your views here.
def apdf_htmltopdf(request, id):
    detalles = models.Computadora.objects.get(pk = id)
    componente_interno = models.Hardware.objects.filter(computadora = id)
    componente_externo = models.Periferico.objects.filter(computadora = id)

    pdf_config = pdfConf.objects.last()

    data = {
        'detalle':detalles,
        'componente_interno':componente_interno,
        'componente_externo':componente_externo,
        'title':detalles.nombre,
        'logo':pdf_config.logo,
        'empresa':pdf_config.empresa,
        'aprobador':pdf_config.aprobador,
        'responsable_seg':pdf_config.responsable_seg,
        'responsable_tec':pdf_config.responsable_tec
    }
    
    pdf = render_to_pdf('exporter/topdf.html', data)

    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="'+detalles.nombre+'"'
    return response

def apdf_topdf(request, id):
    detalles = models.Computadora.objects.get(pk = id)
    componente_interno = models.Hardware.objects.filter(computadora = id)
    componente_externo = models.Periferico.objects.filter(computadora = id)

    pdf_config = pdfConf.objects.last()

    data = {
        'detalle':detalles,
        'componente_interno':componente_interno,
        'componente_externo':componente_externo,
        'title':detalles.nombre,
        'logo':pdf_config.logo,
        'empresa':pdf_config.empresa,
        'aprobador':pdf_config.aprobador,
        'responsable_seg':pdf_config.responsable_seg,
        'responsable_tec':pdf_config.responsable_tec
    }
    
    pdf = render_to_pdf('exporter/topdf.html', data)

    response = HttpResponse(pdf, content_type='application/pdf')
    print(response)
    return response