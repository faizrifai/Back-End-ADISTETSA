from factory.django import DjangoModelFactory

from .models import *
from .enums import *

import factory

from django.db.models import Model
from kurikulum.models import OfferingKelas

# random function section
def random_enum(nama_enum):
    pilihan = [x[0] for x in nama_enum]
    return pilihan

def random_id_from_model(model: Model):
    result = model.objects.all()
    ids = []
    for data in result:
        ids.append(data)

    return ids


# factory class section
class BukuTamuFactory(DjangoModelFactory):
    class Meta:
        model = BukuTamu
        
    NAMA = factory.Faker('name')
    INSTANSI_ASAL = factory.Faker('company')
    ALAMAT = factory.Faker('address')
    NO_HP = factory.Faker('phone_number')
    TANGGAL = factory.Faker('date')
    JAM = factory.Faker('time')
    KEPERLUAN = factory.Faker('catch_phrase')

class LogUKSSiswaFactory(DjangoModelFactory):
    class Meta:
        model = LogUKSSiswa

    JENIS_PTK = 'Siswa'
    NAMA = factory.Faker('name')
    KELAS = factory.Faker('random_element', elements=random_id_from_model(OfferingKelas))
    NISN = factory.Faker('credit_card_number')
    TANGGAL = factory.Faker('date')
    JENIS_PEMERIKSAAN = factory.Faker('catch_phrase')
    OBAT_DIBERIKAN = factory.Faker('catch_phrase')
    TINDAK_LANJUT = factory.Faker('catch_phrase')

class LogUKSTendikFactory(DjangoModelFactory):
    class Meta:
        model = LogUKSTendik

    JENIS_PTK = factory.Faker('random_element', elements=random_enum(ENUM_JENIS_PTK_UKS))
    NAMA = factory.Faker('name')
    TANGGAL = factory.Faker('date')
    JENIS_PEMERIKSAAN = factory.Faker('catch_phrase')
    OBAT_DIBERIKAN = factory.Faker('catch_phrase')
    TINDAK_LANJUT = factory.Faker('catch_phrase')