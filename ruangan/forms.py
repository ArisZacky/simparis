from django import forms
from .models import Reservasi, Ruangan

class CheckAvail(forms.ModelForm):
    class Meta:
        model = Reservasi
        fields = ['checkIn', 'checkOut', 'idRuangan']

class Reservation(forms.ModelForm):
    class Meta:
        model = Reservasi
        fields = ['namaPelanggan', 'email', 'checkIn', 'checkOut', 'total', 'idRuangan']

class RuanganForm(forms.ModelForm):
    class Meta:
        model = Ruangan
        fields = ['namaRuangan', 'luasRuangan', 'kapasitasOrang', 'jTempatTidur', 'harga']