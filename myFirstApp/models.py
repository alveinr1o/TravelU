from django.db import models
from datetime import date

# Create your models here.
class Penumpang(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    NIM = models.CharField(max_length=15)

class Reservasi(models.Model):
    penumpangid = models.CharField(max_length=50)
    busid = models.CharField(max_length=50)
    tanggalreservasi = models.DateField(default=date(2001, 1, 1))
    statusreservasi = models.CharField(max_length=50, default='waiting')

class Bus(models.Model):
    driverid = models.CharField(max_length=50)
    lokasiawal = models.CharField(max_length=50)
    lokasiakhir = models.CharField(max_length=50)
    waktukeberangkatan = models.TimeField()

class Driver(models.Model):
    namadriver = models.CharField(max_length=50)
    nomorpegawai = models.CharField(max_length=50)

class Admin(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    namaadmin = models.CharField(max_length=50)