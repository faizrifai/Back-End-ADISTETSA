from factory.django import DjangoModelFactory

from .models import *
from .enums import *

from django.db.models import Model
from dataprofil.models import DataSiswa, DataPelatih

import factory
import random
import datetime


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


def random_jam():
    jam = random.randint(1, 15)

    return datetime.datetime(2022, 1, 1, jam, 0, 0)


# factory class section
class PengajuanLaporanPelanggaranFactory(DjangoModelFactory):
    class Meta:
        model = PengajuanLaporanPelanggaran

    DATA_SISWA = factory.Iterator(DataSiswa.objects.all())
    BUKTI_PELANGGARAN = factory.django.ImageField(color="blue")
    JENIS_PELANGGARAN = factory.Iterator(PoinPelanggaran.objects.all())
    TANGGAL_PENGAJUAN = factory.Faker(
        "date_time", tzinfo=timezone.get_current_timezone()
    )


class PengajuanProgramKebaikanFactory(DjangoModelFactory):
    class Meta:
        model = PengajuanProgramKebaikan

    DATA_SISWA = factory.Iterator(DataSiswa.objects.all())
    BUKTI_PROGRAM_KEBAIKAN = factory.django.ImageField(color="blue")
    JENIS_PROGRAM_KEBAIKAN = factory.Iterator(PoinProgramKebaikan.objects.all())
    TANGGAL_PENGAJUAN = factory.Faker(
        "date_time", tzinfo=timezone.get_current_timezone()
    )


class JadwalEkskulFactory(DjangoModelFactory):
    class Meta:
        model = JadwalEkskul
        django_get_or_create = (
            "PELATIH",
            "HARI",
            "TAHUN_AJARAN",
            "WAKTU_MULAI",
            "WAKTU_BERAKHIR",
        )

    PELATIH = factory.Iterator(DataPelatih.objects.all())
    TAHUN_AJARAN = factory.Iterator(TahunAjaran.objects.all())
    SEMESTER = factory.Iterator(DataSemester.objects.all())
    EKSKUL = factory.Iterator(KatalogEkskul.objects.all())
    HARI = factory.Faker("random_element", elements=random_enum(ENUM_HARI))
    WAKTU_MULAI = factory.LazyFunction(random_jam)
    WAKTU_BERAKHIR = factory.LazyAttribute(
        lambda self: self.WAKTU_MULAI + datetime.timedelta(hours=2)
    )


class PengajuanEkskulFactory(DjangoModelFactory):
    class Meta:
        model = PengajuanEkskul

    KELAS_SISWA = factory.Iterator(KelasSiswa.objects.all())
    EKSKUL = factory.Iterator(KatalogEkskul.objects.all())
    TAHUN_AJARAN = factory.LazyAttribute(
        lambda self: self.KELAS_SISWA.KELAS.KELAS.TAHUN_AJARAN
    )
    TANGGAL_PENGAJUAN = factory.Faker(
        "date_time", tzinfo=timezone.get_current_timezone()
    )
