from telnetlib import STATUS
from django import shortcuts
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save, m2m_changed
from django.db.models.query_utils import select_related_descend
from django.db.models.signals import post_save
from django.utils.text import Truncator

from dataprofil.models import DataGuru, DataSiswa
from kurikulum.models import PoinPelanggaran
import datetime

from .enums import *


class PengajuanLaporanPelanggaran(models.Model):
    ID = models.BigAutoField(primary_key=True)
    DATA_SISWA = models.ForeignKey(DataSiswa, on_delete=models.CASCADE)
    BUKTI_PELANGGARAN = models.FileField(max_length=255, upload_to='BuktiPelanggaran')
    JENIS_PELANGGARAN = models.ForeignKey(PoinPelanggaran, on_delete=models.CASCADE)
    STATUS_PENGAJUAN = models.CharField(
        max_length=255, 
        choices=ENUM_PENGAJUAN_PELANGGARAN,
        default='Diajukan'
    )
    class Meta:
        verbose_name_plural = "Pengajuan Laporan Pelanggaran"
    
class PelanggaranSiswa(models.Model):
    ID = models.BigAutoField(primary_key=True)
    DATA_SISWA = models.ForeignKey(DataSiswa, on_delete=models.CASCADE)
    POIN = models.PositiveBigIntegerField(default=0)
    class Meta:
        verbose_name_plural = "Pelanggaran Siswa"

def post_save_data_siswa(sender, instance, **kwargs):
    PelanggaranSiswa.objects.get_or_create(
        DATA_SISWA = instance.NIS,
    )

post_save.connect(post_save_data_siswa, sender = DataSiswa)
        
class RiwayatLaporanPelanggaran(models.Model):
    ID = models.BigAutoField(primary_key=True)
    DATA_SISWA = models.ForeignKey(DataSiswa, on_delete=models.CASCADE)
    BUKTI_PELANGGARAN = models.FileField(max_length=255, upload_to='BuktiPelanggaran')
    JENIS_PELANGGARAN = models.ForeignKey(PoinPelanggaran, on_delete=models.CASCADE)
    STATUS_PENGAJUAN = models.CharField(
        max_length=255, 
        choices=ENUM_PENGAJUAN_PELANGGARAN,
        default='Diajukan'
    )
    class Meta:
        verbose_name_plural = "Riwayat Laporan Pelanggaran"

def post_save_persetujuan_laporan(sender, instance, **kwargs):
    try: 
        if instance.STATUS_PENGAJUAN == 'Disetujui' :
            obj = PelanggaranSiswa.objects.get_or_create(
                DATA_SISWA = instance.DATA_SISWA,
            )[0]
            print(obj)
            obj.POIN += instance.JENIS_PELANGGARAN.POIN
            obj.save()
            try:
                riwayat = RiwayatLaporanPelanggaran.objects.create(
                    DATA_SISWA = instance.DATA_SISWA,
                    BUKTI_PELANGGARAN = instance.BUKTI_PELANGGARAN,
                    JENIS_PELANGGARAN = instance.JENIS_PELANGGARAN, 
                    STATUS_PENGAJUAN = instance.STATUS_PENGAJUAN
                )
                riwayat.save()
                instance.delete()
            except Exception as e:
                print(str(e))
                
        elif instance.STATUS_PENGAJUAN == 'Ditolak' :
            instance.delete()
    except Exception as e:
        print(str(e))

post_save.connect(post_save_persetujuan_laporan, sender =  PengajuanLaporanPelanggaran)

# post_save.connect(post_save_pengajuan_laporan_pelanggaran, sender=PengajuanLaporanPelanggaran)
class KategoriProgramKebaikan(models.Model):
    ID = models.BigAutoField(primary_key=True)
    NAMA = models.CharField(max_length=255)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['NAMA'], name='%(app_label)s_%(class)s_unique')
        ]
        verbose_name_plural = "Kategori Program Kebaikan"
        ordering = ['NAMA']
    
    def __str__(self):
        return Truncator(self.NAMA).chars(50)
    

class ProgramKebaikan(models.Model):
    ID = models.BigAutoField(primary_key=True)
    KETERANGAN = models.CharField(max_length=255)
    KATEGORI = models.ForeignKey(KategoriProgramKebaikan, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['KETERANGAN'], name='%(app_label)s_%(class)s_unique')
        ]
        verbose_name_plural = "Program Kebaikan"
        ordering = ['KETERANGAN']
    
    def __str__(self):
        return Truncator(self.KETERANGAN).chars(50)

class PoinProgramKebaikan(models.Model):
    ID = models.BigAutoField(primary_key=True)
    KETERANGAN = models.CharField(max_length=255)
    POIN = models.PositiveIntegerField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['KETERANGAN', 'POIN'], name='%(app_label)s_%(class)s_unique')
        ]
        verbose_name_plural = "Poin Program Kebaikan"
        ordering = ['KETERANGAN']
    
    def __str__(self):
        return self.KETERANGAN


class PengajuanProgramKebaikan(models.Model):
    ID = models.BigAutoField(primary_key=True)
    DATA_SISWA = models.ForeignKey(DataSiswa, on_delete=models.CASCADE)
    BUKTI_PROGRAM_KEBAIKAN = models.FileField(max_length=255, upload_to='BuktiProgramKebaikan')
    JENIS_PROGRAM_KEBAIKAN = models.ForeignKey(PoinProgramKebaikan, on_delete=models.CASCADE)
    STATUS_PENGAJUAN = models.CharField(
        max_length=255, 
        choices=ENUM_PENGAJUAN_PELANGGARAN,
        default='Diajukan',
    )
    
    class Meta:
        verbose_name_plural = "Pengajuan Program Kebaikan"

class RiwayatProgramKebaikan(models.Model):
    ID = models.BigAutoField(primary_key=True)
    DATA_SISWA = models.ForeignKey(DataSiswa, on_delete=models.CASCADE)
    BUKTI_PROGRAM_KEBAIKAN = models.FileField(max_length=255, upload_to='BuktiProgramKebaikan')
    JENIS_PROGRAM_KEBAIKAN = models.ForeignKey(PoinProgramKebaikan, on_delete=models.CASCADE)
    STATUS_PENGAJUAN = models.CharField(
        max_length=255, 
        choices=ENUM_PENGAJUAN_PELANGGARAN,
        default='Diajukan',
    )
    class Meta:
        verbose_name_plural = "Riwayat Program Kebaikan"
        

def post_save_pengajuan_program_kebaikan(sender, instance, **kwargs):
    try: 
        if instance.STATUS_PENGAJUAN == 'Disetujui' :
            obj = PelanggaranSiswa.objects.get_or_create(
                DATA_SISWA = instance.DATA_SISWA
            )[0]
            if obj.POIN < instance.JENIS_PROGRAM_KEBAIKAN.POIN :
                obj.POIN = 0 
                obj.save()
            elif obj.POIN >= instance.JENIS_PROGRAM_KEBAIKAN.POIN :
                obj.POIN -= instance.JENIS_PROGRAM_KEBAIKAN.POIN
                obj.save()
            try:
                riwayat = RiwayatProgramKebaikan.objects.create(
                    DATA_SISWA = instance.DATA_SISWA,
                    BUKTI_PROGRAM_KEBAIKAN = instance.BUKTI_PROGRAM_KEBAIKAN,
                    JENIS_PROGRAM_KEBAIKAN = instance.JENIS_PROGRAM_KEBAIKAN, 
                    STATUS_PENGAJUAN = instance.STATUS_PENGAJUAN
                )
                riwayat.save()
                instance.delete()
            except Exception as e:
                print(str(e))
                
        elif instance.STATUS_PENGAJUAN == 'Ditolak' :
            instance.delete()
    except:
        pass

post_save.connect(post_save_pengajuan_program_kebaikan, sender =  PengajuanProgramKebaikan)

