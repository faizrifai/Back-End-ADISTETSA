from factory.django import DjangoModelFactory

from .models import *
from .enums import *

import factory


def random_enum(nama_enum):
    pilihan = [x[0] for x in nama_enum]
    return pilihan


class PengajuanSiswaFactory(DjangoModelFactory):
    class Meta:
        model = PengajuanPeminjamanSiswa
        django_get_or_create = (
            "NIS",
            "TANGGAL_PENGAJUAN",
            "STATUS_PENGAJUAN",
            "JANGKA_PEMINJAMAN",
        )

    NIS = factory.Iterator(DataSiswa.objects.all())
    TANGGAL_PENGAJUAN = factory.Faker("date")
    JANGKA_PEMINJAMAN = factory.Faker(
        "random_element", elements=random_enum(ENUM_JANGKA_PEMINJAMAN)
    )
    STATUS_PENGAJUAN = "Pengajuan"

    @factory.post_generation
    def buku(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for data in extracted:
                self.BUKU.add(data)


class PengajuanGuruFactory(DjangoModelFactory):
    class Meta:
        model = PengajuanPeminjamanGuru
        django_get_or_create = (
            "DATA_GURU",
            "TANGGAL_PENGAJUAN",
            "STATUS_PENGAJUAN",
            "JANGKA_PEMINJAMAN",
        )

    DATA_GURU = factory.Iterator(DataGuru.objects.all())
    TANGGAL_PENGAJUAN = factory.Faker("date")
    JANGKA_PEMINJAMAN = factory.Faker(
        "random_element", elements=random_enum(ENUM_JANGKA_PEMINJAMAN)
    )
    STATUS_PENGAJUAN = "Diajukan"

    @factory.post_generation
    def buku(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for data in extracted:
                self.BUKU.add(data)
