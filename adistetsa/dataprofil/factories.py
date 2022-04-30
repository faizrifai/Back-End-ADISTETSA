import factory

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
        exclude = ('nama', 'tempat_lahir')

    nama = factory.Faker('name')
    tempat_lahir = factory.Faker('city')

    NIS = factory.Faker('credit_card_number')
    NISN = factory.Faker('credit_card_number')
    NAMA = factory.LazyAttribute(lambda p: '{}'.format(p.nama.upper()))
    NIPD = factory.Faker('credit_card_number')
    JENIS_KELAMIN = factory.Faker('random_element', elements=random_enum(ENUM_JENIS_KELAMIN))
    TEMPAT_LAHIR = factory.LazyAttribute(lambda p: '{}'.format(p.tempat_lahir.upper()))
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
    PENERIMA_KPS = 'Tidak'
    PENERIMA_KIP = 'Tidak'
    LAYAK_PIP = 'Tidak'
    
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
        exclude = ('nama', 'nama_sekolah', 'nama_ibu_kandung', 'nama_wajib_pajak', 'nama_pasangan', 'pekerjaan_pasangan', 'tempat_lahir')

    nama = factory.Faker('name')
    nama_sekolah = factory.Faker('company')
    nama_ibu_kandung = factory.Faker('name')
    nama_wajib_pajak = factory.Faker('name')
    nama_pasangan = factory.Faker('name')
    pekerjaan_pasangan = factory.Faker('job')
    tempat_lahir = factory.Faker('city')
        
    NAMA_SEKOLAH = factory.LazyAttribute(lambda p: '{}'.format(p.nama_sekolah.upper()))
    NSS = factory.Faker('credit_card_number')
    NPSN = factory.Faker('credit_card_number')
    ALAMAT_SEKOLAH = factory.Faker('address')
    NAMA_LENGKAP = factory.LazyAttribute(lambda p: '{}'.format(p.nama.upper()))
    NIK = factory.Faker('credit_card_number')
    JENIS_KELAMIN = factory.Faker('random_element', elements=random_enum(ENUM_JENIS_KELAMIN))
    TEMPAT_LAHIR = factory.Faker('city')
    TANGGAL_LAHIR = factory.Faker('date')
    NAMA_IBU_KANDUNG = factory.LazyAttribute(lambda p: '{}'.format(p.nama_ibu_kandung.upper()))
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
    NAMA_WAJIB_PAJAK = factory.LazyAttribute(lambda p: '{}'.format(p.nama_wajib_pajak.upper()))
    KEWARGANEGARAAN = 'Indonesia'
    STATUS_KAWIN = factory.Faker('random_element', elements=random_enum(ENUM_STATUS_KAWIN))
    NAMA_PASANGAN = factory.LazyAttribute(lambda p: '{}'.format(p.nama_pasangan.upper()))
    PEKERJAAN_PASANGAN = 'Guru'
    PASANGAN_PNS = factory.Faker('random_element', elements=random_enum(ENUM_LAYAK_PIP))
    NIP_PASANGAN = factory.Faker('credit_card_number')
    STATUS_PEGAWAI = factory.Faker('random_element', elements=random_enum(ENUM_STATUS_AKTIF))
    PNS = factory.Faker('random_element', elements=random_enum(ENUM_PNS))
    NIP = factory.Faker('credit_card_number')
    NIY = factory.Faker('credit_card_number')
    NIGB = factory.Faker('credit_card_number')
    NUPTK = factory.Faker('credit_card_number')
    JENIS_PTK = factory.Faker('random_element', elements=random_enum(ENUM_PTK))
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
        exclude = ('nama', 'nama_sekolah', 'nama_ibu_kandung', 'nama_wajib_pajak', 'nama_pasangan', 'pekerjaan_pasangan', 'tempat_lahir')

    nama = factory.Faker('name')
    nama_sekolah = factory.Faker('company')
    nama_ibu_kandung = factory.Faker('name')
    nama_wajib_pajak = factory.Faker('name')
    nama_pasangan = factory.Faker('name')
    pekerjaan_pasangan = factory.Faker('job')
    tempat_lahir = factory.Faker('city')
        
    NAMA_SEKOLAH = factory.LazyAttribute(lambda p: '{}'.format(p.nama_sekolah.upper()))
    NSS = factory.Faker('credit_card_number')
    NPSN = factory.Faker('credit_card_number')
    ALAMAT_SEKOLAH = factory.Faker('address')
    NAMA_LENGKAP = factory.LazyAttribute(lambda p: '{}'.format(p.nama.upper()))
    NIK = factory.Faker('credit_card_number')
    JENIS_KELAMIN = factory.Faker('random_element', elements=random_enum(ENUM_JENIS_KELAMIN))
    TEMPAT_LAHIR = factory.Faker('city')
    TANGGAL_LAHIR = factory.Faker('date')
    NAMA_IBU_KANDUNG = factory.LazyAttribute(lambda p: '{}'.format(p.nama_ibu_kandung.upper()))
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
    NAMA_WAJIB_PAJAK = factory.LazyAttribute(lambda p: '{}'.format(p.nama_wajib_pajak.upper()))
    KEWARGANEGARAAN = 'Indonesia'
    STATUS_KAWIN = factory.Faker('random_element', elements=random_enum(ENUM_STATUS_KAWIN))
    NAMA_PASANGAN = factory.LazyAttribute(lambda p: '{}'.format(p.nama_pasangan.upper()))
    PEKERJAAN_PASANGAN = 'Guru'
    PASANGAN_PNS = factory.Faker('random_element', elements=random_enum(ENUM_LAYAK_PIP))
    NIP_PASANGAN = factory.Faker('credit_card_number')
    STATUS_PEGAWAI = factory.Faker('random_element', elements=random_enum(ENUM_STATUS_AKTIF))
    PNS = factory.Faker('random_element', elements=random_enum(ENUM_PNS))
    NIP = factory.Faker('credit_card_number')
    NIY = factory.Faker('credit_card_number')
    NIGB = factory.Faker('credit_card_number')
    NUPTK = factory.Faker('credit_card_number')
    JENIS_PTK = factory.Faker('random_element', elements=random_enum(ENUM_PTK))
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

class DataPelatihFactory(DjangoModelFactory):
    class Meta:
        model = DataPelatih

    NAMA = factory.Faker('name')