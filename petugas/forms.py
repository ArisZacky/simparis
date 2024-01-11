# accounts/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from login.models import Petugas

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = Petugas
        fields = ("namaPetugas", "jKelamin", "tanggalLahir", "alamat", "noTlpn", "email", "level")

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = Petugas
        fields = ("namaPetugas", "jKelamin", "tanggalLahir", "alamat", "noTlpn", "email", "level")