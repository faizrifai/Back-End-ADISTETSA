from django.db import transaction
from django.core.management.base import BaseCommand

from perpustakaan.models import *
from perpustakaan.factories import *

import random


class Command(BaseCommand):
    help = "Melakukan generate data dummy Perpustakaan"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Menghapus data lama...")
        models = [PengajuanPeminjamanSiswa, PengajuanPeminjamanGuru]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Membuat data baru...")
        buku = KatalogBukuCopy.objects.all()

        for _ in range(100):
            n = random.randint(2, 4)
            sampel = random.choices(buku, k=n)

            PengajuanSiswaFactory(buku=sampel)

        for _ in range(100):
            n = random.randint(2, 4)
            sampel = random.choices(buku, k=n)

            PengajuanGuruFactory(buku=sampel)
