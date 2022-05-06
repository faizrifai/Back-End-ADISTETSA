from factory.django import DjangoModelFactory
from factory_djoy import CleanModelFactory

from .models import *
from .enums import *

import random, datetime

import factory
# random function section
def random_enum(nama_enum):
    pilihan = [x[0] for x in nama_enum]
    return pilihan

def random_jam():
    jam = random.randint(1, 15)

    return datetime.datetime(2022, 1, 1, jam, 0, 0)


# factory class section
class PengajuanPeminjamanRuanganFactory(CleanModelFactory):
    class Meta:
        model = PengajuanPeminjamanRuangan
        exclude = ('nama', 'nomor')

    nama = factory.Faker('name')
    nomor = factory.Faker('msisdn')

    USER = factory.Iterator(User.objects.all())
    PENGGUNA = factory.LazyAttribute(lambda p: '{}'.format(p.nama.upper()))
    NO_HP = factory.LazyAttribute(lambda p: f'08{p.nomor}')
    KEGIATAN = factory.Faker('sentence')
    RUANGAN =  factory.Iterator(Ruangan.objects.all())
    TANGGAL_PENGAJUAN = factory.LazyFunction(random_jam)
    TANGGAL_PEMAKAIAN = factory.SelfAttribute('TANGGAL_PENGAJUAN')
    TANGGAL_BERAKHIR = factory.LazyAttribute(lambda self: self.TANGGAL_PEMAKAIAN + datetime.timedelta(days=30))
    JAM_PENGGUNAAN = factory.SelfAttribute('TANGGAL_PENGAJUAN')
    JAM_BERAKHIR = factory.LazyAttribute(lambda self: self.JAM_PENGGUNAAN + datetime.timedelta(hours = 2))
    JENIS_PEMINJAMAN = factory.Faker('random_element', elements=random_enum(ENUM_JENIS_PEMINJAMAN))
    KETERANGAN = factory.Faker('sentence')
    TANDA_TANGAN = factory.django.ImageField(color='white')

class PengajuanPeminjamanBarangFactory(CleanModelFactory):
    class Meta:
        model = PengajuanPeminjamanBarang
        exclude = ('nama', 'nomor')

    nama = factory.Faker('name')
    nomor = factory.Faker('msisdn')

    USER = factory.Iterator(User.objects.all())
    NAMA_PEMINJAM = factory.LazyAttribute(lambda p: '{}'.format(p.nama.upper()))
    NO_TELEPON = factory.LazyAttribute(lambda p: f'08{p.nomor}')
    KEGIATAN = factory.Faker('sentence')
    TANGGAL_PENGAJUAN = factory.LazyFunction(random_jam)
    TANGGAL_PENGGUNAAN = factory.SelfAttribute('TANGGAL_PENGAJUAN')
    TANGGAL_PENGEMBALIAN = factory.LazyAttribute(lambda self: self.TANGGAL_PENGGUNAAN + datetime.timedelta(days=30))
    KETERANGAN = factory.Faker('sentence')
    TANDA_TANGAN = factory.django.ImageField(color='white')

    @factory.post_generation
    def alat(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for data in extracted:
                self.ALAT.add(data)