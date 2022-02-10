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
    PUKUL = models.CharField(max_length=255)
    
    def __str__(self):
        return str(self.JAM_KE) + ' - ' + self.PUKUL

class HariPenggunaan(models.Model):
    ID = models.BigAutoField(primary_key=True)
    HARI = models.CharField(max_length=255)
    JAM =  models.ForeignKey(JamPenggunaan, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.HARI
    

class JenisSarana(models.Model):
    ID = models.BigAutoField(primary_key=True)
    KATEGORI = models.CharField(max_length=255)
    def __str__(self):
        return self.KATEGORI
    
    
class Sarana(models.Model):
    ID = models.BigAutoField(primary_key=True)
    NAMA = models.CharField(max_length=255)
    JENIS = models.ForeignKey(JenisSarana, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.NAMA

class JenisRuangan(models.Model):
    ID = models.BigAutoField(primary_key=True)
    KATEGORI = models.CharField(max_length=255)
    def __str__(self):
        return self.KATEGORI

class Ruangan(models.Model):
    ID = models.BigAutoField(primary_key=True)
    NAMA = models.CharField(max_length=255)
    JENIS = models.ForeignKey(JenisRuangan, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.NAMA
    

class PengajuanPeminjamanBarang(models.Model):
    ID = models.BigAutoField(primary_key=True)
    DATA_SISWA = models.ForeignKey(DataSiswa, on_delete=models.CASCADE)
    ALAT = models.ForeignKey(Sarana, on_delete=models.CASCADE)
    KEGIATAN = models.CharField(max_length=255)
    TANGGAL_PENGAJUAN = models.DateField()
    TANGGAL_PENGGUNAAN = models.DateField()
    TANGGAL_PENGEMBALIAN = models.DateField()
    KETERANGAN = models.CharField(max_length=255)
    TANDA_TANGAN = models.FileField(max_length=255, upload_to='BuktiPelanggaran')

class JadwalPenggunaanRuangan(models.Model):
    ID = models.BigAutoField(primary_key=True)
    RUANGAN = models.ForeignKey(Ruangan, on_delete=models.CASCADE)
    JAM = models.ForeignKey(JamPenggunaan, on_delete=models.CASCADE)
    STATUS = models.CharField(
        max_length=255, 
        choices=ENUM_STATUS_PENGAJUAN,
        default='Selesai Dipinjam',
    )
    HARI = models.CharField(
        max_length=255,
        choices = ENUM_HARI, 
    )
    
    def __str__(self):
        return str(self.RUANGAN.NAMA) + ' - ' + self.HARI + ' Jam Ke = ' + str(self.JAM.JAM_KE)
    
class PengajuanPeminjamanRuangan(models.Model):
    ID = models.BigAutoField(primary_key=True)
    PENGGUNA = models.CharField(max_length=255)
    NO_HP = models.PositiveBigIntegerField()
    KEGIATAN = models.CharField(max_length=255)
    RUANGAN = models.ManyToManyField(JadwalPenggunaanRuangan)
    TANGGAL_PENGAJUAN = models.DateField()
    TANGGAL_PENGGUNAAN = models.DateField()
    STATUS = models.CharField(
        max_length=255, 
        choices=ENUM_STATUS_PENGAJUAN,
        default='Diajukan',
    )
    JENIS_PEMINJAMAN = models.CharField(
        max_length=255, 
        choices=ENUM_JENIS_PEMINJAMAN,
    )
    KETERANGAN = models.TextField(max_length=255)
    
class RiwayatPeminjamanRuangan(models.Model):
    ID = models.BigAutoField(primary_key=True)
    PENGGUNA = models.CharField(max_length=255)
    NO_HP = models.PositiveBigIntegerField()
    KEGIATAN = models.CharField(max_length=255)
    RUANGAN = models.ManyToManyField(JadwalPenggunaanRuangan)
    TANGGAL_PENGAJUAN = models.DateField()
    TANGGAL_SELESAI = models.DateField()
    JENIS_PEMINJAMAN = models.CharField(
        max_length=255, 
        choices=ENUM_JENIS_PEMINJAMAN,
    )
    STATUS = models.CharField(
        max_length=255, 
        choices=ENUM_STATUS_PENGAJUAN,
        default='Diajukan',
    )
    KETERANGAN = models.TextField(max_length=255)

def post_save_pengajuan_peminjaman_ruangan(sender, instance, created, **kwargs):
    # ubah status peminjaman setelah disetujui
    
    if instance.STATUS == 'Sedang Dipinjam':
        try:
            for data in instance.RUANGAN.values():
                print ('Merdeka')
                obj = JadwalPenggunaanRuangan.objects.get(ID=data['ID'])
                obj.STATUS = 'Sedang Dipinjam'
                obj.save()
                # add riwayat peminjaman
                if (instance.JENIS_PEMINJAMAN == 'Jangka Panjang'):
                    tanggal_pengembalian = datetime.timedelta(weeks=52)
                if (instance.JENIS_PEMINJAMAN == 'Jangka Pendek'):
                    tanggal_pengembalian = datetime.timedelta(weeks=7)
                    
                    
                ruangan_m2m = []
                for data in instance.RUANGAN.all():
                    ruangan_m2m.append(data.ID)
                
                obj = RiwayatPeminjamanRuangan.objects.create(
                    PENGGUNA = instance.PENGGUNA,
                    NO_HP = instance.NO_HP,
                    KEGIATAN = instance.KEGIATAN,
                    TANGGAL_PENGAJUAN = instance.TANGGAL_PENGAJUAN,
                    TANGGAL_SELESAI = datetime.date.today() + tanggal_pengembalian,
                    JENIS_PEMINJAMAN = instance.JENIS_PEMINJAMAN,
                    STATUS = 'Sedang Dipinjam',
                    KETERANGAN = instance.KETERANGAN
                )
                obj.RUANGAN.set(ruangan_m2m)
                obj.save()
                instance.delete()
                    
        except Exception as e:
            print(str(e))
            
    elif instance.STATUS == '' or instance.STATUS == 'Ditolak':
        try:
            for data in instance.RUANGAN.values():
                obj = JadwalPenggunaanRuangan.objects.get(ID=data['ID'])
                obj.STATUS = 'Selesai Dipinjam'
                obj.save()
                # add riwayat peminjaman
                if (instance.JENIS_PEMINJAMAN == 'Jangka Panjang'):
                    tanggal_pengembalian = datetime.timedelta(weeks=52)
                if (instance.JENIS_PEMINJAMAN == 'Jangka Pendek'):
                    tanggal_pengembalian = datetime.timedelta(weeks=7)
                    
                    
                ruangan_m2m = []
                for data in instance.RUANGAN.all():
                    ruangan_m2m.append(data.ID)
                
                obj = RiwayatPeminjamanRuangan.objects.create(
                    PENGGUNA = instance.PENGGUNA,
                    NO_HP = instance.NO_HP,
                    KEGIATAN = instance.KEGIATAN,
                    TANGGAL_PENGAJUAN = instance.TANGGAL_PENGAJUAN,
                    TANGGAL_SELESAI = instance.TANGGAL_PENGGUNAAN + tanggal_pengembalian,
                    JENIS_PEMINJAMAN = instance.JENIS_PEMINJAMAN,
                    STATUS = 'Ditolak',
                    KETERANGAN = instance.KETERANGAN
                )
                obj.RUANGAN.set(ruangan_m2m)
                obj.save()
                instance.delete()
                                    
        except Exception as e:
            print(str(e))

post_save.connect(post_save_pengajuan_peminjaman_ruangan, sender=PengajuanPeminjamanRuangan)

def ruangan_changed(sender, instance, action, pk_set=None, **kwargs):
    if action == 'post_add':
        for pk in pk_set:
            print ('Penthouse Mas')
            obj = JadwalPenggunaanRuangan.objects.get(pk=pk)
            print('add: ' + str(obj))
            obj.STATUS = 'Pengajuan' 
            obj.save()           
            
    elif action == 'post_remove':
        for pk in pk_set:
            obj = JadwalPenggunaanRuangan.objects.get(pk=pk)
            print('delete: ' + str(obj))
            obj.STATUS = 'Sudah Dikembalikan'
            obj.save()
    
m2m_changed.connect(ruangan_changed, sender=PengajuanPeminjamanRuangan.RUANGAN.through)