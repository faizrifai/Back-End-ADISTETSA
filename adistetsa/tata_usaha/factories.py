from factory.django import DjangoModelFactory

from kurikulum.enums import ENUM_TINGKATAN

from .models import *
from .enums import *

from dataprofil.models import DataSiswa, DataOrangTua
from kurikulum.models import KelasSiswa

import factory
import random


kelompok = ["IPA", "IPS", "Bahasa"]
sekolah_masuk = [
    "SMPN 1 Malang",
    "SMPN 2 Malang",
    "SMPN 3 Malang",
    "MTSN 1 Malang",
    "MTSN 2 Malang",
    "MTSN 3 Malang",
]
sekolah_keluar = [
    "SMAN 1 Malang",
    "SMAN 2 Malang",
    "MAN 1 Malang",
    "MAN 2 Malang",
    "MAN 3 Malang",
]

# random function section
def random_enum(nama_enum):
    pilihan = [x[0] for x in nama_enum]
    return pilihan


def datasiswa():
    kelas_siswa = KelasSiswa.objects.filter(KELAS__KELAS__TINGKATAN="X")
    kelas_siswa_ids = []

    for data in kelas_siswa:
        orang_tua = DataOrangTua.objects.filter(DATA_ANAK__in=[data.NIS.pk])

        if orang_tua:
            kelas_siswa_ids.append(data.NIS.pk)

    data = kelas_siswa.filter(NIS__pk__in=kelas_siswa_ids)

    siswa = random.choices(list(data))
    return DataSiswa.objects.get(NIS=siswa[0].NIS.NIS)


# factory class section
class BukuIndukFactory(DjangoModelFactory):
    class Meta:
        model = BukuInduk
        django_get_or_create = ("NIS", "ORANG_TUA")

    NIS = factory.LazyFunction(datasiswa)
    NAMA_PANGGILAN = factory.Faker("first_name")
    KEWARGANEGARAAN = factory.Faker("country")
    JUMLAH_SAUDARA_TIRI = factory.Faker("pyint", min_value=1, max_value=5)
    JUMLAH_SAUDARA_ANGKAT = factory.Faker("pyint", min_value=1, max_value=5)
    ANAK_YATIM_PIATU = factory.Faker(
        "random_element", elements=random_enum(ENUM_ANAK_YATIM_PIATU)
    )
    BAHASA = factory.Faker("country")
    GOLONGAN_DARAH = factory.Faker(
        "random_element", elements=random_enum(ENUM_GOLONGAN_DARAH)
    )
    DITERIMA_DI_KELAS = factory.Faker(
        "random_element", elements=random_enum(ENUM_TINGKATAN)
    )
    KELOMPOK = factory.Faker("random_element", elements=random_enum(kelompok))
    TANGGAL_DITERIMA = factory.Faker("date")
    ORANG_TUA = factory.Iterator(DataOrangTua.objects.all())
    TANGGAL_NO_IJAZAH = factory.Faker("date")
    NO_IJAZAH = factory.Faker("credit_card_number")
    TANGGAL_NO_SKHUN = factory.Faker("date")
    NO_SKHUN = factory.Faker("credit_card_number")
    RATA_RATA_NUN = factory.Faker("pyint", min_value=75, max_value=100)


class DataBeasiswaSiswaFactory(DjangoModelFactory):
    class Meta:
        model = DataBeasiswaSiswa
        django_get_or_create = ("BUKU_INDUK",)

    TAHUN = factory.Faker("year")
    KELAS = factory.Faker("random_element", elements=random_enum(ENUM_TINGKATAN))
    DARI = factory.Faker("company")
    BUKU_INDUK = factory.Iterator(BukuInduk.objects.all())


class MutasiMasukFactory(DjangoModelFactory):
    class Meta:
        model = MutasiMasuk
        # django_get_or_create=(
        #     'NAMA_SISWA'
        # )

    # NAMA_SISWA = factory.Iterator(DataSiswa.objects.all())
    NAMA_SISWA = factory.Faker("name")
    ASAL_SEKOLAH = factory.Faker("random_element", elements=random_enum(sekolah_masuk))
    NO_INDUK_ASAL = factory.Faker("credit_card_number")
    ALAMAT = factory.Faker("address")
    KELAS = factory.Faker("random_element", elements=random_enum(ENUM_TINGKATAN))
    NO_INDUK_BARU = factory.Faker("credit_card_number")
    TANGGAL_SURAT = factory.Faker("date")
    NO_SURAT = factory.Faker("credit_card_number")
    BULAN = factory.Faker("random_element", elements=random_enum(ENUM_BULAN))
    TAHUN = factory.Faker("pyint", min_value=2018, max_value=2022)


class MutasiKeluarFactory(DjangoModelFactory):
    class Meta:
        model = MutasiKeluar
        # django_get_or_create=(
        #     'NAMA_SISWA'
        # )

    NAMA_SISWA = factory.Faker("name")
    KELAS = factory.Faker("random_element", elements=random_enum(ENUM_TINGKATAN))
    NO_INDUK = factory.Faker("credit_card_number")
    PINDAH_KE = factory.Faker("random_element", elements=random_enum(sekolah_keluar))
    TANGGAL_SURAT = factory.Faker("date")
    NO_SURAT = factory.Faker("credit_card_number")
    BULAN = factory.Faker("random_element", elements=random_enum(ENUM_BULAN))
    TAHUN = factory.Faker("pyint", min_value=2018, max_value=2022)
