from django.db import transaction
from django.core.management.base import BaseCommand

from kurikulum.models import *
from kurikulum.factories import *
from sarana_prasarana.models import *
from sarana_prasarana.factories import (
    PengajuanPeminjamanBarangFactory,
    PengajuanPeminjamanRuanganFactory,
)

import random


class Command(BaseCommand):
    help = "Melakukan generate data dummy sarana prasarana"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Menghapus data lama...")
        models = [
            Sarana,
            Ruangan,
            PengajuanPeminjamanRuangan,
            PengajuanPeminjamanBarang,
        ]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Membuat data baru...")

        # Sarana
        sarana = [
            {
                "NAMA": "LCD Proyektor",
                "JENIS": JenisSarana.objects.get(KATEGORI="Informasi Teknologi"),
                "STATUS": "Sudah Dikembalikan",
            },
            {
                "NAMA": "Sapu",
                "JENIS": JenisSarana.objects.get(KATEGORI="Inventaris Rumah Tangga"),
                "STATUS": "Sudah Dikembalikan",
            },
            {
                "NAMA": "Kabel HDMI",
                "JENIS": JenisSarana.objects.get(KATEGORI="Informasi Teknologi"),
                "STATUS": "Sudah Dikembalikan",
            },
            {
                "NAMA": "Spidol",
                "JENIS": JenisSarana.objects.get(KATEGORI="Alat Tulis Kerja"),
                "STATUS": "Sudah Dikembalikan",
            },
            {
                "NAMA": "Penghapus",
                "JENIS": JenisSarana.objects.get(KATEGORI="Informasi Teknologi"),
                "STATUS": "Sudah Dikembalikan",
            },
            {
                "NAMA": "Bolpoin",
                "JENIS": JenisSarana.objects.get(KATEGORI="Informasi Teknologi"),
                "STATUS": "Sudah Dikembalikan",
            },
            {
                "NAMA": "Kemoceng",
                "JENIS": JenisSarana.objects.get(KATEGORI="Inventaris Rumah Tangga"),
                "STATUS": "Sudah Dikembalikan",
            },
            {
                "NAMA": "Cikrak",
                "JENIS": JenisSarana.objects.get(KATEGORI="Inventaris Rumah Tangga"),
                "STATUS": "Sudah Dikembalikan",
            },
            {
                "NAMA": "Komputer",
                "JENIS": JenisSarana.objects.get(KATEGORI="Informasi Teknologi"),
                "STATUS": "Sudah Dikembalikan",
            },
            {
                "NAMA": "Flashdisk",
                "JENIS": JenisSarana.objects.get(KATEGORI="Informasi Teknologi"),
                "STATUS": "Sudah Dikembalikan",
            },
        ]

        for data_sarana in sarana:
            Sarana.objects.create(**data_sarana)

        # Ruangan
        ruangan = [
            {
                "NAMA": "A1",
                "JENIS": JenisRuangan.objects.get(KATEGORI="Kelas"),
                "STATUS": "Sudah Dikembalikan",
            },
            {
                "NAMA": "A2",
                "JENIS": JenisRuangan.objects.get(KATEGORI="Kelas"),
                "STATUS": "Sudah Dikembalikan",
            },
            {
                "NAMA": "A3",
                "JENIS": JenisRuangan.objects.get(KATEGORI="Kelas"),
                "STATUS": "Sudah Dikembalikan",
            },
            {
                "NAMA": "A4",
                "JENIS": JenisRuangan.objects.get(KATEGORI="Kelas"),
                "STATUS": "Sudah Dikembalikan",
            },
            {
                "NAMA": "A5",
                "JENIS": JenisRuangan.objects.get(KATEGORI="Kelas"),
                "STATUS": "Sudah Dikembalikan",
            },
            {
                "NAMA": "Aula",
                "JENIS": JenisRuangan.objects.get(KATEGORI="Serbaguna"),
                "STATUS": "Sudah Dikembalikan",
            },
            {
                "NAMA": "Lapangan",
                "JENIS": JenisRuangan.objects.get(KATEGORI="Serbaguna"),
                "STATUS": "Sudah Dikembalikan",
            },
            {
                "NAMA": "Laboratorium Fisika",
                "JENIS": JenisRuangan.objects.get(KATEGORI="Penunjang"),
                "STATUS": "Sudah Dikembalikan",
            },
            {
                "NAMA": "Laboratorium Kimia",
                "JENIS": JenisRuangan.objects.get(KATEGORI="Penunjang"),
                "STATUS": "Sudah Dikembalikan",
            },
            {
                "NAMA": "Laboratorium Komputer",
                "JENIS": JenisRuangan.objects.get(KATEGORI="Penunjang"),
                "STATUS": "Sudah Dikembalikan",
            },
        ]

        for data_ruangan in ruangan:
            Ruangan.objects.create(**data_ruangan)

        for _ in range(10):
            PengajuanPeminjamanRuanganFactory()

        barang = Sarana.objects.all()

        for _ in range(20):
            n = random.randint(2, 4)
            sampel = random.choices(barang, k=n)

            PengajuanPeminjamanBarangFactory(alat=sampel)
