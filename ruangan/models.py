from django.db import models
from django.utils.text import slugify
# Create your models here.


class Ruangan(models.Model):

    TEMPATTIDURCHOICE = (
        ("S", "Single"),
        ("D", "Double")
    )
    idRuangan = models.AutoField(primary_key=True)
    namaRuangan = models.CharField(max_length=60)
    luasRuangan = models.SmallIntegerField("Luas Ruangan", default=0)
    kapasitasOrang = models.SmallIntegerField("Kapasitas Orang", default=0)
    jTempatTidur = models.CharField(choices=TEMPATTIDURCHOICE, max_length=6)
    harga = models.DecimalField(max_digits=10, decimal_places=0)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.namaRuangan)
        super(Ruangan, self).save(*args, **kwargs)

    def __str__(self):
        return "{}".format(self.namaRuangan)
    
class Reservasi(models.Model):
    STATUSCHOICE = (
        ("Belum Check In", "Proses"),
        ("Sudah Check In", "Check In"),
        ("Sudah Check Out", "Check Out")
    )
        
    idReservasi = models.AutoField(primary_key=True)
    namaPelanggan = models.CharField(max_length=60)
    email = models.CharField(max_length=50)
    checkIn = models.DateField("Check In")
    checkOut = models.DateField("Check Out")
    waktuPesanan = models.DateTimeField(auto_now_add = True)
    total = models.DecimalField(max_digits = 10, decimal_places = 0)
    status = models.CharField(choices=STATUSCHOICE, max_length=20, default="Belum Check In")
    idRuangan = models.ForeignKey(Ruangan, on_delete=models.CASCADE)
   
    def __str__(self):
        return "{}".format(self.namaPelanggan)