from factory.django import DjangoModelFactory

from .models import *
from .enums import *

import factory

from django.db.models import Model
from kurikulum.models import DataSiswa, DataSemester, MataPelajaran

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
class NilaiRaportFactory(DjangoModelFactory):
    class Meta:
        model = NilaiRaport
        django_get_or_create=(
            'KELAS_SISWA','SEMESTER','MATA_PELAJARAN'
        )
    
    KELAS_SISWA = factory.Faker('random_element', elements=random_id_from_model(KelasSiswa))
    SEMESTER = factory.Faker('random_element', elements=random_id_from_model(DataSemester))
    MATA_PELAJARAN = factory.Faker('random_element', elements=random_id_from_model(MataPelajaran))                            
    KELOMPOK_MATA_PELAJARAN = factory.Faker('random_element', elements=random_enum(ENUM_KELOMPOK_MATA_PELAJARAN))
    BEBAN = factory.Faker('pyint', min_value=1, max_value=4)
    NILAI_PENGETAHUAN = factory.Faker('pyint', min_value=75, max_value=100)
    NILAI_KETERAMPILAN = factory.Faker('pyint', min_value=75, max_value=100)
    DESKRIPSI_PENGETAHUAN = factory.Faker('bs')
    DESKRIPSI_KETERAMPILAN = factory.Faker('bs')
