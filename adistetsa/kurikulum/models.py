from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models.base import Model
from dataprofil.models import DataGuru, DataSiswa

from .enums import *

def current_year():
    pass

# Create your models here.
class KTSP(models.Model):
    ID = models.BigAutoField(primary_key=True)
    TAHUN_AJARAN_AWAL = models.PositiveIntegerField(validators=[MinValueValidator(2000), MaxValueValidator(9999)])
    TAHUN_AJARAN_AKHIR= models.PositiveIntegerField(validators=[MinValueValidator(2000), MaxValueValidator(9999)])
    NAMA_FILE = models.FileField(max_length=255, upload_to='Dokumen_KTSP')
    
    def __str__(self):
        return self.NAMA_FILE.name + ' - ' + str(self.TAHUN_AJARAN_AWAL) + '/' + str(self.TAHUN_AJARAN_AKHIR)

class MataPelajaran(models.Model):
    KODE = models.CharField(max_length=255, primary_key=True)
    NAMA = models.CharField(max_length=255)

class Kelas(models.Model):
    ID = models.BigAutoField(primary_key=True)
    TAHUN_AJARAN_AWAL = models.PositiveIntegerField(validators=[MinValueValidator(2000), MaxValueValidator(9999)])
    TAHUN_AJARAN_AKHIR = models.PositiveIntegerField(validators=[MinValueValidator(2000), MaxValueValidator(9999)])
    TINGKATAN = models.CharField(
        max_length = 255,
        choices = ENUM_TINGKATAN,
    )
    KODE_KELAS = models.CharField(max_length=255, blank=True)
    

class SilabusRPB(models.Model):
    ID = models.BigAutoField(primary_key=True)
    MATA_PELAJARAN = models.ForeignKey(MataPelajaran, on_delete=models.CASCADE)
    TAHUN_AJARAN_AWAL = models.PositiveIntegerField(validators=[MinValueValidator(2000), MaxValueValidator(9999)])
    TAHUN_AJARAN_AKHIR = models.PositiveIntegerField(validators=[MinValueValidator(2000), MaxValueValidator(9999)])
    NAMA_FILE = models.FileField(max_length=255, upload_to='Dokumen_SilabusRPB')
    KELAS = models.ForeignKey(Kelas, on_delete=models.CASCADE)
    
class BulanMinggu(models.Model):
    ID = models.BigAutoField(primary_key=True)
    NAMA_BULAN = models.CharField(max_length=255)
    JUMLAH_MINGGU = models.IntegerField()
    TAHUN = models.PositiveIntegerField(validators=[MinValueValidator(2000), MaxValueValidator(9999)])

class JadwalPekanEfektifSemester(models.Model):
    ID = models.BigAutoField(primary_key=True)
    BANYAK_MINGGU = models.ManyToManyField(BulanMinggu)
    JUMLAH = models.IntegerField()
    
class KegiatanPekanTidakEfektif(models.Model):
    ID = models.BigAutoField(primary_key=True)
    URAIAN_KEGIATAN = models.CharField(max_length=255)
    JUMLAH_MINGGU = models.IntegerField()
    KETERANGAN = models.CharField(max_length=255)
    
class JadwalPekanTidakEfektif(models.Model):
    ID = models.BigAutoField(primary_key=True)
    KEGIATAN = models.ManyToManyField(KegiatanPekanTidakEfektif)
    
class JadwalPekanAktif(models.Model):
    ID = models.BigAutoField(primary_key=True)
    SEMESTER = models.CharField(
        max_length = 255, 
        choices = ENUM_SEMESTER
    )
    PEKAN_AKTIF = models.ForeignKey(JadwalPekanEfektifSemester, on_delete=models.CASCADE)
    PEKAN_TIDAK_EFEKTIF = models.ForeignKey(JadwalPekanTidakEfektif, on_delete=models.CASCADE)
    
class DeskripsiTataTertib(models.Model):
    ID = models.BigAutoField(primary_key=True)
    KETERANGAN = models.CharField(max_length=255)
    POIN = models.PositiveIntegerField()

class TataTertib(models.Model):
    ID = models.BigAutoField(primary_key=True)
    DAFTAR = models.ManyToManyField(DeskripsiTataTertib)

class Mengajar(models.Model):
    ID = models.BigAutoField(primary_key=True)
    ID_GURU = models.ForeignKey(DataGuru, on_delete=models.CASCADE)
    MATA_PELAJARAN = models.ForeignKey(MataPelajaran, on_delete=models.CASCADE)
    
class WaktuPelajaran(models.Model):
    ID = models.BigAutoField(primary_key=True)
    WAKTU_MULAI = models.TimeField()
    WAKTU_BERAKHIR = models.TimeField()
    JAM_KE = models.IntegerField()
    
class Pelajaran(models.Model):
    ID = models.BigAutoField(primary_key=True)
    MATA_PELAJARAN = models.ForeignKey(MataPelajaran, on_delete=models.CASCADE)
    WAKTU = models.ForeignKey(WaktuPelajaran, on_delete=models.CASCADE)
    GURU = models.ForeignKey(Mengajar, on_delete=models.CASCADE)

class JadwalHarian(models.Model):
    ID = models.BigAutoField(primary_key=True)
    HARI = models.CharField(
        max_length = 255,
        choices = ENUM_HARI
    )
    PELAJARAN = models.ManyToManyField(Pelajaran)
    KELAS = models.ForeignKey(Kelas, on_delete=models.CASCADE)


class JadwalPelajaran(models.Model):
    ID = models.BigAutoField(primary_key=True)
    SEMESTER =  models.CharField(
        max_length = 255, 
        choices = ENUM_SEMESTER,
    )
    JADWAL_HARIAN = models.ManyToManyField(JadwalHarian)
    
class KelasSiswa(models.Model):
    ID = models.BigAutoField(primary_key=True)
    NIS = models.ForeignKey(DataSiswa, on_delete=models.CASCADE)
    KELAS = models.ForeignKey(Kelas, on_delete=models.CASCADE)

class AbsensiSiswa(models.Model):
    ID = models.BigAutoField(primary_key=True)
    KELAS = models.ForeignKey(Kelas, on_delete=models.CASCADE)
    TANGGAL = models.DateField()
    KETERANGAN = models.CharField(
        choices=ENUM_KETERANGAN_ABSEN,
        max_length=255
    )
    FILE_DOKUMEN = models.FileField(max_length=255, upload_to='Dokumen_AbsensiSiswa')

class JurnalBelajar(models.Model):
    ID = models.BigAutoField(primary_key=True)
    KELAS = models.ForeignKey(Kelas, on_delete=models.CASCADE)
    TANGGAL_MENGAJAR = models.DateField()
    PELAJARAN = models.ForeignKey(Pelajaran, on_delete=models.CASCADE)
    DESKRIPSI_MATERI = models.CharField(max_length=1020)
    FILE_DOKUMENTASI = models.FileField(max_length=255, upload_to='JurnalBelajar')
    