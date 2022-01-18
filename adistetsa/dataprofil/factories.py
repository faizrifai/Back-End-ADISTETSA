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

    NIS = factory.Faker('credit_card_number')
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

    NIK_AYAH = factory.Faker('credit_card_number')
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
    
class DataGuruFactory(DjangoModelFactory):
    class Meta:
        model = DataGuru
        
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
    EMAIL = factory.Faker('email')
    
class DataKaryawanFactory(DjangoModelFactory):
    class Meta:
        model = DataKaryawan
        
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
    EMAIL = factory.Faker('email')