from logging import raiseExceptions
from django.contrib.auth.models import User

from django.db import models
from django.db.models.signals import post_save, m2m_changed, pre_save
from django.db.models.query_utils import select_related_descend
from django.db.models.signals import post_save
from django.forms import ValidationError
from django.utils import timezone

from dataprofil.models import DataSiswa
import calendar

from .enums import *    

class JenisSarana(models.Model):
    ID = models.BigAutoField(primary_key=True)
    KATEGORI = models.CharField(max_length=255)

    def __str__(self):
        return self.KATEGORI
    
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

    def __str__(self):
        return self.KATEGORI

class Ruangan(models.Model):
    ID = models.BigAutoField(primary_key=True)
    NAMA = models.CharField(max_length=255)
    JENIS = models.ForeignKey(JenisRuangan, on_delete=models.CASCADE)
    STATUS = models.CharField(
        max_length=255,
        choices=ENUM_STATUS_PEMINJAMAN,
        default='Sudah Dikembalikan',
    )
    def __str__(self):
        return self.NAMA  
  
class PengajuanPeminjamanRuangan(models.Model):
    ID = models.BigAutoField(primary_key=True)
    USER = models.ForeignKey(User, on_delete=models.CASCADE)
    PENGGUNA = models.CharField(max_length=255)
    NO_HP = models.CharField(max_length=255)
    KEGIATAN = models.CharField(max_length=255)
    RUANGAN =  models.ForeignKey(Ruangan, on_delete=models.CASCADE)
    TANGGAL_PENGAJUAN = models.DateField(auto_now_add=True)
    TANGGAL_PEMAKAIAN = models.DateField()
    TANGGAL_BERAKHIR = models.DateField()
    JAM_PENGGUNAAN = models.TimeField()
    JAM_BERAKHIR = models.TimeField()
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
    TANDA_TANGAN = models.FileField(max_length=255, upload_to='PeminjamanRuangan', blank=True)


    def clean(self):
        if self.TANGGAL_PENGAJUAN > self.TANGGAL_PEMAKAIAN:
            raise ValidationError('Tidak bisa mengambil hari Sebelumnya')
        if self.TANGGAL_PEMAKAIAN > self.TANGGAL_BERAKHIR :
            raise ValidationError('Tanggal Berakhir Tidak Valid')
        if self.JAM_PENGGUNAAN > self.JAM_BERAKHIR :
            raise ValidationError('Jam Penggunaan Tidak Valid')
        if self.JAM_PENGGUNAAN == self.JAM_BERAKHIR :
            raise ValidationError('Jam Penggunaan Tidak Valid')
        sukses = False
        ruangan = self.RUANGAN
        waktu = self.TANGGAL_PEMAKAIAN
        penggunaan = self.JAM_PENGGUNAAN
        berakhir = self.JAM_BERAKHIR
        hari = calendar.day_name[waktu.weekday()]
        if (ruangan.STATUS != 'Sudah Dikembalikan'):
            obj = RiwayatPeminjamanRuangan.objects.filter(RUANGAN=ruangan)
            for data in obj:
                data_waktu = data.TANGGAL_PEMAKAIAN 
                data_hari = calendar.day_name[data_waktu.weekday()]
                # Jika Hari Penggunaan Sama
                if (hari == data_hari):
                    data_penggunaan = data.JAM_PENGGUNAAN
                    data_berakhir = data.JAM_BERAKHIR
                    # Menghindari konflik jadwal
                    if (penggunaan < data_penggunaan and berakhir < data_penggunaan):
                        sukses = True
                    elif (penggunaan > data_berakhir and berakhir > data_berakhir):
                        sukses = True
                    else:
                        sukses = False
                else: 
                    sukses = True  

            if (not sukses):
                raise ValidationError('Ruangan sudah digunakan, coba pilih waktu pemakaian dan waktu berakhir yang berbeda')

def post_save_pengajuan_peminjaman_ruangan(sender, instance, created, **kwargs):
    try:
        ruangan = instance.RUANGAN 
        ruangan.STATUS = 'Pengajuan'
        ruangan.save()
        
    except Exception as e:
            print(str(e))
        
    if instance.STATUS == 'Sedang Dipinjam':
        try:
            obj = instance.RUANGAN
            obj.STATUS = 'Sedang Dipinjam'
            obj.save()
            # add riwayat peminjaman

            obj = RiwayatPeminjamanRuangan.objects.create(
                USER = instance.USER,
                PENGGUNA = instance.PENGGUNA,
                NO_HP = instance.NO_HP,
                KEGIATAN = instance.KEGIATAN,
                RUANGAN = instance.RUANGAN,
                TANGGAL_PENGAJUAN = instance.TANGGAL_PENGAJUAN,
                TANGGAL_PEMAKAIAN = instance.TANGGAL_PEMAKAIAN,
                TANGGAL_BERAKHIR = instance.TANGGAL_BERAKHIR,
                JAM_PENGGUNAAN = instance.JAM_PENGGUNAAN,
                JAM_BERAKHIR = instance.JAM_BERAKHIR,
                JENIS_PEMINJAMAN = instance.JENIS_PEMINJAMAN,
                STATUS = 'Sedang Dipinjam',
                KETERANGAN = instance.KETERANGAN,
                TANDA_TANGAN = instance.TANDA_TANGAN
            )
            obj.save()
            instance.delete()

        except Exception as e:
            print(str(e))

    elif instance.STATUS == '' or instance.STATUS == 'Ditolak':
        try:
            obj = instance.RUANGAN
            obj.STATUS = 'Selesai Dipinjam'
            obj.save()
            # add riwayat peminjaman

            obj = RiwayatPeminjamanRuangan.objects.create(
                USER = instance.USER,
                PENGGUNA = instance.PENGGUNA,
                NO_HP = instance.NO_HP,
                KEGIATAN = instance.KEGIATAN,
                RUANGAN = instance.RUANGAN,
                TANGGAL_PENGAJUAN = instance.TANGGAL_PENGAJUAN,
                TANGGAL_PEMAKAIAN = instance.TANGGAL_PEMAKAIAN,
                TANGGAL_BERAKHIR = instance.TANGGAL_BERAKHIR,
                JAM_PENGGUNAAN = instance.JAM_PENGGUNAAN,
                JAM_BERAKHIR = instance.JAM_BERAKHIR,
                JENIS_PEMINJAMAN = instance.JENIS_PEMINJAMAN,
                STATUS = 'Ditolak',
                KETERANGAN = instance.KETERANGAN,
                TANDA_TANGAN = instance.TANDA_TANGAN
            )
            obj.save()
            instance.delete()

        except Exception as e:
            print(str(e))

post_save.connect(post_save_pengajuan_peminjaman_ruangan, sender=PengajuanPeminjamanRuangan)


class RiwayatPeminjamanRuangan(models.Model):
    ID = models.BigAutoField(primary_key=True)
    USER = models.ForeignKey(User, on_delete=models.CASCADE)
    PENGGUNA = models.CharField(max_length=255)
    NO_HP = models.CharField(max_length=255)
    KEGIATAN = models.CharField(max_length=255)
    RUANGAN =  models.ForeignKey(Ruangan, on_delete=models.CASCADE)
    TANGGAL_PENGAJUAN = models.DateField(default=timezone.now)
    TANGGAL_PEMAKAIAN = models.DateField(default=timezone.now)
    TANGGAL_BERAKHIR = models.DateField(default=timezone.now)
    JAM_PENGGUNAAN = models.TimeField(default=timezone.now)
    JAM_BERAKHIR = models.TimeField(default=timezone.now)
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
    TANDA_TANGAN = models.FileField(max_length=255, upload_to='PeminjamanRuangan', blank=True)


# def post_save_pengajuan_peminjaman_ruangan(sender, instance, created, **kwargs):
#     # ubah status peminjaman setelah disetujui

#     if instance.STATUS == 'Sedang Dipinjam':
#         try:
#             for data in instance.RUANGAN.values():
#                 obj = JadwalPenggunaanRuangan.objects.get(ID=data['ID'])
#                 obj.STATUS = 'Sedang Dipinjam'
#                 obj.save()
#                 # add riwayat peminjaman
#                 if (instance.JENIS_PEMINJAMAN == 'Jangka Panjang'):
#                     tanggal_pengembalian = datetime.timedelta(weeks=52)
#                 if (instance.JENIS_PEMINJAMAN == 'Jangka Pendek'):
#                     tanggal_pengembalian = datetime.timedelta(weeks=7)


#                 ruangan_m2m = []
#                 for data in instance.RUANGAN.all():
#                     ruangan_m2m.append(data.ID)

#                 obj = RiwayatPeminjamanRuangan.objects.create(
#                     USER = instance.USER,
#                     PENGGUNA = instance.PENGGUNA,
#                     NO_HP = instance.NO_HP,
#                     KEGIATAN = instance.KEGIATAN,
#                     TANGGAL_PENGAJUAN = instance.TANGGAL_PENGAJUAN,
#                     TANGGAL_SELESAI = datetime.date.today() + tanggal_pengembalian,
#                     JENIS_PEMINJAMAN = instance.JENIS_PEMINJAMAN,
#                     STATUS = 'Sedang Dipinjam',
#                     KETERANGAN = instance.KETERANGAN
#                 )
#                 obj.RUANGAN.set(ruangan_m2m)
#                 obj.save()
#                 instance.delete()

#         except Exception as e:
#             print(str(e))

#     elif instance.STATUS == '' or instance.STATUS == 'Ditolak':
#         try:
#             for data in instance.RUANGAN.values():
#                 obj = JadwalPenggunaanRuangan.objects.get(ID=data['ID'])
#                 obj.STATUS = 'Selesai Dipinjam'
#                 obj.save()
#                 # add riwayat peminjaman
#                 if (instance.JENIS_PEMINJAMAN == 'Jangka Panjang'):
#                     tanggal_pengembalian = datetime.timedelta(weeks=52)
#                 if (instance.JENIS_PEMINJAMAN == 'Jangka Pendek'):
#                     tanggal_pengembalian = datetime.timedelta(weeks=7)


#                 ruangan_m2m = []
#                 for data in instance.RUANGAN.all():
#                     ruangan_m2m.append(data.ID)

#                 obj = RiwayatPeminjamanRuangan.objects.create(
#                     USER = instance.USER,
#                     PENGGUNA = instance.PENGGUNA,
#                     NO_HP = instance.NO_HP,
#                     KEGIATAN = instance.KEGIATAN,
#                     TANGGAL_PENGAJUAN = instance.TANGGAL_PENGAJUAN,
#                     TANGGAL_SELESAI = instance.TANGGAL_PENGGUNAAN + tanggal_pengembalian,
#                     JENIS_PEMINJAMAN = instance.JENIS_PEMINJAMAN,
#                     STATUS = 'Ditolak',
#                     KETERANGAN = instance.KETERANGAN
#                 )
#                 obj.RUANGAN.set(ruangan_m2m)
#                 obj.save()
#                 instance.delete()

#         except Exception as e:
#             print(str(e))

# post_save.connect(post_save_pengajuan_peminjaman_ruangan, sender=PengajuanPeminjamanRuangan)

class PengajuanPeminjamanBarang(models.Model):
    ID = models.BigAutoField(primary_key=True)
    USER = models.ForeignKey(User, on_delete=models.CASCADE)
    NAMA_PEMINJAM = models.CharField(max_length=255, default='')
    NO_TELEPON = models.CharField(max_length=255, default='')
    ALAT = models.ManyToManyField(Sarana)
    KEGIATAN = models.CharField(max_length=255)
    TANGGAL_PENGAJUAN = models.DateField(auto_now_add=True)
    TANGGAL_PENGGUNAAN = models.DateField()
    TANGGAL_PENGEMBALIAN = models.DateField()
    KETERANGAN = models.CharField(max_length=255)
    STATUS_PENGAJUAN = models.CharField(
        max_length=255, 
        choices=ENUM_PENGAJUAN,
        default='Pengajuan',
    )
    TANDA_TANGAN = models.FileField(max_length=255, upload_to='PeminjamanBarang', blank=True)
    
    def clean(self):
        if self.TANGGAL_PENGGUNAAN > self.TANGGAL_PENGEMBALIAN:
            raise ValidationError('Tanggal Tidak Valid')
    
class RiwayatPeminjamanBarang(models.Model):
    ID = models.BigAutoField(primary_key=True)
    USER = models.ForeignKey(User, on_delete=models.CASCADE)
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
    TANDA_TANGAN = models.FileField(max_length=255, upload_to='PeminjamanBarang', blank=True)


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
                    USER = instance.USER,
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
                    USER = instance.USER,
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

# def ruangan_changed(sender, instance, action, pk_set=None, **kwargs):
#     if action == 'post_add':
#         for pk in pk_set:
#             obj = JadwalPenggunaanRuangan.objects.get(pk=pk)
#             print('add: ' + str(obj))
#             obj.STATUS = 'Diajukan' 
#             obj.save()

#             ruangan = Ruangan.objects.get(pk=obj.RUANGAN.ID)
#             ruangan.status = 'Pengajuan'
#             ruangan.save()
            
#     elif action == 'post_remove':
#         for pk in pk_set:
#             obj = JadwalPenggunaanRuangan.objects.get(pk=pk)
#             print('delete: ' + str(obj))
#             obj.STATUS = 'Selesai Dipinjam'
#             obj.save()

#             ruangan = Ruangan.objects.get(pk=obj.RUANGAN.ID)
#             ruangan.status = 'Sudah Dikembalikan'
#             ruangan.save()

# m2m_changed.connect(ruangan_changed, sender=PengajuanPeminjamanRuangan.RUANGAN.through)
    

