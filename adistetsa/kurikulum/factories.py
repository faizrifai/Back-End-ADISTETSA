from factory.django import DjangoModelFactory

from .models import *
from .enums import *

import factory

from .models import DataSiswa, DataSemester, MataPelajaran

# random function section
def random_enum(nama_enum):
    pilihan = [x[0] for x in nama_enum]
    return pilihan


# factory class section
class KelasFactory(DjangoModelFactory):
    class Meta:
        model = Kelas
        django_get_or_create=(
            'TAHUN_AJARAN','TINGKATAN','JURUSAN'
        )

    TAHUN_AJARAN = factory.Iterator(TahunAjaran.objects.all())
    TINGKATAN = factory.Faker('random_element', elements=random_enum(ENUM_TINGKATAN))
    JURUSAN = factory.Iterator(Jurusan.objects.all())

class OfferingKelasFactory(DjangoModelFactory):
    class Meta:
        model = OfferingKelas
        django_get_or_create=(
            'KELAS','OFFERING'
        )

    KELAS = factory.Iterator(Kelas.objects.all())
    OFFERING = factory.Iterator(NamaOfferingKelas.objects.all())


class KelasSiswaFactory(DjangoModelFactory):
    class Meta:
        model = KelasSiswa
        django_get_or_create=(
            'NIS','KELAS'
        )

    NIS = factory.Iterator(DataSiswa.objects.all())
    KELAS = factory.Iterator(OfferingKelas.objects.all())


class JadwalMengajarFactory(DjangoModelFactory):
    class Meta:
        model = JadwalMengajar
        django_get_or_create=(
            'KELAS','MATA_PELAJARAN','HARI'
        )

    GURU = factory.Iterator(DataGuru.objects.all())
    TAHUN_AJARAN = factory.Iterator(TahunAjaran.objects.all())
    SEMESTER = factory.Iterator(DataSemester.objects.all())
    KELAS = factory.Iterator(OfferingKelas.objects.all())
    MATA_PELAJARAN = factory.Iterator(MataPelajaran.objects.all())
    HARI = factory.Faker('random_element', elements=random_enum(ENUM_HARI))

    @factory.post_generation
    def waktu_pelajaran(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for data in extracted:
                self.WAKTU_PELAJARAN.add(data)


class NilaiRaportFactory(DjangoModelFactory):
    class Meta:
        model = NilaiRaport
        django_get_or_create=(
            'RAPORT','MATA_PELAJARAN'
        )
    
    RAPORT = models.ForeignKey(Raport, on_delete=models.CASCADE)
    MATA_PELAJARAN = factory.Iterator(MataPelajaran.objects.all())
    KELOMPOK_MATA_PELAJARAN = factory.Faker('random_element', elements=random_enum(ENUM_KELOMPOK_MATA_PELAJARAN))
    BEBAN = factory.Faker('pyint', min_value=1, max_value=4)
    NILAI_PENGETAHUAN = factory.Faker('pyint', min_value=75, max_value=100)
    NILAI_KETERAMPILAN = factory.Faker('pyint', min_value=75, max_value=100)
    DESKRIPSI_PENGETAHUAN = factory.Faker('bs')
    DESKRIPSI_KETERAMPILAN = factory.Faker('bs')

class KTSPFactory(DjangoModelFactory):
    class Meta:
        model = KTSP
        django_get_or_create=(
            'TAHUN_AJARAN',
        )

    TAHUN_AJARAN = factory.Iterator(TahunAjaran.objects.all())
    NAMA_FILE = factory.django.ImageField(color='blue')