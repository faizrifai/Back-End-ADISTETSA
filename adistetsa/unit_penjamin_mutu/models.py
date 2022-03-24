from ast import mod
from itertools import count
from django.db import models
from django.db.models.signals import pre_save, post_save

from .custom_function import buat_file_prototype
from unit_penjamin_mutu.enums import ENUM_KATEGORI_BAHAN_BUKU
from django.db.models.signals import post_save

import pandas as pd

# from dataprofil.models import DataGuru
from kurikulum.models import TahunAjaran, DataSemester, OfferingKelas
from dataprofil.models import DataGuru
# Create your models here.

class BahanBukuUPM(models.Model):
    ID = models.BigAutoField(primary_key=True)
    KATEGORI = models.CharField(
        max_length=255,
        choices=ENUM_KATEGORI_BAHAN_BUKU,
        default=''
    )
    TAHUN_AJARAN = models.ForeignKey(TahunAjaran, on_delete=models.CASCADE)
    SEMESTER = models.ForeignKey(DataSemester, on_delete=models.CASCADE)
    TEMPLATE = models.FileField(max_length=255, upload_to='FileBahanBuku', blank=True) 
    START_ROW = models.IntegerField(default=0)
    START_COL = models.IntegerField(default=0)
    GENERATE = models.BooleanField()
    FILE = models.FileField(max_length=255, upload_to='FileBahanBuku', blank=True)
    FILE_HASIL = models.FileField(max_length=255, upload_to='FileBahanBuku', blank=True)
    
    class Meta:
        verbose_name_plural = 'Bahan Buku UPM'
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        if self.GENERATE:
            if self.KATEGORI =='Pembagian Tugas BK Semester':
                count = PembagianTugasGuruBK.objects.all()
                self.FILE = buat_file_prototype(self, count)
            elif self.KATEGORI == 'Pembagian Tugas Pokok dan Tambahan Tenaga Kependidikan':
                print ('Makan Lur')
                count = PembagianTugasPokokTambahanTendik.objects.all()
                self.FILE = buat_file_prototype(self, count)
                
            count = ''
            self.FILE = buat_file_prototype(self, count)
            
        return super().save(*args, **kwargs)

class PembagianTugasGuruBK(models.Model):
    ID = models.BigAutoField(primary_key=True)
    DATA_GURU = models.ForeignKey(DataGuru, on_delete=models.CASCADE)
    TAHUN_AJARAN = models.ForeignKey(TahunAjaran, on_delete=models.CASCADE)
    SEMESTER = models.ForeignKey(DataSemester, on_delete=models.CASCADE)
    DATA_KELAS = models.ManyToManyField(OfferingKelas)
    KETERANGAN_TUGAS = models.TextField(blank=True)
    
    class Meta:
        verbose_name_plural = 'Pembagian Tugas Guru BK'

class TugasPokokTendik(models.Model):
    ID = models.BigAutoField(primary_key=True)
    JENIS_TUGAS = models.CharField(max_length=255)
    
    def __str__(self):
        return self.JENIS_TUGAS
    
    class Meta:
        verbose_name_plural = 'Tugas Pokok Tendik'
        
class  PembagianTugasPokokTambahanTendik(models.Model):
    ID = models.BigAutoField(primary_key=True)
    DATA_GURU = models.ForeignKey(DataGuru, on_delete=models.CASCADE)
    TUGAS_POKOK = models.ForeignKey(TugasPokokTendik, on_delete=models.CASCADE)
    TUGAS_TAMBAHAN = models.CharField(max_length=255)
    
    class Meta:
        verbose_name_plural = 'Pembagian Tugas Pokok Tenaga Pendidikan'
    

    						
    