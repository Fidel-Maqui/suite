from django import forms
from computadoras.models import Computadora, Hardware, Periferico, Softwares, Programs

class ComputadoraForm(forms.ModelForm):
    class Meta:
        model = Computadora
        fields = '__all__'
        widgets = {
            'responsable': forms.Select(attrs={'class':'form-select', 'hidden':True}),
            'nombre': forms.TextInput(attrs={'class':'form-control', 'autofocus':True}),
            'ip': forms.TextInput(attrs={'class':'form-control'}),
            'num_de_inventario': forms.TextInput(attrs={'class':'form-control'}),
            'sello_1': forms.TextInput(attrs={'class':'form-control'}),
            'sello_2': forms.TextInput(attrs={'class':'form-control'}),
            'baja': forms.CheckboxInput(attrs={'class':'form-check-input'}),
        }

class HardwareForm(forms.ModelForm):
    class Meta:
        model = Hardware
        fields = '__all__'
        widgets = {
            'computadora': forms.Select(attrs={'class':'form-select'}),
            'nombre': forms.Select(attrs={'class':'form-select'}),
            'fabricante': forms.TextInput(attrs={'class':'form-control'}),
            'modelo': forms.TextInput(attrs={'class':'form-control'}),
            'capacidad_gb': forms.TextInput(attrs={'class':'form-control'}),
            'velocidad': forms.TextInput(attrs={'class':'form-control'}),
            'num_de_serie': forms.TextInput(attrs={'class':'form-control'}),
            'baja': forms.CheckboxInput(attrs={'class':'form-check-input'}),

        }

class PerifericoForm(forms.ModelForm):
    class Meta:
        model = Periferico
        fields = '__all__'
        widgets = {
            'computadora': forms.Select(attrs={'class':'form-select'}),
            'nombre': forms.Select(attrs={'class':'form-select'}),
            'fabricante': forms.TextInput(attrs={'class':'form-control'}),
            'modelo': forms.TextInput(attrs={'class':'form-control'}),
            'num_inventario': forms.TextInput(attrs={'class':'form-control'}),
            'num_de_serie': forms.TextInput(attrs={'class':'form-control'}),
            'baja': forms.CheckboxInput(attrs={'class':'form-check-input'}),

        }

class SoftwaresForm(forms.ModelForm):
    class Meta:
        model = Softwares
        fields = '__all__'
        widgets = {
            'computadora': forms.Select(attrs={'class':'form-select'}),
            'nombre': forms.Select(attrs={'class':'form-select'}),
        }
        
class ProgramsForm(forms.ModelForm):
    class Meta:
        model = Programs
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
        }
        