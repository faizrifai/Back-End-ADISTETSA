from django.db import models
from django.contrib.auth.models import User, Group
from pytz import timezone
from kustom_autentikasi.models import DataSiswaUser
from django.core.exceptions import ValidationError
from kurikulum.models import TahunAjaran
from .enums import ENUM_STATUS_KONSULTASI
from kurikulum.models import Jurusan
from dataprofil.models import (
    DataSiswa,
    DataKompetensiGuru,
    DataRiwayatPendidikanFormalGuru,
)
from bimbingan_konseling.enums import (
    ENUM_JENIS_MASALAH,
    ENUM_KATEGORI_PEMINATAN_LINTAS_MINAT,
    ENUM_STATUS,
)
import datetime
from kurikulum.models import KelasSiswa, Kelas
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.signals import post_save


# Create your models here.
class DataAlumni(models.Model):
    ID = models.BigAutoField(primary_key=True)
    NAMA_SISWA = models.CharField(max_length=255)
    KELAS = models.CharField(max_length=255)
    NISN = models.CharField(max_length=255)
    NIS = models.CharField(max_length=255)
    TAHUN_AJARAN = models.CharField(max_length=255)
    NAMA_PT = models.CharField(max_length=255, blank=True)
    PROGRAM_STUDI = models.CharField(max_length=255, blank=True)
    MEDIA_SOSIAL = models.CharField(max_length=255, blank=True)
    EMAIL = models.EmailField(max_length=255, blank=True)
    ALAMAT = models.CharField(max_length=255, blank=True)
    TEMPAT_BEKERJA = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.NAMA_SISWA + " _ " + self.NISN

    class Meta:
        verbose_name_plural = "Data Alumni"


class PeminatanLintasMinat(models.Model):
    ID = models.BigAutoField(primary_key=True)
    KELAS_SISWA = models.ForeignKey(KelasSiswa, on_delete=models.CASCADE)
    KATEGORI = models.CharField(
        max_length=255, choices=ENUM_KATEGORI_PEMINATAN_LINTAS_MINAT
    )
    FILE_ANGKET = models.FileField(
        max_length=255,
        upload_to="Dokumen_Peminatan_Lintas_Minat",
        null=True,
        blank=True,
    )
    FILE = models.FileField(
        max_length=255,
        upload_to="Dokumen_Peminatan_Lintas_Minat",
        null=True,
        blank=True,
    )

    def __str__(self):
        return str(self.KELAS_SISWA) + " _ " + self.KATEGORI

    class Meta:
        verbose_name_plural = "Peminatan dan Lintas Minat"
        constraints = [
            models.UniqueConstraint(
                fields=[
                    "KELAS_SISWA",
                    "KATEGORI",
                ],
                name="%(app_label)s_%(class)s_unique",
            )
        ]


def post_save_peminatan_lintas_minat(sender, instance, created, **kwargs):
    if instance.KELAS.KELAS.TINGKATAN == "X":
        try:
            for kategori in ENUM_KATEGORI_PEMINATAN_LINTAS_MINAT:
                obj = PeminatanLintasMinat.objects.update_or_create(
                    KELAS_SISWA=instance,
                    KATEGORI=kategori[0],
                )
        except Exception as e:
            print(str(e))


post_save.connect(post_save_peminatan_lintas_minat, sender=KelasSiswa)


class KatalogKonselor(models.Model):
    ID = models.BigAutoField(primary_key=True)
    USER = models.ForeignKey(User, on_delete=models.CASCADE)
    NAMA = models.CharField(max_length=255, blank=True)
    KOMPETENSI = models.CharField(max_length=255, blank=True)
    ALUMNUS = models.CharField(max_length=255, blank=True)
    WHATSAPP = models.URLField(max_length=255, blank=True)
    CONFERENCE = models.URLField(max_length=255, blank=True)
    FOTO = models.ImageField(max_length=255, upload_to="Foto_Profil_BK", blank=True)
    STATUS = models.CharField(max_length=255, choices=ENUM_STATUS, default="Offline")

    def __str__(self):
        return str(self.USER)

    class Meta:
        verbose_name_plural = "Katalog Konselor"


class Konsultasi(models.Model):
    ID = models.BigAutoField(primary_key=True)
    USER = models.ForeignKey(User, on_delete=models.CASCADE)
    KONSELOR = models.ForeignKey(KatalogKonselor, on_delete=models.CASCADE)
    TANGGAL_KONSULTASI = models.DateField(max_length=255, default=datetime.date.today)
    JAM_AWAL = models.TimeField()
    JAM_AKHIR = models.TimeField()
    JENIS_MASALAH = models.CharField(max_length=255, choices=ENUM_JENIS_MASALAH)
    RATING = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)], null=True, blank=True
    )
    STATUS = models.CharField(
        max_length=255, choices=ENUM_STATUS_KONSULTASI, default="Diajukan"
    )
    KRITIK_SARAN = models.TextField(max_length=255, blank=True)

    class Meta:
        verbose_name_plural = "Konsultasi"

    def __str__(self):
        return str(self.USER) + " _ " + self.JENIS_MASALAH

    def clean(self):
        if self.JAM_AWAL > self.JAM_AKHIR:
            raise ValidationError("Jam awal tidak boleh lebih dari jam akhir")
        if self.JAM_AWAL == self.JAM_AKHIR:
            raise ValidationError("Jam awal tidak boleh sama dengan jam akhir")


def post_save_konsultasi(sender, instance, created, **kwargs):

    if instance.STATUS == "Dijadwalkan":
        try:
            instance.STATUS = "Dijadwalkan"

        except Exception as e:
            print(str(e))
    if instance.STATUS == "Selesai":
        try:
            instance.STATUS = "Selesai"

        except Exception as e:
            print(str(e))
    if instance.STATUS == "Telah Mengisi Feedback":
        try:
            instance.STATUS = "Telah Mengisi Feedback"

        except Exception as e:
            print(str(e))
    elif instance.STATUS == "" or instance.STATUS == "Ditolak":
        try:
            instance.delete()

        except Exception as e:
            print(str(e))


post_save.connect(post_save_konsultasi, sender=Konsultasi)
