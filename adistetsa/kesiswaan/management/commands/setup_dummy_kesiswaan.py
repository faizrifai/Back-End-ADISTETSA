from django.db import transaction
from django.core.management.base import BaseCommand

from kesiswaan.models import *
from kesiswaan.factories import *

NUM_DATA = 10

class Command(BaseCommand):
    help = "Melakukan generate data dummy kesiswaan"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Menghapus data lama...")
        models = [
            PengajuanLaporanPelanggaran, PelanggaranSiswa, PoinProgramKebaikan,
            PengajuanProgramKebaikan, JadwalEkskul, PengajuanEkskul
        ]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Membuat data pre kesiswaan...")

        # Poin program kebaikan
        PoinProgramKebaikan.objects.create(KETERANGAN='Membuat kerajinan tangan', POIN=10)
        PoinProgramKebaikan.objects.create(KETERANGAN='Membuat artikel untuk mading sekolah', POIN=20)
        PoinProgramKebaikan.objects.create(KETERANGAN='Membantu guru membawa buku tugas siswa', POIN=30)
        PoinProgramKebaikan.objects.create(KETERANGAN='Membersihkan halaman sekolah', POIN=40)
        PoinProgramKebaikan.objects.create(KETERANGAN='Menjadi pemimpin upacara', POIN=50)

        # Katalog ekskul
        katalog_ekskul = [
            {'NAMA': 'Sepak Bola', 'KATEGORI': 'Pilihan', 'DESKRIPSI': 'Ini adalah ekskul sepak bola'},
            {'NAMA': 'Basket', 'KATEGORI': 'Pilihan', 'DESKRIPSI': 'Ini adalah ekskul basket'},
            {'NAMA': 'Bola Voli', 'KATEGORI': 'Pilihan', 'DESKRIPSI': 'Ini adalah ekskul bola voli'},
            {'NAMA': 'Band', 'KATEGORI': 'Mandiri', 'DESKRIPSI': 'Ini adalah ekskul band'},
            {'NAMA': 'Jurnalis', 'KATEGORI': 'Pilihan', 'DESKRIPSI': 'Ini adalah ekskul jurnalis'},
            {'NAMA': 'Paduan Suara', 'KATEGORI': 'Pilihan', 'DESKRIPSI': 'Ini adalah ekskul paduan suara'},
            {'NAMA': 'Robotik', 'KATEGORI': 'Mandiri', 'DESKRIPSI': 'Ini adalah ekskul robotik'},
        ]

        for data in katalog_ekskul:
            KatalogEkskul.objects.update_or_create(**data)

        self.stdout.write("Membuat data kesiswaan...")

        for _ in range(30):
            PengajuanLaporanPelanggaranFactory()
            PengajuanProgramKebaikanFactory()
            JadwalEkskulFactory()

        for _ in range(20):
            PengajuanEkskulFactory()