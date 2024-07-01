from django import forms
from django.forms import ModelForm
from .models import *

class SiswaForm(ModelForm):

    class Meta:
        model = Siswa
        fields = '__all__'
        widgets = {
            'no': forms.TextInput(attrs={'class': 'form-control'}),
            'makanan': forms.TextInput(attrs={'class': 'form-control'}),
            'minuman': forms.TextInput(attrs={'class': 'form-control'}),
        }
        