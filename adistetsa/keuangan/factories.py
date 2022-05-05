from pyexpat import model
import django
from factory.django import DjangoModelFactory

from .models import *
from .enums import *

import factory

# from django.db.models import Model

# random function section
def random_enum(nama_enum):
    pilihan = [x[0] for x in nama_enum]
    return pilihan


class PembayaranFactory(DjangoModelFactory):
    class Meta:
        model = Pembayaran
    
    NAMA_SISWA = factory.Iterator(KelasSiswa.objects.all())
    TANGGAL_PEMBAYARAN = factory.Faker('date')
    PEMBAYARAN_DPSM_RUTIN = factory.Faker('random_element', elements=random_enum(ENUM_NOMINAL_PEMBAYARAN))
    PEMBAYARAN_DPSM_INSINDENTAL = factory.Faker('random_element', elements=random_enum(ENUM_NOMINAL_PEMBAYARAN))
    BIMBEL = factory.Faker('random_element', elements=random_enum(ENUM_NOMINAL_PEMBAYARAN))
    NOMINAL_SPP = '100000'
    PEMBAYARAN_SPP = factory.Faker('random_element', elements=random_enum(ENUM_BULAN))
    GENERATE = False