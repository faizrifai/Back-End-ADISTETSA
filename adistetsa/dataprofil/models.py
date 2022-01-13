from django.db import models

from .enums import *

# Constant number
DEFAULT_LENGTH = 225

# Create your models here.
class DataSiswa(models.Model):
    NIS = models.CharField(max_length=DEFAULT_LENGTH, primary_key=True)
    NISN = models.CharField(max_length=DEFAULT_LENGTH)
    NAMA = models.CharField(max_length=DEFAULT_LENGTH)
    NIPD = models.CharField(max_length=DEFAULT_LENGTH)
    JENIS_KELAMIN = models.CharField(
        max_length=20,
        choices=ENUM_JENIS_KELAMIN,
    )
    TEMPAT_LAHIR = models.CharField(max_length=DEFAULT_LENGTH)
    TANGGAL_LAHIR = models.DateField()
    NIK = models.CharField(max_length=DEFAULT_LENGTH)
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
    TELEPON = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    HP = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    EMAIL = models.EmailField(max_length=DEFAULT_LENGTH, blank=True)
    SKHUN = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    PENERIMA_KPS = models.CharField(
        max_length=5,
        choices=ENUM_PENERIMA_KPS,
    )
    NO_KPS = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    ROMBEL_SAAT_INI = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    NO_PESERTA_UJIAN_NASIONAL = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    NO_SERI_IJAZAH = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    PENERIMA_KIP = models.CharField(
        max_length=5,
        choices=ENUM_PENERIMA_KIP,
    )
    NO_KKS = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
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
    NO_KK = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    BERAT_BADAN = models.IntegerField(blank=True, null=True)
    TINGGI_BADAN = models.IntegerField(blank=True, null=True)
    LINGKAR_KEPALA = models.IntegerField(blank=True, null=True)
    JUMLAH_SAUDARA_KANDUNG = models.IntegerField(blank=True, null=True)
    JARAK_RUMAH_KESEKOLAH_KM = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.NIS) + ' - ' + self.NAMA

    class Meta:
        verbose_name_plural = "Data Siswa"


class DataOrangTua(models.Model):
    ID = models.BigAutoField(primary_key=True)
    NIK_AYAH = models.CharField(max_length=DEFAULT_LENGTH)
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
    NIK_IBU = models.CharField(max_length=DEFAULT_LENGTH)
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
    NIK_WALI = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
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
    DATA_ANAK = models.ManyToManyField(DataSiswa, verbose_name="DAFTAR ANAK", blank=True)
    
    def __str__(self):
        return self.NAMA_AYAH

    class Meta:
        verbose_name_plural = "Data Orangtua dan Wali"

    
class DataGuru(models.Model):
    ID = models.BigAutoField(primary_key=True)
    NAMA_SEKOLAH = models.CharField(max_length=DEFAULT_LENGTH)
    NSS = models.CharField(max_length=DEFAULT_LENGTH)
    NPSN = models.CharField(max_length=DEFAULT_LENGTH)
    ALAMAT_SEKOLAH = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    NAMA_LENGKAP = models.CharField(max_length=DEFAULT_LENGTH)
    NIK = models.CharField(max_length=DEFAULT_LENGTH)
    JENIS_KELAMIN = models.CharField(
        max_length=20,
        choices=ENUM_JENIS_KELAMIN,
    )
    TEMPAT_LAHIR = models.CharField(max_length=DEFAULT_LENGTH)
    TANGGAL_LAHIR = models.DateField()
    NAMA_IBU_KANDUNG = models.CharField(max_length=DEFAULT_LENGTH)
    ALAMAT_TEMPAT_TINGGAL = models.CharField(max_length=DEFAULT_LENGTH)
    DUSUN = models.CharField(max_length=DEFAULT_LENGTH)
    KELURAHAN = models.CharField(max_length=DEFAULT_LENGTH)
    KECAMATAN = models.CharField(max_length=DEFAULT_LENGTH)
    KOTA = models.CharField(max_length=DEFAULT_LENGTH)
    PROVINSI = models.CharField(max_length=DEFAULT_LENGTH)
    LINTANG_1 = models.CharField(max_length=DEFAULT_LENGTH)
    LINTANG_2 = models.CharField(max_length=DEFAULT_LENGTH)
    AGAMA = models.CharField(
        max_length=20,
        choices=ENUM_AGAMA,
    )
    NPWP = models.CharField(max_length=DEFAULT_LENGTH)
    NAMA_WAJIB_PAJAK = models.CharField(max_length=DEFAULT_LENGTH)
    KEWARGANEGARAAN = models.CharField(max_length=DEFAULT_LENGTH)
    STATUS_KAWIN = models.CharField(
        max_length=11,
        choices=ENUM_STATUS_KAWIN,
    )
    NAMA_PASANGAN = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    PEKERJAAN_PASANGAN = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    PASANGAN_PNS = models.CharField(
        max_length=5,
        choices=ENUM_PASANGAN_PNS,
        blank=True,
    )
    NIP_PASANGAN = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    STATUS_PEGAWAI = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    PNS = models.CharField(
        max_length=5,
        choices=ENUM_PNS,
        blank=True
    )
    NIP = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    NIY = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    NIGB = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    NUPTK = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    JENIS_PTK = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    STATUS_AKTIF = models.CharField(
        max_length=11,
        choices=ENUM_STATUS_AKTIF,
        blank=True
    )
    SK_PENGANGKATAN = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    TMT_PENGANGKATAN = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    LEMBAGA_PENGANGKATAN = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    SK_CPNS = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    TMT_CPNS = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    TMT_PNS = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    PANGKAT = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    SUMBER_GAJI = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    KARTU_PEGAWAI = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    KARIS = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    NO_SURAT = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    TGL_SURAT = models.DateField(blank=True, null=True)
    TMT_TUGAS = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    SEKOLAH_INDUK = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    LISENSI_KEPALA_SEKOLAH = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    KODE_PROGRAM_KEAHLIAN = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    JENIS_KETUNAAN = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    SPESIALIS_MENANGANI = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    STATUS_AKTIF = models.CharField(
        max_length=14,
        choices=ENUM_STATUS_AKTIF,
        blank=True
    )
    HP = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    EMAIL = models.EmailField(max_length=DEFAULT_LENGTH, blank=True)
    
    def __str__(self):
        return str(self.NIK) + ' - ' + self.NAMA_LENGKAP
    
    class Meta:
        verbose_name_plural = "Data Guru"
        
class DataKaryawan(models.Model):
    ID = models.BigAutoField(primary_key=True)
    NAMA_SEKOLAH = models.CharField(max_length=DEFAULT_LENGTH)
    NSS = models.CharField(max_length=DEFAULT_LENGTH)
    NPSN = models.CharField(max_length=DEFAULT_LENGTH)
    ALAMAT_SEKOLAH = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    NAMA_LENGKAP = models.CharField(max_length=DEFAULT_LENGTH)
    NIK = models.CharField(max_length=DEFAULT_LENGTH)
    JENIS_KELAMIN = models.CharField(
        max_length=20,
        choices=ENUM_JENIS_KELAMIN,
    )
    TEMPAT_LAHIR = models.CharField(max_length=DEFAULT_LENGTH)
    TANGGAL_LAHIR = models.DateField()
    NAMA_IBU_KANDUNG = models.CharField(max_length=DEFAULT_LENGTH)
    ALAMAT_TEMPAT_TINGGAL = models.CharField(max_length=DEFAULT_LENGTH)
    DUSUN = models.CharField(max_length=DEFAULT_LENGTH)
    KELURAHAN = models.CharField(max_length=DEFAULT_LENGTH)
    KECAMATAN = models.CharField(max_length=DEFAULT_LENGTH)
    KOTA = models.CharField(max_length=DEFAULT_LENGTH)
    PROVINSI = models.CharField(max_length=DEFAULT_LENGTH)
    LINTANG_1 = models.CharField(max_length=DEFAULT_LENGTH)
    LINTANG_2 = models.CharField(max_length=DEFAULT_LENGTH)
    AGAMA = models.CharField(
        max_length=20,
        choices=ENUM_AGAMA,
    )
    NPWP = models.CharField(max_length=DEFAULT_LENGTH)
    NAMA_WAJIB_PAJAK = models.CharField(max_length=DEFAULT_LENGTH)
    KEWARGANEGARAAN = models.CharField(max_length=DEFAULT_LENGTH)
    STATUS_KAWIN = models.CharField(
        max_length=11,
        choices=ENUM_STATUS_KAWIN,
    )
    NAMA_PASANGAN = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    PEKERJAAN_PASANGAN = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    PASANGAN_PNS = models.CharField(
        max_length=5,
        choices=ENUM_PASANGAN_PNS,
        blank=True,
    )
    NIP_PASANGAN = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    STATUS_PEGAWAI = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    PNS = models.CharField(
        max_length=5,
        choices=ENUM_PNS,
        blank=True
    )
    NIP = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    NIY = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    NIGB = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    NUPTK = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    JENIS_PTK = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    STATUS_AKTIF = models.CharField(
        max_length=11,
        choices=ENUM_STATUS_AKTIF,
        blank=True
    )
    SK_PENGANGKATAN = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    TMT_PENGANGKATAN = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    LEMBAGA_PENGANGKATAN = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    SK_CPNS = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    TMT_CPNS = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    TMT_PNS = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    PANGKAT = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    SUMBER_GAJI = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    KARTU_PEGAWAI = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    KARIS = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    NO_SURAT = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    TGL_SURAT = models.DateField(blank=True, null=True)
    TMT_TUGAS = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    SEKOLAH_INDUK = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    LISENSI_KEPALA_SEKOLAH = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    KODE_PROGRAM_KEAHLIAN = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    JENIS_KETUNAAN = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    SPESIALIS_MENANGANI = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    STATUS_AKTIF = models.CharField(
        max_length=14,
        choices=ENUM_STATUS_AKTIF,
        blank=True
    )
    HP = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    EMAIL = models.EmailField(max_length=DEFAULT_LENGTH, blank=True)
    
    def __str__(self):
        return str(self.NIK) + ' - ' + self.NAMA_LENGKAP
    
    class Meta:
        verbose_name_plural = "Data Karyawan"

class DataKompetensiGuru(models.Model):
    OWNER = models.ForeignKey(DataGuru, on_delete=models.CASCADE)
    ID = models.BigAutoField(primary_key=True)
    BIDANG_STUDI = models.CharField(max_length=DEFAULT_LENGTH, help_text=('Bidang studi'))
    URUTAN = models.CharField(max_length=DEFAULT_LENGTH)
    def __str__(self):
        return self.BIDANG_STUDI + ' _ ' + self.URUTAN

    class Meta:
        verbose_name_plural = "Data Kompetensi Guru"

class DataKompetensiKaryawan(models.Model):
    OWNER = models.ForeignKey(DataKaryawan, on_delete=models.CASCADE)
    ID = models.BigAutoField(primary_key=True)
    BIDANG_STUDI = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    URUTAN= models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    def __str__(self):
        return self.BIDANG_STUDI + ' _ ' + self.URUTAN

    class Meta:
        verbose_name_plural = "Data Kompetensi Karyawan"

class DataAnakGuru(models.Model):
    OWNER = models.ForeignKey(DataGuru, on_delete=models.CASCADE)
    ID = models.BigAutoField(primary_key=True)
    STATUS = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    JENJANG = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    NISN = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    NAMA = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    JENIS_KELAMIN= models.CharField(
        max_length=20,
        choices=ENUM_JENIS_KELAMIN,
        blank=True
    )
    TEMPAT_LAHIR = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    TANGGAL_LAHIR = models.DateField(blank=True)
    TAHUN_MASUK = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    def __str__(self):
         return self.STATUS + ' - ' + self.JENJANG + ' - ' + self.NISN + ' - ' + self.NAMA + ' - ' + self.JENIS_KELAMIN + ' - ' + self.TEMPAT_LAHIR + ' - ' + self.TAHUN_MASUK

    class Meta:
        verbose_name_plural = "Data Anak Guru"

class DataAnakKaryawan(models.Model):
    OWNER = models.ForeignKey(DataKaryawan, on_delete=models.CASCADE)
    ID = models.BigAutoField(primary_key=True)
    STATUS = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    JENJANG = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    NISN = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    NAMA = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    JENIS_KELAMIN= models.CharField(
        max_length=20,
        choices=ENUM_JENIS_KELAMIN,
        blank=True
    )
    TEMPAT_LAHIR = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    TANGGAL_LAHIR = models.DateField(blank=True)
    TAHUN_MASUK = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    def __str__(self):
         return self.STATUS + ' - ' + self.JENJANG + ' - ' + self.NISN + ' - ' + self.NAMA + ' - ' + self.JENIS_KELAMIN + ' - ' + self.TEMPAT_LAHIR + ' - ' + self.TAHUN_MASUK

    class Meta:
        verbose_name_plural = "Data Anak Karyawan"

class DataBeasiswaGuru(models.Model):
    OWNER = models.ForeignKey(DataGuru, on_delete=models.CASCADE)
    ID = models.BigAutoField(primary_key=True)
    JENIS = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    PENYELENGGARA = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    DARI_TAHUN = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    SAMPAI_TAHUN = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    MASIH_MENERIMA = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    
    def __str__(self):
        return self.JENIS + ' - ' + self.PENYELENGGARA + ' - ' + self.DARI_TAHUN + ' - ' + self.SAMPAI_TAHUN + ' - ' + self.MASIH_MENERIMA
    
    class Meta:
        verbose_name_plural = "Data Beasiswa Guru"

class DataBeasiswaKaryawan(models.Model):
    OWNER = models.ForeignKey(DataKaryawan, on_delete=models.CASCADE)
    ID = models.BigAutoField(primary_key=True)
    JENIS = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    PENYELENGGARA = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    DARI_TAHUN = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    SAMPAI_TAHUN = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    MASIH_MENERIMA = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    
    def __str__(self):
        return self.JENIS + ' - ' + self.PENYELENGGARA + ' - ' + self.DARI_TAHUN + ' - ' + self.SAMPAI_TAHUN + ' - ' + self.MASIH_MENERIMA
    
    class Meta:
        verbose_name_plural = "Data Beasiswa Karyawan"
    
class DataBukuGuru(models.Model):
    OWNER = models.ForeignKey(DataGuru, on_delete=models.CASCADE)
    ID = models.BigAutoField(primary_key=True)
    JUDUL_BUKU = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    TAHUN_BUKU = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    PENERBIT_BUKU = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    def __str__(self):
        return self.JUDUL_BUKU + ' - ' + self.TAHUN_BUKU + ' - ' + self.PENERBIT_BUKU
    
    class Meta:
        verbose_name_plural = "Data Buku Guru"

class DataBukuKaryawan(models.Model):
    OWNER = models.ForeignKey(DataKaryawan, on_delete=models.CASCADE)
    ID = models.BigAutoField(primary_key=True)
    JUDUL_BUKU = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    TAHUN_BUKU = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    PENERBIT_BUKU = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    def __str__(self):
        return self.JUDUL_BUKU + ' - ' + self.TAHUN_BUKU + ' - ' + self.PENERBIT_BUKU
    
    class Meta:
        verbose_name_plural = "Data Buku Karyawan"

class DataDiklatGuru(models.Model):
    OWNER = models.ForeignKey(DataGuru, on_delete=models.CASCADE)
    ID = models.BigAutoField(primary_key=True)
    JENIS_DIKLAT = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    NAMA = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    PENYELENGGARA = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    TAHUN = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    PERAN = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    def __str__(self):
        return self.JENIS_DIKLAT + ' - ' + self.NAMA + ' - ' + self.PENYELENGGARA + ' - ' + self.TAHUN + ' - ' + self.PERAN
    
    class Meta:
        verbose_name_plural = "Data Diklat Guru"

class DataDiklatKaryawan(models.Model):
    OWNER = models.ForeignKey(DataKaryawan, on_delete=models.CASCADE)
    ID = models.BigAutoField(primary_key=True)
    JENIS_DIKLAT = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    NAMA = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    PENYELENGGARA = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    TAHUN = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    PERAN = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    def __str__(self):
        return self.JENIS_DIKLAT + ' - ' + self.NAMA + ' - ' + self.PENYELENGGARA + ' - ' + self.TAHUN + ' - ' + self.PERAN
    
    class Meta:
        verbose_name_plural = "Data Diklat Karyawan"

class DataKaryaTulisGuru(models.Model):
    OWNER = models.ForeignKey(DataGuru, on_delete=models.CASCADE)
    ID = models.BigAutoField(primary_key=True)
    JUDUL = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    TAHUN = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    PUBLIKASI = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    KETERANGAN = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    def __str__(self):
        return self.JUDUL + ' - ' + self.TAHUN + ' - ' + self.PUBLIKASI + ' - ' + self.KETERANGAN
    
    class Meta:
        verbose_name_plural = "Data Karya Tulis Guru"


class DataKaryaTulisKaryawan(models.Model):
    OWNER = models.ForeignKey(DataKaryawan, on_delete=models.CASCADE)
    ID = models.BigAutoField(primary_key=True)
    JUDUL = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    TAHUN = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    PUBLIKASI = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    KETERANGAN = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    def __str__(self):
        return self.JUDUL + ' - ' + self.TAHUN + ' - ' + self.PUBLIKASI + ' - ' + self.KETERANGAN
    
    class Meta:
        verbose_name_plural = "Data Karya Tulis Guru"
        
class DataKesejahteraanGuru(models.Model):
    OWNER = models.ForeignKey(DataGuru, on_delete=models.CASCADE)
    ID = models.BigAutoField(primary_key=True)
    JENIS = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    NAMA = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    PENYELENGGARA = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    DARI_TAHUN = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    SAMPAI_TAHUN = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    STATUS = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    def __str__(self):
        return self.JENIS + ' - ' + self.NAMA + ' - ' + self.PENYELENGGARA + ' - ' + self.DARI_TAHUN + ' - ' + self.SAMPAI_TAHUN + ' - ' + self.STATUS
    
    class Meta:
        verbose_name_plural = "Data Kesejahteraan Karyawan"

class DataKesejahteraanKaryawan(models.Model):
    OWNER = models.ForeignKey(DataKaryawan, on_delete=models.CASCADE)
    ID = models.BigAutoField(primary_key=True)
    JENIS = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    NAMA = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    PENYELENGGARA = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    DARI_TAHUN = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    SAMPAI_TAHUN = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    STATUS = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    def __str__(self):
        return self.JENIS + ' - ' + self.NAMA + ' - ' + self.PENYELENGGARA + ' - ' + self.DARI_TAHUN + ' - ' + self.SAMPAI_TAHUN + ' - ' + self.STATUS
    
    class Meta:
        verbose_name_plural = "Data Kesejahteraan Karyawan"
    
class DataTunjanganGuru(models.Model):
    OWNER = models.ForeignKey(DataGuru, on_delete=models.CASCADE)
    ID = models.AutoField(primary_key=True)
    JENIS = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    NAMA = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    INSTANSI = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    SUMBER_DANA = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    DARI_TAHUN = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    SAMPAI_TAHUN = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    NOMINAL = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    STATUS = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    def __str__(self):
        return self.JENIS + ' - ' + self.NAMA + ' - ' + self.INSTANSI + ' - ' + self.SUMBER_DANA + ' - ' + self.DARI_TAHUN + ' - ' + self.SAMPAI_TAHUN + ' - ' + self.NOMINAL + ' - ' + self.STATUS
    
    class Meta:
        verbose_name_plural = "Data Tunjangan Guru"

class DataTunjanganKaryawan(models.Model):
    OWNER = models.ForeignKey(DataKaryawan, on_delete=models.CASCADE)
    ID = models.AutoField(primary_key=True)
    JENIS = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    NAMA = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    INSTANSI = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    SUMBER_DANA = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    DARI_TAHUN = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    SAMPAI_TAHUN = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    NOMINAL = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    STATUS = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    def __str__(self):
        return self.JENIS + ' - ' + self.NAMA + ' - ' + self.INSTANSI + ' - ' + self.SUMBER_DANA + ' - ' + self.DARI_TAHUN + ' - ' + self.SAMPAI_TAHUN + ' - ' + self.NOMINAL + ' - ' + self.STATUS
    
    class Meta:
        verbose_name_plural = "Data Tunjangan Karyawan"
        
class DataTugasTambahanGuru(models.Model):
    OWNER = models.ForeignKey(DataGuru, on_delete=models.CASCADE)
    ID = models.BigAutoField(primary_key=True)
    JABATAN_PTK = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    JPM = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    NO_SK = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    TMT_TAMBAHAN = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    TST_TAMBAHAN = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    def __str__(self):
        return self.JABATAN_PTK + ' - ' + self.JPM + ' - ' + self.NO_SK + ' - ' + self.TMT_TAMBAHAN + ' - ' + self.TST_TAMBAHAN
     
    class Meta:
        verbose_name_plural = "Data Tugas Tambahan Guru"

class DataTugasTambahanKaryawan(models.Model):
    OWNER = models.ForeignKey(DataKaryawan, on_delete=models.CASCADE)
    ID = models.BigAutoField(primary_key=True)
    JABATAN_PTK = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    JPM = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    NO_SK = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    TMT_TAMBAHAN = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    TST_TAMBAHAN = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    def __str__(self):
        return self.JABATAN_PTK + ' - ' + self.JPM + ' - ' + self.NO_SK + ' - ' + self.TMT_TAMBAHAN + ' - ' + self.TST_TAMBAHAN
     
    class Meta:
        verbose_name_plural = "Data Tugas Tambahan Karyawan"
    
class DataPenghargaanGuru(models.Model):
    OWNER = models.ForeignKey(DataGuru, on_delete=models.CASCADE)
    ID = models.BigAutoField(primary_key=True)
    TINGKAT_PERNGHARGAAN = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    JENIS_PENGHARGAAN = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    NAMA = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    TAHUN = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    INSTANSI = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    def __str__(self):
        return self.TINGKAT_PERNGHARGAAN + ' - ' + self.JENIS_PENGHARGAAN + ' - ' + self.NAMA + ' - ' + self.TAHUN + ' - ' + self.INSTANSI
    
    class Meta:
        verbose_name_plural = "Data Penghargaan Guru"

class DataPenghargaanKaryawan(models.Model):
    OWNER = models.ForeignKey(DataKaryawan, on_delete=models.CASCADE)
    ID = models.BigAutoField(primary_key=True)
    TINGKAT_PERNGHARGAAN = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    JENIS_PENGHARGAAN = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    NAMA = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    TAHUN = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    INSTANSI = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    def __str__(self):
        return self.TINGKAT_PERNGHARGAAN + ' - ' + self.JENIS_PENGHARGAAN + ' - ' + self.NAMA + ' - ' + self.TAHUN + ' - ' + self.INSTANSI
    
    class Meta:
        verbose_name_plural = "Data Penghargaan Karyawan"

class DataNilaiTesGuru(models.Model):
    OWNER = models.ForeignKey(DataGuru, on_delete=models.CASCADE)
    ID = models.BigAutoField(primary_key=True)
    JENIS = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    NAMA = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    PENYELENGGARA = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    TAHUN = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    SKOR = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    def __str__(self):
        return self.JENIS + ' - ' + self.NAMA + ' - ' + self.PENYELENGGARA + ' - ' + self.TAHUN + ' - ' + self.SKOR
    
    class Meta:
        verbose_name_plural = "Data Nilai Test Guru"

class DataNilaiTesKaryawan(models.Model):
    OWNER = models.ForeignKey(DataKaryawan, on_delete=models.CASCADE)
    ID = models.BigAutoField(primary_key=True)
    JENIS = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    NAMA = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    PENYELENGGARA = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    TAHUN = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    SKOR = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    def __str__(self):
        return self.JENIS + ' - ' + self.NAMA + ' - ' + self.PENYELENGGARA + ' - ' + self.TAHUN + ' - ' + self.SKOR
    
    class Meta:
        verbose_name_plural = "Data Nilai Test Karyawan"
    
class DataRiwayatGajiBerkalaGuru(models.Model):
    OWNER = models.ForeignKey(DataGuru, on_delete=models.CASCADE)
    ID = models.BigAutoField(primary_key=True)
    PANGKAT_GOLONGAN = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    NO_SK = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    TANGGAL_SK = models.DateField()
    TMT_KGB = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    TAHUN_MK = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    BULAN_MK = models.CharField(max_length=DEFAULT_LENGTH, blank=True)     
    GAJI_POKOK = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    def __str__(self):
        return self.PANGKAT_GOLONGAN + ' - ' + self.NO_SK + ' - ' + self.TMT_KGB + ' - ' + self.TAHUN_MK + ' - ' + self.BULAN_MK + ' - ' + self.GAJI_POKOK
    
    class Meta:
        verbose_name_plural = "Data Riwayat Gaji Berkala Guru"

class DataRiwayatGajiBerkalaKaryawan(models.Model):
    OWNER = models.ForeignKey(DataKaryawan, on_delete=models.CASCADE)
    ID = models.BigAutoField(primary_key=True)
    PANGKAT_GOLONGAN = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    NO_SK = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    TANGGAL_SK = models.DateField()
    TMT_KGB = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    TAHUN_MK = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    BULAN_MK = models.CharField(max_length=DEFAULT_LENGTH, blank=True)     
    GAJI_POKOK = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    def __str__(self):
        return self.PANGKAT_GOLONGAN + ' - ' + self.NO_SK + ' - ' + self.TMT_KGB + ' - ' + self.TAHUN_MK + ' - ' + self.BULAN_MK + ' - ' + self.GAJI_POKOK
    
    class Meta:
        verbose_name_plural = "Data Riwayat Gaji Berkala Karyawan"
    
class DataRiwayatJabatanStrukturalGuru(models.Model):
    OWNER = models.ForeignKey(DataGuru, on_delete=models.CASCADE)
    ID = models.BigAutoField(primary_key=True)
    JABATAN_PTK = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    SK_STRUKTURAL = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    TMT_JABATAN = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    def __str__(self):
        return self.JABATAN_PTK + ' - ' + self.SK_STRUKTURAL + ' - ' + self.TMT_JABATAN
    
    class Meta:
        verbose_name_plural = "Data Riwayat Jabatan Struktural Guru"

class DataRiwayatJabatanStrukturalKaryawan(models.Model):
    OWNER = models.ForeignKey(DataKaryawan, on_delete=models.CASCADE)
    ID = models.BigAutoField(primary_key=True)
    JABATAN_PTK = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    SK_STRUKTURAL = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    TMT_JABATAN = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    def __str__(self):
        return self.JABATAN_PTK + ' - ' + self.SK_STRUKTURAL + ' - ' + self.TMT_JABATAN
    
    class Meta:
        verbose_name_plural = "Data Riwayat Jabatan Struktural Karyawan"



class DataRiwayatKepangkatanGuru(models.Model):
    OWNER = models.ForeignKey(DataGuru, on_delete=models.CASCADE)
    ID = models.BigAutoField(primary_key=True)
    PANGKAT_GOLONGAN = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    NO_SK = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    TANGGAL_SK = models.DateField()
    PANGKAT_GOLONGAN = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    MK_TAHUN = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    MK_BULAN = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    
    def __str__(self):
        return self.PANGKAT_GOLONGAN + ' - ' + self.NO_SK + ' - ' + self.PANGKAT_GOLONGAN + ' - ' + self.MK_TAHUN + ' - ' + self.MK_BULAN
    
    class Meta:
        verbose_name_plural = "Data Riwayat Kepangkatan Guru"

class DataRiwayatKepangkatanKaryawan(models.Model):
    OWNER = models.ForeignKey(DataKaryawan, on_delete=models.CASCADE)
    ID = models.BigAutoField(primary_key=True)
    PANGKAT_GOLONGAN = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    NO_SK = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    TANGGAL_SK = models.DateField()
    PANGKAT_GOLONGAN = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    MK_TAHUN = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    MK_BULAN = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    
    def __str__(self):
        return self.PANGKAT_GOLONGAN + ' - ' + self.NO_SK + ' - ' + self.PANGKAT_GOLONGAN + ' - ' + self.MK_TAHUN + ' - ' + self.MK_BULAN
    
    class Meta:
        verbose_name_plural = "Data Riwayat Kepangkatan Karyawan"
    
class DataRiwayatPendidikanFormalGuru(models.Model):
    OWNER = models.ForeignKey(DataGuru, on_delete=models.CASCADE)
    ID = models.BigAutoField(primary_key=True)
    BIDANG_STUDI = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    JENJANG = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    GELAR = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    SATUAN = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    FAKULTAS = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    KEPENDIDIKAN = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    TAHUN_MASUK = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    TAHUN_LULUS = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    NIM = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    MASIH = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    SMT = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    IPK = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    def __str__(self):
        return self.BIDANG_STUDI + ' - ' + self.JENJANG + ' - ' + self.GELAR + ' - ' + self.SATUAN + ' - ' + self.FAKULTAS + ' - ' + self.KEPENDIDIKAN + ' - ' + self.TAHUN_MASUK + ' - ' + self.TAHUN_LULUS + ' - ' + self.NIM + ' - ' + self.MASIH + ' - ' + self.SMT + ' - ' + self.IPK
    
    class Meta:
        verbose_name_plural = "Data Riwayat Pendidikan Formal Guru"

class DataRiwayatPendidikanFormalKaryawan(models.Model):
    OWNER = models.ForeignKey(DataKaryawan, on_delete=models.CASCADE)
    ID = models.BigAutoField(primary_key=True)
    BIDANG_STUDI = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    JENJANG = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    GELAR = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    SATUAN = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    FAKULTAS = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    KEPENDIDIKAN = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    TAHUN_MASUK = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    TAHUN_LULUS = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    NIM = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    MASIH = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    SMT = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    IPK = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    def __str__(self):
        return self.BIDANG_STUDI + ' - ' + self.JENJANG + ' - ' + self.GELAR + ' - ' + self.SATUAN + ' - ' + self.FAKULTAS + ' - ' + self.KEPENDIDIKAN + ' - ' + self.TAHUN_MASUK + ' - ' + self.TAHUN_LULUS + ' - ' + self.NIM + ' - ' + self.MASIH + ' - ' + self.SMT + ' - ' + self.IPK
    
    class Meta:
        verbose_name_plural = "Data Riwayat Pendidikan Formal Karyawan"
        
class DataRiwayatSertifikasiGuru(models.Model):
    OWNER = models.ForeignKey(DataGuru, on_delete=models.CASCADE)
    ID = models.BigAutoField(primary_key=True)
    JENIS_SERTIFIKASI = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    NO_SERTIFIKASI = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    TAHUN_SERTIFIKASI = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    BIDANG_STUDI = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    NO_REGISTRASI = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    NO_PESERTA = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    def __str__(self):
        return self.JENIS_SERTIFIKASI + ' - ' + self.NO_SERTIFIKASI + ' - ' + self.TAHUN_SERTIFIKASI + ' - ' + self.BIDANG_STUDI + ' - ' + self.NO_REGISTRASI + ' - ' + self.NO_PESERTA
    
    class Meta:
        verbose_name_plural = "Data Riwayat Sertifikasi Guru"

class DataRiwayatSertifikasiKaryawan(models.Model):
    OWNER = models.ForeignKey(DataKaryawan, on_delete=models.CASCADE)
    ID = models.BigAutoField(primary_key=True)
    JENIS_SERTIFIKASI = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    NO_SERTIFIKASI = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    TAHUN_SERTIFIKASI = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    BIDANG_STUDI = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    NO_REGISTRASI = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    NO_PESERTA = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    def __str__(self):
        return self.JENIS_SERTIFIKASI + ' - ' + self.NO_SERTIFIKASI + ' - ' + self.TAHUN_SERTIFIKASI + ' - ' + self.BIDANG_STUDI + ' - ' + self.NO_REGISTRASI + ' - ' + self.NO_PESERTA
    
    class Meta:
        verbose_name_plural = "Data Riwayat Sertifikasi Karyawan"
    
class DataRiwayatJabatanFungsionalGuru(models.Model):
    OWNER = models.ForeignKey(DataGuru, on_delete=models.CASCADE)
    ID = models.BigAutoField(primary_key=True)
    JABATAN_FUNGSIONAL = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    SK_JABATAN_FUNGSIONAL = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    TMT_JABATAN = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    def __str__(self):
        return self.JABATAN_FUNGSIONAL + ' - ' + self.SK_JABATAN_FUNGSIONAL + ' - ' + self.TMT_JABATAN
    
    class Meta:
        verbose_name_plural = "Data Riwayat Jabatan Fungsional Guru"
    
class DataRiwayatJabatanFungsionalKaryawan(models.Model):
    OWNER = models.ForeignKey(DataKaryawan, on_delete=models.CASCADE)
    ID = models.BigAutoField(primary_key=True)
    JABATAN_FUNGSIONAL = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    SK_JABATAN_FUNGSIONAL = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    TMT_JABATAN = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    def __str__(self):
        return self.JABATAN_FUNGSIONAL + ' - ' + self.SK_JABATAN_FUNGSIONAL + ' - ' + self.TMT_JABATAN
    
    class Meta:
        verbose_name_plural = "Data Riwayat Jabatan Fungsional Karyawan"
          
class DataRiwayatKarirGuru(models.Model):
    OWNER = models.ForeignKey(DataGuru, on_delete=models.CASCADE)
    ID = models.BigAutoField(primary_key=True)
    JENJANG = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    JENIS_LEMBAGA = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    STS_KEPEGAWAIAN = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    JENIS_PTK = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    LEMBAGA = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    NO_SK_KERJA = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    TGL_SK_KERJA = models.DateField()
    TMT_KERJA = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    TST_KERJA = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    TEMPAT_KERJA = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    TTD_SK_KERJA = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    MAPEL_DIAJARKAN = models.CharField(max_length=DEFAULT_LENGTH, blank=True)

    def __str__(self):
        return self.JENJANG + ' - ' + self.JENIS_LEMBAGA + ' - ' + self.STS_KEPEGAWAIAN + ' - ' + self.JENIS_PTK + ' - ' + self.LEMBAGA + ' - ' + self.LEMBAGA + ' - ' + self.NO_SK_KERJA + ' - ' + self.TMT_KERJA + ' - ' + self.TST_KERJA + ' - ' + self.TEMPAT_KERJA + ' - ' + self.TTD_SK_KERJA + ' - ' + self.MAPEL_DIAJARKAN
    
    class Meta:
        verbose_name_plural = "Data Riwayat Karir Guru Guru"

class DataRiwayatKarirKaryawan(models.Model):
    OWNER = models.ForeignKey(DataKaryawan, on_delete=models.CASCADE)
    ID = models.BigAutoField(primary_key=True)
    JENJANG = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    JENIS_LEMBAGA = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    STS_KEPEGAWAIAN = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    JENIS_PTK = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    LEMBAGA = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    NO_SK_KERJA = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    TGL_SK_KERJA = models.DateField()
    TMT_KERJA = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    TST_KERJA = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    TEMPAT_KERJA = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    TTD_SK_KERJA = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    MAPEL_DIAJARKAN = models.CharField(max_length=DEFAULT_LENGTH, blank=True)

    def __str__(self):
        return self.JENJANG + ' - ' + self.JENIS_LEMBAGA + ' - ' + self.STS_KEPEGAWAIAN + ' - ' + self.JENIS_PTK + ' - ' + self.LEMBAGA + ' - ' + self.LEMBAGA + ' - ' + self.NO_SK_KERJA + ' - ' + self.TMT_KERJA + ' - ' + self.TST_KERJA + ' - ' + self.TEMPAT_KERJA + ' - ' + self.TTD_SK_KERJA + ' - ' + self.MAPEL_DIAJARKAN
    
    class Meta:
        verbose_name_plural = "Data Riwayat Karir Karyawan "