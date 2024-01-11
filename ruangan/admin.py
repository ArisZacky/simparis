from django.contrib import admin

# Register your models here.
from .models import Ruangan
from fasilitas.models import Fasilitas
# admin.site.register(Petugas)
admin.site.register(Fasilitas)
admin.site.register(Ruangan)