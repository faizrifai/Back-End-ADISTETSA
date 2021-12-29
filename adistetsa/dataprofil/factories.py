import factory
import random

from factory.django import DjangoModelFactory

from .models import *
from .enums import *

# random function section


def random_enum(nama_enum):
    pilihan = [x[0] for x in nama_enum]
    return pilihan


# factory class section
class DataSiswaFactory(DjangoModelFactory):
    class Meta:
        model = DataSiswa

    NISN = factory.Faker('credit_card_number')
    NAMA = factory.Faker('name')
    NIPD = factory.Faker('credit_card_number')
    JENIS_KELAMIN = factory.Faker('random_element', elements=random_enum(ENUM_JENIS_KELAMIN))
    TEMPAT_LAHIR = factory.Faker('city')
    TANGGAL_LAHIR = factory.Faker('date')
    NIK = factory.Faker('credit_card_number')
    AGAMA = factory.Faker('random_element', elements=random_enum(ENUM_AGAMA))
    ALAMAT = factory.Faker('address')
    RT = factory.Faker('pyint', min_value=1, max_value=999)
    RW = factory.Faker('pyint', min_value=1, max_value=999)
    DUSUN = factory.Faker('city')
    KELURAHAN = factory.Faker('city')
    KECAMATAN = factory.Faker('city')
    KODE_POS = factory.Faker('postcode')
    JENIS_TINGGAL = factory.Faker('random_element', elements=random_enum(ENUM_JENIS_TINGGAL))
    
class DataOrangTuaFactory(DjangoModelFactory):
    class Meta:
        model = DataOrangTua
        
    NAMA_AYAH = factory.Faker('name')
    TAHUN_LAHIR_AYAH = factory.Faker('date')
    JENJANG_PENDIDIKAN_AYAH = factory.Faker('random_element', elements=random_enum(ENUM_JENJANG_PENDIDIKAN))
    PEKERJAAN_AYAH = factory.Faker('job')
    PENGHASILAN_AYAH = factory.Faker('random_element', elements=random_enum(ENUM_PENGHASILAN))
    NIK_IBU = factory.Faker('credit_card_number')
    NAMA_IBU = factory.Faker('name')
    TAHUN_LAHIR_IBU  = factory.Faker('date')
    JENJANG_PENDIDIKAN_IBU = factory.Faker('random_element', elements=random_enum(ENUM_JENJANG_PENDIDIKAN))
    PEKERJAAN_IBU = factory.Faker('job')
    PENGHASILAN_IBU = factory.Faker('random_element', elements=random_enum(ENUM_PENGHASILAN))
    NIK_WALI = factory.Faker('credit_card_number')
    NAMA_WALI = factory.Faker('name')
    TAHUN_LAHIR_WALI  = factory.Faker('date')
    JENJANG_PENDIDIKAN_WALI = factory.Faker('random_element', elements=random_enum(ENUM_JENJANG_PENDIDIKAN))
    PEKERJAAN_WALI = factory.Faker('job')
    PENGHASILAN_WALI = factory.Faker('random_element', elements=random_enum(ENUM_PENGHASILAN))
  
class DataKompetensiPegawaiFactory(DjangoModelFactory):
    class Meta:
        model = DataKompetensiPegawai
         
    BIDANG_STUDI = factory.Faker('words')
    URUTAN= factory.Faker('pyint', min_value=1, max_value=10)

class DataAnakPegawaiFactory(DjangoModelFactory):
    class Meta:
        model = DataAnakPegawai
        
    STATUS = factory.Faker('pybool')
    JENJANG = factory.Faker('random_element', elements=random_enum(ENUM_JENJANG_PENDIDIKAN))
    NISN = factory.Faker('credit_card_number')
    NAMA = factory.Faker('name')
    JENIS_KELAMIN= factory.Faker('random_element', elements=random_enum(ENUM_JENIS_KELAMIN))
    TEMPAT_LAHIR = factory.Faker('city')
    TANGGAL_LAHIR = factory.Faker('date')
    TAHUN_MASUK = factory.Faker('year')
    
class DataBeasiswaPegawaiFactory(DjangoModelFactory):
    class Meta:
        model = DataBeasiswaPegawai
        
    JENIS = factory.Faker('word')
    PENYELENGGARA = factory.Faker('company')
    DARI_TAHUN = factory.Faker('year')
    SAMPAI_TAHUN = factory.Faker('year')
    MASIH_MENERIMA = factory.Faker('pybool')
    
class DataBukuPegawaiFactory(DjangoModelFactory):
    class Meta:
        model = DataBukuPegawai
        
    JUDUL_BUKU = factory.Faker('sentence')
    TAHUN_BUKU = factory.Faker('year')
    PENERBIT_BUKU = factory.Faker('company')
    
class DataDiklatPegawaiFactory(DjangoModelFactory):
    class Meta:
        model = DataDiklatPegawai
        
    JENIS_DIKLAT = factory.Faker('word')
    NAMA = factory.Faker('name')
    PENYELENGGARA = factory.Faker('company')
    TAHUN = factory.Faker('year')
    PERAN = factory.Faker('word')
    
class DataKaryaTulisPegawaiFactory(DjangoModelFactory):
    class Meta:
        model = DataKaryaTulisPegawai

    JUDUL = factory.Faker('sentence')
    TAHUN = factory.Faker('year')
    PUBLIKASI = factory.Faker('company')
    KETERANGAN = factory.Faker('word')
    
class DataKesejahteraanPegawaiFactory(DjangoModelFactory):
    class Meta:
        model = DataKesejahteraanPegawai
        
    JENIS = factory.Faker('word')
    NAMA = factory.Faker('name')
    PENYELENGGARA = factory.Faker('company')
    DARI_TAHUN = factory.Faker('year')
    SAMPAI_TAHUN = factory.Faker('year')
    STATUS = factory.Faker('pybool')
    
class DataTunjanganPegawaiFactory(DjangoModelFactory):
    class Meta:
        model = DataTunjanganPegawai
        
    JENIS = factory.Faker('word')
    NAMA = factory.Faker('name')
    INSTANSI = factory.Faker('company')
    SUMBER_DANA = factory.Faker('word')
    DARI_TAHUN = factory.Faker('year')
    SAMPAI_TAHUN = factory.Faker('year')
    NOMINAL = factory.Faker('pyint', min_value=100000, max_value=99999999)
    STATUS = factory.Faker('pybool')
    
class DataTugasTambahanPegawaiFactory(DjangoModelFactory):
    class Meta:
        model = DataTugasTambahanPegawai
        
    JABATAN_PTK = factory.Faker('word')
    JPM = factory.Faker('pyint', min_value=1, max_value=99)
    NO_SK = factory.Faker('credit_card_number')
    TMT_TAMBAHAN = factory.Faker('word')
    TST_TAMBAHAN = factory.Faker('word') 
    
class DataPenghargaanPegawaiFactory(DjangoModelFactory):
    class Meta:
        model = DataPenghargaanPegawai
        
    TINGKAT_PERNGHARGAAN = factory.Faker('pyint', min_value=1, max_value=99)
    JENIS_PENGHARGAAN = factory.Faker('word')
    NAMA = factory.Faker('name')
    TAHUN = factory.Faker('year')
    INSTANSI = factory.Faker('company')
    
class DataNilaiTesPegawaiFactory(DjangoModelFactory):
    class Meta:
        model = DataNilaiTesPegawai
        
    JENIS = factory.Faker('word')
    NAMA = factory.Faker('name')
    PENYELENGGARA = factory.Faker('company')
    TAHUN = factory.Faker('year')
    SKOR = factory.Faker('pyint', min_value=10, max_value=100)
    
class DataRiwayatGajiBerkalaPegawaiFactory(DjangoModelFactory):
    class Meta:
        model = DataRiwayatGajiBerkalaPegawai
        
    PANGKAT_GOLONGAN = factory.Faker('pyint', min_value=1, max_value=16)
    NO_SK = factory.Faker('credit_card_number')
    TANGGAL_SK = factory.Faker('date')
    TMT_KGB = factory.Faker('word')
    TAHUN_MK = factory.Faker('year')
    BULAN_MK = factory.Faker('year')     
    GAJI_POKOK = factory.Faker('pyint', min_value=100000, max_value=99999999)
    
class DataRiwayatJabatanStrukturalPegawaiFactory(DjangoModelFactory):
    class Meta:
        model = DataRiwayatJabatanStrukturalPegawai

    JABATAN_PTK = factory.Faker('word')
    SK_STRUKTURAL = factory.Faker('credit_card_number')
    TMT_JABATAN = factory.Faker('word')
    
class DataRiwayatKepangkatanPegawaiFactory(DjangoModelFactory):
    class Meta:
        model = DataRiwayatKepangkatanPegawai
        
    PANGKAT_GOLONGAN = factory.Faker('pyint', min_value=1, max_value=16)
    NO_SK = factory.Faker('credit_card_number')
    TANGGAL_SK = factory.Faker('date')
    PANGKAT_GOLONGAN = factory.Faker('pyint', min_value=1, max_value=16)
    MK_TAHUN = factory.Faker('year')
    MK_BULAN = factory.Faker('month')
    
class DataRiwayatPendidikanFormalPegawaiFactory(DjangoModelFactory):
    class Meta:
        model = DataRiwayatPendidikanFormalPegawai
        
    BIDANG_STUDI = factory.Faker('word')
    JENJANG = factory.Faker('random_element', elements=random_enum(ENUM_JENJANG_PENDIDIKAN))
    GELAR = factory.Faker('word')
    SATUAN = factory.Faker('word')
    FAKULTAS = factory.Faker('word')
    KEPENDIDIKAN = factory.Faker('word')
    TAHUN_MASUK = factory.Faker('year')
    TAHUN_LULUS = factory.Faker('year')
    NIM = factory.Faker('credit_card_number')
    MASIH = factory.Faker('pybool')
    SMT = factory.Faker('pyint', min_value=1, max_value=8)
    IPK = factory.Faker('pyfloat', min_value=1, max_value=4)
    
class DataRiwayatSertifikasiPegawaiFactory(DjangoModelFactory):
    class Meta:
        model = DataRiwayatSertifikasiPegawai
        
    JENIS_SERTIFIKASI = factory.Faker('word')
    NO_SERTIFIKASI = factory.Faker('credit_card_number')
    TAHUN_SERTIFIKASI = factory.Faker('year')
    BIDANG_STUDI = factory.Faker('word')
    NO_REGISTRASI = factory.Faker('credit_card_number')
    NO_PESERTA = factory.Faker('pyint', min_value=1, max_value=999)
    
class DataRiwayatJabatanFungsionalPegawaiFactory(DjangoModelFactory):
    class Meta:
        model = DataRiwayatJabatanFungsionalPegawai
        
    JABATAN_FUNGSIONAL = factory.Faker('word')
    SK_JABATAN_FUNGSIONAL = factory.Faker('credit_card_number')
    TMT_JABATAN = factory.Faker('word')
    
class DataRiwayatKarirGuruPegawaiFactory(DjangoModelFactory):
    class Meta:
        model = DataRiwayatKarirGuruPegawai
        
    JENJANG = factory.Faker('random_element', elements=random_enum(ENUM_JENJANG_PENDIDIKAN))
    JENIS_LEMBAGA = factory.Faker('company')
    STS_KEPEGAWAIAN = factory.Faker('random_element', elements=random_enum(ENUM_STATUS_AKTIF))
    JENIS_PTK = factory.Faker('word')
    LEMBAGA = factory.Faker('company')
    NO_SK_KERJA = factory.Faker('credit_card_number')
    TGL_SK_KERJA = factory.Faker('date')
    TMT_KERJA = factory.Faker('word')
    TST_KERJA = factory.Faker('word')
    TEMPAT_KERJA = factory.Faker('city')
    TTD_SK_KERJA = factory.Faker('words')
    MAPEL_DIAJARKAN = factory.Faker('company')
    
class DataPegawaiFactory(DjangoModelFactory):
    class Meta:
        model = DataPegawai
        
    NAMA_SEKOLAH = factory.Faker('company')
    NSS = factory.Faker('credit_card_number')
    NPSN = factory.Faker('credit_card_number')
    ALAMAT_SEKOLAH = factory.Faker('address')
    NAMA_LENGKAP = factory.Faker('name')
    NIK = factory.Faker('credit_card_number')
    JENIS_KELAMIN = factory.Faker('random_element', elements=random_enum(ENUM_JENIS_KELAMIN))
    TEMPAT_LAHIR = factory.Faker('city')
    TANGGAL_LAHIR = factory.Faker('date')
    NAMA_IBU_KANDUNG = factory.Faker('name')
    ALAMAT_TEMPAT_TINGGAL = factory.Faker('address')
    DUSUN = factory.Faker('city')
    KELURAHAN = factory.Faker('city')
    KECAMATAN = factory.Faker('city')
    KOTA = factory.Faker('city')
    PROVINSI = factory.Faker('city')
    LINTANG_1 = factory.Faker('latitude')
    LINTANG_2 = factory.Faker('latitude')
    AGAMA = factory.Faker('random_element', elements=random_enum(ENUM_AGAMA))
    NPWP = factory.Faker('credit_card_number')
    NAMA_WAJIB_PAJAK = factory.Faker('name')
    KEWARGANEGARAAN = factory.Faker('country')
    STATUS_KAWIN = factory.Faker('random_element', elements=random_enum(ENUM_STATUS_KAWIN))
    NAMA_PASANGAN = factory.Faker('name')
    PEKERJAAN_PASANGAN = factory.Faker('job')
    PASANGAN_PNS = factory.Faker('random_element', elements=random_enum(ENUM_LAYAK_PIP))
    NIP_PASANGAN = factory.Faker('credit_card_number')
    STATUS_PEGAWAI = factory.Faker('random_element', elements=random_enum(ENUM_STATUS_AKTIF))
    PNS = factory.Faker('random_element', elements=random_enum(ENUM_PNS))
    NIP = factory.Faker('credit_card_number')
    NIY = factory.Faker('credit_card_number')
    NIGB = factory.Faker('credit_card_number')
    NUPTK = factory.Faker('credit_card_number')
    JENIS_PTK = factory.Faker('word')
    STATUS_AKTIF = factory.Faker('random_element', elements=random_enum(ENUM_STATUS_AKTIF))
    SK_PENGANGKATAN = factory.Faker('credit_card_number')
    TMT_PENGANGKATAN = factory.Faker('credit_card_number')
    LEMBAGA_PENGANGKATAN = factory.Faker('company')
    SK_CPNS = factory.Faker('credit_card_number')
    TMT_CPNS = factory.Faker('credit_card_number')
    TMT_PNS = factory.Faker('credit_card_number')
    PANGKAT = factory.Faker('words')
    SUMBER_GAJI = factory.Faker('company')
    KARTU_PEGAWAI = factory.Faker('credit_card_number')
    KARIS = factory.Faker('credit_card_number')
    NO_SURAT = factory.Faker('credit_card_number')
    TGL_SURAT = factory.Faker('date')
    TMT_TUGAS = factory.Faker('credit_card_number')
    SEKOLAH_INDUK = factory.Faker('sentence')
    LISENSI_KEPALA_SEKOLAH = factory.Faker('sentence')
    KODE_PROGRAM_KEAHLIAN = factory.Faker('credit_card_number')
    JENIS_KETUNAAN = factory.Faker('words')
    SPESIALIS_MENANGANI = factory.Faker('words')
    STATUS_AKTIF = factory.Faker('random_element', elements=random_enum(ENUM_STATUS_AKTIF))
    NO_TELP = factory.Faker('phone_number')
    EMAIL = factory.Faker('email')