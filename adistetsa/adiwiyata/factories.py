from factory.django import DjangoModelFactory

from .models import *
from .enums import *

import factory

from django.db.models import Model
from dataprofil.models import DataSiswa

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
class SanitasiDrainaseFactory(DjangoModelFactory):
    class Meta:
        model = SanitasiDrainase

    TANGGAL = factory.Faker('date')
    NAMA_KEGIATAN = factory.Faker('catch_phrase')
    UNSUR_TERLIBAT = factory.Faker('name')
    KETERANGAN = factory.Faker('bs')
    FILE = factory.django.FileField(filename='sanitasidrainase.txt', data=b'tes')

class JaringanKerjaFactory(DjangoModelFactory):
    class Meta:
        model = JaringanKerja

    TANGGAL = factory.Faker('date')
    NAMA_KEGIATAN = factory.Faker('catch_phrase')
    KETERANGAN = factory.Faker('bs')
    FILE_MOU = factory.django.FileField(filename='jaringankerja.txt', data=b'tes')
    FILE_DOKUMENTASI = factory.django.FileField(filename='jaringankerja.txt', data=b'tes')

class PublikasiFactory(DjangoModelFactory):
    class Meta:
        model = Publikasi

    TANGGAL = factory.Faker('date')
    NAMA_KEGIATAN = factory.Faker('catch_phrase')
    JENIS_MEDIA = factory.Faker('company_suffix')
    KETERANGAN = factory.Faker('bs')
    FILE = factory.django.FileField(filename='publikasi.txt', data=b'tes')

class DaftarKaderFactory(DjangoModelFactory):
    class Meta:
        model = DaftarKader

    NIS = factory.Faker('random_element', elements=random_id_from_model(DataSiswa))

class KegiatanKaderFactory(DjangoModelFactory):
    class Meta:
        model = KegiatanKader

    TANGGAL = factory.Faker('date')
    NAMA_KEGIATAN = factory.Faker('catch_phrase')
    KETERANGAN = factory.Faker('bs')
    FILE = factory.django.FileField(filename='kegiatan_kader.txt', data=b'tes')

class KonservasiFactory(DjangoModelFactory):
    class Meta:
        model = Konservasi

    TANGGAL = factory.Faker('date')
    KATEGORI = factory.Faker('random_element', elements=random_enum(ENUM_KONSERVASI))
    NAMA_KEGIATAN = factory.Faker('catch_phrase')
    KETERANGAN = factory.Faker('bs')
    FILE = factory.django.FileField(filename='konservasi.txt', data=b'tes')

class PenanamanPohonFactory(DjangoModelFactory):
    class Meta:
        model = PenanamanPohon

    TANGGAL = factory.Faker('date')
    NAMA_KEGIATAN = factory.Faker('catch_phrase')
    JUMLAH = factory.Faker('pyint', min_value=1, max_value=20)
    KETERANGAN = factory.Faker('bs')
    FILE = factory.django.FileField(filename='penanaman_pohon.txt', data=b'tes')

class PembibitanPohonFactory(DjangoModelFactory):
    class Meta:
        model = PembibitanPohon

    TANGGAL = factory.Faker('date')
    NAMA_KEGIATAN = factory.Faker('catch_phrase')
    KETERANGAN = factory.Faker('bs')
    FILE = factory.django.FileField(filename='pembibitan_pohon.txt', data=b'tes')

class PemeliharaanPohonFactory(DjangoModelFactory):
    class Meta:
        model = PemeliharaanPohon

    TANGGAL = factory.Faker('date')
    NAMA_KEGIATAN = factory.Faker('catch_phrase')
    KETERANGAN = factory.Faker('bs')
    FILE = factory.django.FileField(filename='pemeliharaan_pohon.txt', data=b'tes')

class KaryaInovatifFactory(DjangoModelFactory):
    class Meta:
        model = KaryaInovatif

    TANGGAL = factory.Faker('date')
    NAMA_INOVATOR = factory.Faker('name')
    NAMA_KARYA_INOVATIF = factory.Faker('catch_phrase')
    JENIS = factory.Faker('bs')
    FILE = factory.django.FileField(filename='karya.txt', data=b'tes')

class PenerapanPRLHFactory(DjangoModelFactory):
    class Meta:
        model = PenerapanPRLH

    TANGGAL = factory.Faker('date')
    NAMA_KEGIATAN = factory.Faker('catch_phrase')
    PESERTA = factory.Faker('name')
    KETERANGAN = factory.Faker('bs')
    FILE = factory.django.FileField(filename='penerapan_prlh.txt', data=b'tes')

class ReuseReduceRecycleFactory(DjangoModelFactory):
    class Meta:
        model = ReuseReduceRecycle

    TANGGAL = factory.Faker('date')
    NAMA_KEGIATAN = factory.Faker('catch_phrase')
    JENIS_KEGIATAN = factory.Faker('random_element', elements=random_enum(ENUM_3R))
    PIHAK_TERLIBAT = factory.Faker('name')
    KETERANGAN = factory.Faker('bs')
    FILE = factory.django.FileField(filename='3R.txt', data=b'tes')

class PemeliharaanSampahFactory(DjangoModelFactory):
    class Meta:
        model = PemeliharaanSampah

    TANGGAL = factory.Faker('date')
    NAMA_KEGIATAN = factory.Faker('catch_phrase')
    KETERANGAN = factory.Faker('bs')
    FILE = factory.django.FileField(filename='pemeliharaan_sampah.txt', data=b'tes')

class TabunganSampahFactory(DjangoModelFactory):
    class Meta:
        model = TabunganSampah

    KATEGORI = factory.Faker('random_element', elements=random_enum(ENUM_JENIS_SAMPAH))
    TANGGAL = factory.Faker('date')
    JUMLAH = factory.Faker('pyint', min_value=1, max_value=20)