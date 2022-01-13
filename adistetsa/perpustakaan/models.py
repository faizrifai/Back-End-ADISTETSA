from os import truncate
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from adistetsa.kurikulum.models import Kelas
from dataprofil.models import DataGuru, DataSiswa
from kurikulum.models import OfferingKelas
from django.core.exceptions import ValidationError
from django.utils.html import format_html
from django.utils.text import Truncator
from django.conf import settings
from .enums import *

class KatalokBuku(models.Model):
    ID = models.BigAutoField(primary_key=True)
    NAMA_BUKU = models.CharField(max_length=255)

class AdminPerpustakaan(models.Model):
    ID = models.BigAutoField(primary_key=True)
    NAMA = models.CharField(max_length=255)
    KODE_ADMIN = models.CharField(max_length=255)

class PeminjamanJangkaPendek(models.Model):
    ID = models.BigAutoField(primary_key=True)
    NAMA = models.ForeignKey(DataSiswa, on_delete=models.CASCADE)
    KELAS = models.ForeignKey(OfferingKelas, on_delete=models.CASCADE)
    JUDUL_BUKU = models.ManyToManyField(KatalokBuku)
    NO_INDUK_MANUAL = models.CharField(max_length=255)
    NO_BARCODE = models.CharField(max_length=255)
    JUMLAH = models.IntegerField()
    KETERANGAN = models.TextField()
    
    
class PeminjamanJangkaPanjang(models.Model):
    ID = models.BigAutoField(primary_key=True)
    NAMA = models.ForeignKey(DataSiswa, on_delete=models.CASCADE)
    KELAS = models.ForeignKey(OfferingKelas, on_delete=models.CASCADE)
    TANGGAL_PEMINJAMAN = models.DateField()
    TANGGAL_PENGGEMBALIAN = models.DateField()
    JUDUL_BUKU = models.CharField(max_length=255) #Fk Data Buku
    NO_INDUK_MANUAL = models.CharField(max_length=255)
    NO_BARCODE = models.CharField(max_length=255)
    JUMLAH = models.IntegerField()
    KETERANGAN = models.TextField()

class RiwayatPeminjamanAnggota(models.Model):
    ID = models.BigAutoField(primary_key=True)
    PEMINJAMAN_JANGKA_PENDEK  = models.ForeignKey(PeminjamanJangkaPanjang, on_delete=models.CASCADE)
    PEMINJAMAN_JANGKA_PANJANG  = models.ForeignKey(PeminjamanJangkaPanjang, on_delete=models.CASCADE)
    
class AnggotaPerpustakaan(models.Model):
    ID = models.BigAutoField(primary_key=True)
    NAMA  = models.ForeignKey(DataSiswa, on_delete=models.CASCADE)
    
    
    