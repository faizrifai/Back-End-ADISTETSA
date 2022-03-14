from datetime import datetime
from django.db import models
from pytz import timezone
from .enums import ENUM_BULAN
from dataprofil.models import DataSiswa
# Create your models here.

class MutasiMasuk(models.Model):
    ID = models.BigAutoField(primary_key=True)
    NAMA_SISWA = models.CharField(max_length=255)
    ASAL_SEKOLAH = models.CharField(max_length=255)
    NO_INDUK_ASAL = models.CharField(max_length=255)
    ALAMAT = models.CharField(max_length=255)
    KELAS = models.CharField(max_length=255)
    NO_INDUK_BARU = models.CharField(max_length=255)
    TANGGAL_SURAT = models.DateField(max_length=255)
    NO_SURAT = models.CharField(max_length=255)
    BULAN = models.CharField(max_length=255, choices=ENUM_BULAN)
    TAHUN = models.CharField(max_length=255)
    
    class Meta:
        verbose_name_plural = "Mutasi Masuk"
    
    def __str__(self):
        return self.NAMA_SISWA

class MutasiKeluar (models.Model):
    ID = models.BigAutoField(primary_key=True)
    NAMA_SISWA = models.CharField(max_length=255)
    KELAS = models.CharField(max_length=255)
    NO_INDUK = models.CharField(max_length=255)
    PINDAH_KE = models.CharField(max_length=255)
    TANGGAL_SURAT = models.DateField()
    NO_SURAT = models.CharField(max_length=255)
    BULAN = models.CharField(max_length=255, choices=ENUM_BULAN)
    TAHUN = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Mutasi Keluar"
    
    def __str__(self):
        return self.NAMA_SISWA