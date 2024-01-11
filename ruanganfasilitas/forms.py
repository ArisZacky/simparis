from django import forms
from .models import RuanganFasilitas

class RuanganFasilitasForm(forms.ModelForm):
    class Meta:
        model = RuanganFasilitas
        fields = ['jumlahBarang', 'idFasilitas', 'idRuangan']