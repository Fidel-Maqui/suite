from django.shortcuts import render, redirect
from entidades.models import Area, Trabajador
from .models import Computadora, Hardware, Periferico, Diferencias, Softwares, Programs
from . import forms
import os
import bs4
import lxml
from django.contrib import messages
from computadoras import extractor as ext
from django.contrib.auth.decorators import login_required
# allows advanced query search(Ex: Items.objects.filter(Q(field1=value) | Q(field2=value)))
from django.db.models import Q
from django.http import HttpResponse
# Create your views here.

path_to_files = r".\static\computadoras\files"  # windows
# path_to_files = ".\computadoras\static\computadoras\\files"     #windows
# path_to_files = "/projectpy/suite/static/computadoras/files"  #linux


def get_possible_resp(pista):
    if pista == "":
        return None

    trabs = Trabajador.objects.all()
    posT = trabs.filter(nombre__icontains=pista)
    if posT:
        return trabs.get(pk=posT[0].pk)
    else:
        return None


def crear_new_comp(req, obj_resp: Computadora, nombre_compu: str, ip: str):
    comps = Computadora.objects.filter(baja=0)
    new_comp = comps.create(
        responsable=obj_resp,
        nombre=nombre_compu,
        ip=ip,
    )
    return new_comp


def index(request):
    comps = Computadora.objects.filter(baja=0).order_by('-cambios', 'nombre')

    if request.method == "GET":
        if request.GET.get("buscar"):
            fields = request.GET.get("fields")
            user = Trabajador.objects.filter(nombre__icontains=fields)
            if user:
                comps = Computadora.objects.filter(
                    Q(responsable=user.first()) |
                    Q(nombre__icontains=fields) |
                    Q(ip__icontains=fields) |
                    Q(num_de_inventario__icontains=fields)
                    # Q(baja = 0)
                ).order_by('nombre')
            else:
                comps = Computadora.objects.filter(
                    Q(nombre__icontains=fields) |
                    Q(ip__icontains=fields) |
                    Q(num_de_inventario__icontains=fields)
                    # Q(baja = 0)
                ).order_by('nombre')

    diction = {'comps': comps}
    return render(request, "computadoras/index.html", diction)


@login_required
def scan(request):
    comps = Computadora.objects.filter(baja=0)
    hards = Hardware.objects.filter(baja=0)
    peris = Periferico.objects.all()
    # progs = Softwares.objects.all()
    difs = Diferencias.objects.all()

    # path_to_files = ".\computadoras\static\computadoras\\files"     #windows
    # path_to_files = "/projectpy/suite/static/computadoras/files"  #linux
    if not os.path.exists(path_to_files):
        messages.error(
            request, ("La carpeta de origen de archivos no existe."))
        return redirect("computadoras:index")
    list_of_files = os.listdir(path_to_files)

    if len(list_of_files) == 0:
        messages.success(request, ("No hay archivos que escanear"))
        return redirect('computadoras:index')
    new_lista = []
    del_lista = []
    list_of_files.sort()
    list_of_files.reverse()
    new_lista.append(list_of_files[0])
    for i in range(1, len(list_of_files)):
        if list_of_files[i].split('-')[0] != new_lista[-1].split('-')[0]:
            new_lista.append(list_of_files[i])
        else:
            del_lista.append(list_of_files[i])

    new_comps_cant = 0
    for i in new_lista:
        src = os.path.join(path_to_files, i)

        if not os.stat(src).st_size:
            print("archivo vacio", i.split('-')[0])
            continue

        with open(src, 'r', encoding="utf-8") as f:
            file = f.read()

        dom = bs4.BeautifulSoup(file, features='xml')
        nombre_compu = dom.HARDWARE.NAME.getText()
        nombre_user = dom.HARDWARE.USERID.getText()

        existe_comp = comps.filter(nombre=nombre_compu)
        if existe_comp:
            # veo si hay diferencias, si hay lo guardo en una tabla para mostrarlo luego, sino nada
            existing_comp = comps.get(nombre=nombre_compu)
            if existing_comp.ip != ext.get_ip(dom):
                ext.crear_diferencia(existing_comp, "IP", ext.get_ip(dom))
            # compruebo hardware
            existing_hard = hards.filter(computadora=existing_comp)
            # storage
            ext.check_storage(existing_comp, existing_hard, dom)
            # ram
            ext.check_ram(existing_comp, existing_hard, dom)
            # cpu
            ext.check_cpu(existing_comp, existing_hard, dom)
            # board
            ext.check_board(existing_comp, existing_hard, dom)

            # compruebo perifericos
            existing_peri = peris.filter(computadora=existing_comp)
            # # monitor
            ext.check_monitor(existing_comp, existing_peri, dom)
            # teclado
            ext.check_teclado(existing_comp, existing_peri, dom)
            # # mouse #ok
            ext.check_mouse(existing_comp, existing_peri, dom)

        else:
            # creo la computadora
            # new_comp = 0 #ver si no hace falta
            try:
                new_comp = crear_new_comp(request, get_possible_resp(
                    nombre_user), nombre_compu, ext.get_ip(dom))
            except:
                # print(f"Error al crear la computadora {nombre_compu}")
                new_comp = None
            else:
                new_comps_cant += 1
            if new_comp:
                # creo hardware
                ext.create_storages(request, dom, new_comp)
                ext.create_ram(request, dom, new_comp)
                ext.create_cpu(request, dom, new_comp)
                ext.create_board(request, dom, new_comp)
                # creo perifericos
                ext.create_teclados(request, dom, new_comp)
                ext.create_mouse(request, dom, new_comp)
                ext.create_monitors(request, dom, new_comp)
                ext.create_progs(request, dom, new_comp)

    #     try:
    #         os.remove(src)
    #     except:
    #         print("fallo al borrar", i)
    # del_lista = os.listdir(path_to_files)
    print("del_lista:", len(del_lista))

    for fi in del_lista:
        src = os.path.join(path_to_files, fi)
        # src = path_to_files+"\\"+fi
        try:
            os.remove(src)
        except:
            print("fallo al borrar:", fi)

    if new_comps_cant == 1:
        messages.success(request, (f"Se agregó {nombre_compu}"))
    if new_comps_cant > 1:
        messages.success(
            request, (f"Se agregaron {new_comps_cant} computadoras nuevas"))
    if new_comps_cant == 0:
        messages.success(request, (f"No se agregaron computadoras nuevas"))
    # si se crearon diferencias para esta comp cambio el
    # atributo cambio en comp para señalar q si tiene cambios
    for c in comps:
        cant_difs = difs.filter(computadora=c)
        if cant_difs.count() > 0:
            c.cambios = True
            c.save()
        else:
            if c.cambios:
                c.cambios = False
                c.save()
    return redirect('computadoras:index')


@login_required
def verC(request, fid):
    comps = Computadora.objects.filter(responsable=fid, baja=0)
    if len(comps) == 0:
        return redirect("computadoras:addC", fid)
    diction = {'comps': comps}
    return render(request, "computadoras/index.html", diction)


@login_required
def verC_area(request, fid):
    areas = Area.objects.get(pk=fid)
    trabs = Trabajador.objects.filter(area=areas)
    comps = Computadora.objects.filter(responsable__in=trabs, baja=0)

    diction = {'comps': comps}
    return render(request, "computadoras/index.html", diction)


@login_required
def addC(request, fid):
    form = forms.ComputadoraForm(initial={'responsable': fid})
    if request.method == "POST":
        if request.POST.get('save'):
            form = forms.ComputadoraForm(request.POST)
            if form.is_valid():
                clean = form.save(commit=False)
                clean.nombre = request.POST.get("nombre").title()
                clean.save()
                return redirect("computadoras:verC", fid)  # fix
            else:
                for i in form.errors:
                    messages.error(request, (i))

    diction = {
        'form': form
    }
    return render(request, "computadoras/addC.html", diction)


@login_required
def add_hard(request, c):
    form = forms.HardwareForm(initial={'computadora': c})
    if request.method == "POST":
        if request.POST.get('upd'):
            form = forms.HardwareForm(request.POST)
            if form.is_valid():
                clean = form.save(commit=False)
                clean.nombre = request.POST.get("nombre").title()
                clean.save()
                return redirect("computadoras:detalles", c)  # fix

    diction = {
        'form': form, 'c': c
    }
    return render(request, "computadoras/upd_hard.html", diction)


@login_required
def add_peri(request, c):
    form = forms.PerifericoForm(initial={'computadora': c})
    if request.method == "POST":
        if request.POST.get('upd'):
            form = forms.PerifericoForm(request.POST)
            if form.is_valid():
                clean = form.save(commit=False)
                clean.nombre = request.POST.get("nombre").title()
                clean.save()
                return redirect("computadoras:detalles", c)  # fix

    diction = {
        'form': form, 'c': c
    }
    return render(request, "computadoras/upd_hard.html", diction)


@login_required
def add_prog(request, c):
    form = forms.SoftwaresForm(initial={'computadora': c})
    if request.method == "POST":
        if request.POST.get('upd'):
            form = forms.SoftwaresForm(request.POST)
            if form.is_valid():
                clean = form.save(commit=False)
                clean.nombre = request.POST.get("nombre").title()
                clean.save()
                return redirect("computadoras:detalles", c)  # fix

    diction = {
        'form': form, 'c': c
    }
    return render(request, "computadoras/upd_prog.html", diction)


@login_required
def detalles(request, id):
    comp = Computadora.objects.get(id=id)
    hard = Hardware.objects.filter(computadora=id)
    peri = Periferico.objects.filter(computadora=id)
    prog = Softwares.objects.filter(computadora=id)
    difs = Diferencias.objects.filter(computadora=comp)
    diction = {'comp': comp, 'id': id, 'hard': hard,
               'peri': peri, 'prog': prog, 'difs': difs}
    return render(request, "computadoras/detalles.html", diction)


@login_required
def upd_comp(request, id):
    comp = Computadora.objects.get(id=id)
    trabs = Trabajador.objects.all()
    form = forms.ComputadoraForm(instance=comp)
    if request.method == 'POST':
        if request.POST.get('upd'):
            form = forms.ComputadoraForm(request.POST, instance=comp)
            if form.is_valid():
                form.save()

                messages.success(request, ("Exito"))
                return redirect("computadoras:detalles", id)
            else:
                messages.error(request, ("Error"))
                for i in form.errors:
                    messages.error(request, (i))

    diction = {'comp': comp, 'form': form, 'trabs': trabs}
    return render(request, "computadoras/upd_comp.html", diction)


@login_required
def ping(request, ip):
    response = os.popen(f"ping {ip} ").read()
    response = response.splitlines()[-1]
    if ("100") in response or "perdidos" in response:
        return HttpResponse("No Conectado")
    else:
        return HttpResponse("Conectado")


@login_required
def delc(request, id, ent):
    # comp
    if ent == 1:
        data = Computadora.objects.get(id=id)
    # hard
    elif ent == 2:
        data = Hardware.objects.get(id=id)
    # peri
    elif ent == 3:
        data = Periferico.objects.get(id=id)
    # prog
    elif ent == 4:
        data = Softwares.objects.get(id=id)
    else:
        return redirect('computadoras:index')
    if request.method == "POST":
        if request.POST.get('delete'):
            if ent == 1:
                data.delete()
                return redirect("computadoras:index")
            back_id = data.computadora.id
            data.delete()
            return redirect("computadoras:detalles", back_id)
    diction = {
        'data': data, 'ent': ent,
    }
    return render(request, "computadoras/dele.html", diction)


@login_required
def upd_hard(request, id, c):
    comp = Hardware.objects.get(id=id)
    form = forms.HardwareForm(instance=comp)
    if request.method == 'POST':
        if request.POST.get('upd'):
            form = forms.HardwareForm(request.POST, instance=comp)
            if form.is_valid():
                form.save()

                messages.success(request, ("Exito"))
                return redirect("computadoras:detalles", c)
            else:
                messages.error(request, ("Error"))
                for i in form.errors:
                    messages.error(request, (i))
        if request.POST.get('dele'):
            comp.delete()
            messages.success(request, ("Eliminado"))
            return redirect("computadoras:detalles", c)

    diction = {'comp': comp, 'form': form, 'c': c, 'editing': True}
    return render(request, "computadoras/upd_hard.html", diction)


@login_required
def upd_peri(request, id, c):
    comp = Periferico.objects.get(id=id)
    form = forms.PerifericoForm(instance=comp)
    if request.method == 'POST':
        if request.POST.get('upd'):
            form = forms.PerifericoForm(request.POST, instance=comp)
            if form.is_valid():
                form.save()

                messages.success(request, ("Exito"))
                return redirect("computadoras:detalles", c)
            else:
                messages.error(request, ("Error"))
                for i in form.errors:
                    messages.error(request, (i))
        if request.POST.get('dele'):
            comp.delete()
            messages.success(request, ("Eliminado"))
            return redirect("computadoras:detalles", c)

    diction = {'comp': comp, 'form': form,
               'c': c, 'editing': True, 'peri': True}
    return render(request, "computadoras/upd_hard.html", diction)


@login_required
def upd_prog(request, id, c):
    comp = Softwares.objects.get(id=id)
    form = forms.SoftwaresForm(instance=comp)
    if request.method == 'POST':
        if request.POST.get('upd'):
            form = forms.SoftwaresForm(request.POST, instance=comp)
            if form.is_valid():
                form.save()

                messages.success(request, ("Exito"))
                return redirect("computadoras:detalles", c)
            else:
                messages.error(request, ("Error"))
                for i in form.errors:
                    messages.error(request, (i))
        # if request.POST.get('dele'):
        #     comp.delete()
        #     messages.success(request, ("Eliminado"))
        #     return redirect("computadoras:detalles", c)

    diction = {'comp': comp, 'form': form, 'c': c, 'editing': True}
    return render(request, "computadoras/upd_prog.html", diction)


@login_required
def del_all_difs(request, comp):
    item = Computadora.objects.get(pk=comp)
    difs = Diferencias.objects.filter(computadora=item)
    for i in difs:
        i.delete()
    messages.success(request, ("Cambios eliminados."))
    return redirect("computadoras:detalles", comp)


@login_required
def del_dif(request, id):
    dif = Diferencias.objects.get(pk=id)
    comp = Computadora.objects.get(nombre=dif.computadora)
    dif.delete()
    messages.success(request, ("Cambio eliminado."))
    return redirect("computadoras:detalles", comp.pk)


@login_required
def programas(request):
    progs = Programs.objects.all()
    softs = Softwares.objects.all().order_by('-computadora')
    diction = {"progs": progs, "softs": softs}
    return render(request, "computadoras/programas.html", diction)


@login_required
def scan_prog(request):
    if not os.path.exists(path_to_files):
        messages.error(
            request, ("La carpeta de origen de archivos no existe."))
        return redirect("computadoras:programas")
    list_of_files = os.listdir(path_to_files)

    if len(list_of_files) == 0:
        messages.success(request, ("No hay archivos que escanear"))
        return redirect('computadoras:programas')
    new_lista = []
    list_of_files.sort()
    list_of_files.reverse()
    new_lista.append(list_of_files[0])
    for i in range(1, len(list_of_files)):
        if list_of_files[i].split('-')[0] != new_lista[-1].split('-')[0]:
            new_lista.append(list_of_files[i])

    comps = Computadora.objects.all()
    for i in new_lista:
        src = os.path.join(path_to_files, i)

        if not os.stat(src).st_size:
            print("archivo vacio", i.split('-')[0])
            continue

        with open(src, 'r', encoding="utf-8") as f:
            file = f.read()

        dom = bs4.BeautifulSoup(file, features='xml')
        nombre_compu = dom.HARDWARE.NAME.getText()
        comp = comps.filter(nombre=nombre_compu)
        if comp:
            ext.create_progs(request, dom, comp.first())

        try:
            os.remove(src)
        except:
            print("fallo al borrar", i)
    del_lista = os.listdir(path_to_files)
    print("del_lista:", len(del_lista))

    for fi in del_lista:
        src = os.path.join(path_to_files, fi)
        try:
            os.remove(src)
        except:
            print("fallo al borrar:", fi)

    progs = Programs.objects.all()
    softs = Softwares.objects.all()
    diction = {"progs": progs, "softs": softs}
    return render(request, "computadoras/programas.html", diction)


@login_required
def form_prog(request):
    progs = Programs.objects.all()
    form = forms.ProgramsForm()
    if request.method == 'POST':
        if request.POST.get('save'):
            form = forms.ProgramsForm(request.POST)
            if form.is_valid():
                form.save()

                messages.success(request, ("Exito"))
            else:
                messages.error(request, ("Error"))
    diction = {'form': form, "progs": progs, 'editing': False}
    return render(request, "computadoras/form_prog.html", diction)


@login_required
def upd_soft(request, id):
    progs = Programs.objects.all()
    prog = Programs.objects.get(pk=id)
    form = forms.ProgramsForm(instance=prog)
    if request.method == 'POST':
        if request.POST.get('upd'):
            form = forms.ProgramsForm(request.POST, instance=prog)
            if form.is_valid():
                form.save()

                messages.success(request, ("Exito"))
                return redirect("computadoras:form_prog")
            else:
                messages.error(request, ("Error"))
        if request.POST.get('dele'):
            prog.delete()
    diction = {'form': form, "progs": progs, 'editing': True}
    return render(request, "computadoras/form_prog.html", diction)
