from django.db import models
from dataprofil.models import DataSiswa
from .enums import *

# Create your models here.
class SanitasiDrainase(models.Model):
    ID = models.BigAutoField(primary_key=True)
    TANGGAL = models.DateField()
    NAMA_KEGIATAN = models.CharField(max_length=255)
    UNSUR_TERLIBAT = models.CharField(max_length=255)
    KETERANGAN = models.CharField(max_length=255)
    FILE = models.FileField(upload_to='SanitasiDrainase', max_length=255)
    
    class Meta:
        verbose_name_plural ='Sanitasi Drainase'
    
class JaringanKerja(models.Model):
    ID = models.BigAutoField(primary_key=True)
    TANGGAL = models.DateField()
    NAMA_KEGIATAN = models.CharField(max_length=255)
    KETERANGAN = models.CharField(max_length=255)
    FILE = models.FileField(upload_to='JaringanKerja', max_length=255)
    
    class Meta:
        verbose_name_plural ='Jaringan Kerja'
        
class Publikasi(models.Model):
    ID = models.BigAutoField(primary_key=True)
    TANGGAL = models.DateField()
    NAMA_KEGIATAN = models.CharField(max_length=255)
    JENIS_MEDIA = models.CharField(max_length=255)
    KETERANGAN = models.CharField(max_length=255)
    FILE = models.FileField(upload_to='Publikasi', max_length=255)
    
    class Meta:
        verbose_name_plural ='Publikasi'
    
class DaftarKader(models.Model):
    ID = models.BigAutoField(primary_key=True)
    NIS = models.ForeignKey(DataSiswa, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name_plural ='Daftar Kader'

class KegiatanKader(models.Model):
    ID = models.BigAutoField(primary_key=True)
    TANGGAL = models.DateField()
    NAMA_KEGIATAN = models.CharField(max_length=255)
    KETERANGAN = models.CharField(max_length=255)
    FILE = models.FileField(upload_to='KegiatanKader', max_length=255)
    
    class Meta:
        verbose_name_plural ='Kegiatan Kader'
    
class Konservasi(models.Model):
    ID = models.BigAutoField(primary_key=True)
    TANGGAL = models.DateField()
    KATEGORI = models.CharField(max_length=255, choices=ENUM_KONSERVASI)
    NAMA_KEGIATAN = models.CharField(max_length=255)
    KETERANGAN = models.CharField(max_length=255)
    FILE = models.FileField(upload_to='Konservasi', max_length=255)
    
    class Meta:
        verbose_name_plural ='Konservasi'

class PenanamanPohon(models.Model):
    ID = models.BigAutoField(primary_key=True)
    TANGGAL = models.DateField()
    NAMA_KEGIATAN = models.CharField(max_length=255)
    JUMLAH = models.CharField(max_length=255)
    KETERANGAN = models.CharField(max_length=255)
    FILE = models.FileField(upload_to='PenanamanPohon', max_length=255)
    
    class Meta:
        verbose_name_plural ='Penanaman Pohon'
    
class PembibitanPohon(models.Model):
    ID = models.BigAutoField(primary_key=True)
    TANGGAL = models.DateField()
    NAMA_KEGIATAN = models.CharField(max_length=255)
    KETERANGAN = models.CharField(max_length=255)
    FILE = models.FileField(upload_to='PembibitanPohon', max_length=255)
    
    class Meta:
        verbose_name_plural ='Pembibitan Pohon'

class PemeliharaanPohon(models.Model):
    ID = models.BigAutoField(primary_key=True)
    TANGGAL = models.DateField()
    NAMA_KEGIATAN = models.CharField(max_length=255)
    KETERANGAN = models.CharField(max_length=255)
    FILE = models.FileField(upload_to='PemeliharaanPohon', max_length=255)
    
    class Meta:
        verbose_name_plural ='Pemeliharaan Pohon'
    
class KaryaInovatif(models.Model):
    ID = models.BigAutoField(primary_key=True)
    TANGGAL = models.DateField()
    NAMA_INOVATOR = models.CharField(max_length=255)
    NAMA_KARYA_INOVATIF = models.CharField(max_length=255)
    JENIS = models.CharField(max_length=255)
    FILE = models.FileField(upload_to='KaryaInovatif', max_length=255)
    
    class Meta:
        verbose_name_plural ='Karya Inovatif'
    
class PenerapanPRLH(models.Model):
    ID = models.BigAutoField(primary_key=True)
    TANGGAL = models.DateField()
    NAMA_KEGIATAN = models.CharField(max_length=255)
    PESERTA = models.CharField(max_length=255)
    KETERANGAN = models.TextField()
    FILE = models.FileField(upload_to='PenerapanPRLH', max_length=255)
    
    class Meta:
        verbose_name_plural ='Penerapan PRLH'
    
class ReuseReduceRecycle(models.Model):
    ID = models.BigAutoField(primary_key=True)
    TANGGAL = models.DateField()
    NAMA_KEGIATAN = models.CharField(max_length=255)
    JENIS_KEGIATAN = models.CharField(
        max_length=255, 
        choices=ENUM_3R,
    )
    PIHAK_TERLIBAT = models.CharField(max_length=255)
    KETERANGAN = models.TextField()
    FILE = models.FileField(upload_to='ReuseReduceRecycle', max_length=255)
    
    class Meta:
        verbose_name_plural ='Reuse Reduce Recycle'
    
class PemeliharaanSampah(models.Model):
    ID = models.BigAutoField(primary_key=True)
    TANGGAL = models.DateField()
    NAMA_KEGIATAN = models.CharField(max_length=255)
    KETERANGAN = models.TextField()
    FILE = models.FileField(upload_to='PemeliharaanSampah', max_length=255)
    
    class Meta:
        verbose_name_plural ='Pemeliharaan Sampah'
        
class TabunganSampah(models.Model):
    ID = models.BigAutoField(primary_key=True)
    KATEGORI = models.CharField(max_length=255, choices=ENUM_JENIS_SAMPAH)
    TANGGAL = models.DateField()
    JUMLAH = models.PositiveIntegerField()
    
    class Meta:
        verbose_name_plural ='Tabungan Sampah'

class TabunganSampahProxy(TabunganSampah):
    class Meta:
        ordering = ["TANGGAL"]
        proxy = True    
        verbose_name_plural ='Jumlah Tabungan Sampah'
    
    

