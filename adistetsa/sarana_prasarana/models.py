from fileinput import filename
from django.contrib.auth.models import User

from django.db import models
from django.db.models.signals import post_save, m2m_changed
from django.forms import ValidationError
import calendar, datetime

from isort import file

from adistetsa.custom_function import *

from .enums import *

# utility
def cek_konflik(awal, tengah, akhir):
    return awal <= tengah <= akhir

def cek_hari_konflik(a_tanggal_pemakaian, b_tanggal_penggunaan, b_tanggal_berakhir):
    a_hari_pemakaian = calendar.day_name[a_tanggal_pemakaian.weekday()]

    b_delta = b_tanggal_berakhir - b_tanggal_penggunaan
    for i in range(b_delta.days + 1):
        tanggal = b_tanggal_penggunaan + datetime.timedelta(days=i)
        b_hari = calendar.day_name[tanggal.weekday()]
        if a_hari_pemakaian == b_hari:
            return True

    return False

def cek_dua_hari_konflik(a_tanggal_pemakaian, b_tanggal_pemakaian):
    a_hari_pemakaian = calendar.day_name[a_tanggal_pemakaian.weekday()]
    b_hari_pemakaian = calendar.day_name[b_tanggal_pemakaian.weekday()]

    return a_hari_pemakaian == b_hari_pemakaian

def cek_jangka_pendek(data):
    # cek pengajuan
    obj_pengajuan = PengajuanPeminjamanRuangan.objects.filter(RUANGAN=data.RUANGAN).exclude(ID=data.ID)
    for diajukan in obj_pengajuan:
        if diajukan.JENIS_PEMINJAMAN == 'Jangka Pendek':
            # cek tanggal pemakaian yang diajukan berada di antara tanggal yang sudah mengajukan duluan
            if cek_konflik(diajukan.TANGGAL_PEMAKAIAN, data.TANGGAL_PEMAKAIAN, diajukan.TANGGAL_BERAKHIR)\
                or cek_konflik(diajukan.TANGGAL_PEMAKAIAN, data.TANGGAL_BERAKHIR, diajukan.TANGGAL_BERAKHIR):

                # Menghindari konflik jam
                if cek_konflik(diajukan.JAM_PENGGUNAAN, data.JAM_PENGGUNAAN, diajukan.JAM_BERAKHIR)\
                    or cek_konflik(diajukan.JAM_PENGGUNAAN, data.JAM_BERAKHIR, diajukan.JAM_BERAKHIR):
                    sukses = False
                else:
                    sukses = True
            else:
                sukses = True
        elif diajukan.JENIS_PEMINJAMAN == 'Jangka Panjang':
            # cek hari pemakaian konflik
            if cek_hari_konflik(diajukan.TANGGAL_PEMAKAIAN, data.TANGGAL_PEMAKAIAN, data.TANGGAL_BERAKHIR):
                # Menghindari konflik jam
                if cek_konflik(diajukan.JAM_PENGGUNAAN, data.JAM_PENGGUNAAN, diajukan.JAM_BERAKHIR)\
                    or cek_konflik(diajukan.JAM_PENGGUNAAN, data.JAM_BERAKHIR, diajukan.JAM_BERAKHIR):
                    sukses = False
                else:
                    sukses = True
            else:
                sukses = True
    
    if not obj_pengajuan:
        sukses = True

    if (not sukses):
        raise ValidationError('Ruangan sudah diajukan pada tanggal yang sama dan jam pemakaian bersinggungan dengan waktu yang dipilih')

    # cek riwayat
    obj_riwayat = RiwayatPeminjamanRuangan.objects.filter(RUANGAN=data.RUANGAN).filter(STATUS='Sedang Dipinjam')
    for riwayat in obj_riwayat:
        if riwayat.JENIS_PEMINJAMAN == 'Jangka Pendek':
            # cek tanggal pemakaian yang diajukan berada di antara tanggal yang sudah meminjam duluan
            if cek_konflik(riwayat.TANGGAL_PEMAKAIAN, data.TANGGAL_PEMAKAIAN, riwayat.TANGGAL_BERAKHIR)\
                or cek_konflik(riwayat.TANGGAL_PEMAKAIAN, data.TANGGAL_BERAKHIR, riwayat.TANGGAL_BERAKHIR):

                # Menghindari konflik jam
                if cek_konflik(riwayat.JAM_PENGGUNAAN, data.JAM_PENGGUNAAN, riwayat.JAM_BERAKHIR)\
                    or cek_konflik(riwayat.JAM_PENGGUNAAN, data.JAM_BERAKHIR, riwayat.JAM_BERAKHIR):
                    sukses = False
                else:
                    sukses = True
            else:
                sukses = True
        elif riwayat.JENIS_PEMINJAMAN == 'Jangka Panjang':
            # cek hari pemakaian konflik
            if cek_hari_konflik(riwayat.TANGGAL_PEMAKAIAN, data.TANGGAL_PEMAKAIAN, data.TANGGAL_BERAKHIR):
                # Menghindari konflik jam
                if cek_konflik(riwayat.JAM_PENGGUNAAN, data.JAM_PENGGUNAAN, riwayat.JAM_BERAKHIR)\
                    or cek_konflik(riwayat.JAM_PENGGUNAAN, data.JAM_BERAKHIR, riwayat.JAM_BERAKHIR):
                    sukses = False
                else:
                    sukses = True
            else:
                sukses = True
    
    if not obj_riwayat:
        sukses = True

    if (not sukses):
        raise ValidationError('Ruangan sudah dipinjam pada tanggal yang sama dan jam pemakaian bersinggungan dengan waktu yang dipilih')

def cek_jangka_panjang(data):
    # cek pengajuan
    obj_pengajuan = PengajuanPeminjamanRuangan.objects.filter(RUANGAN=data.RUANGAN).exclude(ID=data.ID)
    for diajukan in obj_pengajuan:
        if diajukan.JENIS_PEMINJAMAN == 'Jangka Pendek':
            # cek hari pemakaian yang diajukan konflik dengan tanggal yang sudah mengajukan duluan
            if cek_hari_konflik(data.TANGGAL_PEMAKAIAN, diajukan.TANGGAL_PEMAKAIAN, diajukan.TANGGAL_BERAKHIR):

                # Menghindari konflik jam
                if cek_konflik(diajukan.JAM_PENGGUNAAN, data.JAM_PENGGUNAAN, diajukan.JAM_BERAKHIR)\
                    or cek_konflik(diajukan.JAM_PENGGUNAAN, data.JAM_BERAKHIR, diajukan.JAM_BERAKHIR):
                    sukses = False
                else:
                    sukses = True
            else:
                sukses = True
        elif diajukan.JENIS_PEMINJAMAN == 'Jangka Panjang':
            # cek hari pemakaian konflik
            if cek_dua_hari_konflik(data.TANGGAL_PEMAKAIAN, diajukan.TANGGAL_PEMAKAIAN):
                # Menghindari konflik jam
                if cek_konflik(diajukan.JAM_PENGGUNAAN, data.JAM_PENGGUNAAN, diajukan.JAM_BERAKHIR)\
                    or cek_konflik(diajukan.JAM_PENGGUNAAN, data.JAM_BERAKHIR, diajukan.JAM_BERAKHIR):
                    sukses = False
                else:
                    sukses = True
            else:
                sukses = True
    
    if not obj_pengajuan:
        sukses = True

    if (not sukses):
        raise ValidationError('Ruangan sudah diajukan pada hari yang sama dan jam pemakaian bersinggungan dengan waktu yang dipilih')

    # cek riwayat
    obj_riwayat = RiwayatPeminjamanRuangan.objects.filter(RUANGAN=data.RUANGAN).filter(STATUS='Sedang Dipinjam')
    for riwayat in obj_riwayat:
        if riwayat.JENIS_PEMINJAMAN == 'Jangka Pendek':
            # cek hari pemakaian yang diajukan konflik dengan tanggal yang sudah meminjam duluan
            if cek_hari_konflik(data.TANGGAL_PEMAKAIAN, riwayat.TANGGAL_PEMAKAIAN, riwayat.TANGGAL_BERAKHIR):

                # Menghindari konflik jam
                if cek_konflik(riwayat.JAM_PENGGUNAAN, data.JAM_PENGGUNAAN, riwayat.JAM_BERAKHIR)\
                    or cek_konflik(riwayat.JAM_PENGGUNAAN, data.JAM_BERAKHIR, riwayat.JAM_BERAKHIR):
                    sukses = False
                else:
                    sukses = True
            else:
                sukses = True
        elif riwayat.JENIS_PEMINJAMAN == 'Jangka Panjang':
            # cek hari pemakaian konflik
            if cek_dua_hari_konflik(data.TANGGAL_PEMAKAIAN, riwayat.TANGGAL_PEMAKAIAN):
                # Menghindari konflik jam
                if cek_konflik(riwayat.JAM_PENGGUNAAN, data.JAM_PENGGUNAAN, riwayat.JAM_BERAKHIR)\
                    or cek_konflik(riwayat.JAM_PENGGUNAAN, data.JAM_BERAKHIR, riwayat.JAM_BERAKHIR):
                    sukses = False
                else:
                    sukses = True
            else:
                sukses = True
    
    if not obj_riwayat:
        sukses = True

    if (not sukses):
        raise ValidationError('Ruangan sudah dipinjam pada hari yang sama dan jam pemakaian bersinggungan dengan waktu yang dipilih')



# Model
class JenisSarana(models.Model):
    ID = models.BigAutoField(primary_key=True)
    KATEGORI = models.CharField(max_length=255, validators=[cek_huruf_besar_awal_kalimat])

    def __str__(self):
        return self.KATEGORI
    
class Sarana(models.Model):
    ID = models.BigAutoField(primary_key=True)
    NAMA = models.CharField(max_length=255, validators=[cek_huruf_besar_awal_kalimat])
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
    KATEGORI = models.CharField(max_length=255, validators=[cek_huruf_besar_awal_kalimat])

    def __str__(self):
        return self.KATEGORI

class Ruangan(models.Model):
    ID = models.BigAutoField(primary_key=True)
    NAMA = models.CharField(max_length=255, validators=[cek_huruf_besar_awal_kalimat])
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
    PENGGUNA = models.CharField(max_length=255, validators=[paksa_huruf_besar])
    NO_HP = models.CharField(max_length=255, validators=[validasi_integer])
    KEGIATAN = models.CharField(max_length=255)
    RUANGAN =  models.ForeignKey(Ruangan, on_delete=models.CASCADE)
    TANGGAL_PENGAJUAN = models.DateField(default=datetime.date.today)
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
        if self.TANGGAL_PEMAKAIAN > self.TANGGAL_BERAKHIR :
            raise ValidationError('Tanggal Pemakaian tidak boleh lebih dari Tanggal Berakhir')
        if self.JAM_PENGGUNAAN > self.JAM_BERAKHIR :
            raise ValidationError('Jam Penggunaan tidak boleh lebih dari Jam Berakhir')
        if self.JAM_PENGGUNAAN == self.JAM_BERAKHIR :
            raise ValidationError('Jam Penggunaan tidak boleh sama dengan Jam Berakhir')

        if self.JENIS_PEMINJAMAN == 'Jangka Pendek':
            cek_jangka_pendek(self)
        elif self.JENIS_PEMINJAMAN == 'Jangka Panjang':
            cek_jangka_panjang(self)
        else:
            raise ValidationError('Jenis Peminjaman tidak valid')


    def save(self, *args, **kwargs):
        self.full_clean()

        return super().save(*args, **kwargs)


def post_save_pengajuan_peminjaman_ruangan(sender, instance, created, **kwargs):        
    if instance.STATUS == 'Sedang Dipinjam':
        try:
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
                TANDA_TANGAN = duplikat_file(instance, instance.TANDA_TANGAN.read(), instance.TANDA_TANGAN.name),
            )
            obj.save()
            instance.delete()

        except Exception as e:
            print(str(e))

    elif instance.STATUS == '' or instance.STATUS == 'Ditolak':
        try:
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
    TANGGAL_PENGAJUAN = models.DateField()
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


class PengajuanPeminjamanBarang(models.Model):
    ID = models.BigAutoField(primary_key=True)
    USER = models.ForeignKey(User, on_delete=models.CASCADE)
    NAMA_PEMINJAM = models.CharField(max_length=255, default='')
    NO_TELEPON = models.CharField(max_length=255, default='')
    ALAT = models.ManyToManyField(Sarana)
    KEGIATAN = models.CharField(max_length=255)
    TANGGAL_PENGAJUAN = models.DateField(default=datetime.date.today)
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
    TANGGAL_PENGAJUAN = models.DateField()
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
                    TANGGAL_PENGAJUAN = instance.TANGGAL_PENGAJUAN,
                    TANGGAL_PENGGUNAAN = instance.TANGGAL_PENGGUNAAN,
                    TANGGAL_PENGEMBALIAN = instance.TANGGAL_PENGEMBALIAN,
                    KETERANGAN = instance.KETERANGAN,
                    TANDA_TANGAN = duplikat_file(instance, instance.TANDA_TANGAN.read(), instance.TANDA_TANGAN.name),
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
                    TANGGAL_PENGAJUAN = instance.TANGGAL_PENGAJUAN,
                    TANGGAL_PENGGUNAAN = instance.TANGGAL_PENGGUNAAN,
                    TANGGAL_PENGEMBALIAN = instance.TANGGAL_PENGEMBALIAN,
                    KETERANGAN = instance.KETERANGAN,
                    STATUS_PEMINJAMAN = 'Ditolak',
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
    

