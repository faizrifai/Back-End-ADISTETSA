from factory.django import DjangoModelFactory

from .models import *
from .enums import *

import factory, random

from django.db.models import Model
from kurikulum.models import MataPelajaran, OfferingKelas
from kustom_autentikasi.models import DataGuruUser, DataKaryawanUser

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

def random_staf_bk():
    data_guru = DataGuruUser.objects.filter(USER__groups__name__in=['Staf BK'])
    data_karyawan = DataKaryawanUser.objects.filter(USER__groups__name__in=['Staf BK'])

    result = []
    for data in data_guru:
        result.append({
            'USER': data.USER,
            'NAMA': data.DATA_GURU.NAMA_LENGKAP
        })

    for data in data_karyawan:
        result.append({
            'USER': data.USER,
            'NAMA': data.DATA_KARYAWAN.NAMA_LENGKAP
        })

    return result

def random_siswa_user():
    result = DataSiswaUser.objects.all()

    siswa = []
    for data in result:
        siswa.append(data.USER)

    return siswa


# factory class section
class DataAlumniFactory(DjangoModelFactory):
    class Meta:
        model = DataAlumni

    NAMA_SISWA = factory.Faker('name')
    KELAS = factory.Faker('random_element', elements=random_id_from_model(OfferingKelas))
    NIS = factory.Faker('credit_card_number')
    NISN = factory.Faker('credit_card_number')
    TAHUN_AJARAN = factory.Faker('random_element', elements=random_id_from_model(TahunAjaran))
    NAMA_PT = factory.Faker('company')
    PROGRAM_STUDI = factory.Faker('job')
    MEDIA_SOSIAL = factory.Faker('domain_word')
    EMAIL = factory.Faker('ascii_email')
    ALAMAT = factory.Faker('address')
    TEMPAT_BEKERJA = factory.Faker('address')

class KatalogKonselorFactory(DjangoModelFactory):
    class Meta:
        model = KatalogKonselor
        django_get_or_create=(
            'USER',
        )
        exclude = ('data_user',)

    data_user = random.choice(random_staf_bk())

    USER = data_user['USER']
    NAMA = data_user['NAMA']
    KOMPETENSI = factory.Faker('random_element', elements=random_id_from_model(MataPelajaran))
    ALUMNUS = factory.Faker('company')
    WHATSAPP = 'https://wa.me/082394033'
    CONFERENCE = 'https://meet.google.com'
    FOTO = factory.django.ImageField(color='blue')
    STATUS = factory.Faker('random_element', elements=random_enum(ENUM_STATUS))

class KonsultasiFactory(DjangoModelFactory):
    class Meta:
        model = Konsultasi

    USER = factory.Faker('random_element', elements=random_siswa_user())
    KONSELOR = factory.Faker('random_element', elements=random_id_from_model(KatalogKonselor))
    TANGGAL_KONSULTASI = factory.Faker('date')
    JAM_AWAL = '05:00'
    JAM_AKHIR = '08:00'
    JENIS_MASALAH = factory.Faker('random_element', elements=random_enum(ENUM_JENIS_MASALAH))
    STATUS = 'Diajukan'