from wsgiref.validate import validator
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save, m2m_changed
from django.db.models.query_utils import select_related_descend
from django.db.models.signals import post_save

from utility.custom_function import *

from dataprofil.models import DataGuru, DataSiswa
import datetime

from .enums import *


# Create your models here.

class TipeBahasa(models.Model):
    KODE_BAHASA = models.CharField(primary_key=True, max_length=255)
    BAHASA = models.CharField(max_length=255, validators=[cek_huruf_besar_awal_kalimat])
    
    class Meta:
        verbose_name_plural = "Tipe Bahasa"

    def __str__(self):
        return self.KODE_BAHASA + ' - ' + self.BAHASA
        
class TipeBuku(models.Model):
    KODE_TIPE = models.CharField(primary_key=True, max_length = 255,)
    NAMA_TIPE = models.CharField(max_length = 255, validators=[cek_huruf_besar_awal_kalimat])
    
    class Meta:
        verbose_name_plural = "Tipe Buku"

    def __str__(self):
        return self.KODE_TIPE + ' - '  + self.NAMA_TIPE  
    
class Pendanaan(models.Model):
    KODE_PENDANAAN = models.CharField(primary_key=True, max_length = 255)
    NAMA_PENDANAAN = models.CharField(max_length = 255, validators=[cek_huruf_besar_awal_kalimat])
    
    class Meta:
        verbose_name_plural = "Pendanaan"

    def __str__(self):
        return self.NAMA_PENDANAAN
    
class Lokasi(models.Model):
    KODE_LOKASI = models.CharField(primary_key=True, max_length = 255)
    NAMA_LOKASI = models.CharField(max_length = 255, validators=[cek_huruf_besar_awal_kalimat])
    
    class Meta:
        verbose_name_plural = "Lokasi"

    def __str__(self):
        return self.KODE_LOKASI + ' - ' + self.NAMA_LOKASI
    
class LokasiSpesifik(models.Model):
    LOKASI_SPESIFIK = models.CharField(primary_key=True, max_length = 255)
    NAMA = models.CharField(max_length = 255,)
    
    class Meta:
        verbose_name_plural = "Lokasi Spesifik"

    def __str__(self):
        return self.LOKASI_SPESIFIK + ' ' + self.NAMA

class KunjunganSiswa(models.Model): 
    NIS = models.ForeignKey(DataSiswa, on_delete=models.CASCADE)
    TANGGAL_KUNJUNGAN = models.DateField(default=datetime.date.today)
    
    class Meta:
        verbose_name_plural = "Kunjungan Siswa"

class KunjunganGuru(models.Model):
    NIP = models.ForeignKey(DataGuru, on_delete=models.CASCADE)
    TANGGAL_KUNJUNGAN = models.DateField(default=datetime.date.today)
    
    class Meta:
        verbose_name_plural = "Kunjungan Guru"

class TipeMedia(models.Model):
    KODE_MEDIA = models.CharField(primary_key=True, max_length = 255)
    NAMA_MEDIA = models.CharField(max_length = 255,)

    def __str__(self):
        return str(self.KODE_MEDIA) + ' - ' + self.NAMA_MEDIA
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['KODE_MEDIA', 'NAMA_MEDIA'], name='%(app_label)s_%(class)s_unique')
        ]
        verbose_name_plural = "Tipe Media"
    
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
    
    class Meta:
        verbose_name_plural = "Operator"

    def __str__(self):
        return str(self.KODE_OPERATOR)
        


class Author(models.Model):
    KODE_AUTHOR = models.CharField(primary_key=True, max_length=255)
    NAMA_AUTHOR = models.CharField(max_length=255, validators=[cek_huruf_besar_awal_kalimat])
    
    class Meta:
        verbose_name_plural = "Author"

    def __str__(self):
        return self.KODE_AUTHOR + ' - ' + self.NAMA_AUTHOR

class TahunTerbit(models.Model):
    TAHUN_TERBIT = models.CharField(primary_key=True, max_length=255)
    
    class Meta:
        verbose_name_plural = "Tahun Terbit"

    def __str__(self):
        return str(self.TAHUN_TERBIT)
    
# class DeskripsiFisik(models.Model):
#     ID = models.BigAutoField(primary_key=True)
#     JUMLAH_HALAMAN = models.PositiveBigIntegerField(blank=True)
#     TEBAL_BUKU = models.PositiveBigIntegerField(blank=True)
    
#     def __str__(self):
#         return str(self.JUMLAH_HALAMAN) + ' Hlm, Tebal ' + str(self.TEBAL_BUKU) + ' CM'


    
class KatalogBuku(models.Model):
    REGISTER = models.CharField(primary_key=True, max_length = 255, validators=[validasi_integer])
    ISBN = models.CharField(max_length = 255, blank=True, )
    JUDUL = models.CharField(max_length = 255, )
    VOLUME = models.CharField(max_length = 255, validators=[validasi_integer])
    EDISI = models.CharField(max_length = 255, validators=[validasi_integer])
    BAHASA = models.ForeignKey(TipeBahasa, on_delete=models.CASCADE)
    KODE_MEDIA = models.ForeignKey(TipeMedia, on_delete=models.CASCADE)
    KODE_TIPE = models.ForeignKey(TipeBuku, on_delete=models.CASCADE)
    NOMER_DEWEY = models.CharField(max_length = 255, )
    KODE_AUTHOR = models.ForeignKey(Author, on_delete=models.CASCADE)
    KODE_JUDUL = models.CharField(max_length = 255, blank=True)
    TAHUN_TERBIT = models.ForeignKey(TahunTerbit, on_delete=models.CASCADE)
    KOTA_PENERBIT = models.CharField(max_length = 255, validators=[cek_huruf_besar_awal_kalimat])
    PENERBIT = models.CharField(max_length = 255, )
    DESKRIPSI_FISIK = models.CharField(max_length = 255)
    INDEX = models.CharField(max_length = 255, blank=True)
    BIBLIOGRAPHY = models.CharField(max_length = 255, blank=True)
    KODE_LOKASI = models.ForeignKey(Lokasi, on_delete=models.CASCADE)
    LOKASI_SPESIFIK = models.ForeignKey(LokasiSpesifik, on_delete=models.CASCADE)
    HARGA = models.CharField(max_length = 255, )
    DATA_ENTRY = models.DateField(max_length = 255, default=datetime.date.today)
    OPERATOR_CODE = models.ForeignKey(Operator, on_delete=models.CASCADE)    
    
    def __str__(self):
        return self.JUDUL

    class Meta:
        verbose_name_plural = "Katalog Buku"

class DonasiBuku (models.Model):
    REGISTER_DONASI = models.ForeignKey(KatalogBuku, on_delete=models.CASCADE)
    DUPLIKAT = models.PositiveBigIntegerField()
    KODE_DONASI = models.ForeignKey(Pendanaan, on_delete=models.CASCADE)
    TANGGAL_PENERIMAAN = models.DateField(max_length = 255, default=datetime.date.today)
    CATATAN_DONASI = models.CharField(max_length = 255)

    class Meta:
        verbose_name_plural = "Donasi Buku"
    
    def __str__(self):
        return str(self.REGISTER_DONASI.JUDUL)
    

class KatalogBukuCopy(models.Model):
    DATA_DONASI = models.ForeignKey(DonasiBuku, on_delete=models.CASCADE)
    REGISTER_COPY = models.CharField(max_length=255)
    STATUS = models.CharField(
        max_length=255,
        choices=ENUM_STATUS_PEMINJAMAN,
        default='Sudah Dikembalikan',
    )
    
    class Meta:
        verbose_name_plural = "Katalog Buku Copy"

    def __str__(self):
        return str(self.REGISTER_COPY) + ' - ' + str(self.DATA_DONASI.REGISTER_DONASI.JUDUL)
    
def post_save_donasi_buku(sender, instance, **kwargs):
    try:
        donasi_buku = DonasiBuku.objects.filter(REGISTER_DONASI=instance.REGISTER_DONASI)
        jumlah_buku = []
        for data in donasi_buku:
            print('Ini adalah ' + data.REGISTER_DONASI.JUDUL)
            jumlah_buku.append({'data_donasi': data.id, 'jumlah': data.DUPLIKAT})
            
        last_index = 1
        for data in jumlah_buku:
            for i in range(data['jumlah']):
                if data['data_donasi'] == instance.id:
                    buku_copy = KatalogBukuCopy.objects.update_or_create(
                        DATA_DONASI_id = data['data_donasi'],
                        REGISTER_COPY = str(instance.REGISTER_DONASI_id) + str(last_index)
                    )
                last_index += 1
    except Exception as e:
        print(str(e))

post_save.connect(post_save_donasi_buku, sender=DonasiBuku)
            

class PengajuanPeminjamanSiswa(models.Model):
    ID = models.BigAutoField(primary_key=True)
    NIS = models.ForeignKey(DataSiswa, on_delete=models.CASCADE)
    BUKU = models.ManyToManyField(KatalogBukuCopy)
    TANGGAL_PENGAJUAN = models.DateField(default=datetime.date.today)
    STATUS_PENGAJUAN = models.CharField(
        max_length=255,
        choices=ENUM_PENGAJUAN,
        default='Pengajuan',
    )
    JANGKA_PEMINJAMAN = models.CharField(
        max_length=255,
        choices=ENUM_JANGKA_PEMINJAMAN,
        blank=True,
    )
    FILE_TTD_PENGAJUAN = models.FileField(max_length=255, upload_to='Dokumen_Peminjaman_Jangka_Panjang_Siswa', blank=True)
    
    class Meta:
        verbose_name_plural = "Pengajuan Peminjaman Siswa"


class RiwayatPeminjamanSiswa(models.Model):
    ID = models.BigAutoField(primary_key=True)
    NIS = models.ForeignKey(DataSiswa, on_delete=models.CASCADE)
    BUKU = models.ManyToManyField(KatalogBukuCopy)
    TANGGAL_PEMINJAMAN = models.DateField(default=datetime.date.today)
    TANGGAL_PENGEMBALIAN = models.DateField(default=datetime.date.today)
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
    
    
    class Meta:
        verbose_name_plural = "Riwayat Peminjaman Siswa"

def post_save_pengajuan_peminjaman_siswa(sender, instance, created, **kwargs):
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
                )
                obj.BUKU.set(buku_m2m)
                
                if instance.JANGKA_PEMINJAMAN == 'Jangka Panjang' and instance.FILE_TTD_PENGAJUAN:
                    obj.FILE_TTD_PENGAJUAN = duplikat_file(instance, instance.FILE_TTD_PENGAJUAN.read(), instance.FILE_TTD_PENGAJUAN.name)

                obj.save()

                instance.delete()
                    
        except Exception as e:
            print(str(e))
            
    elif instance.STATUS_PENGAJUAN == '' or instance.STATUS_PENGAJUAN == 'Ditolak':
        try:
            for data in instance.BUKU.values():
                obj = KatalogBukuCopy.objects.get(REGISTER_COPY=data['REGISTER_COPY'])
                obj.STATUS = 'Sudah Dikembalikan'
                obj.save()
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
                    STATUS_PEMINJAMAN = 'Ditolak',
                )
                obj.BUKU.set(buku_m2m)
                obj.save()
                instance.delete()
                    
        except Exception as e:
            print(str(e))

post_save.connect(post_save_pengajuan_peminjaman_siswa, sender=PengajuanPeminjamanSiswa)

def buku_changed_siswa(sender, instance, action, pk_set=None, **kwargs):
    if action == 'post_add':
        for pk in pk_set:
            print ('Penthouse Mas')
            obj = KatalogBukuCopy.objects.get(pk=pk)
            print('add: ' + str(obj))
            obj.STATUS = 'Pengajuan' 
            obj.save()           
            
    elif action == 'post_remove':
        for pk in pk_set:
            obj = KatalogBukuCopy.objects.get(pk=pk)
            print('delete: ' + str(obj))
            obj.STATUS = 'Sudah Dikembalikan'
            obj.save()
    
m2m_changed.connect(buku_changed_siswa, sender=PengajuanPeminjamanSiswa.BUKU.through)

class PengajuanPeminjamanGuru(models.Model):
    ID = models.BigAutoField(primary_key=True)
    DATA_GURU = models.ForeignKey(DataGuru, on_delete=models.CASCADE)
    BUKU = models.ManyToManyField(KatalogBukuCopy)
    TANGGAL_PENGAJUAN = models.DateField(default=datetime.date.today)
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
    
    
    class Meta:
        verbose_name_plural = "Pengajuan Peminjaman Guru"


class RiwayatPeminjamanGuru(models.Model):
    ID = models.BigAutoField(primary_key=True)
    DATA_GURU = models.ForeignKey(DataGuru, on_delete=models.CASCADE)
    BUKU = models.ManyToManyField(KatalogBukuCopy)
    TANGGAL_PEMINJAMAN = models.DateField(default=datetime.date.today)
    TANGGAL_PENGEMBALIAN = models.DateField(default=datetime.date.today)
    JANGKA_PEMINJAMAN = models.CharField(
        max_length=255,
        choices=ENUM_JANGKA_PEMINJAMAN,
        blank=True, 
    )
    FILE_TTD_PENGAJUAN = models.FileField(max_length=255, upload_to='Dokumen_Peminjaman_Jangka_Panjang_Guru', null=True)
    STATUS_PEMINJAMAN = models.CharField(
        max_length=255,
        choices=ENUM_STATUS_PEMINJAMAN,
        default= 'Sedang Dipinjam'
    )
    
    class Meta:
        verbose_name_plural = "Riwayat Peminjaman Guru"

def post_save_pengajuan_peminjaman_guru(sender, instance, created, **kwargs):
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
                )
                obj.BUKU.set(buku_m2m)
                
                if instance.JANGKA_PEMINJAMAN == 'Jangka Panjang' and instance.FILE_TTD_PENGAJUAN:
                    obj.FILE_TTD_PENGAJUAN = duplikat_file(instance, instance.FILE_TTD_PENGAJUAN.read(), instance.FILE_TTD_PENGAJUAN.name)
                
                obj.save()
                instance.delete()
                    
        except Exception as e:
            print(str(e))
            
    elif instance.STATUS_PENGAJUAN == '' or instance.STATUS_PENGAJUAN == 'Ditolak':
        try:
            for data in instance.BUKU.values():
                obj = KatalogBukuCopy.objects.get(REGISTER_COPY=data['REGISTER_COPY'])
                obj.STATUS = 'Sudah Dikembalikan'
                obj.save()
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
                    STATUS_PEMINJAMAN = 'Ditolak',
                )
                obj.BUKU.set(buku_m2m)
                obj.save()
                instance.delete()
                    
        except Exception as e:
            print(str(e))


post_save.connect(post_save_pengajuan_peminjaman_guru, sender=PengajuanPeminjamanGuru)

def buku_changed_guru(sender, instance, action, pk_set=None, **kwargs):
    if action == 'post_add':
        for pk in pk_set:
            obj = KatalogBukuCopy.objects.get(pk=pk)
            print('add: ' + str(obj))
            obj.STATUS = 'Pengajuan' 
            obj.save()           
            
    elif action == 'post_remove':
        for pk in pk_set:
            obj = KatalogBukuCopy.objects.get(pk=pk)
            print('delete: ' + str(obj))
            obj.STATUS = 'Sudah Dikembalikan'
            obj.save()
    
m2m_changed.connect(buku_changed_guru, sender=PengajuanPeminjamanGuru.BUKU.through)


    
class Abstrak (models.Model):
    REGISTER = models.ForeignKey(KatalogBuku,on_delete=models.CASCADE)
    ABSTRAK = models.CharField(max_length=255, default="")

    class Meta:
        verbose_name_plural = "Abstrak"