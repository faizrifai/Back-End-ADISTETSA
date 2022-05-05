from django.db import models
from django.db.models.signals import post_save, pre_save
from django.utils.text import Truncator
from django.core.exceptions import ValidationError
from dataprofil.models import DataSiswa, DataPelatih
from kurikulum.models import PoinPelanggaran, TahunAjaran, DataSemester, KelasSiswa, Raport
from django.utils import timezone
from .enums import *
import datetime
from adistetsa.custom_function import duplikat_file

class PengajuanLaporanPelanggaran(models.Model):
    ID = models.BigAutoField(primary_key=True)
    DATA_SISWA = models.ForeignKey(DataSiswa, on_delete=models.CASCADE)
    BUKTI_PELANGGARAN = models.FileField(max_length=255, upload_to='BuktiPelanggaran')
    JENIS_PELANGGARAN = models.ForeignKey(PoinPelanggaran, on_delete=models.CASCADE)
    TANGGAL_PENGAJUAN = models.DateTimeField(default=timezone.now)
    STATUS_PENGAJUAN = models.CharField(
        max_length=255, 
        choices=ENUM_PENGAJUAN_PELANGGARAN,
        default='Diajukan'
    )
    class Meta:
        verbose_name_plural = "Pengajuan Laporan Pelanggaran"
    
class PelanggaranSiswa(models.Model):
    ID = models.BigAutoField(primary_key=True)
    DATA_SISWA = models.ForeignKey(DataSiswa, on_delete=models.CASCADE)
    POIN = models.PositiveBigIntegerField(default=0)
    class Meta:
        verbose_name_plural = "Pelanggaran Siswa"

def post_save_data_siswa(sender, instance, **kwargs):
    PelanggaranSiswa.objects.get_or_create(
        DATA_SISWA = instance,
    )

post_save.connect(post_save_data_siswa, sender = DataSiswa)

class RiwayatLaporanPelanggaran(models.Model):
    ID = models.BigAutoField(primary_key=True)
    DATA_SISWA = models.ForeignKey(DataSiswa, on_delete=models.CASCADE)
    BUKTI_PELANGGARAN = models.FileField(max_length=255, upload_to='BuktiPelanggaran')
    JENIS_PELANGGARAN = models.ForeignKey(PoinPelanggaran, on_delete=models.CASCADE)
    TANGGAL_PENGAJUAN = models.DateTimeField(default=timezone.now)
    STATUS_PENGAJUAN = models.CharField(
        max_length=255, 
        choices=ENUM_PENGAJUAN_PELANGGARAN,
        default='Diajukan'
    )
    class Meta:
        verbose_name_plural = "Riwayat Laporan Pelanggaran"

def post_save_persetujuan_laporan(sender, instance, **kwargs):
    try: 
        if instance.STATUS_PENGAJUAN == 'Disetujui' :
            obj = PelanggaranSiswa.objects.get_or_create(
                DATA_SISWA = instance.DATA_SISWA,
            )[0]
            print(obj)
            obj.POIN += instance.JENIS_PELANGGARAN.POIN
            obj.save()
            try:
                riwayat = RiwayatLaporanPelanggaran.objects.create(
                    DATA_SISWA = instance.DATA_SISWA,
                    BUKTI_PELANGGARAN = duplikat_file(instance, instance.BUKTI_PELANGGARAN.read(), instance.BUKTI_PELANGGARAN.name),
                    JENIS_PELANGGARAN = instance.JENIS_PELANGGARAN, 
                    TANGGAL_PENGAJUAN = instance.TANGGAL_PENGAJUAN,
                    STATUS_PENGAJUAN = instance.STATUS_PENGAJUAN
                )
                riwayat.save()
                instance.delete()
            except Exception as e:
                print(str(e))
                
        elif instance.STATUS_PENGAJUAN == 'Ditolak' :
            instance.delete()
    except Exception as e:
        print(str(e))

post_save.connect(post_save_persetujuan_laporan, sender =  PengajuanLaporanPelanggaran)

# post_save.connect(post_save_pengajuan_laporan_pelanggaran, sender=PengajuanLaporanPelanggaran)
class KategoriProgramKebaikan(models.Model):
    ID = models.BigAutoField(primary_key=True)
    NAMA = models.CharField(max_length=255)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['NAMA'], name='%(app_label)s_%(class)s_unique')
        ]
        verbose_name_plural = "Kategori Program Kebaikan"
        ordering = ['NAMA']
    
    def __str__(self):
        return Truncator(self.NAMA).chars(50)
    

class ProgramKebaikan(models.Model):
    ID = models.BigAutoField(primary_key=True)
    KETERANGAN = models.CharField(max_length=255)
    KATEGORI = models.ForeignKey(KategoriProgramKebaikan, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['KETERANGAN'], name='%(app_label)s_%(class)s_unique')
        ]
        verbose_name_plural = "Program Kebaikan"
        ordering = ['KETERANGAN']
    
    def __str__(self):
        return Truncator(self.KETERANGAN).chars(50)

class PoinProgramKebaikan(models.Model):
    ID = models.BigAutoField(primary_key=True)
    KETERANGAN = models.CharField(max_length=255)
    POIN = models.PositiveIntegerField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['KETERANGAN', 'POIN'], name='%(app_label)s_%(class)s_unique')
        ]
        verbose_name_plural = "Poin Program Kebaikan"
        ordering = ['KETERANGAN']
    
    def __str__(self):
        return self.KETERANGAN


class PengajuanProgramKebaikan(models.Model):
    ID = models.BigAutoField(primary_key=True)
    DATA_SISWA = models.ForeignKey(DataSiswa, on_delete=models.CASCADE)
    BUKTI_PROGRAM_KEBAIKAN = models.FileField(max_length=255, upload_to='BuktiProgramKebaikan')
    JENIS_PROGRAM_KEBAIKAN = models.ForeignKey(PoinProgramKebaikan, on_delete=models.CASCADE)
    TANGGAL_PENGAJUAN = models.DateTimeField(default=timezone.now)
    STATUS_PENGAJUAN = models.CharField(
        max_length=255, 
        choices=ENUM_PENGAJUAN_PELANGGARAN,
        default='Diajukan',
    )
    
    class Meta:
        verbose_name_plural = "Pengajuan Program Kebaikan"

class RiwayatProgramKebaikan(models.Model):
    ID = models.BigAutoField(primary_key=True)
    DATA_SISWA = models.ForeignKey(DataSiswa, on_delete=models.CASCADE)
    BUKTI_PROGRAM_KEBAIKAN = models.FileField(max_length=255, upload_to='BuktiProgramKebaikan')
    JENIS_PROGRAM_KEBAIKAN = models.ForeignKey(PoinProgramKebaikan, on_delete=models.CASCADE)
    TANGGAL_PENGAJUAN = models.DateTimeField(default=timezone.now)
    STATUS_PENGAJUAN = models.CharField(
        max_length=255, 
        choices=ENUM_PENGAJUAN_PELANGGARAN,
        default='Diajukan',
    )
    class Meta:
        verbose_name_plural = "Riwayat Program Kebaikan"
        

def post_save_pengajuan_program_kebaikan(sender, instance, **kwargs):
    try: 
        if instance.STATUS_PENGAJUAN == 'Disetujui' :
            obj = PelanggaranSiswa.objects.get_or_create(
                DATA_SISWA = instance.DATA_SISWA
            )[0]
            if obj.POIN < instance.JENIS_PROGRAM_KEBAIKAN.POIN :
                obj.POIN = 0 
                obj.save()
            elif obj.POIN >= instance.JENIS_PROGRAM_KEBAIKAN.POIN :
                obj.POIN -= instance.JENIS_PROGRAM_KEBAIKAN.POIN
                obj.save()
            try:
                riwayat = RiwayatProgramKebaikan.objects.create(
                    DATA_SISWA = instance.DATA_SISWA,
                    BUKTI_PROGRAM_KEBAIKAN = duplikat_file(instance, instance.BUKTI_PROGRAM_KEBAIKAN.read(), instance.BUKTI_PROGRAM_KEBAIKAN.name),
                    JENIS_PROGRAM_KEBAIKAN = instance.JENIS_PROGRAM_KEBAIKAN, 
                    TANGGAL_PENGAJUAN = instance.TANGGAL_PENGAJUAN,
                    STATUS_PENGAJUAN = instance.STATUS_PENGAJUAN
                )
                riwayat.save()
                instance.delete()
            except Exception as e:
                print(str(e))
                
        elif instance.STATUS_PENGAJUAN == 'Ditolak' :
            instance.delete()
    except:
        pass

post_save.connect(post_save_pengajuan_program_kebaikan, sender =  PengajuanProgramKebaikan)

class KatalogEkskul (models.Model):
    ID = models.BigAutoField(primary_key=True)
    NAMA = models.CharField(max_length=255)
    KATEGORI = models.CharField(
        max_length=255,
        choices=ENUM_KATEGORI_EKSKUL,
    )
    DESKRIPSI = models.CharField(max_length=255)
    DOKUMENTASI = models.ImageField(upload_to='KatalogEkskul', max_length=255, blank=True)
    
    def __str__(self):
        return self.NAMA

class JadwalEkskul (models.Model):
    ID = models.BigAutoField(primary_key=True)
    PELATIH = models.ForeignKey(DataPelatih, on_delete=models.CASCADE)
    TAHUN_AJARAN = models.ForeignKey(TahunAjaran, on_delete=models.CASCADE)
    SEMESTER = models.ForeignKey(DataSemester, on_delete=models.CASCADE)
    EKSKUL = models.ForeignKey(KatalogEkskul, on_delete=models.CASCADE)
    HARI = models.CharField(
        max_length=255,
        choices=ENUM_HARI,
    )
    WAKTU_MULAI = models.TimeField()
    WAKTU_BERAKHIR = models.TimeField()
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['PELATIH','HARI','TAHUN_AJARAN','WAKTU_MULAI','WAKTU_BERAKHIR'], name='%(app_label)s_%(class)s_unique')
        ]
    
    def clean(self):
        if self.WAKTU_MULAI > self.WAKTU_BERAKHIR:
            raise ValidationError('Waktu mulai tidak boleh lebih dari waktu berakhir')
        if self.WAKTU_MULAI == self.WAKTU_BERAKHIR:
            raise ValidationError('Waktu mulai tidak boleh sama dengan waktu berakhir')
    
    def __str__(self):
        return str(self.WAKTU_MULAI) + ' - ' + str(self.WAKTU_BERAKHIR)
    

def post_save_jadwal_ekskul(sender, instance, **kwargs):
    try:
        daftar_jurnal_ekskul = DaftarJurnalEkskul.objects.update_or_create(
            PELATIH = instance.PELATIH,
            EKSKUL = instance.EKSKUL,
            SEMESTER = instance.SEMESTER,
            JADWAL_EKSKUL = instance,
        )
    except Exception as e:
        print(str(e))

post_save.connect(post_save_jadwal_ekskul, sender=JadwalEkskul)

class DaftarJurnalEkskul(models.Model):
    ID = models.BigAutoField(primary_key=True)
    PELATIH = models.ForeignKey(DataPelatih,on_delete=models.CASCADE)
    EKSKUL = models.ForeignKey(KatalogEkskul, on_delete=models.CASCADE, default='')
    SEMESTER = models.ForeignKey(DataSemester, on_delete=models.CASCADE)
    JADWAL_EKSKUL = models.ForeignKey(JadwalEkskul, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.EKSKUL.NAMA + ' ' + self.SEMESTER.NAMA


class JurnalEkskul(models.Model):
    ID = models.BigAutoField(primary_key=True)
    PELATIH = models.ForeignKey(DataPelatih,on_delete=models.CASCADE)
    PERTEMUAN = models.CharField(max_length=255)
    TANGGAL_MELATIH = models.DateField(default=datetime.date.today)
    DESKRIPSI_KEGIATAN = models.TextField()
    FILE_DOKUMENTASI = models.FileField(max_length=255, upload_to='JurnalEkskul')
    DAFTAR = models.ForeignKey(DaftarJurnalEkskul, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.DAFTAR.EKSKUL) +  ' - ' + str(self.DAFTAR.SEMESTER) + ' - Pertemuan : ' + self.PERTEMUAN


def pre_save_jurnal_ekskul(sender, instance, **kwargs):
    try:
        daftar = DaftarJurnalEkskul.objects.get(ID=instance.DAFTAR.ID)
        print(daftar)
        instance.PELATIH = daftar.PELATIH
    except Exception as e:
        print(str(e))

pre_save.connect(pre_save_jurnal_ekskul, sender=JurnalEkskul)

def post_save_jurnal_ekskul(sender, instance, created, **kwargs):
    try:
        ekskul = AnggotaEkskul.objects.filter(EKSKUL = instance.DAFTAR.EKSKUL)
        for kelas_siswa in ekskul:
            anggota_ekskul = AnggotaEkskul.objects.get(KELAS_SISWA=kelas_siswa.KELAS_SISWA, EKSKUL=instance.DAFTAR.EKSKUL)
            if (anggota_ekskul.STATUS == 'Nonaktif'):
                continue
            
            AbsensiEkskul.objects.update_or_create(
                NIS=kelas_siswa.KELAS_SISWA.NIS, 
                JURNAL_EKSKUL=instance)
            
    except Exception as e:
        print(str(e))
        
post_save.connect(post_save_jurnal_ekskul, sender=JurnalEkskul)


class AbsensiEkskul(models.Model):
    ID = models.BigAutoField(primary_key=True)
    NIS = models.ForeignKey(DataSiswa, on_delete=models.CASCADE)
    KETERANGAN = models.CharField(
        max_length=255, 
        choices= ENUM_KETERANGAN_ABSEN,
        default='Hadir'
    )
    FILE_KETERANGAN = models.FileField(max_length=255, upload_to='AbsensiEkskul', blank=True)
    JURNAL_EKSKUL = models.ForeignKey(JurnalEkskul, on_delete=models.CASCADE)

    
class PengajuanEkskul (models.Model):
    ID = models.BigAutoField(primary_key=True)
    KELAS_SISWA = models.ForeignKey(KelasSiswa, on_delete=models.CASCADE)
    EKSKUL = models.ForeignKey(KatalogEkskul, on_delete=models.CASCADE)
    TAHUN_AJARAN = models.ForeignKey(TahunAjaran, on_delete=models.CASCADE)
    TANGGAL_PENGAJUAN = models.DateField(default=datetime.date.today)
    STATUS_PENGAJUAN = models.CharField(
        max_length=255,
        choices=ENUM_PENGAJUAN,
        default='Pengajuan',
    )
    
def post_save_pengajuan_ekskul(sender, instance, created, **kwargs):
    # ubah status peminjaman setelah disetujui
    
    if instance.STATUS_PENGAJUAN == 'Disetujui':
        try:
            AnggotaEkskul.objects.update_or_create(
                KELAS_SISWA = instance.KELAS_SISWA, 
                EKSKUL=instance.EKSKUL,
                TAHUN_AJARAN = instance.TAHUN_AJARAN,
                STATUS='Aktif')
            instance.delete()
                    
        except Exception as e:
            print(str(e))
            
    elif instance.STATUS_PENGAJUAN == '' or instance.STATUS_PENGAJUAN == 'Ditolak':
        try:
            instance.delete()
        except Exception as e:
            print(str(e))

post_save.connect(post_save_pengajuan_ekskul, sender=PengajuanEkskul)

class AnggotaEkskul(models.Model):
    ID = models.BigAutoField(primary_key=True)
    KELAS_SISWA = models.ForeignKey(KelasSiswa, on_delete=models.CASCADE)
    TAHUN_AJARAN = models.ForeignKey(TahunAjaran, on_delete=models.CASCADE)
    EKSKUL = models.ForeignKey(KatalogEkskul, on_delete=models.CASCADE)
    STATUS = models.CharField(
        max_length= 255,
        choices=ENUM_STATUS_ANGGOTA_EKSKUL,
        default='',
    )
    
    def __str__(self):
        return str(self.KELAS_SISWA.NIS.NAMA) + ' - ' + str(self.EKSKUL.NAMA) 
    
    def save(self, *args, **kwargs):
        self.TAHUN_AJARAN = self.KELAS_SISWA.KELAS.KELAS.TAHUN_AJARAN
        super(AnggotaEkskul, self).save(*args, **kwargs)
      

class ProgramKerjaEkskul(models.Model):
    ID = models.BigAutoField(primary_key=True)
    PELATIH = models.ForeignKey(DataPelatih, on_delete=models.CASCADE)
    EKSKUL = models.ForeignKey(KatalogEkskul, on_delete=models.CASCADE)
    TAHUN_AJARAN = models.ForeignKey(TahunAjaran, on_delete=models.CASCADE)
    FILE_PROGRAM_KERJA = models.FileField(max_length=255, upload_to='ProgramKerjaEkskul')
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['PELATIH','EKSKUL','TAHUN_AJARAN'], name='%(app_label)s_%(class)s_unique')
        ]
    
    def __str__(self):
        return self.EKSKUL.NAMA 

def post_save_kelas_siswa(sender, instance, created, **kwargs):
    # ubah status peminjaman setelah disetujui
    try:
        daftar = KatalogEkskul.objects.get(NAMA = 'PRAMUKA')
        instance.EKSKUL = daftar
        try:
            AnggotaEkskul.objects.update_or_create(
                KELAS_SISWA = instance, 
                EKSKUL=instance.EKSKUL,
                TAHUN_AJARAN = instance.KELAS.KELAS.TAHUN_AJARAN,
                STATUS = 'Aktif')
        except Exception as e:
            print(str(e))
                    
    except Exception as e:
        print(str(e))
            
post_save.connect(post_save_kelas_siswa, sender=KelasSiswa)

class NilaiEkskul(models.Model):
    ID = models.BigAutoField(primary_key=True)
    DATA_ANGGOTA = models.ForeignKey(AnggotaEkskul, on_delete=models.CASCADE)
    PREDIKAT = models.CharField(
        max_length= 255,
        choices=ENUM_PREDIKAT_EKSKUL,
    )
    DESKRIPSI = models.TextField(max_length= 1020)
    RAPORT= models.ForeignKey(Raport, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.DATA_ANGGOTA)

def post_save_raport(sender, instance, created, **kwargs):
    try:
        anggota_ekskul = AnggotaEkskul.objects.filter(KELAS_SISWA = instance.KELAS_SISWA, STATUS='Aktif')
        for siswa in anggota_ekskul:
            NilaiEkskul.objects.update_or_create(
                DATA_ANGGOTA=siswa,
                RAPORT = instance
            )
    except Exception as e:
        print(str(e))
        
post_save.connect(post_save_raport, sender=Raport)