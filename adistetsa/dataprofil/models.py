from typing import DefaultDict
from django.db import models
from django.db.models.base import Model


# Constant number
DEFAULT_LENGTH = 225

# Create your models here.
class DataSiswa(models.Model):
    NISN = models.BigIntegerField(max_length=DEFAULT_LENGTH, primary_key=True)
    NAMA = models.CharField(max_length=DEFAULT_LENGTH)
    NIPD = models.IntegerField(max_length=DEFAULT_LENGTH)
    ENUM_JENIS_KELAMIN = [
    ('Laki-laki', 'Laki-laki'),
    ('Perempuan', 'Perempuan'),
    ]
    JENIS_KELAMIN = models.CharField(
        max_length=20,
        choices=ENUM_JENIS_KELAMIN,
    )
    TEMPAT_LAHIR = models.CharField(max_length=DEFAULT_LENGTH)
    TANGGAL_LAHIR = models.DateField()
    NIK = models.BigIntegerField(max_length=DEFAULT_LENGTH)
    ENUM_AGAMA = [
        ('Islam', 'Islam'),
        ('Kristen', 'Kristen'),
        ('Katolik', 'Katolik'),
        ('Budha', 'Budha'),
        ('Hindu', 'Hindu'),
        ('Konghuchu', 'Konghuchu'),
    ]
    AGAMA = models.CharField(
        max_length=20,
        choices=ENUM_AGAMA,
    )
    ALAMAT = models.CharField(max_length=DEFAULT_LENGTH)
    RT = models.BigIntegerField(max_length=3)
    RW = models.BigIntegerField(max_length=3)
    DUSUN = models.CharField(max_length=DEFAULT_LENGTH)
    KELURAHAN = models.CharField(max_length=DEFAULT_LENGTH)
    KECAMATAN = models.CharField(max_length=DEFAULT_LENGTH)
    KODE_POS = models.BigIntegerField(max_length=DEFAULT_LENGTH)
    ENUM_JENIS_TINGGAL = [
        ('Bersama Orang Tua', 'Bersama Orang Tua'),
        ('Bersama Wali', 'Bersama Wali'),
        ('Mandiri', 'Mandiri')
    ]
    JENIS_TINGGAL = models.CharField(
        max_length=DEFAULT_LENGTH,
        choices=ENUM_JENIS_TINGGAL,
    )
    ENUM_ALAT_TRANSPORTASI = [
        ('Jalan Kaki', 'Jalan Kaki'),
        ('Kendaraan Pribadi', 'Kendaraan Pribadi'),
        ('Kendaraan Umum', 'Kendaraan Umum'),
    ]
    TELEPON = models.BigIntegerField(max_length=DEFAULT_LENGTH, blank=True)
    HP = models.BigIntegerField(max_length=DEFAULT_LENGTH, blank=True)
    EMAIL = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    SKHUN = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    ENUM_PENERIMA_KPS = [
        ('Iya', 'Iya'),
        ('Tidak', 'Tidak'),
    ]
    PENERIMA_KPS = models.CharField(
        max_length=5,
        choices=ENUM_PENERIMA_KPS,
    )
    NO_KPS = models.BigIntegerField(max_length=DEFAULT_LENGTH, blank=True)
    ROMBEL_SAAT_INI = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    NO_PESERTA_UJIAN_NASIONAL = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    NO_SERI_IJAZAH = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    ENUM_PENERIMA_KIP = [
        ('Iya', 'Iya'),
        ('Tidak', 'Tidak'),
    ]
    PENERIMA_KIP = models.CharField(
        max_length=5,
        choices=ENUM_PENERIMA_KIP,
    )
    NO_KKS = models.BigIntegerField(max_length=DEFAULT_LENGTH, blank=True)
    NO_REGRISTASI_AKTA_LAHIR = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    BANK = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    NO_REKENING_BANK = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    REKENING_ATAS_NAMA = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    ENUM_LAYAK_PIP = [
        ('Iya', 'Iya'),
        ('Tidak', 'Tidak'),
    ]
    LAYAK_PIP = models.CharField(
        max_length=5,
        choices=ENUM_LAYAK_PIP,
    )
    KEBUTUHAN_KHUSUS = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    ANAK_KE = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    LINTANG = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    BUJUR = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    NO_KK = models.BigIntegerField(max_length=DEFAULT_LENGTH, blank=True)
    BERAT_BADAN = models.IntegerField(max_length=3, blank=True)
    TINGGI_BADAN = models.IntegerField(max_length=3, blank=True)
    LINGKAR_KEPALA = models.IntegerField(max_length=5, blank=True)
    JUMLAH_SAUDARA_KANDUNG = models.IntegerField(max_length=5, blank=True)
    JARAK_RUMAH_KESEKOLAH_KM = models.IntegerField(max_length=DEFAULT_LENGTH, blank=True)
