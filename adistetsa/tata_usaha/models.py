from email.policy import default
from django.db import models
from pytz import timezone
from django.db.models.signals import post_save
from kurikulum.models import KelasSiswa
from dataprofil.models import DataOrangTua
from .enums import ENUM_ANAK_YATIM_PIATU, ENUM_BULAN, ENUM_GOLONGAN_DARAH
from dataprofil.models import DataSiswa
from adistetsa.custom_function import *
import datetime
# Create your models here.

class BukuInduk(models.Model):
    ID = models.BigAutoField(primary_key=True)
    NIS = models.ForeignKey(DataSiswa, on_delete=models.CASCADE)
    NAMA_PANGGILAN = models.CharField(max_length=255)
    KEWARGANEGARAAN = models.CharField(max_length=255, default='WNI')
    JUMLAH_SAUDARA_TIRI = models.CharField(max_length=255, blank=True)
    JUMLAH_SAUDARA_ANGKAT = models.CharField(max_length=255, blank=True)
    ANAK_YATIM_PIATU = models.CharField(max_length=255, blank=True, choices=ENUM_ANAK_YATIM_PIATU)
    BAHASA =  models.CharField(max_length=255, default='BAHASA INDONESIA')
    
    # TEMPAT TINGGAL
    
    # KETERANGAN KESEHATAN
    GOLONGAN_DARAH = models.CharField(max_length=2, choices=ENUM_GOLONGAN_DARAH)
    PENYAKIT_PERNAH_DIDERITA = models.CharField(max_length=255, blank=True)
    KELAINAN_JASMANI = models.CharField(max_length=255, blank=True)
    
    # KETERANGAN PENDIDIKAN
    # pendidikan sebelumnya
    TAMATAN_DARI = models.CharField(max_length=255, blank=True)
    TANGGAL_IJAZAH_S = models.DateField(blank=True, null=True)
    NO_IJAZAH_S = models.CharField(max_length=255, blank=True)
    NO_SKHUN_S = models.CharField(max_length=255, blank=True)
    TANGGAL_SKHUN_S = models.DateField(blank=True, null=True)
    LAMA_BELAJAR = models.CharField(max_length=255, blank=True)
    PINDAHAN_DARI = models.CharField(max_length=255, blank=True)
    ALASAN_PINDAHAN = models.CharField(max_length=255, blank=True)
    DITERIMA_DI_KELAS = models.CharField(max_length=255, blank=True)
    KELOMPOK = models.CharField(max_length=255)
    TANGGAL_DITERIMA = models.DateField(blank=True, null=True)
    
    # KETERANGAN AYAH KANDUNG
    ORANG_TUA = models.ForeignKey(DataOrangTua, on_delete=models.CASCADE, null=True)
    
    # KEGEMARAN PESERTA DIDIK
    KESENIAN = models.CharField(max_length=255, blank=True)
    OLAHRAGA = models.CharField(max_length=255, blank=True)
    KEMASYARAKATAN = models.CharField(max_length=255, blank=True)
    LAIN_LAIN = models.CharField(max_length=255, blank=True)
    
    # KETERANGAN PERKEMBANGAN PESERTA DIDIK
    TANGGAL_MENINGGALKAN_SEKOLAH = models.DateField(blank=True, null=True)
    ALASAN_MENINGGALKAN_SEKOLAH = models.CharField(max_length=255, blank=True)
    TAMAT_BELAJAR = models.CharField(max_length=255, blank=True)
    TANGGAL_NO_IJAZAH = models.DateField(blank=True, null=True)
    NO_IJAZAH = models.CharField(max_length=255, blank=True)
    TANGGAL_NO_SKHUN = models.DateField(blank=True, null=True)
    NO_SKHUN = models.CharField(max_length=255, blank=True)
    RATA_RATA_NUN = models.CharField(max_length=255, blank=True)
    
    # KETERANGAN SETELAH SELESAI PENDIDIKAN
    MELANJUTKAN_KE = models.CharField(max_length=255, blank=True)
    BEKERJA_DI = models.CharField(max_length=255, blank=True)
    
    class Meta:
        verbose_name_plural = "Buku Induk"
        
    def save(self, *args, **kwargs):
        kelas = KelasSiswa.objects.get(NIS__NIS=self.NIS.NIS)
        self.DITERIMA_DI_KELAS = kelas.KELAS.KELAS.TINGKATAN + str(kelas.KELAS.KELAS.JURUSAN)
        self.KELOMPOK = kelas.KELAS.OFFERING.NAMA
        self.ORANG_TUA = DataOrangTua.objects.get(DATA_ANAK__NIS=self.NIS.NIS)
        print(self.ORANG_TUA)
        super(BukuInduk, self).save(*args, **kwargs)
    
class DataBeasiswaSiswa(models.Model):
    ID = models.BigAutoField(primary_key=True)
    TAHUN = models.CharField(max_length=255)
    KELAS = models.CharField(max_length=255)
    DARI = models.CharField(max_length=255)
    BUKU_INDUK = models.ForeignKey(BukuInduk, on_delete=models.CASCADE)
    # TEST = models.CharField(max_length=255)    
    
class MutasiMasuk(models.Model):
    ID = models.BigAutoField(primary_key=True)
    NAMA_SISWA = models.CharField(max_length=255)
    ASAL_SEKOLAH = models.CharField(max_length=255)
    NO_INDUK_ASAL = models.CharField(max_length=255)
    ALAMAT = models.CharField(max_length=255)
    KELAS = models.CharField(max_length=255)
    NO_INDUK_BARU = models.CharField(max_length=255)
    TANGGAL_SURAT = models.DateField(max_length=255)
    NO_SURAT = models.CharField(max_length=255)
    BULAN = models.CharField(max_length=255, choices=ENUM_BULAN)
    TAHUN = models.CharField(max_length=255)
    
    class Meta:
        verbose_name_plural = "Mutasi Masuk"
    
    def __str__(self):
        return self.NAMA_SISWA

class MutasiKeluar (models.Model):
    ID = models.BigAutoField(primary_key=True)
    NAMA_SISWA = models.CharField(max_length=255)
    KELAS = models.CharField(max_length=255)
    NO_INDUK = models.CharField(max_length=255)
    PINDAH_KE = models.CharField(max_length=255)
    TANGGAL_SURAT = models.DateField()
    NO_SURAT = models.CharField(max_length=255)
    BULAN = models.CharField(max_length=255, choices=ENUM_BULAN)
    TAHUN = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Mutasi Keluar"
    
    def __str__(self):
        return self.NAMA_SISWA