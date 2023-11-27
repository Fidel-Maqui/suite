from django import forms
from entidades.models import Area, Trabajador


class AreaForm(forms.ModelForm):

    class Meta:
        model = Area
        fields = "__all__"
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'title': 'Nombre de la área'}),
        }


class TrabajadorForm(forms.ModelForm):

    class Meta:
        model = Trabajador
        fields = "__all__"
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'title': 'Nombre del trabajador'}),
            'cargo': forms.TextInput(attrs={'class': 'form-control', 'title': 'Cargo del trabajador'}),
            'area': forms.Select(attrs={'class': 'form-select', 'title': 'Area del trabajador'}),
        }
