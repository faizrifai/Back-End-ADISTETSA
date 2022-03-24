from django.db import models
from kurikulum.enums import ENUM_HARI
from hubungan_masyarakat.enums import ENUM_JENIS_PTK_UKS
import datetime
from django.utils import timezone

# Create your models here.
class BukuTamu(models.Model):
    ID = models.BigAutoField(primary_key=True)
    NAMA = models.CharField(max_length=255)
    INSTANSI_ASAL = models.CharField(max_length=255)
    ALAMAT = models.CharField(max_length=255)
    NO_HP = models.CharField(max_length=255)
    HARI = models.CharField(max_length=255)
    TANGGAL = models.DateField()
    JAM = models.TimeField()
    KEPERLUAN = models.CharField(max_length=255)
    
    class Meta:
        verbose_name_plural = "Buku Tamu"
        
    def save(self, *args, **kwargs):
        hari = self.TANGGAL.weekday()
        self.HARI = ENUM_HARI[hari][0]
        super(BukuTamu, self).save(*args, **kwargs)
    
class LogUKSSiswa (models.Model):
    ID = models.BigAutoField(primary_key=True)
    JENIS_PTK = models.CharField(max_length=255, default='Siswa')
    NAMA = models.CharField(max_length=255)
    KELAS = models.CharField(max_length=255)
    NISN = models.CharField(max_length=255)
    TANGGAL = models.DateField()
    JENIS_PEMERIKSAAN = models.CharField(max_length=255)
    OBAT_DIBERIKAN = models.CharField(max_length=255)
    TINDAK_LANJUT = models.CharField(max_length=255)
    
    class Meta:
        verbose_name_plural = "Log UKS Siswa"
    
    
class LogUKSTendik (models.Model):
    ID = models.BigAutoField(primary_key=True)
    JENIS_PTK = models.CharField(max_length=255, choices=ENUM_JENIS_PTK_UKS)
    NAMA = models.CharField(max_length=255)
    TANGGAL = models.DateField()
    JENIS_PEMERIKSAAN = models.CharField(max_length=255)
    OBAT_DIBERIKAN = models.CharField(max_length=255)
    TINDAK_LANJUT = models.CharField(max_length=255)
    
    class Meta:
        verbose_name_plural = "Log UKS Tendik"