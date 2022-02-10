from ast import mod
from telnetlib import STATUS
from turtle import mode
from xml.parsers.expat import model
from django import shortcuts
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save, m2m_changed
from django.db.models.query_utils import select_related_descend
from django.db.models.signals import post_save

from dataprofil.models import DataGuru, DataSiswa
from kurikulum.models import PoinPelanggaran
import datetime

from .enums import *    

class JamPenggunaan(models.Model):
    ID = models.BigAutoField(primary_key=True)
    JAM_KE = models.IntegerField()
    PUKUL = models.TimeField()

class HariPenggunaan(models.Model):
    ID = models.BigAutoField(primary_key=True)
    HARI = models.CharField(max_length=255)
    JAM =  models.ForeignKey(JamPenggunaan, on_delete=models.CASCADE)

class JenisSarana(models.Model):
    ID = models.BigAutoField(primary_key=True)
    KATEGORI = models.CharField(max_length=255)
   
    def __str__(self):
        return str(self.KATEGORI)
    
class Sarana(models.Model):
    ID = models.BigAutoField(primary_key=True)
    NAMA = models.CharField(max_length=255)
    JENIS = models.ForeignKey(JenisSarana, on_delete=models.CASCADE)
    STATUS = models.CharField(
        max_length=255,
        choices=ENUM_STATUS_PEMINJAMAN,
        default='Sudah Dikembalikan',
    )
    def __str__(self):
        return str(self.NAMA) + ' - ' + str(self.JENIS.KATEGORI)

class JenisRuangan(models.Model):
    ID = models.BigAutoField(primary_key=True)
    KATEGORI = models.CharField(max_length=255)

class Ruangan(models.Model):
    ID = models.BigAutoField(primary_key=True)
    NAMA = models.CharField(max_length=255)
    JENIS = models.ForeignKey(JenisRuangan, on_delete=models.CASCADE)
    

class PengajuanPeminjamanBarang(models.Model):
    ID = models.BigAutoField(primary_key=True)
    NAMA_PEMINJAM = models.CharField(max_length=255, default='')
    NO_TELEPON = models.CharField(max_length=255, default='')
    ALAT = models.ManyToManyField(Sarana)
    KEGIATAN = models.CharField(max_length=255)
    TANGGAL_PENGAJUAN = models.DateField()
    TANGGAL_PENGGUNAAN = models.DateField()
    TANGGAL_PENGEMBALIAN = models.DateField(blank=True, null=True)
    KETERANGAN = models.CharField(max_length=255)
    STATUS_PENGAJUAN = models.CharField(
        max_length=255, 
        choices=ENUM_PENGAJUAN,
        default='Pengajuan',
    )
    TANDA_TANGAN = models.FileField(max_length=255, upload_to='BuktiPelanggaran', blank=True)

class RiwayatPeminjamanBarang(models.Model):
    ID = models.BigAutoField(primary_key=True)
    NAMA_PEMINJAM = models.CharField(max_length=255, default='')
    NO_TELEPON = models.CharField(max_length=255, default='')
    ALAT = models.ManyToManyField(Sarana)
    KEGIATAN = models.CharField(max_length=255)
    TANGGAL_PENGGUNAAN = models.DateField()
    TANGGAL_PENGEMBALIAN = models.DateField()
    KETERANGAN = models.CharField(max_length=255)
    STATUS_PEMINJAMAN = models.CharField(
        max_length=255, 
        choices=ENUM_STATUS_PEMINJAMAN,
        default= 'Sedang Dipinjam'
    )
    TANDA_TANGAN = models.FileField(max_length=255, upload_to='BuktiPelanggaran', blank=True)


def post_save_pengajuan_peminjaman_barang(sender, instance, created, **kwargs):
    # ubah status peminjaman setelah disetujui
    
    if instance.STATUS_PENGAJUAN == 'Disetujui':
        try:
            for data in instance.ALAT.values():
                obj = Sarana.objects.get(ID=data['ID'])
                obj.STATUS = 'Sedang Dipinjam'
                obj.save()    
                    
                alat_m2m = []
                for data in instance.ALAT.all():
                    alat_m2m.append(data.ID)
                
                obj = RiwayatPeminjamanBarang.objects.create(
                    NAMA_PEMINJAM = instance.NAMA_PEMINJAM,
                    NO_TELEPON = instance.NO_TELEPON,
                    KEGIATAN = instance.KEGIATAN,
                    TANGGAL_PENGGUNAAN = instance.TANGGAL_PENGGUNAAN,
                    TANGGAL_PENGEMBALIAN = instance.TANGGAL_PENGEMBALIAN,
                    KETERANGAN = instance.KETERANGAN,
                    TANDA_TANGAN = instance.TANDA_TANGAN
                )
                obj.ALAT.set(alat_m2m)
                obj.save()
                instance.delete()
                    
        except Exception as e:
            print(str(e))
            
    elif instance.STATUS_PENGAJUAN == '' or instance.STATUS_PENGAJUAN == 'Ditolak':
        
        try:
            for data in instance.ALAT.values():
                obj = Sarana.objects.get(ID=data['ID'])
                obj.STATUS = 'Sudah Dikembalikan'
                obj.save()
                
                print ('TEST')
                
                alat_m2m = []
                for data in instance.ALAT.all():
                    alat_m2m.append(data.ID)
                
                obj = RiwayatPeminjamanBarang.objects.create(
                    NAMA_PEMINJAM = instance.NAMA_PEMINJAM,
                    NO_TELEPON = instance.NO_TELEPON,
                    KEGIATAN = instance.KEGIATAN,
                    TANGGAL_PENGGUNAAN = instance.TANGGAL_PENGGUNAAN,
                    TANGGAL_PENGEMBALIAN = instance.TANGGAL_PENGEMBALIAN,
                    KETERANGAN = instance.KETERANGAN,
                    STATUS_PEMINJAMAN = 'Ditolak',
                    TANDA_TANGAN = instance.TANDA_TANGAN
                )
                obj.ALAT.set(alat_m2m)
                obj.save()
                instance.delete()
                    
        except Exception as e:
            print(str(e))

post_save.connect(post_save_pengajuan_peminjaman_barang, sender=PengajuanPeminjamanBarang)

def alat_changed(sender, instance, action, pk_set=None, **kwargs):
    if action == 'post_add':
        for pk in pk_set:
            obj = Sarana.objects.get(pk=pk)
            print('add: ' + str(obj))
            obj.STATUS = 'Pengajuan' 
            obj.save()           
            
    elif action == 'post_remove':
        for pk in pk_set:
            obj = Sarana.objects.get(pk=pk)
            print('delete: ' + str(obj))
            obj.STATUS = 'Sudah Dikembalikan'
            obj.save()
    
m2m_changed.connect(alat_changed, sender=PengajuanPeminjamanBarang.ALAT.through)

    
class PengajuanPeminjamanRuanganPendek(models.Model):
    ID = models.BigAutoField(primary_key=True)
    DATA_SISWA = models.ForeignKey(DataSiswa, on_delete=models.CASCADE)
    KEGIATAN = models.CharField(max_length=255)
    RUANGAN = models.ForeignKey(Ruangan, on_delete=models.CASCADE)
    TANGGAL_PENGAJUAN = models.DateField()
    TANGGAL_PENGGUNAAN = models.DateField()
    HARI_PENGGUNAAN = models.ForeignKey(HariPenggunaan, on_delete=models.CASCADE)
    KETERANGAN = models.TextField(max_length=255)
        