from django.shortcuts import render, redirect
from .models import Area, Trabajador
from computadoras import models
from . import forms
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.


def updArea():
    areas = Area.objects.all()
    trabs = Trabajador.objects.all()

    for a in areas:
        utrab = trabs.filter(area=a.pk)
        a.cant_trabs = utrab.count()
        a.save()

@login_required
def index(request):
    updArea()
    l_area = Area.objects.all()

    if request.method == "GET":
        if request.GET.get("buscar"):
            fields = request.GET.get("fields")
            l_area = l_area.filter(nombre__icontains=fields)

    diction = {'l_area': l_area
               }
    return render(request, "entidades/index.html", diction)


@login_required
def trabs(request):
    l_trabs = Trabajador.objects.all()
    if request.method == "GET":
        if request.GET.get("buscar"):
            fields = request.GET.get("fields")
            l_trabs = l_trabs.filter(nombre__icontains=fields)

    diction = {
        'l_trabs': l_trabs, 'cant_trabs': l_trabs.count
    }
    return render(request, "entidades/trabs.html", diction)


@login_required
def trabxarea(request, fid):
    area = Area.objects.get(pk=fid)
    l_trabs = Trabajador.objects.filter(area=area.pk)
    diction = {
        'l_trabs': l_trabs, 'cant_trabs': l_trabs.count
    }
    return render(request, "entidades/trabs.html", diction)


@login_required
def addA(request, fid):
    if request.method == "POST":
        if request.POST.get('save'):
            form = forms.AreaForm(request.POST)
            if form.is_valid():
                clean = form.save(commit=False)
                clean.nombre = request.POST.get("nombre").title()
                clean.save()
            # return redirect("entidades:index")
    form = forms.AreaForm()

    diction = {
        'form': form
    }
    return render(request, "entidades/addA.html", diction)


@login_required
def addT(request, fid):
    data = 0
    if request.method == "POST":
        if request.POST.get('save'):
            form = forms.TrabajadorForm(request.POST)
            if form.is_valid():
                clean = form.save(commit=False)
                clean.nombre = request.POST.get("nombre").title()
                clean.save()
            else:
                print(form.errors)
                messages.error(request, ("Fallo al guardar."))
            # return redirect("entidades:index")
    form = forms.TrabajadorForm(initial={'area': fid})
    diction = {
        'form': form, 'data': data
    }
    return render(request, "entidades/addT.html", diction)


@login_required
def updA(request, fid):
    editing = True
    data = Area.objects.get(id=fid)
    form = forms.AreaForm(instance=data)

    if request.method == "POST":
        if request.POST.get('save'):
            form = forms.AreaForm(request.POST, instance=data)

            if form.is_valid():
                clean = form.save(commit=False)
                clean.nombre = request.POST.get("nombre").title()
                clean.save()
            return redirect("entidades:index")
    diction = {
        'form': form, 'editing': editing
    }
    return render(request, "entidades/addA.html", diction)


@login_required
def updT(request, fid):
    editing = True
    data = Trabajador.objects.get(id=fid)
    form = forms.TrabajadorForm(instance=data)

    if request.method == "POST":
        if request.POST.get('save'):
            form = forms.TrabajadorForm(request.POST, instance=data)

            if form.is_valid():
                clean = form.save(commit=False)
                clean.nombre = request.POST.get("nombre").title()
                clean.save()
            else:
                messages.error(request, ("Fallo al guardar."))
            return redirect("entidades:trabs")
    diction = {
        'form': form, 'data': data, 'editing': editing
    }
    return render(request, "entidades/addT.html", diction)


@login_required
def dele(request, id, ent):
    if ent == 2:
        data = Area.objects.get(id=id)
    elif ent == 3:
        data = Trabajador.objects.get(id=id)
    else:
        return redirect('entidades:index')
    if request.method == "POST":
        if request.POST.get('delete'):
            data.delete()
            if ent == 3:
                return redirect("entidades:trabs")
            return redirect("entidades:index")
    diction = {
        'data': data, 'ent': ent,
    }
    return render(request, "entidades/dele.html", diction)


@login_required
def setHead(request, id, opt):
    worker = Trabajador.objects.get(id=id)
    if opt:
        pass
        # upueb
    else:
        pass
    return redirect('entidades:updT', id)
