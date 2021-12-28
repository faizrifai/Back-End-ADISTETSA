import factory
import random

from factory.django import DjangoModelFactory

from .models import *
from .enums import *

# random function section
def random_jenis_kelamin():
    pilihan = [x[0] for x in ENUM_JENIS_KELAMIN]
    return random.choice(pilihan)

def random_agama():
    pilihan = [x[0] for x in ENUM_AGAMA]
    return random.choice(pilihan)

def random_jenis_tinggal():
    pilihan = [x[0] for x in ENUM_JENIS_TINGGAL]
    return random.choice(pilihan)

def random_penerima_kps():
    pilihan = [x[0] for x in ENUM_PENERIMA_KPS]
    return random.choice(pilihan)

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
    JENIS_KELAMIN = factory.LazyFunction(random_jenis_kelamin)
    TEMPAT_LAHIR = factory.Faker('city')
    TANGGAL_LAHIR = factory.Faker('date')
    NIK = factory.Faker('credit_card_number')
    AGAMA = factory.LazyFunction(random_agama)
    ALAMAT = factory.Faker('address')
    RT = factory.Faker('pyint', min_value=1, max_value=999)
    RW = factory.Faker('pyint', min_value=1, max_value=999)
    DUSUN = factory.Faker('city')
    KELURAHAN = factory.Faker('city')
    KECAMATAN = factory.Faker('city')
    KODE_POS = factory.Faker('postcode')
    JENIS_TINGGAL = factory.LazyFunction(random_jenis_tinggal)
    
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
  