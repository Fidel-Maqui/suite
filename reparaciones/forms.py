from django import forms
from reparaciones.models import Reparacion

class ReparacionForm(forms.ModelForm):
    class Meta:
        model = Reparacion
        fields = "__all__"
        widgets = {
            "recurso": forms.Select(attrs={"class":"form-select", "title":"recurso"}),
            "sello_1": forms.TextInput(attrs={"class":"form-control", "title":"sello_1"}),
            "sello_2": forms.TextInput(attrs={"class":"form-control", "title":"sello_2"}),
            "tenico": forms.Select(attrs={"class":"form-select", "title":"tenico"}),
            "descripcion": forms.Textarea(attrs={"class":"form-control", "title":"descripcion", "rows":4}),
            "modified": forms.TextInput(attrs={"class":"form-control", "title":"modified"}),
            "created": forms.TextInput(attrs={"class":"form-control", "title":"created"}),
        }