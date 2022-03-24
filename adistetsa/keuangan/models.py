from ast import Str
from operator import mod
from django.db import models
from django.db.models.signals import post_save, pre_save
from kurikulum.enums import ENUM_BULAN
from dataprofil.models import DataSiswa
from kurikulum.models import KelasSiswa
from django.utils.text import Truncator
from django.conf import settings
# from .enums import *


# Create your models here.
class JenisPembayaran(models.Model):
    ID = models.BigAutoField(primary_key=True)
    JENIS_PEMBAYARAN = models.CharField(max_length=255)
    
    def __str__(self):
        return self.JENIS_PEMBAYARAN

class Pembayaran(models.Model):
    ID = models.BigAutoField(primary_key=True)
    NAMA_SISWA = models.ForeignKey(KelasSiswa, on_delete=models.CASCADE)
    JENIS_PEMBAYARAN = models.ForeignKey(JenisPembayaran, on_delete=models.CASCADE)
    PEMBAYARAN_BULAN = models.CharField(
        max_length=255, 
        choices=ENUM_BULAN,
    )
    TANGGAL_PEMBAYARAN = models.DateField()
    NOMINAL_PEMBAYARAN = models.PositiveIntegerField()
    
    
    