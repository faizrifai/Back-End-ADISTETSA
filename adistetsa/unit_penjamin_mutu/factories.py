from pyexpat import model
from attr import Factory
import django
from factory.django import DjangoModelFactory

from .models import *
from .enums import *

import factory

def random_enum(nama_enum):
    pilihan = [x[0] for x in nama_enum]
    return pilihan

class TugasPokokTendikFactory(DjangoModelFactory):
    class Meta:
        model = TugasPokokTendik

    JENIS_TUGAS = factory.Faker('sentence')

class JenisBidangFactory(DjangoModelFactory):
    class Meta:
        model = JenisBidang

    KODE_BIDANG = factory.Faker('pyint', min_value=1, max_value=999)
    NAMA_BIDANG = factory.Faker('bs')

class PembagianTugasBKFactory(DjangoModelFactory):
    class Meta:
        model = PembagianTugasGuruBK
        django_get_or_create=(
            'DATA_GURU', 'TAHUN_AJARAN', 'SEMESTER', 'KETERANGAN_TUGAS'
        )
    
    DATA_GURU = factory.Iterator(DataGuru.objects.all())
    TAHUN_AJARAN = factory.Iterator(TahunAjaran.objects.all())
    SEMESTER = factory.Iterator(DataSemester.objects.all())
    KETERANGAN_TUGAS = factory.Faker('bs')
    
    @factory.post_generation
    def data_kelas(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for data in extracted:
                self.DATA_KELAS.add(data)
                
class PembagianTugasTIKFactory(DjangoModelFactory):
    class Meta:
        model = PembagianTugasGuruTIK
        django_get_or_create=(
            'DATA_GURU', 'TAHUN_AJARAN', 'SEMESTER', 'KETERANGAN_TUGAS'
        )
    
    DATA_GURU = factory.Iterator(DataGuru.objects.all())
    TAHUN_AJARAN = factory.Iterator(TahunAjaran.objects.all())
    SEMESTER = factory.Iterator(DataSemester.objects.all())
    KETERANGAN_TUGAS = factory.Faker('bs')
    
    @factory.post_generation
    def data_kelas(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for data in extracted:
                self.DATA_KELAS.add(data)

class PembagianTugasPokokTambahanTendikFactory(DjangoModelFactory):
    class Meta: 
        model = PembagianTugasPokokTambahanTendik
        django_get_or_create = (
            'DATA_GURU', 'TAHUN_AJARAN', 'TUGAS_POKOK', 'TUGAS_TAMBAHAN'
        )
        
    DATA_GURU = factory.Iterator(DataGuru.objects.all())
    TAHUN_AJARAN = factory.Iterator(TahunAjaran.objects.all())
    TUGAS_POKOK = factory.Iterator(TugasPokokTendik.objects.all())
    TUGAS_TAMBAHAN = factory.Faker('bs')
    

class RincianTugasPokokTambahanTendikFactory(DjangoModelFactory):
    class Meta:
        model = RincianTugasPokokTambahanTendik
        django_get_or_create = (
            'DATA_GURU', 'TAHUN_AJARAN', 'TUGAS_POKOK', 'TUGAS_TAMBAHAN'
        )

    DATA_GURU = factory.Iterator(DataGuru.objects.all())
    TAHUN_AJARAN = factory.Iterator(TahunAjaran.objects.all())
    TUGAS_POKOK = factory.Faker('bs')
    TUGAS_TAMBAHAN = factory.Faker('bs')
    
class TugasTambahanKepanitiaanTendikFactory(DjangoModelFactory):
    class Meta:
        model = TugasTambahanKepanitiaanTendik
        django_get_or_create = (
            'DATA_GURU', 'TAHUN_AJARAN', 'BIDANG', 'SUB_BIDANG', 'TUGAS'
        )
        
    DATA_GURU = factory.Iterator(DataGuru.objects.all())
    TAHUN_AJARAN = factory.Iterator(TahunAjaran.objects.all())
    BIDANG = factory.Iterator(JenisBidang.objects.all())
    TUGAS = factory.Faker('bs')
    SUB_BIDANG = '-'
    

    

    
    