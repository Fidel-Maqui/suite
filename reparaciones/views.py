from django.shortcuts import render, redirect
from entidades.models import Trabajador
from computadoras.models import Computadora
from reparaciones.models import Reparacion
from reparaciones.forms import ReparacionForm
from django.core.paginator import Paginator
from django.db.models import Q #allows advanced query search(Ex: Items.objects.filter(Q(field1=value) | Q(field2=value)))
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    items = Reparacion.objects.all()

    if request.method == "GET":
        if request.GET.get("buscar"):
            fields = request.GET.get("fields")
            comp = Computadora.objects.filter(nombre__icontains = fields, baja = 0)
            tecnico = Trabajador.objects.filter(nombre__icontains = fields)
            if comp and tecnico:
                items = Reparacion.objects.filter(
                    Q(recurso = comp.first()) |
                    Q(sello_1__icontains = fields) |
                    Q(sello_2__icontains = fields) |
                    Q(descripcion__icontains = fields) |
                    Q(modified__icontains = fields) |
                    Q(created__icontains = fields) |
                    Q(tenico = tecnico.first())
                    ).order_by('pk')
            elif tecnico and not comp:
                items = Reparacion.objects.filter(
                    Q(sello_1__icontains = fields) |
                    Q(sello_2__icontains = fields) |
                    Q(descripcion__icontains = fields) |
                    Q(modified__icontains = fields) |
                    Q(created__icontains = fields) |
                    Q(tenico = tecnico.first())
                    ).order_by('pk')
            elif comp and not tecnico:
                items = Reparacion.objects.filter(
                    Q(recurso = comp.first()) |
                    Q(sello_1__icontains = fields) |
                    Q(sello_2__icontains = fields) |
                    Q(descripcion__icontains = fields) |
                    Q(modified__icontains = fields) |
                    Q(created__icontains = fields) 
                    ).order_by('pk')
            else:
                items = Reparacion.objects.filter(
                    Q(sello_1__icontains = fields) |
                    Q(sello_2__icontains = fields) |
                    Q(descripcion__icontains = fields) |
                    Q(modified__icontains = fields) |
                    Q(created__icontains = fields) 
                    ).order_by('pk')

    paginator = Paginator(items, 20)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    diction = {
        "items":page_obj
    }
    return render(request, "reparaciones/index.html", diction)

@login_required
def add(request):
    form = ReparacionForm()
    trabs = Trabajador.objects.filter(cargo__icontains = "inform")
    comps = Computadora.objects.filter(baja = 0)
    
    if request.method == "POST":
        if request.POST.get("save"):
            form = ReparacionForm(request.POST)
            if form.is_valid():
                form.save()
            return redirect("reparaciones:index")
    diction={"form":form, "trabs":trabs, "comps":comps}
    return render(request, "reparaciones/form.html", diction)

@login_required
def reparar(request, id):
    form = ReparacionForm()
    trabs = Trabajador.objects.filter(cargo__icontains = "inform")
    comps = Computadora.objects.filter(pk=id)
    if request.method == "GET":
        if request.GET.get("buscar"):
            comp_name = request.GET.get("comp")
            comps = Computadora.objects.filter(nombre__icontains=comp_name, baja = 0) | Computadora.objects.filter(ip__icontains=comp_name, baja = 0)

    if request.method == "POST":
        if request.POST.get("save"):
            form = ReparacionForm(request.POST)
            if form.is_valid():
                form.save()
            return redirect("reparaciones:index")
    diction={"form":form, "trabs":trabs, "comps":comps}
    return render(request, "reparaciones/form.html", diction)

@login_required
def upd(request, id):
    item = Reparacion.objects.get(pk = id)
    form = ReparacionForm(instance=item)
    trabs = Trabajador.objects.filter(cargo__icontains = "inform")
    comp = Computadora.objects.filter(pk = item.recurso.pk)
    if request.method == "GET":
        if request.GET.get("buscar"):
            comp_name = request.GET.get("comp")
            comp = Computadora.objects.filter(nombre__icontains=comp_name, baja = 0) | Computadora.objects.filter(ip__icontains=comp_name, baja = 0).nombre

    if request.method == "POST":
        if request.POST.get("save"):
            form = ReparacionForm(request.POST, instance=item)
            if form.is_valid():
                form.save()
            return redirect("reparaciones:index")
    diction={"form":form, "trabs":trabs, "comp":comp}
    return render(request, "reparaciones/form.html", diction)

@login_required
def dele(request, id):
    item = Reparacion.objects.get(pk = id)

    if request.method == "POST":
        if request.POST.get("dele"):
            item.delete()
            return redirect("reparaciones:index")
    diction={"item":item}
    return render(request, "reparaciones/conf.html", diction)
