from django.db import transaction
from django.core.management.base import BaseCommand

from sarana_prasarana.models import *


class Command(BaseCommand):
    help = "Melakukan generate data dummy dependensi sarana prasarana"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Menghapus data lama...")
        models = [JenisSarana, JenisRuangan]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Membuat data baru...")

        # Kategori Sarana
        kategori_sarana = [
            "Alat Tulis Kerja",
            "Informasi Teknologi",
            "Inventaris Rumah Tangga",
        ]

        for jenis_sarana in kategori_sarana:
            JenisSarana.objects.create(KATEGORI=jenis_sarana)

        # Kategori Ruangan
        kategori_ruangan = ["Serbaguna", "Kelas", "Penunjang"]

        for jenis_ruangan in kategori_ruangan:
            JenisRuangan.objects.create(KATEGORI=jenis_ruangan)
