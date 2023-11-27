from django.shortcuts import render, redirect
from .models import PrinterOwner, PrinterStack
from .forms import OwnerForm, PrinterForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    items = PrinterOwner.objects.all()

    paginator = Paginator(items, 9)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    diction = {
        "items":page_obj,
    }
    return render(request, "printers/index.html", diction)
    # return render(request, "entidades/trabs.html", diction)

@login_required
def list_printer(request):
    items = PrinterStack.objects.all()
    diction = {
        "items":items,
    }
    return render(request, "printers/list_printer.html", diction)

@login_required
def add_conn(request):
    form = OwnerForm()

    if request.method == "POST":
        if request.POST.get("save"):
            form = OwnerForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, ("Exito"))
                return redirect("printers:index")
            for f in form.errors:
                messages.error(request, (f"Error: {f}"))

    diction={"form":form, "back":1}
    return render(request, "printers/form.html", diction)

@login_required
def upd_conn(request, id):
    item = PrinterOwner.objects.get(pk = id)
    form = OwnerForm(instance=item)

    if request.method == "POST":
        if request.POST.get("save"):
            form = OwnerForm(request.POST, instance=item)
            if form.is_valid():
                form.save()
                messages.success(request, ("Exito"))
                return redirect("printers:index")
            messages.error(request, ("Error"))
    
    diction = {"form":form, "back":1}
    return render(request, "printers/form.html", diction)

@login_required
def del_conn(request, id):
    item = PrinterOwner.objects.get(pk = id)
    if request.method == "POST":
        if request.POST.get("dele"):
            item.delete()
            messages.success(request, ("Exito"))
            return redirect("printers:index")
        
        messages.error(request, ("Error"))
    diction = {
        "item":item, "back":1
    }
    return render(request, "printers/conf.html", diction)



@login_required
def add_printer(request):
    form = PrinterForm()

    if request.method == "POST":
        if request.POST.get("save"):
            form = PrinterForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, ("Exito"))
                return redirect("printers:list_printer")
            for f in form.errors:
                messages.error(request, (f"Error: {f}"))

    diction={"form":form, "back":0}
    return render(request, "printers/form.html", diction)

@login_required
def upd_printer(request, id):
    item = PrinterStack.objects.get(pk = id)
    form = PrinterForm(instance=item)

    if request.method == "POST":
        if request.POST.get("save"):
            form = PrinterForm(request.POST, instance=item)
            if form.is_valid():
                form.save()
                messages.success(request, ("Exito"))
                return redirect("printers:list_printer")
            messages.error(request, ("Error"))
    
    diction = {"form":form, "back":0}
    return render(request, "printers/form.html", diction)
            

@login_required
def del_printer(request, id):
    item = PrinterStack.objects.get(pk = id)
    if request.method == "POST":
        if request.POST.get("dele"):
            item.delete()
            messages.success(request, ("Exito"))
            return redirect("printers:list_printer")
        
        messages.error(request, ("Error"))
    diction = {
        "item":item, "back":0
    }
    return render(request, "printers/conf.html", diction)

