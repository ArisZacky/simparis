from django.db import models

from ruangan.models import Ruangan
from fasilitas.models import Fasilitas

# Create your models here.
class RuanganFasilitas(models.Model):
    idRF = models.AutoField(primary_key=True)
    idRuangan = models.ForeignKey(Ruangan, on_delete=models.CASCADE)
    idFasilitas = models.ForeignKey(Fasilitas, on_delete=models.CASCADE)
    jumlahBarang = models.SmallIntegerField("Jumlah Barang", default=0)