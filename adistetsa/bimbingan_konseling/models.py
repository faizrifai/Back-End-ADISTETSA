from cgi import print_arguments
from pickle import TRUE
from django.db import models
from django.contrib.auth.models import User
from kurikulum.models import Jurusan
from dataprofil.models import DataKompetensiGuru, DataRiwayatPendidikanFormalGuru
from bimbingan_konseling.enums import ENUM_JENIS_MASALAH, ENUM_KATEGORI_PEMINATAN_LINTAS_MINAT, ENUM_STATUS
import datetime
from kurikulum.models import KelasSiswa, Kelas

# Create your models here.
class DataAlumni(models.Model):
    ID = models.BigAutoField(primary_key=True)
    NAMA_SISWA = models.CharField(max_length=255)
    NISN = models.CharField(max_length=255)
    TAHUN_AJARAN = models.CharField(max_length=255)
    NAMA_PT = models.CharField(max_length=255, blank=True)
    PROGRAM_STUDI = models.CharField(max_length=255, blank=True)
    MEDIA_SOSIAL = models.CharField(max_length=255, blank=True)
    EMAIL = models.EmailField(max_length=255, blank=True)
    ALAMAT = models.CharField(max_length=255, blank=True)
    TEMPAT_BEKERJA = models.CharField(max_length=255, blank=True)
    def __str__(self):
        return self.NAMA_SISWA + ' _ ' + self.NISN

    class Meta:
        verbose_name_plural = "Data Alumni"

class PeminatanLintasMinat(models.Model):
    ID = models.BigAutoField(primary_key=True)
    KELAS_SISWA = models.ForeignKey(KelasSiswa, on_delete=models.CASCADE)
    KATEGORI = models.CharField(max_length=255, choices=ENUM_KATEGORI_PEMINATAN_LINTAS_MINAT)
    FILE = models.FileField(max_length=255, upload_to='Dokumen_Peminatan_Lintas_Minat')
    def __str__(self):
        return str(self.KELAS_SISWA) + ' _ ' + self.KATEGORI

    class Meta:
        verbose_name_plural = "Peminatan dan Lintas Minat"
        
class KatalogKonselor (models.Model):
    ID = models.BigAutoField(primary_key=True)
    USER = models.ForeignKey(User, on_delete=models.CASCADE)
    KOMPETENSI = models.CharField(max_length=255, blank=True)
    ALUMNUS = models.CharField(max_length=255, blank=True)
    WHATSAPP = models.URLField(max_length=255, blank=True)
    CONFERENCE = models.URLField(max_length=255, blank=True)
    STATUS = models.CharField(max_length=255, choices=ENUM_STATUS, default='Offline')
    # def __str__(self):
    #     pass# return str(self.DATA_GURU) + ' _ ' + self.STATUS
    
    class Meta:
        verbose_name_plural = "KatalogKonselor"
        
    

    
    # def save(self, *args, **kwargs):
    #     self.ALUMNUS = DataRiwayatPendidikanFormalGuru.objects.get(OWNER__NIP = self.DATA_GURU.OWNER.NIP).KEPENDIDIKAN
    #     super(KatalogKonselor, self).save(*args, **kwargs)

class Konsultasi(models.Model):
    ID = models.BigAutoField(primary_key=True)
    USER = models.ForeignKey(User, on_delete=models.CASCADE)
    KONSELOR = models.ForeignKey(KatalogKonselor, on_delete=models.CASCADE)
    TANGGAL = models.DateTimeField(max_length=255, default=datetime.datetime.today)
    JENIS_MASALAH = models.CharField(max_length=255, choices=ENUM_JENIS_MASALAH)
    
    class Meta:
        verbose_name_plural = "Konsultasi"
    
    def __str__(self):
        return str(self.KONSELOR) + ' _ ' + self.JENIS_MASALAH
