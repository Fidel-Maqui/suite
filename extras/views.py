from django.shortcuts import render, redirect
from extras import forms
from extras import models
from entidades import models as ent_models
from computadoras import models as comp_models
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.
def banco(request):
    items = models.Banco.objects.all().order_by('responsable')
            
    if request.method == "GET":
        if request.GET.get("buscar"):
            nombre = request.GET.get('nombre')
            if nombre:
                trabajadores = ent_models.Trabajador.filter(nombre__icontains = nombre)
            items = items.filter(responsable__in = trabajadores)
            

    paginator = Paginator(items, 18)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    diction = {'items': page_obj, 'cant':items.count()}
    return render(request, "extras/banco.html", diction)

def addProblema(request):
    form = forms.BancoForm()
    
    if request.method == "POST":
        if request.POST.get('save'):
            form = forms.BancoForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("extras:banco")
            for f in form.errors:
                messages.error(request, (f"Error en {f}"))

    diction = {"form":form}
    return render(request, "extras/formBanco.html", diction)

def updProblema(request, id):
    item =  models.Banco.objects.get(id = id)
    form = forms.BancoForm(instance=item)
    
    if request.method == "POST":
        if request.POST.get('upd'):
            form = forms.BancoForm(request.POST, instance=item)
            if form.is_valid():
                form.save()
                return redirect("extras:banco")

    diction = {"form":form, "editing": True}
    return render(request, "extras/formBanco.html", diction)

def delProblema(request, id):
    item = models.Banco.objects.get(pk = id)
    item.delete()
    return redirect("extras:banco")

def bajas(request):
    comps = comp_models.Computadora.objects.filter(baja = 1)
    hard = comp_models.Hardware.objects.filter(baja = 1)
    peri = comp_models.Periferico.objects.filter(baja = 1)

    diction = { "comps":comps, "hard":hard, "peri":peri, }
    return render(request, "extras/bajas.html", diction)

def darBaja_Comp(request, id):
    item = comp_models.Computadora.objects.get(pk= id)
    item.delete()
    return redirect("computadoras:index")

def darBaja_Hard(request, id):
    item = comp_models.Hardware.objects.get(pk= id)
    comp = comp_models.Computadora.objects.get(id=item.computadora)
    item.delete()
    return redirect("computadoras:detalles", comp.id)

def darBaja_Peri(request, id):
    item = comp_models.Periferico.objects.get(pk= id)
    comp = comp_models.Computadora.objects.get(id=item.computadora)
    item.delete()
    return redirect("computadoras:detalles", comp.id)