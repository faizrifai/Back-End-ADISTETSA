from ast import mod
from itertools import count
from django.db import models
from django.db.models.signals import pre_save, post_save
from pyrsistent import m

from .custom_function import buat_file_prototype, pembagian_bk, pembagian_jadwal_mengajar, pembagian_tugas_guru_bk, pembagian_tugas_guru_tik, pembagian_tugas_pokok_tendik, rekapitulasi_jam_mengajar, rincian_tugas_pokok_tendik, tugas_tambahan_kepanitiaan
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
    # TEMPLATE = models.FileField(max_length=255, upload_to='FileBahanBuku', blank=True) 
    # START_ROW = models.IntegerField(default=0)
    # START_COL = models.IntegerField(default=0)
    GENERATE = models.BooleanField()
    FILE = models.FileField(max_length=255, upload_to='FileBahanBuku', blank=True)
    # FILE_HASIL = models.FileField(max_length=255, upload_to='FileBahanBuku', blank=True)
    
    class Meta:
        verbose_name_plural = 'Bahan Buku UPM'
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        if self.GENERATE:
            if self.KATEGORI =='Pembagian Jadwal Mengajar':
                self.FILE = pembagian_jadwal_mengajar(self)
            elif self.KATEGORI == 'Rekapitulasi Jumlah Jam Mengajar':
                self.FILE = rekapitulasi_jam_mengajar(self)
            elif self.KATEGORI == 'Pembagian Tugas BK Semester':
                data = PembagianTugasGuruBK.objects.all()
                pembagian_tugas_guru_bk(self, data)
            elif self.KATEGORI == 'Pembagian Tugas TIK Semester':
                data = PembagianTugasGuruTIK.objects.all()
                pembagian_tugas_guru_tik(self, data)
            elif self.KATEGORI == 'Pembagian Tugas Pokok dan Tambahan Tenaga Kependidikan':
                data = PembagianTugasPokokTambahanTendik.objects.all()
                pembagian_tugas_pokok_tendik(self, data)
            elif self.KATEGORI == 'Rincian Tugas Pokok dan Tambahan Tenaga Kependidikan':
                data = RincianTugasPokokTambahanTendik.objects.all()
                rincian_tugas_pokok_tendik(self, data)
            elif self.KATEGORI == 'Lampiran Tugas Tambahan dan Kepanitiaan':
                data = TugasTambahanKepanitiaanTendik.objects.all().order_by('BIDANG__KODE_BIDANG',)
                tugas_tambahan_kepanitiaan(self, data)
    
            
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

class PembagianTugasGuruTIK(models.Model):
    ID = models.BigAutoField(primary_key=True)
    DATA_GURU = models.ForeignKey(DataGuru, on_delete=models.CASCADE)
    TAHUN_AJARAN = models.ForeignKey(TahunAjaran, on_delete=models.CASCADE)
    SEMESTER = models.ForeignKey(DataSemester, on_delete=models.CASCADE)
    DATA_KELAS = models.ManyToManyField(OfferingKelas)
    KETERANGAN_TUGAS = models.TextField(blank=True)
    
    class Meta:
        verbose_name_plural = 'Pembagian Tugas Guru TIK'

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
    TAHUN_AJARAN = models.ForeignKey(TahunAjaran, on_delete=models.CASCADE)
    TUGAS_POKOK = models.ForeignKey(TugasPokokTendik, on_delete=models.CASCADE)
    TUGAS_TAMBAHAN = models.TextField()
    
    class Meta:
        verbose_name_plural = 'Pembagian Tugas Pokok Tenaga Pendidikan'
    
class RincianTugasPokokTambahanTendik(models.Model):
    ID = models.BigAutoField(primary_key=True)
    DATA_GURU = models.ForeignKey(DataGuru, on_delete=models.CASCADE)
    TAHUN_AJARAN = models.ForeignKey(TahunAjaran, on_delete=models.CASCADE)
    TUGAS_POKOK = models.TextField()
    TUGAS_TAMBAHAN = models.TextField()
    
    class Meta:
        verbose_name_plural = 'Rincian Tugas Pokok Tenaga Pendidikan'
        
class JenisBidang(models.Model):
    ID = models.BigAutoField(primary_key=True)
    KODE_BIDANG = models.PositiveIntegerField()
    NAMA_BIDANG = models.CharField(max_length=255)
    def __str__(self):
        return self.NAMA_BIDANG
    class Meta:
        verbose_name_plural = 'Jenis Bidang'

class TugasTambahanKepanitiaanTendik(models.Model):
    ID = models.BigAutoField(primary_key=True)
    DATA_GURU = models.ForeignKey(DataGuru, on_delete=models.CASCADE)
    TAHUN_AJARAN = models.ForeignKey(TahunAjaran, on_delete=models.CASCADE)
    BIDANG = models.ForeignKey(JenisBidang, on_delete=models.CASCADE)
    SUB_BIDANG = models.CharField(max_length=255, blank=True)
    TUGAS = models.CharField(max_length=255)
    
    class Meta:
        verbose_name_plural = 'Pembagian Tugas Tambahan dan Kepanitiaan Tendik'
    