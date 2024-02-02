from django.db import models
from ruangan.models import Reservasi

# Create your models here.
class Transaksi(models.Model):
    STATUSCHOICE = (
        ("Proses", "proses"),
        ("Lunas", "lunas"),
        ("Batal", "batal")
    )

    idTransaksi = models.AutoField(primary_key=True)
    idReservasi = models.ForeignKey(Reservasi, on_delete=models.CASCADE)
    kodeTransaksi = models.CharField(max_length=13)
    tanggalTransaksi = models.DateTimeField()
    nominal = models.DecimalField(max_digits = 10, decimal_places = 0)
    status = models.CharField(choices=STATUSCHOICE, max_length=10)