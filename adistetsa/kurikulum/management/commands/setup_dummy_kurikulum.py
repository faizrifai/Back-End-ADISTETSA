from django.db import transaction
from django.core.management.base import BaseCommand

from kurikulum.models import *
from kurikulum.factories import *

import random


class Command(BaseCommand):
    help = "Melakukan generate data dummy kurikulum"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Menghapus data lama...")
        models = [Kelas, OfferingKelas, KelasSiswa, JadwalMengajar, NilaiRaport]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Membuat data baru...")

        # Kelas
        for _ in range(20):
            KelasFactory()

        # Offering Kelas
        for _ in range(20):
            OfferingKelasFactory()

        # Kelas Siswa
        for _ in range(100):
            KelasSiswaFactory()

        waktu_pelajaran = WaktuPelajaran.objects.all()

        # Jadwal Mengajar
        for _ in range(100):
            n = random.randint(2, 4)
            sampel = random.choices(waktu_pelajaran, k=n)

            JadwalMengajarFactory(waktu_pelajaran=sampel)
