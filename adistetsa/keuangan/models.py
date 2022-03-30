from django.db import models
from django.db.models.signals import post_save, pre_save
from kurikulum.models import KelasSiswa
from django.conf import settings
from .enums import ENUM_JENIS_PEMBAYARAN
from .customs_template import buat_kuitansi
# from .enums import *


# Create your models here.
# class JenisPembayaran(models.Model):
#     ID = models.BigAutoField(primary_key=True)
#     JENIS_PEMBAYARAN = models.CharField(max_length=255)
    
#     def __str__(self):
#         return self.JENIS_PEMBAYARAN

class Pembayaran(models.Model):
    ID = models.BigAutoField(primary_key=True)
    NAMA_SISWA = models.ForeignKey(KelasSiswa, on_delete=models.CASCADE)
    # JENIS_PEMBAYARAN = models.CharField(max_length=255, blank=True)
    TANGGAL_PEMBAYARAN = models.DateField()
    PEMBAYARAN_DPSM_RUTIN = models.CharField(blank=True, default='', max_length=1024)
    PEMBAYARAN_DPSM_INSINDENTAL = models.CharField(blank=True, default='', max_length=1024)
    BIMBEL = models.CharField(blank=True, default='', max_length=1024)
    NOMINAL_SPP = models.CharField(blank=True, default='', max_length=1024)
    PEMBAYARAN_SPP = models.CharField(max_length=1024,blank=True, default='')
    GENERATE = models.BooleanField(default= False)
    TEMPLATE = models.FileField(upload_to='DataKeuangan', max_length=255, blank=True)
    KUITANSI = models.FileField(upload_to='DataKeuangan', max_length=255, blank=True)
    
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.KUITANSI = buat_kuitansi(self)
        if self.GENERATE :
            self.KUITANSI = buat_kuitansi(self)
            
        return super().save(*args, **kwargs)
    
# class KuitansiPembayaranProxy(Pembayaran):
#     class Meta:
#         ordering = ["NAMA_SISWA"]
#         proxy = True    
#         verbose_name_plural ='Kwitansi Pembayaran'
    
    
    