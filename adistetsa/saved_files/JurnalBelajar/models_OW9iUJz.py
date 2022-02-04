from ast import mod
from os import truncate
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from dataprofil.models import DataGuru, DataSiswa
from django.core.exceptions import ValidationError
from django.utils.html import format_html
from django.utils.text import Truncator
from django.conf import settings
from .enums import *

# def path_file(name):
#     def wrapper(user, filename):
#         file_upload_dir = os.path.join(settings.MEDIA_ROOT, name)
#         if os.path.exists(file_upload_dir):
#             import shutil
#             shutil.rmtree(file_upload_dir)
#         return os.path.join(file_upload_dir, filename)
#     return wrapper

# class PathFile(name):
    
#     def __init__(self, sub_path):
#         self.path = sub_path
    
#     def __call__(self, instance, filename):
#         file_upload_dir = os.path.join(settings.MEDIA_ROOT, name)
#         if os.path.exists(file_upload_dir):
#             import shutil
#             shutil.rmtree(file_upload_dir)
#         return os.path.join(file_upload_dir, filename)

# Master Model
class DataSemester(models.Model):
    KE = models.CharField(
        max_length=255, 
        choices=ENUM_SEMESTER,
    )
    NAMA = models.CharField(max_length=255, blank=True, verbose_name='SEMESTER')

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['KE'], name='%(app_label)s_%(class)s_unique')
        ]
        verbose_name_plural = "Semester"
        ordering = ['KE']

    def __str__(self):
        return self.NAMA
    
    def save(self, *args, **kwargs):
        self.NAMA = 'Semester ' + self.KE
        super(DataSemester, self).save(*args, **kwargs)
        
class TahunAjaran(models.Model):
    ID = models.BigAutoField(primary_key=True)
    TAHUN_AJARAN_AWAL = models.PositiveIntegerField(validators=[MinValueValidator(2000), MaxValueValidator(9999)])
    TAHUN_AJARAN_AKHIR= models.PositiveIntegerField(validators=[MinValueValidator(2000), MaxValueValidator(9999)])

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['TAHUN_AJARAN_AWAL', 'TAHUN_AJARAN_AKHIR'], name='%(app_label)s_%(class)s_unique')
        ]
        verbose_name_plural = "Tahun Ajaran"
    
    def clean(self):
        if self.TAHUN_AJARAN_AWAL > self.TAHUN_AJARAN_AKHIR:
            raise ValidationError('Tahun ajaran awal tidak boleh lebih dari tahun ajaran akhir')
        if (self.TAHUN_AJARAN_AKHIR - self.TAHUN_AJARAN_AWAL) > 1:
            raise ValidationError('Selisih tahun ajaran tidak boleh dari 1')
    
    def __str__(self):
        return str(self.TAHUN_AJARAN_AWAL) + '/' + str(self.TAHUN_AJARAN_AKHIR)

class MataPelajaran(models.Model):
    KODE = models.CharField(max_length=255, primary_key=True)
    NAMA = models.CharField(max_length=255, verbose_name="MATA PELAJARAN")

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['KODE', 'NAMA'], name='%(app_label)s_%(class)s_unique')
        ]
        verbose_name_plural = "Mata Pelajaran"
        ordering = ['NAMA']
    
    def __str__(self):
        return self.KODE + ' - ' + self.NAMA
    
class Jurusan(models.Model):
    ID = models.BigAutoField(primary_key=True)
    NAMA = models.CharField(max_length=255)
    
    def __str__(self):
        return self.NAMA
    
class TipeKelas(models.Model):
    ID = models.BigAutoField(primary_key=True)
    NAMA = models.CharField(max_length=255)
    
    def __str__(self):
        return self.NAMA

class Kelas(models.Model):
    ID = models.BigAutoField(primary_key=True)
    TAHUN_AJARAN = models.ForeignKey(TahunAjaran, on_delete=models.CASCADE)
    TINGKATAN = models.CharField(
        max_length = 255,
        choices = ENUM_TINGKATAN,
    )
    JURUSAN =  models.ForeignKey(Jurusan, on_delete=models.CASCADE)
    KODE_KELAS = models.CharField(max_length=255, unique=True, blank=True, verbose_name='KELAS')

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['TAHUN_AJARAN', 'TINGKATAN', 'JURUSAN'], name='%(app_label)s_%(class)s_unique')
        ]
        verbose_name_plural = "Kelas"
        ordering = ['TAHUN_AJARAN']
    
    def __str__(self):
        return self.KODE_KELAS 
    
    def save(self, *args, **kwargs):
        self.KODE_KELAS = self.TINGKATAN + ' ' + self.JURUSAN.NAMA + '-' + str(self.TAHUN_AJARAN)
        super(Kelas, self).save(*args, **kwargs)
        
class NamaOfferingKelas(models.Model):
    ID = models.BigAutoField(primary_key=True)
    NAMA = models.CharField(max_length=255)
    
    def __str__(self):
        return self.NAMA
        
class OfferingKelas(models.Model):
    ID = models.BigAutoField(primary_key=True)
    KELAS = models.ForeignKey(Kelas, on_delete=models.CASCADE)
    OFFERING = models.ForeignKey(NamaOfferingKelas, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.KELAS.KODE_KELAS + ' ' + self.OFFERING.NAMA

class BulanMinggu(models.Model):
    ID = models.BigAutoField(primary_key=True)
    NAMA_BULAN = models.CharField(max_length=255)
    JUMLAH_MINGGU = models.IntegerField()
    TAHUN = models.PositiveIntegerField(validators=[MinValueValidator(2000), MaxValueValidator(9999)])

    def __str__(self):
        return self.NAMA_BULAN + ' ' + str(self.TAHUN) + ' - Jumlah Minggu = ' + str(self.JUMLAH_MINGGU)

class KategoriTataTertib(models.Model):
    ID = models.BigAutoField(primary_key=True)
    NAMA = models.CharField(max_length=255)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['NAMA'], name='%(app_label)s_%(class)s_unique')
        ]
        verbose_name_plural = "Kategori Tata Tertib"
        ordering = ['NAMA']
    
    def __str__(self):
        return Truncator(self.NAMA).chars(50)

# Model Turunan
class KTSP(models.Model):
    ID = models.BigAutoField(primary_key=True)
    TAHUN_AJARAN = models.ForeignKey(TahunAjaran, on_delete=models.CASCADE)
    NAMA_FILE = models.FileField(max_length=255, upload_to='Dokumen_KTSP')

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['TAHUN_AJARAN'], name='%(app_label)s_%(class)s_unique')
        ]
        verbose_name_plural = "KTSP"
    
    def __str__(self):
        return self.NAMA_FILE.name + ' - ' + str(self.TAHUN_AJARAN.TAHUN_AJARAN_AWAL) + '/' + str(self.TAHUN_AJARAN.TAHUN_AJARAN_AKHIR)

class SilabusRPB(models.Model):
    ID = models.BigAutoField(primary_key=True)
    MATA_PELAJARAN = models.ForeignKey(MataPelajaran, on_delete=models.CASCADE)
    TAHUN_AJARAN = models.ForeignKey(TahunAjaran, on_delete=models.CASCADE)
    NAMA_FILE = models.FileField(max_length=255, upload_to='Dokumen_SilabusRPB')
    KELAS = models.ForeignKey(Kelas, on_delete=models.CASCADE)
    SEMESTER = models.ForeignKey(DataSemester, on_delete=models.CASCADE, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['MATA_PELAJARAN', 'TAHUN_AJARAN', 'KELAS', 'SEMESTER'], name='%(app_label)s_%(class)s_unique')
        ]
        verbose_name_plural = "Silabus RPB"
    
    def __str__(self):
        return self.NAMA_FILE.name + ' - ' + str(self.TAHUN_AJARAN.TAHUN_AJARAN_AWAL) + '/' + str(self.TAHUN_AJARAN.TAHUN_AJARAN_AKHIR)

class TataTertib(models.Model):
    ID = models.BigAutoField(primary_key=True)
    KETERANGAN = models.CharField(max_length=255)
    KATEGORI = models.ForeignKey(KategoriTataTertib, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['KETERANGAN'], name='%(app_label)s_%(class)s_unique')
        ]
        verbose_name_plural = "Tata Tertib"
        ordering = ['KETERANGAN']
    
    def __str__(self):
        return Truncator(self.KETERANGAN).chars(50)
    
class PoinPelanggaran(models.Model):
    ID = models.BigAutoField(primary_key=True)
    KETERANGAN = models.CharField(max_length=255)
    POIN = models.PositiveIntegerField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['KETERANGAN', 'POIN'], name='%(app_label)s_%(class)s_unique')
        ]
        verbose_name_plural = "Poin Pelanggaran"
        ordering = ['KETERANGAN']
    
    def __str__(self):
        return Truncator(self.KETERANGAN).chars(50)

class Mengajar(models.Model):
    ID = models.BigAutoField(primary_key=True)
    ID_GURU = models.ForeignKey(DataGuru, on_delete=models.CASCADE)
    MATA_PELAJARAN = models.ForeignKey(MataPelajaran, on_delete=models.CASCADE)
    SEMESTER = models.ForeignKey(DataSemester, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.ID_GURU.NAMA_LENGKAP)
    
class WaktuPelajaran(models.Model):
    ID = models.BigAutoField(primary_key=True)
    WAKTU_MULAI = models.TimeField()
    WAKTU_BERAKHIR = models.TimeField()
    JAM_KE = models.IntegerField()

    class Meta:
        ordering = ['JAM_KE']
    
    def __str__(self):
        return str(self.WAKTU_MULAI) + '-' + str(self.WAKTU_BERAKHIR) + ' (Jam Ke-' + str(self.JAM_KE) + ')'
    
class Pelajaran(models.Model):
    ID = models.BigAutoField(primary_key=True)
    MATA_PELAJARAN = models.ForeignKey(MataPelajaran, on_delete=models.CASCADE)
    WAKTU = models.ManyToManyField(WaktuPelajaran)
    GURU = models.ForeignKey(Mengajar, on_delete=models.CASCADE)

    def __str__(self):
        waktu = self.WAKTU.all()
        daftar_waktu = "Jam Ke "
        for data in waktu:
            daftar_waktu += str(data.JAM_KE) + "/ "
        return str(self.MATA_PELAJARAN) + ' - ' + self.GURU.ID_GURU.NAMA_LENGKAP + ' (' + daftar_waktu + ')'
    
class JadwalHarian(models.Model):
    ID = models.BigAutoField(primary_key=True)
    HARI = models.CharField(
        max_length = 255,
        choices = ENUM_HARI
    )
    PELAJARAN = models.ManyToManyField(Pelajaran)
    KELAS = models.ForeignKey(OfferingKelas, on_delete=models.CASCADE)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['HARI', 'KELAS'], name='%(app_label)s_%(class)s_unique')
        ]

    def __str__(self):
        return self.HARI + ' ' + str(self.KELAS)

class JadwalPelajaran(models.Model):
    ID = models.BigAutoField(primary_key=True)
    TAHUN_AJARAN = models.ForeignKey(TahunAjaran, on_delete=models.CASCADE)
    JADWAL_HARIAN = models.ManyToManyField(JadwalHarian)
    
    def __str__(self):
        return str(self.TAHUN_AJARAN)
    
class KelasSiswa(models.Model):
    ID = models.BigAutoField(primary_key=True)
    NIS = models.ForeignKey(DataSiswa, on_delete=models.CASCADE)
    KELAS = models.ForeignKey(OfferingKelas, on_delete=models.CASCADE)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['NIS', 'KELAS'], name='%(app_label)s_%(class)s_unique')
        ]
        verbose_name_plural = "Kelas Siswa"
    
    
    def __str__(self):
        return self.NIS.NAMA + ' - ' + str(self.KELAS)
    

class AbsensiSiswa(models.Model):
    ID = models.BigAutoField(primary_key=True)
    KELAS = models.ForeignKey(Kelas, on_delete=models.CASCADE)
    TANGGAL = models.DateField()
    KETERANGAN = models.CharField(
        choices=ENUM_KETERANGAN_ABSEN,
        max_length=255
    )
    FILE_DOKUMEN = models.FileField(max_length=255,blank=True, upload_to='Dokumen_AbsensiSiswa')

class DaftarJurnalBelajar(models.Model):
    ID = models.BigAutoField(primary_key=True)
    GURU = models.ForeignKey(DataGuru, on_delete=models.CASCADE)
    MATA_PELAJARAN = models.ForeignKey(MataPelajaran, on_delete=models.CASCADE)
    KELAS = models.ForeignKey(OfferingKelas, on_delete=models.CASCADE)
    SEMESTER = models.ForeignKey(DataSemester, on_delete=models.CASCADE)

    def __str__(self):
        return self.MATA_PELAJARAN.NAMA + ' ' + str(self.KELAS) + ' ' + self.SEMESTER.NAMA

class JurnalBelajar(models.Model):
    ID = models.BigAutoField(primary_key=True)
    GURU = models.ForeignKey(DataGuru, on_delete=models.CASCADE)
    PERTEMUAN = models.CharField(max_length=255)
    TANGGAL_MENGAJAR = models.DateField()
    DESKRIPSI_MATERI = models.TextField()
    FILE_DOKUMENTASI = models.FileField(max_length=255, upload_to='JurnalBelajar')
    DAFTAR = models.ForeignKey(DaftarJurnalBelajar, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['PERTEMUAN'], name='%(app_label)s_%(class)s_unique')
        ]
        verbose_name_plural = "Jurnal Belajar"
        ordering = ['PERTEMUAN']

    def __str__(self):
        return "Pertemuan " + self.PERTEMUAN

class JadwalMengajar(models.Model):
    ID = models.BigAutoField(primary_key=True)
    GURU = models.ForeignKey(DataGuru, on_delete=models.CASCADE)
    TAHUN_AJARAN = models.ForeignKey(TahunAjaran, on_delete=models.CASCADE)
    SEMESTER = models.ForeignKey(DataSemester, on_delete=models.CASCADE)
    KELAS = models.ForeignKey(OfferingKelas, on_delete=models.CASCADE)
    MATA_PELAJARAN = models.ForeignKey(MataPelajaran, on_delete=models.CASCADE)
    HARI = models.CharField(
        max_length=255,
        choices=ENUM_HARI,
    )
    WAKTU_PELAJARAN = models.ManyToManyField(WaktuPelajaran)
    JUMLAH_WAKTU = models.IntegerField(default=0)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['KELAS', 'MATA_PELAJARAN', 'HARI'], name='%(app_label)s_%(class)s_unique')
        ]
        verbose_name_plural = "Jadwal Mengajar"
        ordering = ['TAHUN_AJARAN', 'KELAS', 'HARI', 'JUMLAH_WAKTU']
    
    def __str__(self):
        return self.GURU.NAMA_LENGKAP + ' - ' + self.MATA_PELAJARAN.NAMA

    def save(self, *args, **kwargs):
        # tambahkan ke daftar jurnal belajar
        if not self.ID:
            daftar_jurnal_belajar = DaftarJurnalBelajar.objects.create(
                GURU = self.GURU,
                MATA_PELAJARAN = self.MATA_PELAJARAN,
                KELAS = self.KELAS,
                SEMESTER = self.SEMESTER,
            )

        super(JadwalMengajar, self).save(*args, **kwargs)
        waktu = self.WAKTU_PELAJARAN.all()
        jumlah = 0
        for data in waktu:
            jumlah += data.JAM_KE

        if (self.JUMLAH_WAKTU != jumlah):
            self.JUMLAH_WAKTU = jumlah
            self.save()
    

class JadwalPekanEfektifSemester(models.Model):
    ID = models.BigAutoField(primary_key=True)
    BULAN = models.CharField(
        max_length=255, 
        choices= ENUM_BULAN,
    )
    JUMLAH_MINGGU = models.IntegerField()
    JUMLAH_MINGGU_EFEKTIF = models.IntegerField()
    JUMLAH_MINGGU_TIDAK_EFEKTIF = models.IntegerField()
    KETERANGAN = models.TextField()
    
    def __str__(self):
        return self.BULAN + ' - Jumlah Minggu = ' + str(self.JUMLAH_MINGGU) + ' || Jumlah Minggu Efektif = ' + str(self.JUMLAH_MINGGU_EFEKTIF)
    
class JadwalPekanTidakEfektif(models.Model):
    ID = models.BigAutoField(primary_key=True)
    URAIAN_KEGIATAN =  models.TextField()
    JUMLAH_MINGGU = models.IntegerField()
    KETERANGAN = models.TextField()
    
    def __str__(self):
        return self.URAIAN_KEGIATAN + ' (' + str(self.JUMLAH_MINGGU) + ')'
    
class JadwalPekanAktif(models.Model):
    ID = models.BigAutoField(primary_key=True)
    MINGGU_TIDAK_EFEKTIF = models.ManyToManyField(JadwalPekanTidakEfektif)
    MINGGU_EFEKTIF = models.ManyToManyField(JadwalPekanEfektifSemester)
    MATA_PELAJARAN = models.ForeignKey(MataPelajaran, on_delete=models.CASCADE)
    KELAS = models.ForeignKey(Kelas, on_delete=models.CASCADE)
    SEMESTER = models.ForeignKey(DataSemester, on_delete=models.CASCADE)
