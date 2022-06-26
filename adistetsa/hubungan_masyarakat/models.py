from django.db import models
from kurikulum.enums import ENUM_HARI
from kurikulum.models import KelasSiswa 
from dataprofil.models import DataGuru, DataKaryawan
from django.apps import apps

from .enums import *

import datetime

# Create your models here.
class BukuTamu(models.Model):
    ID = models.BigAutoField(primary_key=True)
    NAMA = models.CharField(max_length=255)
    INSTANSI_ASAL = models.CharField(max_length=255)
    ALAMAT = models.CharField(max_length=255)
    NO_HP = models.CharField(max_length=255)
    HARI = models.CharField(max_length=255)
    TANGGAL = models.DateField()
    JAM = models.TimeField()
    KEPERLUAN = models.CharField(max_length=255)
    
    class Meta:
        verbose_name_plural = "Buku Tamu"
        
    def save(self, *args, **kwargs):
        if isinstance(self.TANGGAL, str):
            hari = datetime.datetime.strptime(self.TANGGAL, '%Y-%m-%d').weekday()
        else:
            hari = self.TANGGAL.weekday()

        self.HARI = ENUM_HARI[hari][0]
        super(BukuTamu, self).save(*args, **kwargs)
    
class LogUKSSiswa (models.Model):
    ID = models.BigAutoField(primary_key=True)
    JENIS_PTK = models.CharField(max_length=255, default='Siswa')
    NAMA = models.ForeignKey(KelasSiswa, on_delete=models.CASCADE)
    TANGGAL = models.DateField()
    JENIS_PEMERIKSAAN = models.CharField(max_length=255)
    OBAT_DIBERIKAN = models.CharField(max_length=255)
    TINDAK_LANJUT = models.CharField(max_length=255)
    
    class Meta:
        verbose_name_plural = "Log UKS Siswa"
    
    
class LogUKSTendik (models.Model):
    ID = models.BigAutoField(primary_key=True)
    JENIS_PTK = models.CharField(max_length=255, choices=ENUM_JENIS_PTK_UKS)
    NAMA = models.ForeignKey(DataGuru, on_delete=models.CASCADE)
    TANGGAL = models.DateField()
    JENIS_PEMERIKSAAN = models.CharField(max_length=255)
    OBAT_DIBERIKAN = models.CharField(max_length=255)
    TINDAK_LANJUT = models.CharField(max_length=255)
    
    class Meta:
        verbose_name_plural = "Log UKS Guru"
        
class LogUKSKaryawan (models.Model):
    ID = models.BigAutoField(primary_key=True)
    JENIS_PTK = models.CharField(max_length=255, choices=ENUM_JENIS_PTK_UKS)
    NAMA = models.ForeignKey(DataKaryawan, on_delete=models.CASCADE)
    TANGGAL = models.DateField()
    JENIS_PEMERIKSAAN = models.CharField(max_length=255)
    OBAT_DIBERIKAN = models.CharField(max_length=255)
    TINDAK_LANJUT = models.CharField(max_length=255)
    
    class Meta:
        verbose_name_plural = "Log UKS Tendik"