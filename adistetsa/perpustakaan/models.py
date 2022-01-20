from ast import mod
from pyexpat import model
from tkinter import CASCADE
from typing import DefaultDict
from typing_extensions import Required
from unittest.mock import DEFAULT
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.db.models.query_utils import select_related_descend
from dataprofil.models import DataGuru, DataSiswa
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
import datetime

from .enums import *



# Create your models here.

class TipeBahasa(models.Model):
    ID = models.BigAutoField(primary_key=True)
    KODE_BAHASA = models.CharField(max_length=255)
    BAHASA = models.CharField(max_length=255)
    
    def __str__(self):
        return self.KODE_BAHASA + ' - ' + self.BAHASA
        
class TipeBuku(models.Model):
    ID = models.BigAutoField(primary_key=True)
    KODE_TIPE = models.CharField(max_length = 255,)
    NAMA_TIPE = models.CharField(max_length = 255,)
    LAMA_PINJAM = models.BigIntegerField()
    DENDA = models.CharField(max_length = 255, blank=True)
    
    def __str__(self):
        return self.KODE_TIPE + ' - '  + self.NAMA_TIPE  
    
class Pendanaan(models.Model):
    ID = models.BigAutoField(primary_key=True)
    KODE_PENDANAAN = models.CharField(max_length = 255)
    NAMA_PENDANAAN = models.CharField(max_length = 255)
    
    def __str__(self):
        return self.NAMA_PENDANAAN
    
    
    
class Lokasi(models.Model):
    ID = models.BigAutoField(primary_key=True)
    KODE_LOKASI = models.CharField(max_length = 255)
    NAMA_LOKASI = models.CharField(max_length = 255)
    def __str__(self):
        return self.KODE_LOKASI + ' - ' + self.NAMA_LOKASI
    
class LokasiSpesifik(models.Model):
    ID = models.BigAutoField(primary_key=True)
    LOKASI_SPESIFIK = models.CharField(max_length = 255)
    NAMA = models.CharField(max_length = 255)
    
    def __str__(self):
        return self.LOKASI_SPESIFIK + ' ' + self.NAMA

class KunjunganSiswa(models.Model): 
    NIS = models.ForeignKey(DataSiswa, on_delete=models.CASCADE)
    TANGGAL_KUNJUNGAN = models.DateField()
    
class KunjunganGuru(models.Model):
    NIP = models.ForeignKey(DataGuru, on_delete=models.CASCADE)
    TANGGAL_KUNJUNGAN = models.DateField()
    
class TipeMedia(models.Model):
    ID = models.BigAutoField(primary_key=True)
    KODE_MEDIA = models.CharField(max_length = 255)
    NAMA_MEDIA = models.CharField(max_length = 255)
    
    def __str__(self):
        return str(self.KODE_MEDIA) + ' - ' + self.NAMA_MEDIA
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['KODE_MEDIA', 'NAMA_MEDIA'], name='%(app_label)s_%(class)s_unique')
        ]
        verbose_name_plural = "TIPE MEDIA"
    
class Operator(models.Model):
    ID = models.BigAutoField(primary_key=True)
    KODE_OPERATOR = models.ForeignKey(User, on_delete=models.CASCADE)
    # PASSWORD = models.CharField(max_length = 255)
    # NAMA_OPERATOR = models.CharField(max_length = 255)
    # NAMA_LENGKAP = models.CharField(max_length = 255)
    UNIT = models.CharField(max_length = 255)
    # PATRON_ACC = models.CharField(
    #     max_length = 255,
    #     choices=ENUM_PATRON_ACC,
    # )
    # BOOK_ACC = models.CharField(
    #     max_length = 255,
    #     choices=ENUM_BOOK_ACC,
    # )
    # SCIENCE_ACC = models.CharField(
    #     max_length = 255,
    #     choices=ENUM_SCIENCE_ACC,
    # )
    # SERIAL_ACC = models.CharField(
    #     max_length = 255,
    #     choices=ENUM_SERIAL_ACC,
    # )
    # CIRCULATION_ACC = models.CharField(
    #     max_length = 255,
    #     choices=ENUM_CIRCULATION_ACC,
    # )
    # HAK_NEGO_DENDA = models.CharField(
    #     max_length = 255,
    #     choices=ENUM_HAK_NEGO_DENDA,
    # )
    # HAK_KATALOG = models.CharField(
    #     max_length = 255,
    #     choices=ENUM_HAK_KATALOG,
    # )
    # HAK_ABSENSI = models.CharField(
    #     max_length = 255,
    #     choices=ENUM_HAK_ABSENSI,
    # )
    
    # object_id = models.PositiveIntegerField()
    # content_object = GenericForeignKey('KODE_OPERATOR', 'object_id')
    def __str__(self):
        return str(self.KODE_OPERATOR)
        


class Author(models.Model):
    ID = models.BigAutoField(primary_key=True)
    KODE_AUTHOR = models.CharField(max_length=255)
    NAMA_AUTHOR = models.CharField(max_length=255)
    
    def __str__(self):
        return self.KODE_AUTHOR + ' - ' + self.NAMA_AUTHOR

class TahunTerbit(models.Model):
    ID = models.BigAutoField(primary_key=True)
    TAHUN_TERBIT = models.PositiveBigIntegerField()
    
    def __str__(self):
        return str(self.TAHUN_TERBIT)
    
# class DeskripsiFisik(models.Model):
#     ID = models.BigAutoField(primary_key=True)
#     JUMLAH_HALAMAN = models.PositiveBigIntegerField(blank=True)
#     TEBAL_BUKU = models.PositiveBigIntegerField(blank=True)
    
#     def __str__(self):
#         return str(self.JUMLAH_HALAMAN) + ' Hlm, Tebal ' + str(self.TEBAL_BUKU) + ' CM'
    
class KatalogBuku(models.Model):
    REGISTER = models.CharField(primary_key=True, max_length = 255)
    ISBN = models.CharField(max_length = 255, blank=True)
    JUDUL = models.CharField(max_length = 255)
    VOLUME = models.CharField(max_length = 255, blank=True)
    EDISI = models.CharField(max_length = 255, blank=True)
    BAHASA = models.ForeignKey(TipeBahasa, on_delete=models.CASCADE)
    DUPLIKAT = models.BigIntegerField()
    KODE_MEDIA = models.ForeignKey(TipeMedia, on_delete=models.CASCADE)
    TIPE_KODE = models.ForeignKey(TipeBuku, on_delete=models.CASCADE)
    NOMER_DEWEY = models.CharField(max_length = 255)
    KODE_AUTHOR = models.ForeignKey(Author, on_delete=models.CASCADE)
    KODE_JUDUL = models.CharField(max_length = 255, blank=True)
    TAHUN_TERBIT = models.ForeignKey(TahunTerbit, on_delete=models.CASCADE)
    KOTA_PENERBIT = models.CharField(max_length = 255)
    PENERBIT = models.CharField(max_length = 255)
    DESKRIPSI_FISIK = models.CharField(max_length = 255)
    INDEX = models.CharField(max_length = 255)
    BIBLIOGRAPHY = models.CharField(max_length = 255, blank=True)
    KODE_LOKASI = models.ForeignKey(Lokasi, on_delete=models.CASCADE)
    LOKASI_SPESIFIK = models.ForeignKey(LokasiSpesifik, on_delete=models.CASCADE)
    HARGA = models.CharField(max_length = 255)
    KODE_DONASI = models.ForeignKey(Pendanaan, on_delete=models.CASCADE)
    CATATAN_DONASI = models.CharField(max_length = 255)
    TANGGAL_PENERIMAAN = models.DateField(max_length = 255)
    DATA_ENTRY = models.DateField(max_length = 255)
    OPERATOR_CODE = models.ForeignKey(Operator, on_delete=models.CASCADE)    
    
    def __str__(self):
        return self.JUDUL

    
    class Meta:
        verbose_name_plural = "Data Book Main"

class KatalogBukuCopy(models.Model):
    DATA_BUKU = models.ForeignKey(KatalogBuku, on_delete=models.CASCADE)
    REGISTER_COPY = models.CharField(max_length=255)
    STATUS = models.CharField(
        max_length=255,
        choices=ENUM_STATUS_PEMINJAMAN,
        default='Sudah Dikembalikan',
    )
    def __str__(self):
        return '"' + self.DATA_BUKU.JUDUL + '"' + ' - ' + self.REGISTER_COPY
    
def post_save_katalog_buku(sender, instance, **kwargs):
    try:
        # hapus duplikat
        KatalogBukuCopy.objects.filter(DATA_BUKU = instance.REGISTER).delete()
        
        jumlah_duplikat = instance.DUPLIKAT
        for i in range(jumlah_duplikat):
            buku_copy = KatalogBukuCopy.objects.create(
                DATA_BUKU_id = instance.REGISTER,
                REGISTER_COPY = instance.REGISTER + str(i + 1)
            )
            buku_copy.save()
    except Exception as e:
        print(str(e))

post_save.connect(post_save_katalog_buku, sender=KatalogBuku)
            
class PeminjamanSiswaPendek (models.Model):
    ID = models.BigAutoField(primary_key=True)
    NIS = models.ForeignKey(DataSiswa, on_delete=models.CASCADE)
    BUKU = models.ManyToManyField(KatalogBukuCopy)
    TANGGAL_PEMINJAMAN = models.DateField()
    TANGGAL_KEMBALI = models.DateField()
    STATUS_PENGAJUAN = models.CharField(
        max_length = 255,
        choices=ENUM_PENGAJUAN
    )
    STATUS_PEMINJAMAN = models.CharField(
        max_length=255,
        blank=True,
        choices=ENUM_STATUS_PEMINJAMAN
    )
    STATUS_CETAKAN = models.CharField(
        max_length = 255,
        choices=ENUM_IS_PRINTED
    )
    OPERATOR = models.ForeignKey(Operator, on_delete=models.CASCADE)
    
    


class PengajuanPeminjamanSiswa(models.Model):
    ID = models.BigAutoField(primary_key=True)
    NIS = models.ForeignKey(DataSiswa, on_delete=models.CASCADE)
    BUKU = models.ManyToManyField(KatalogBukuCopy)
    TANGGAL_PENGAJUAN = models.DateField()
    STATUS_PENGAJUAN = models.CharField(
        max_length=255, 
        choices=ENUM_PENGAJUAN,
        default='Diajukan',
    )
    JANGKA_PEMINJAMAN = models.CharField(
        max_length=255,
        choices=ENUM_JANGKA_PEMINJAMAN,
        blank=True, 
    )
    FILE_TTD_PENGAJUAN = models.FileField(max_length=255, upload_to='Dokumen_Peminjaman_Jangka_Panjang_Siswa', blank=True)
    
    


class RiwayatPeminjamanSiswa(models.Model):
    ID = models.BigAutoField(primary_key=True)
    NIS = models.ForeignKey(DataSiswa, on_delete=models.CASCADE)
    BUKU = models.ManyToManyField(KatalogBukuCopy)
    TANGGAL_PEMINJAMAN = models.DateField()
    TANGGAL_PENGEMBALIAN = models.DateField()
    JANGKA_PEMINJAMAN = models.CharField(
        max_length=255,
        choices=ENUM_JANGKA_PEMINJAMAN,
        blank=True, 
    )
    FILE_TTD_PENGAJUAN = models.FileField(max_length=255, upload_to='Dokumen_Peminjaman_Jangka_Panjang_Siswa', blank=True)
    STATUS_PEMINJAMAN = models.CharField(
        max_length=255,
        choices=ENUM_STATUS_PEMINJAMAN,
        default= 'Sedang Dipinjam'
    )
    

def post_save_pengajuan_peminjaman_siswa(sender, instance, **kwargs):
    # ubah status peminjaman setelah disetujui
    if instance.STATUS_PENGAJUAN == 'Disetujui':
        try:
            for data in instance.BUKU.values():
                obj = KatalogBukuCopy.objects.get(REGISTER_COPY=data['REGISTER_COPY'])
                obj.STATUS = 'Sedang Dipinjam'
                obj.save()
                
                # add riwayat peminjaman
                if (instance.JANGKA_PEMINJAMAN == 'Jangka Pendek'):
                    tanggal_pengembalian = datetime.timedelta(weeks=1)
                elif (instance.JANGKA_PEMINJAMAN == 'Jangka Panjang'):
                    tanggal_pengembalian = datetime.timedelta(weeks=52)
                    
                    
                buku_m2m = []
                for data in instance.BUKU.all():
                    buku_m2m.append(data.id)
                
                obj = RiwayatPeminjamanSiswa.objects.create(
                    NIS = instance.NIS,
                    TANGGAL_PEMINJAMAN = datetime.date.today(),
                    TANGGAL_PENGEMBALIAN = datetime.date.today() + tanggal_pengembalian,
                    JANGKA_PEMINJAMAN = instance.JANGKA_PEMINJAMAN,
                    FILE_TTD_PENGAJUAN = instance.FILE_TTD_PENGAJUAN
                )
                obj.BUKU.set(buku_m2m)
                obj.save()
                instance.delete()
                    
        except Exception as e:
            print(str(e))
            
    elif instance.STATUS_PENGAJUAN == '' or instance.STATUS_PENGAJUAN == 'Pengajuan' or instance.STATUS_PENGAJUAN == 'Ditolak':
        try:
            for data in instance.BUKU.values():
                obj = KatalogBukuCopy.objects.get(REGISTER_COPY=data['REGISTER_COPY'])
                obj.STATUS = 'Sudah Dikembalikan'
                obj.save()
                instance.delete()
                    
        except Exception as e:
            print(str(e))
    
    

post_save.connect(post_save_pengajuan_peminjaman_siswa, sender=PengajuanPeminjamanSiswa)

class PengajuanPeminjamanGuru(models.Model):
    ID = models.BigAutoField(primary_key=True)
    DATA_GURU = models.ForeignKey(DataGuru, on_delete=models.CASCADE)
    BUKU = models.ManyToManyField(KatalogBukuCopy)
    TANGGAL_PENGAJUAN = models.DateField()
    STATUS_PENGAJUAN = models.CharField(
        max_length=255, 
        choices=ENUM_PENGAJUAN,
        default='Diajukan',
    )
    JANGKA_PEMINJAMAN = models.CharField(
        max_length=255,
        choices=ENUM_JANGKA_PEMINJAMAN,
        blank=True, 
    )
    FILE_TTD_PENGAJUAN = models.FileField(max_length=255, upload_to='Dokumen_Peminjaman_Jangka_Panjang_Guru', blank=True)
    
    


class RiwayatPeminjamanGuru(models.Model):
    ID = models.BigAutoField(primary_key=True)
    DATA_GURU = models.ForeignKey(DataGuru, on_delete=models.CASCADE)
    BUKU = models.ManyToManyField(KatalogBukuCopy)
    TANGGAL_PEMINJAMAN = models.DateField()
    TANGGAL_PENGEMBALIAN = models.DateField()
    JANGKA_PEMINJAMAN = models.CharField(
        max_length=255,
        choices=ENUM_JANGKA_PEMINJAMAN,
        blank=True, 
    )
    FILE_TTD_PENGAJUAN = models.FileField(max_length=255, upload_to='Dokumen_Peminjaman_Jangka_Panjang_Guru', blank=True)
    STATUS_PEMINJAMAN = models.CharField(
        max_length=255,
        choices=ENUM_STATUS_PEMINJAMAN,
        default= 'Sedang Dipinjam'
    )
    

def post_save_pengajuan_peminjaman_guru(sender, instance, **kwargs):
    # ubah status peminjaman setelah disetujui
    if instance.STATUS_PENGAJUAN == 'Disetujui':
        try:
            for data in instance.BUKU.values():
                obj = KatalogBukuCopy.objects.get(REGISTER_COPY=data['REGISTER_COPY'])
                obj.STATUS = 'Sedang Dipinjam'
                obj.save()
                
                # add riwayat peminjaman
                if (instance.JANGKA_PEMINJAMAN == 'Jangka Pendek'):
                    tanggal_pengembalian = datetime.timedelta(weeks=1)
                elif (instance.JANGKA_PEMINJAMAN == 'Jangka Panjang'):
                    tanggal_pengembalian = datetime.timedelta(weeks=52)
                    
                    
                buku_m2m = []
                for data in instance.BUKU.all():
                    buku_m2m.append(data.id)
                
                obj = RiwayatPeminjamanGuru.objects.create(
                    DATA_GURU = instance.DATA_GURU,
                    TANGGAL_PEMINJAMAN = datetime.date.today(),
                    TANGGAL_PENGEMBALIAN = datetime.date.today() + tanggal_pengembalian,
                    JANGKA_PEMINJAMAN = instance.JANGKA_PEMINJAMAN,
                    FILE_TTD_PENGAJUAN = instance.FILE_TTD_PENGAJUAN
                )
                obj.BUKU.set(buku_m2m)
                obj.save()
                instance.delete()
                    
        except Exception as e:
            print(str(e))
            
    elif instance.STATUS_PENGAJUAN == '' or instance.STATUS_PENGAJUAN == 'Pengajuan' or instance.STATUS_PENGAJUAN == 'Ditolak':
        try:
            for data in instance.BUKU.values():
                obj = KatalogBukuCopy.objects.get(REGISTER_COPY=data['REGISTER_COPY'])
                obj.STATUS = 'Sudah Dikembalikan'
                obj.save()
                instance.delete()
                    
        except Exception as e:
            print(str(e))

post_save.connect(post_save_pengajuan_peminjaman_guru, sender=PengajuanPeminjamanGuru)



class LoanSiswaPanjang(models.Model):
    ID = models.BigAutoField(primary_key=True)
    NIS = models.ForeignKey(DataSiswa, on_delete=models.CASCADE)
    KELAS = models.CharField(max_length = 255, default='')
    ALAMAT = models.CharField(max_length = 255, default='')
    TANGGAL_PINJAM = models.CharField(max_length = 255, default='')
    REGISTER = models.ForeignKey(KatalogBuku, on_delete=models.CASCADE, default='')
    NO_BARCODE = models.CharField(max_length = 255, default='')
    JUMLAH = models.CharField(max_length = 255, default='')
    TANDA_TANGAN = models.CharField(max_length = 255, default='')
    KETERANGAN = models.CharField(max_length = 255, default='')
    LOAN_STATUS = models.CharField(
        max_length = 255,
        choices=ENUM_LOAN_STATUS
    )
    IS_PRINTED = models.CharField(
        max_length = 255,
        choices=ENUM_IS_PRINTED
    )
    OPERATOR_CODE = models.ForeignKey(Operator, on_delete=models.CASCADE)
    
class LoanGuruPendek (models.Model):
    ID = models.BigAutoField(primary_key=True)
    REGISTER = models.ManyToManyField(KatalogBuku)
    NIP = models.ForeignKey(DataGuru, on_delete=models.CASCADE)
    OUT_DATE = models.DateField()
    DUE_DATE = models.DateField()
    LOAN_STATUS = models.CharField(
        max_length = 255,
        choices=ENUM_LOAN_STATUS
    )
    IS_PRINTED = models.CharField(
        max_length = 255,
        choices=ENUM_IS_PRINTED
    )
    OPERATOR_CODE = models.ForeignKey(Operator, on_delete=models.CASCADE)

class LoanGuruPanjang (models.Model):
    ID = models.BigAutoField(primary_key=True)
    NIP = models.ForeignKey(DataGuru, on_delete=models.CASCADE)
    KELAS = models.CharField(max_length = 255, default='')
    ALAMAT = models.CharField(max_length = 255, default='')
    TANGGAL_PINJAM = models.CharField(max_length = 255, default='')
    REGISTER = models.ForeignKey(KatalogBuku, on_delete=models.CASCADE, default='')
    NO_BARCODE = models.CharField(max_length = 255, default='')
    JUMLAH = models.CharField(max_length = 255, default='')
    TANDA_TANGAN = models.CharField(max_length = 255, default='')
    KETERANGAN = models.CharField(max_length = 255, default='')
    LOAN_STATUS = models.CharField(
        max_length = 255,
        choices=ENUM_LOAN_STATUS
    )
    IS_PRINTED = models.CharField(
        max_length = 255,
        choices=ENUM_IS_PRINTED
    )
    OPERATOR_CODE = models.ForeignKey(Operator, on_delete=models.CASCADE)
    
class Abstrak (models.Model):
    REGISTER = models.ForeignKey(KatalogBuku,on_delete=models.CASCADE)
    ABSTRAK = models.CharField(max_length=255)