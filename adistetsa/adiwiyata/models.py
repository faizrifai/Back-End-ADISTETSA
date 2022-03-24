from distutils.archive_util import make_archive
from distutils.command.upload import upload
from pyexpat import model
from django.db import models
from django.forms import CharField
from dataprofil.models import DataSiswa
from .enums import *

# Create your models here.
class SanitasiDrainase(models.Model):
    ID = models.BigAutoField(primary_key=True)
    TANGGAL = models.DateField()
    NAMA_KEGIATAN = models.CharField(max_length=255)
    UNSUR_TERLIBAT = models.CharField(max_length=255)
    KETERANGAN = models.CharField(max_length=255)
    FILE = models.FileField(upload_to=" ", max_length=255)
    
class JaringanKerja(models.Model):
    ID = models.BigAutoField(primary_key=True)
    TANGGAL = models.DateField()
    NAMA_KEGIATAN = models.CharField(max_length=255)
    KETERANGAN = models.CharField(max_length=255)
    FILE = models.FileField(upload_to=" ", max_length=255)
    
class Publikasi(models.Model):
    ID = models.BigAutoField(primary_key=True)
    TANGGAL = models.DateField()
    NAMA_KEGIATAN = models.CharField(max_length=255)
    JENIS_MEDIA = models.CharField(max_length=255)
    KETERANGAN = models.CharField(max_length=255)
    FILE = models.FileField(upload_to=" ", max_length=255)
    
class DaftarKader(models.Model):
    ID = models.BigAutoField(primary_key=True)
    NIS = models.ForeignKey(DataSiswa, on_delete=models.CASCADE)

class KegiatanKader(models.Model):
    ID = models.BigAutoField(primary_key=True)
    TANGGAL = models.DateField()
    NAMA_KEGIATAN = models.CharField(max_length=255)
    KETERANGAN = models.CharField(max_length=255)
    FILE = models.FileField(upload_to=" ", max_length=255)
    
class Konservasi(models.Model):
    ID = models.BigAutoField(primary_key=True)
    TANGGAL = models.DateField()
    KATEGORI = models.CharField(max_length=255, choices=ENUM_KONSERVASI)
    NAMA_KEGIATAN = models.CharField(max_length=255)
    KETERANGAN = models.CharField(max_length=255)
    FILE = models.FileField(upload_to=" ", max_length=255)

class PenanamanPohon(models.Model):
    ID = models.BigAutoField(primary_key=True)
    TANGGAL = models.DateField()
    NAMA_KEGIATAN = models.CharField(max_length=255)
    JUMLAH = models.CharField(max_length=255)
    KETERANGAN = models.CharField(max_length=255)
    FILE = models.FileField(upload_to=" ", max_length=255)
    
class PembibitanPohon(models.Model):
    ID = models.BigAutoField(primary_key=True)
    TANGGAL = models.DateField()
    NAMA_KEGIATAN = models.CharField(max_length=255)
    KETERANGAN = models.CharField(max_length=255)
    FILE = models.FileField(upload_to=" ", max_length=255)

class PemeliharaanPohon(models.Model):
    ID = models.BigAutoField(primary_key=True)
    TANGGAL = models.DateField()
    NAMA_KEGIATAN = models.CharField(max_length=255)
    KETERANGAN = models.CharField(max_length=255)
    FILE = models.FileField(upload_to=" ", max_length=255)
    
class KaryaInovatif(models.Model):
    ID = models.BigAutoField(primary_key=True)
    TANGGAL = models.DateField()
    NAMA_INOVATOR = models.CharField(max_length=255)
    NAMA_KARYA_INOVATIF = models.CharField(max_length=255)
    JENIS = models.CharField(max_length=255)
    FILE = models.FileField(upload_to=" ", max_length=255)
    
class PenerapanPRLH(models.Model):
    ID = models.BigAutoField(primary_key=True)
    TANGGAL = models.DateField()
    NAMA_KEGIATAN = models.CharField(max_length=255)
    PESERTA = models.CharField(max_length=255)
    KETERANGAN = models.TextField()
    FILE = models.FileField(upload_to=" ", max_length=255)
    
class ReuseReduceRecycle(models.Model):
    ID = models.BigAutoField(primary_key=True)
    TANGGAL = models.DateField()
    NAMA_KEGIATAN = models.CharField(max_length=255)
    JENIS_KEGIATAN = models.CharField(
        max_length=255, 
        choices=ENUM_3R,
    )
    PIHAK_TERLIBAT = models.CharField(max_length=255)
    KETERANGAN = models.TextField()
    FILE = models.FileField(upload_to=" ", max_length=255)
    
class PemeliharaanSampah(models.Model):
    ID = models.BigAutoField(primary_key=True)
    TANGGAL = models.DateField()
    NAMA_KEGIATAN = models.CharField(max_length=255)
    KETERANGAN = models.TextField()
    FILE = models.FileField(upload_to=" ", max_length=255)
    
class TabunganSampah(models.Model):
    ID = models.BigAutoField(primary_key=True)
    TANGGAL = models.DateField()
    JUMLAH_PERTANGGAL = models.PositiveIntegerField()
    
    
    

