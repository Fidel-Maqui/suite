from django import forms
from extras import models

class BancoForm(forms.ModelForm):
    class Meta:
        model = models.Banco
        fields = "__all__"
        widgets = {
            'responsable': forms.Select(attrs={'class':'form-select'}),
            'description': forms.Textarea(attrs={'class':'form-control'}),
        }