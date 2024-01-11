from django.db import models

# Create your models here.
class Fasilitas(models.Model):
    idFasilitas = models.AutoField(primary_key=True)
    namaFasilitas = models.CharField(max_length=60)

    def __str__(self):
        return "{}".format(self.namaFasilitas)