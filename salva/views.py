from django.shortcuts import render, redirect
from salva import models as sal_models
from entidades import models as ent_models
from computadoras import models as comp_models
from django.contrib import messages

# Create your views here.


def index(request):
    Area = ent_models.Area.objects.order_by('id')
    Trabajador = ent_models.Trabajador.objects.order_by('id')
    Computadora = comp_models.Computadora.objects.order_by('id')
    Hardware = comp_models.Hardware.objects.order_by('id')
    Periferico = comp_models.Periferico.objects.order_by('id')
    Diferencias = comp_models.Diferencias.objects.order_by('id')
    Programs = comp_models.Programs.objects.order_by('id')
    Softwares = comp_models.Softwares.objects.order_by('id')

    S_Area = sal_models.SArea.objects.order_by('id')
    S_Trabajador = sal_models.STrabajador.objects.order_by('id')
    S_Computadora = sal_models.SComputadora.objects.order_by('id')
    S_Hardware = sal_models.SHardware.objects.order_by('id')
    S_Periferico = sal_models.SPeriferico.objects.order_by('id')
    S_Diferencias = sal_models.SDiferencias.objects.order_by('id')
    S_Programs = sal_models.SPrograms.objects.order_by('id')
    S_Softwares = sal_models.SSoftwares.objects.order_by('id')
    diction = {'Area': Area, 'Trabajador': Trabajador, 'Computadora': Computadora, 'Hardware': Hardware,
               'Periferico': Periferico, 'Diferencias': Diferencias, 'Programs': Programs, 'Softwares': Softwares,
               'S_Area': S_Area, 'S_Trabajador': S_Trabajador, 'S_Computadora': S_Computadora, 'S_Hardware': S_Hardware,
               'S_Periferico': S_Periferico, 'S_Diferencias': S_Diferencias, 'S_Programs': S_Programs, 'S_Softwares': S_Softwares,
               }
    return render(request, 'salva/index.html', diction)


def save_area(request):
    Area = ent_models.Area.objects.order_by('id')
    S_Area = sal_models.SArea.objects.order_by('id')
    for i in Area:
        try:
            S_Area.create(
                id=i.pk,
                nombre=i.nombre,
            )
        except Exception as e:
            print(f"failed to create {i.nombre} because of {e}")
        else:
            print(f"success to create {i.nombre}")

    return redirect('salva:index')


def save_trabs(request):
    srce = ent_models.Trabajador.objects.order_by('id')
    dest = sal_models.STrabajador.objects.order_by('id')

    for i in srce:
        try:
            dest.create(
                id=i.pk,
                nombre=i.nombre,
                cargo=i.cargo,
                area=i.area,
            )
        except Exception as e:
            if i.area:
                area = sal_models.SArea.objects.get(id=i.area.pk)
                try:
                    dest.create(
                        id=i.pk,
                        nombre=i.nombre,
                        cargo=i.cargo,
                        area=area,
                    )
                except Exception as e:
                    print(f"failed to create sarea {i.nombre} because of {e}")
            print(f"failed to create {i.nombre} because of {e}")
            print(".")
        else:
            print(f"success to create {i.nombre}")

    return redirect('salva:index')


def save_comp(request):
    srce = comp_models.Computadora.objects.order_by('id')
    dest = sal_models.SComputadora.objects.order_by('id')

    for i in srce:
        if i.responsable:
            item = sal_models.STrabajador.objects.get(id=i.responsable.pk)
            try:
                dest.create(
                    id=i.pk,
                    responsable=item,
                    nombre=i.nombre,
                    ip=i.ip,
                    num_de_inventario=i.num_de_inventario,
                    sello_1=i.sello_1,
                    sello_2=i.sello_2,
                    cambios=i.cambios,
                    baja=i.baja,
                )
            except Exception as e:
                print(f"failed to create {i.nombre} because of {e}")
            # else:
            #     print(f"success to create {i.nombre}")
        else:
            try:
                dest.create(
                    id=i.pk,
                    responsable=i.responsable,
                    nombre=i.nombre,
                    ip=i.ip,
                    num_de_inventario=i.num_de_inventario,
                    sello_1=i.sello_1,
                    sello_2=i.sello_2,
                    cambios=i.cambios,
                    baja=i.baja,
                )
            except Exception as e:
                print(f"failed to create {i.nombre} because of {e}")
            # else:
            #     print(f"success to create {i.nombre}")

    return redirect('salva:index')


def save_hard(request):
    srce = comp_models.Hardware.objects.order_by('id')
    dest = sal_models.SHardware.objects.order_by('id')

    for i in srce:
        if i.computadora:
            item = sal_models.SComputadora.objects.get(id=i.computadora.pk)
            try:
                dest.create(
                    id=i.pk,
                    computadora=item,
                    nombre=i.nombre,
                    fabricante=i.fabricante,
                    modelo=i.modelo,
                    capacidad_gb=i.capacidad_gb,
                    velocidad=i.velocidad,
                    num_de_serie=i.num_de_serie,
                    baja=i.baja,
                )
            except Exception as e:
                print(f"failed to create {i.nombre} because of {e}")
            # else:
            #     print(f"success to create {i.nombre}")
        else:
            try:
                dest.create(
                    id=i.pk,
                    computadora=i.computadora,
                    nombre=i.nombre,
                    fabricante=i.fabricante,
                    modelo=i.modelo,
                    capacidad_gb=i.capacidad_gb,
                    velocidad=i.velocidad,
                    num_de_serie=i.num_de_serie,
                    baja=i.baja,
                )
            except Exception as e:
                print(f"failed to create {i.nombre} because of {e}")
            # else:
            #     print(f"success to create {i.nombre}")

    return redirect('salva:index')


def save_peri(request):
    srce = comp_models.Periferico.objects.order_by('id')
    dest = sal_models.SPeriferico.objects.order_by('id')

    for i in srce:
        if i.computadora:
            item = sal_models.SComputadora.objects.get(id=i.computadora.pk)
            try:
                dest.create(
                    id=i.pk,
                    computadora=item,
                    nombre=i.nombre,
                    fabricante=i.fabricante,
                    modelo=i.modelo,
                    num_inventario=i.num_inventario,
                    num_de_serie=i.num_de_serie,
                    baja=i.baja,
                )
            except Exception as e:
                print(f"failed to create {i.nombre} because of {e}")
            # else:
            #     print(f"success to create {i.nombre}")
        else:
            try:
                dest.create(
                    id=i.pk,
                    computadora=i.computadora,
                    nombre=i.nombre,
                    fabricante=i.fabricante,
                    modelo=i.modelo,
                    num_inventario=i.num_inventario,
                    num_de_serie=i.num_de_serie,
                    baja=i.baja,
                )
            except Exception as e:
                print(f"failed to create {i.nombre} because of {e}")
            # else:
            #     print(f"success to create {i.nombre}")

    return redirect('salva:index')


def save_dife(request):
    srce = comp_models.Diferencias.objects.order_by('id')
    dest = sal_models.SDiferencias.objects.order_by('id')

    for i in srce:
        try:
            item = sal_models.SComputadora.objects.get(
                nombre=i.computadora)
        except Exception as e:
            print(f"couldn't find {i.computadora} because of {e}")
        else:
            try:
                dest.create(
                    id=i.pk,
                    computadora=item,
                    campo=i.campo,
                    cambio=i.cambio,
                    fecha=i.fecha,
                )
            except Exception as e:
                print(
                    f"failed to create {i.computadora.nombre} because of {e}")
    return redirect('salva:index')


def save_prog(request):
    srce = comp_models.Programs.objects.order_by('id')
    dest = sal_models.SPrograms.objects.order_by('id')

    for i in srce:
        try:
            dest.create(
                id=i.pk,
                nombre=i.nombre,
            )
        except Exception as e:
            print(f"failed to create {i.nombre} because of {e}")
    return redirect('salva:index')


def save_soft(request):
    srce = comp_models.Softwares.objects.order_by('id')
    dest = sal_models.SSoftwares.objects.order_by('id')
    for i in srce:
        comp = i.computadora
        prog = i.nombre
        if i.computadora:
            try:
                comp = sal_models.SComputadora.objects.get(id=i.computadora.pk)
            except:
                comp = i.computadora
        if i.nombre:
            try:
                prog = sal_models.SPrograms.objects.get(id=i.nombre.pk)
            except:
                prog = i.nombre
        try:
            dest.create(
                id=i.pk,
                computadora=comp,
                nombre=prog,
            )
        except Exception as e:
            print(f"failed to create {i.nombre} because of {e}")
    return redirect('salva:index')


def rest_area(request):
    dest = ent_models.Area.objects.order_by('id')
    srce = sal_models.SArea.objects.order_by('id')
    for i in srce:
        try:
            dest.create(
                id=i.pk,
                nombre=i.nombre,
            )
        except Exception as e:
            print(f"failed to create {i.nombre} because of {e}")
    return redirect('salva:index')


def rest_trabs(request):
    srce = sal_models.STrabajador.objects.order_by('id')
    dest = ent_models.Trabajador.objects.order_by('id')

    for i in srce:
        item = i.area
        print(item)
        if i.area:
            try:
                item = ent_models.Area.objects.get(id=i.area.pk)
            except:
                item = i.area
        try:
            dest.create(
                id=i.pk,
                nombre=i.nombre,
                cargo=i.cargo,
                area=item
            )
        except Exception as e:
            print(f"failed to create {i.nombre} because of {e}")
    return redirect('salva:index')


def rest_comp(request):
    srce = sal_models.SComputadora.objects.order_by('id')
    dest = comp_models.Computadora.objects.order_by('id')

    for i in srce:
        item = i.responsable
        if i.responsable:
            try:
                item = ent_models.Trabajador.objects.get(id=i.responsable.pk)
            except:
                item = i.responsable
        try:
            dest.create(
                id=i.pk,
                responsable=item,
                nombre=i.nombre,
                ip=i.ip,
                num_de_inventario=i.num_de_inventario,
                sello_1=i.sello_1,
                sello_2=i.sello_2,
                cambios=i.cambios,
                baja=i.baja,
            )
        except Exception as e:
            print(f"failed to create {i.nombre} because of {e}")
    return redirect('salva:index')


def rest_hard(request):
    srce = sal_models.SHardware.objects.order_by('id')
    dest = comp_models.Hardware.objects.order_by('id')

    for i in srce:
        item = i.computadora
        if i.computadora:
            try:
                item = comp_models.Computadora.objects.get(id=i.computadora.pk)
            except:
                item = i.computadora
        try:
            dest.create(
                id=i.pk,
                computadora=item,
                nombre=i.nombre,
                fabricante=i.fabricante,
                modelo=i.modelo,
                capacidad_gb=i.capacidad_gb,
                velocidad=i.velocidad,
                num_de_serie=i.num_de_serie,
                baja=i.baja,
            )
        except Exception as e:
            print(f"failed to create {i.nombre} because of {e}")
    return redirect('salva:index')


def rest_peri(request):
    srce = sal_models.SPeriferico.objects.order_by('id')
    dest = comp_models.Periferico.objects.order_by('id')

    for i in srce:
        item = i.computadora
        if i.computadora:
            try:
                item = comp_models.Computadora.objects.get(id=i.computadora.pk)
            except:
                item = i.computadora
        try:
            dest.create(
                id=i.pk,
                computadora=item,
                nombre=i.nombre,
                fabricante=i.fabricante,
                modelo=i.modelo,
                num_inventario=i.num_inventario,
                num_de_serie=i.num_de_serie,
                baja=i.baja,
            )
        except Exception as e:
            print(f"failed to create {i.nombre} because of {e}")
    return redirect('salva:index')


def rest_dife(request):
    srce = sal_models.SDiferencias.objects.order_by('id')
    dest = comp_models.Diferencias.objects.order_by('id')

    for i in srce:
        item = i.computadora
        if i.computadora:
            try:
                item = comp_models.Computadora.objects.get(id=i.computadora.pk)
            except:
                item = i.computadora
        try:
            dest.create(
                id=i.pk,
                computadora=item,
                campo=i.campo,
                cambio=i.cambio,
                fecha=i.fecha,
            )
        except Exception as e:
            print(
                f"failed to create {i.computadora.nombre} because of {e}")
    return redirect('salva:index')


def rest_prog(request):
    srce = sal_models.SPrograms.objects.order_by('id')
    dest = comp_models.Programs.objects.order_by('id')

    for i in srce:
        try:
            dest.create(
                id=i.pk,
                nombre=i.nombre,
            )
        except Exception as e:
            print(f"failed to create {i.nombre} because of {e}")
    return redirect('salva:index')


def rest_soft(request):
    srce = sal_models.SSoftwares.objects.order_by('id')
    dest = comp_models.Softwares.objects.order_by('id')
    for i in srce:
        comp = i.computadora
        prog = i.nombre
        if i.computadora:
            try:
                comp = comp_models.Computadora.objects.get(id=i.computadora.pk)
            except:
                comp = i.computadora
        if i.nombre:
            try:
                prog = comp_models.Programs.objects.get(id=i.nombre.pk)
            except:
                prog = i.nombre
        try:
            dest.create(
                id=i.pk,
                computadora=comp,
                nombre=prog,
            )
        except Exception as e:
            print(f"failed to create {i.nombre} because of {e}")
            messages.error(request, (e))
    return redirect('salva:index')
