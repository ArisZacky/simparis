from django import forms
from .models import Fasilitas

class FasilitasForm(forms.ModelForm):
    class Meta:
        model = Fasilitas
        fields = ['namaFasilitas']