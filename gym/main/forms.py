from django import forms
from .models import Upragneniya, Groups, Trenirovka


class UpragForm(forms.ModelForm):

    class Meta:
        model = Upragneniya
        fields = ('__all__')



class TrenForm(forms.ModelForm):

    class Meta:
        model = Trenirovka
        fields = ('name', 'group', 'max_weight', 'amount1', 'povtor1', 'amount2', 'povtor2', 'level',)
        widgets = {
            'name': forms.Select(attrs={'class': 'form-control', 'id': 'vdszv'}),
            'group': forms.Select(attrs={'class': 'form-control'}),
            'max_weight': forms.TextInput(attrs={'class': 'form-control'}),
            'amount1': forms.NumberInput(attrs={'class': 'form-control'}),
            'amount2': forms.NumberInput(attrs={'class': 'form-control'}),
            'povtor1': forms.NumberInput(attrs={'class': 'form-control'}),
            'povtor2': forms.NumberInput(attrs={'class': 'form-control'}),
            'level': forms.Select(attrs={'class': 'form-control'}),

        }
