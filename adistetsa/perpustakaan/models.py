from typing import DefaultDict
from django.contrib.auth.models import User
from django.db import models
from django.db.models.base import Model
from django.db.models.query_utils import select_related_descend

from adistetsa.dataprofil.enums import ENUM_JENIS_KELAMIN

from .enums import *

from adistetsa.dataprofil.models import DEFAULT_LENGTH

# Create your models here.

class DataIndexBuku(models.Model):
    KODE_BUKU = models.CharField(max_length=DEFAULT_LENGTH ,primary_key=True)
    ISBN = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    JUDUL_BUKU = models.CharField(max_length=DEFAULT_LENGTH)
    JENIS_BUKU = models.CharField(max_length=DEFAULT_LENGTH)
    PENGARANG = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    PENERBIT = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    TAHUN_TERBIT = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    EDISI = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    BAHASA = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    SAMPUL = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    SINOPSIS = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    JUMLAH_BUKU = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    BUKU_TERSEDIA = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    JURNAL = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    
    def __str__(self):
        return self.JUDUL_BUKU

    class Meta:
        verbose_name_plural = "Index Buku"

class DataPeminjaman(models.Model):
    KODE_PEMINJAMAN = models.BigAutoField(primary_key=True)
    NISN = models.BigIntegerField()
    NAMA_PEMINJAM = models.CharField(max_length=DEFAULT_LENGTH)
    KODE_BUKU = models.CharField(max_length=DEFAULT_LENGTH)
    NAMA_BUKU = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    JENIS_BUKU = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    TANGGAL_PINJAM = models.DateField()
    TANGGAL_KEMBALI= models.DateField()
    STATUS = models.CharField(
        max_length=DEFAULT_LENGTH,
        choices=ENUM_STATUS_PINJAMAN,
    )
    def __str__(self):
        return self.NAMA_PEMINJAM + ' - ' + self.NAMA_BUKU 

    class Meta:
        verbose_name_plural = "Data Peminjaman"

class DataAbsensiPerpustakaan(models.Model):
    NO_ANGGOTA = models.BigAutoField(primary_key=True)
    NAMA = models.CharField(max_length=DEFAULT_LENGTH)
    NISN_NIP = models.CharField(max_length=DEFAULT_LENGTH)
    KELAS = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    JURUSAN = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    JENIS_KELAMIN = models.CharField(
        max_length=DEFAULT_LENGTH,
        choices=ENUM_JENIS_KELAMIN,
    )
    JENIS_ANGGOTA = models.CharField(max_length=DEFAULT_LENGTH)
    ALAMAT = models.CharField(max_length=DEFAULT_LENGTH)
    NOMOR_TELEPON = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    TANGGAL_HABIS = models.DateField()
    STATUS = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    def __str__(self):
        return self.NAMA + ' - ' + self.JENIS_ANGGOTA

    class Meta:
        verbose_name_plural = "Data Absensi"

class DataSirkulasi(models.Model):
    ID_PEMINJAMAN = models.BigAutoField(primary_key=True)
    NISN = models.BigIntegerField()
    TANGGAL_PINJAM = models.DateField()
    TANGGAL_KEMBALI = models.DateField()
    def __str__(self):
        return self.ID_PEMINJAMAN

    class Meta:
        verbose_name_plural = "Data Sirkulasi"

