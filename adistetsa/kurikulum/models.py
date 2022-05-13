from django.db import models
from django.db.models.signals import post_save, pre_save, m2m_changed
from django.core.validators import MinValueValidator, MaxValueValidator
from numpy import var
from dataprofil.models import DataGuru, DataSiswa
from django.core.exceptions import ValidationError
from django.utils.html import format_html
from django.utils.text import Truncator
from django.conf import settings
from .enums import *
from config_models.models import ConfigurationModel
from utility.custom_function import *
import datetime
from tata_usaha.models import BukuInduk

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
    NAMA = models.CharField(max_length=255, verbose_name="MATA PELAJARAN", validators=[cek_huruf_besar_awal_kalimat])

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
    NAMA = models.CharField(max_length=255, validators=[paksa_huruf_besar])
    
    class Meta:
        verbose_name_plural = 'Jurusan'

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
    NAMA = models.CharField(max_length=255, validators=[paksa_huruf_besar])
    
    class Meta:
        verbose_name_plural = 'Nama Offering Kelas'

    def __str__(self):
        return self.NAMA
        
class OfferingKelas(models.Model):
    ID = models.BigAutoField(primary_key=True)
    KELAS = models.ForeignKey(Kelas, on_delete=models.CASCADE)
    OFFERING = models.ForeignKey(NamaOfferingKelas, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['KELAS', 'OFFERING'], name='%(app_label)s_%(class)s_unique')
        ]
        verbose_name_plural = 'Offering Kelas'
    
    def __str__(self):
        return self.KELAS.KODE_KELAS + ' ' + self.OFFERING.NAMA

class KategoriTataTertib(models.Model):
    ID = models.BigAutoField(primary_key=True)
    NAMA = models.CharField(max_length=255, validators=[cek_huruf_besar_awal_kalimat])

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
    
class WaktuPelajaran(models.Model):
    ID = models.BigAutoField(primary_key=True)
    WAKTU_MULAI = models.TimeField()
    WAKTU_BERAKHIR = models.TimeField()
    JAM_KE = models.IntegerField()

    class Meta:
        ordering = ['JAM_KE']
        verbose_name_plural = 'Waktu Pelajaran'
    
    def __str__(self):
        return str(self.WAKTU_MULAI) + '-' + str(self.WAKTU_BERAKHIR) + ' (Jam Ke-' + str(self.JAM_KE) + ')'

    def clean(self):
        if self.WAKTU_MULAI > self.WAKTU_BERAKHIR :
            raise ValidationError('Waktu Mulai tidak boleh lebih dari Waktu Berakhir')
        if self.WAKTU_MULAI == self.WAKTU_BERAKHIR :
            raise ValidationError('Waktu Mulai tidak boleh sama dengan Waktu Berakhir')

    def save(self, *args, **kwargs):
        self.full_clean()

        return super().save(*args, **kwargs)


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
    
    def clean(self):
        kelas = KelasSiswa.objects.filter(NIS=self.NIS, KELAS__KELAS__TINGKATAN=self.KELAS.KELAS.TINGKATAN).exclude(ID=self.ID)
        
        if kelas:
            # tingkatan_sama = kelas.KELAS.KELAS.TINGKATAN == self.KELAS.KELAS.TINGKATAN
            # tahun_sama = kelas.KELAS.KELAS.TAHUN_AJARAN == self.KELAS.KELAS.TAHUN_AJARAN
            
            for data in kelas:
                if data.KELAS.KELAS.TINGKATAN == self.KELAS.KELAS.TINGKATAN and data.KELAS.KELAS.TAHUN_AJARAN == self.KELAS.KELAS.TAHUN_AJARAN:
                    raise ValidationError({'KELAS': self.NIS.NAMA + ' sudah terdaftar pada tingkatan dan tahun ajaran yang sama'})

def post_save_buku_induk(sender, instance, created, **kwargs):
    try:
        kelas_siswa = KelasSiswa.objects.filter(NIS = instance.NIS)
        for siswa in kelas_siswa:
            for i in range (2):
                if i == 0:
                    semester = "I"
                elif i == 1:
                    semester = "II"
                Raport.objects.update_or_create(
                    KELAS_SISWA=siswa, 
                    SEMESTER=DataSemester.objects.get(KE=semester),
                    BUKU_INDUK = instance
                )
    except Exception as e:
        print(str(e))
        
post_save.connect(post_save_buku_induk, sender=BukuInduk)

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
            models.UniqueConstraint(fields=['KELAS', 'MATA_PELAJARAN', 'HARI', ], name='%(app_label)s_%(class)s_unique')
        ]
        verbose_name_plural = "Jadwal Mengajar"
        ordering = ['TAHUN_AJARAN', 'KELAS', 'HARI', 'JUMLAH_WAKTU']
    
    def __str__(self):
        return self.GURU.NAMA_LENGKAP + ' - ' + self.MATA_PELAJARAN.NAMA    
    
    # def clean(self):
    #     if text:
    #         raise ValidationError(text_error())
    
    def save(self, *args, **kwargs):
        self.TAHUN_AJARAN = self.KELAS.KELAS.TAHUN_AJARAN
        
        super(JadwalMengajar, self).save(*args, **kwargs)


class DaftarJurnalBelajar(models.Model):
    ID = models.BigAutoField(primary_key=True)
    GURU = models.ForeignKey(DataGuru, on_delete=models.CASCADE)
    MATA_PELAJARAN = models.ForeignKey(MataPelajaran, on_delete=models.CASCADE)
    KELAS = models.ForeignKey(OfferingKelas, on_delete=models.CASCADE)
    SEMESTER = models.ForeignKey(DataSemester, on_delete=models.CASCADE)
    JADWAL_MENGAJAR = models.ForeignKey(JadwalMengajar, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['JADWAL_MENGAJAR'], name='%(app_label)s_%(class)s_unique')
        ]
        verbose_name_plural = "Daftar Jurnal Belajar"
        ordering = ['KELAS']

    def __str__(self):
        return self.MATA_PELAJARAN.NAMA + ' ' + str(self.KELAS) + ' ' + self.SEMESTER.NAMA

      
class JurnalBelajar(models.Model):
    ID = models.BigAutoField(primary_key=True)
    GURU = models.ForeignKey(DataGuru, on_delete=models.CASCADE)
    PERTEMUAN = models.CharField(max_length=255)
    TANGGAL_MENGAJAR = models.DateField(default=datetime.date.today)
    DESKRIPSI_MATERI = models.TextField()
    FILE_DOKUMENTASI = models.FileField(max_length=255, upload_to='JurnalBelajar')
    DAFTAR = models.ForeignKey(DaftarJurnalBelajar, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['PERTEMUAN', 'DAFTAR'], name='%(app_label)s_%(class)s_unique')
        ]
        verbose_name_plural = "Jurnal Belajar"
        ordering = ['PERTEMUAN']

    def __str__(self):
        return str(self.DAFTAR.MATA_PELAJARAN) + ' - ' + str(self.DAFTAR.KELAS) + ' - ' + str(self.DAFTAR.SEMESTER) + ' - Pertemuan : ' + self.PERTEMUAN


def pre_save_jurnal_belajar(sender, instance, **kwargs):
    try:
        daftar = DaftarJurnalBelajar.objects.get(ID=instance.DAFTAR.ID)
        print(daftar)
        instance.GURU = daftar.GURU
    except Exception as e:
        print(str(e))

pre_save.connect(pre_save_jurnal_belajar, sender=JurnalBelajar)
        
    
def post_save_jurnal_belajar(sender, instance, created, **kwargs):
    try:
        kelas_siswa = KelasSiswa.objects.filter(KELAS = instance.DAFTAR.KELAS)
        for siswa in kelas_siswa:
            AbsensiSiswa.objects.update_or_create(NIS=siswa.NIS, JURNAL_BELAJAR=instance)
    except Exception as e:
        print(str(e))
        
post_save.connect(post_save_jurnal_belajar, sender=JurnalBelajar)

class AbsensiSiswa(models.Model):
    ID = models.BigAutoField(primary_key=True)
    NIS = models.ForeignKey(DataSiswa, on_delete=models.CASCADE)
    KETERANGAN = models.CharField(
        max_length=255, 
        choices= ENUM_KETERANGAN_ABSEN,
        default='Hadir'
    )
    FILE_KETERANGAN = models.FileField(max_length=255, upload_to='AbsensiSiswa', blank=True)
    JURNAL_BELAJAR = models.ForeignKey(JurnalBelajar, on_delete=models.CASCADE)
    
def post_save_jadwal_mengajar(sender, instance, **kwargs):
    try:
        daftar_jurnal_belajar = DaftarJurnalBelajar.objects.update_or_create(
            GURU = instance.GURU,
            MATA_PELAJARAN = instance.MATA_PELAJARAN,
            KELAS = instance.KELAS,
            SEMESTER = instance.SEMESTER,
            JADWAL_MENGAJAR = instance,
        )
        daftar_jurnal_belajar.save()
        
        # rekap_jam_guru = RekapJamGuru.objects.update_or_create(
        #     DATA_GURU = instance.GURU,
        #     DATA_MENGAJAR_GURU =+ instance
        # )
        
    except Exception as e:
        print(str(e))

post_save.connect(post_save_jadwal_mengajar, sender=JadwalMengajar)

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

    class Meta:
        verbose_name_plural = 'Jadwal Pekan Efektif Semester'
    
    def __str__(self):
        return self.BULAN + ' - Jumlah Minggu = ' + str(self.JUMLAH_MINGGU) + ' || Jumlah Minggu Efektif = ' + str(self.JUMLAH_MINGGU_EFEKTIF)
    
class JadwalPekanTidakEfektif(models.Model):
    ID = models.BigAutoField(primary_key=True)
    URAIAN_KEGIATAN =  models.TextField()
    JUMLAH_MINGGU = models.IntegerField()
    KETERANGAN = models.TextField()

    class Meta:
        verbose_name_plural = 'Jadwal Pekan Tidak Efektif'
    
    def __str__(self):
        return self.URAIAN_KEGIATAN + ' (' + str(self.JUMLAH_MINGGU) + ')'
    
class JadwalPekanAktif(models.Model):
    ID = models.BigAutoField(primary_key=True)
    MINGGU_TIDAK_EFEKTIF = models.ManyToManyField(JadwalPekanTidakEfektif)
    MINGGU_EFEKTIF = models.ManyToManyField(JadwalPekanEfektifSemester)
    MATA_PELAJARAN = models.ForeignKey(MataPelajaran, on_delete=models.CASCADE)
    KELAS = models.ForeignKey(Kelas, on_delete=models.CASCADE)
    SEMESTER = models.ForeignKey(DataSemester, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Jadwal Pekan Aktif'

class Raport (models.Model):
    ID = models.BigAutoField(primary_key=True)
    KELAS_SISWA = models.ForeignKey(KelasSiswa, on_delete=models.CASCADE)
    SEMESTER = models.ForeignKey(DataSemester, on_delete=models.CASCADE)
    BUKU_INDUK = models.ForeignKey(BukuInduk, on_delete=models.CASCADE)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['KELAS_SISWA', 'SEMESTER'], name='%(app_label)s_%(class)s_unique')
        ]
        verbose_name_plural = "Raport"
    
    def __str__(self):
        return str(self.KELAS_SISWA)
    
    
class NilaiRaport(models.Model):
    ID = models.BigAutoField(primary_key=True)
    RAPORT = models.ForeignKey(Raport, on_delete=models.CASCADE)
    MATA_PELAJARAN = models.ForeignKey(MataPelajaran, on_delete=models.CASCADE)
    KELOMPOK_MATA_PELAJARAN = models.CharField(max_length=255, choices=ENUM_KELOMPOK_MATA_PELAJARAN)
    BEBAN = models.BigIntegerField()
    NILAI_PENGETAHUAN = models.BigIntegerField()
    NILAI_KETERAMPILAN = models.BigIntegerField()
    DESKRIPSI_PENGETAHUAN = models.CharField(max_length=255)
    DESKRIPSI_KETERAMPILAN = models.CharField(max_length=255)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['MATA_PELAJARAN'], name='%(app_label)s_%(class)s_unique')
        ]
        verbose_name_plural = "Nilai Raport"


class RekapJurnalBelajar(models.Model):
    FILE_REKAP = models.FileField(max_length=255, upload_to='Rekap_Jurnal_Belajar')
    FILE_ZIP = models.FileField(max_length=255, upload_to='Rekap_Jurnal_Belajar', blank=True)

    class Meta:
        verbose_name_plural = "Rekap Jurnal Belajar"

    def __str__(self):
        return 'Rekap Jurnal Belajar'
    
    def save(self, *args, **kwargs):
        self.pk = 1
        
        super(RekapJurnalBelajar, self).save(*args, **kwargs)

    @classmethod
    def load(self):
        obj, created = self.objects.get_or_create(pk=1)

        return obj
    
# Configuration Model
class Configuration(ConfigurationModel):
    TAHUN_AJARAN_AKTIF = models.ForeignKey(TahunAjaran, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Configuration"