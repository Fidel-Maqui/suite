from django import forms
from .models import PrinterOwner, PrinterStack
class PrinterForm(forms.ModelForm):
    class Meta:
        model = PrinterStack
        fields = "__all__"
        widgets = {
            'nombre' : forms.TextInput(attrs={"class":"form-control", "title":"Nombre"}),
            'toner' : forms.TextInput(attrs={"class":"form-control", "title":"Toner"}),
        }

class OwnerForm(forms.ModelForm):
    class Meta:
        model = PrinterOwner
        fields = "__all__"
        widgets = {
            'owner' : forms.Select(attrs={"class":"form-select", "title":"Responsable"}),
            'printer' : forms.Select(attrs={"class":"form-select", "title":"Impresora"}),
            'inv' : forms.TextInput(attrs={"class":"form-control", "title":"# de inv"}),
            'serial' : forms.TextInput(attrs={"class":"form-control", "title":"# de serie"}),
        }
