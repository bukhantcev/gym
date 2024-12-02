from django import forms
from .models import Upragneniya, Groups


class UpragForm(forms.ModelForm):

    class Meta:
        model = Upragneniya
        fields = ('__all__')


