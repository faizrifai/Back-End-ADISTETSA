from django.db import transaction
from django.core.management.base import BaseCommand

from hubungan_masyarakat.models import *
from hubungan_masyarakat.factories import *

NUM_DATA = 10

class Command(BaseCommand):
    help = "Melakukan generate data dummy adiwiyata"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Menghapus data lama...")
        models = [
            BukuTamu, LogUKSSiswa, LogUKSTendik,
        ]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Membuat data baru...")

        # Membuat data
        for _ in range(NUM_DATA):
            BukuTamuFactory()
            LogUKSSiswaFactory()
            LogUKSTendikFactory()