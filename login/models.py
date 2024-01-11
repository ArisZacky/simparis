from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

# Create your models here.


class MyUserManager(BaseUserManager):
    def create_user(self, namaPetugas, jKelamin, tanggalLahir, alamat, noTlpn, email, level, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            namaPetugas=namaPetugas,
            jKelamin=jKelamin,
            tanggalLahir=tanggalLahir,
            alamat = alamat,
            noTlpn = noTlpn,
            level = level
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
class Petugas(AbstractBaseUser):
    LEVELCHOICE = (
        ("admin", "Admin"),
        ("petugas", "Petugas")
    )

    JKCHOICE = (
        ("L", "Laki-Laki"),
        ("P", "Perempuan")
    )

    idPetugas = models.AutoField(primary_key=True)
    namaPetugas = models.CharField(max_length=60)
    jKelamin = models.CharField(max_length=1, choices=JKCHOICE)
    tanggalLahir = models.DateField("Tanggal Lahir")
    alamat = models.CharField(max_length=100)
    noTlpn = models.CharField(max_length=15)
    email = models.CharField(max_length=50, unique=True)
    level = models.CharField(choices=LEVELCHOICE, max_length=10)

    objects = MyUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["namaPetugas", "jKelamin", "tanggalLahir", "alamat", "noTlpn", "level"]

    def __str__(self):
        return "{}".format(self.namaPetugas)
