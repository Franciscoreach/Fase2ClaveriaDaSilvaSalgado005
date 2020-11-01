from django import forms

from . models import Entrada

class EntradaForm(forms.ModelForm):
    titulo = forms.CharField(label='Titulo',max_length=100, widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))
    tema = forms.CharField(label='Descripción', max_length=5000, widget=forms.Textarea(
        attrs={
            'class':'form-control'
        }
    ))
    class Meta:
        model = Entrada
        fields = ('titulo', 'tema')