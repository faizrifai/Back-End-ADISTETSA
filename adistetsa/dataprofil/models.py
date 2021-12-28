from typing import DefaultDict
from django.db import models
from django.db.models.base import Model

from .enums import *

# Constant number
DEFAULT_LENGTH = 225

# Create your models here.
class DataSiswa(models.Model):
    NISN = models.BigIntegerField(primary_key=True)
    NAMA = models.CharField(max_length=DEFAULT_LENGTH)
    NIPD = models.BigIntegerField()
    JENIS_KELAMIN = models.CharField(
        max_length=20,
        choices=ENUM_JENIS_KELAMIN,
    )
    TEMPAT_LAHIR = models.CharField(max_length=DEFAULT_LENGTH)
    TANGGAL_LAHIR = models.DateField()
    NIK = models.BigIntegerField()
    AGAMA = models.CharField(
        max_length=20,
        choices=ENUM_AGAMA,
    )
    ALAMAT = models.CharField(max_length=DEFAULT_LENGTH)
    RT = models.BigIntegerField()
    RW = models.BigIntegerField()
    DUSUN = models.CharField(max_length=DEFAULT_LENGTH)
    KELURAHAN = models.CharField(max_length=DEFAULT_LENGTH)
    KECAMATAN = models.CharField(max_length=DEFAULT_LENGTH)
    KODE_POS = models.BigIntegerField()
    JENIS_TINGGAL = models.CharField(
        max_length=DEFAULT_LENGTH,
        choices=ENUM_JENIS_TINGGAL,
    )
    TELEPON = models.BigIntegerField(blank=True, null=True)
    HP = models.BigIntegerField(blank=True, null=True)
    EMAIL = models.EmailField(max_length=DEFAULT_LENGTH, blank=True)
    SKHUN = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    PENERIMA_KPS = models.CharField(
        max_length=5,
        choices=ENUM_PENERIMA_KPS,
    )
    NO_KPS = models.BigIntegerField(blank=True, null=True)
    ROMBEL_SAAT_INI = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    NO_PESERTA_UJIAN_NASIONAL = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    NO_SERI_IJAZAH = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    PENERIMA_KIP = models.CharField(
        max_length=5,
        choices=ENUM_PENERIMA_KIP,
    )
    NO_KKS = models.BigIntegerField(blank=True, null=True)
    NO_REGRISTASI_AKTA_LAHIR = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    BANK = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    NO_REKENING_BANK = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    REKENING_ATAS_NAMA = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    LAYAK_PIP = models.CharField(
        max_length=5,
        choices=ENUM_LAYAK_PIP,
    )
    KEBUTUHAN_KHUSUS = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    ANAK_KE = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    LINTANG = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    BUJUR = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    NO_KK = models.BigIntegerField(blank=True, null=True)
    BERAT_BADAN = models.IntegerField(blank=True, null=True)
    TINGGI_BADAN = models.IntegerField(blank=True, null=True)
    LINGKAR_KEPALA = models.IntegerField(blank=True, null=True)
    JUMLAH_SAUDARA_KANDUNG = models.IntegerField(blank=True, null=True)
    JARAK_RUMAH_KESEKOLAH_KM = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.NISN) + ' - ' + self.NAMA

    class Meta:
        verbose_name_plural = "Data Siswa"


class DataOrangTua(models.Model):
    ID = models.BigAutoField(primary_key=True)
    NAMA_AYAH = models.CharField(max_length=DEFAULT_LENGTH)
    TAHUN_LAHIR_AYAH = models.DateField()
    JENJANG_PENDIDIKAN_AYAH  = models.CharField(
        max_length=20,
        choices=ENUM_JENJANG_PENDIDIKAN,
    )
    PEKERJAAN_AYAH = models.CharField(max_length=DEFAULT_LENGTH)
    PENGHASILAN_AYAH = models.CharField(
        max_length=DEFAULT_LENGTH,
        choices=ENUM_PENGHASILAN,
    )
    NIK_IBU = models.BigIntegerField()
    NAMA_IBU = models.CharField(max_length=DEFAULT_LENGTH)
    TAHUN_LAHIR_IBU  = models.DateField()
    JENJANG_PENDIDIKAN_IBU = models.CharField(
        max_length=20,
        choices= ENUM_JENJANG_PENDIDIKAN,
    )
    PEKERJAAN_IBU = models.CharField(max_length=DEFAULT_LENGTH)
    PENGHASILAN_IBU = models.CharField(
        max_length=DEFAULT_LENGTH,
        choices=ENUM_PENGHASILAN, 
    )
    NIK_WALI = models.BigIntegerField()
    NAMA_WALI = models.CharField(max_length=DEFAULT_LENGTH)
    TAHUN_LAHIR_WALI  = models.DateField()
    JENJANG_PENDIDIKAN_WALI = models.CharField(
        max_length=20,
        choices= ENUM_JENJANG_PENDIDIKAN,
    )
    PEKERJAAN_WALI = models.CharField(max_length=DEFAULT_LENGTH)
    PENGHASILAN_WALI = models.CharField(
        max_length=DEFAULT_LENGTH,
        choices=ENUM_PENGHASILAN, 
    )
    DATA_ANAK = models.ManyToManyField(DataSiswa, verbose_name="DAFTAR ANAK")
    
    def __str__(self):
        return self.NAMA_AYAH

    class Meta:
        verbose_name_plural = "Data Orangtua dan Wali"

