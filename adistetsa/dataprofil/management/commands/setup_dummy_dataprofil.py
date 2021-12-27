import random

from django.db import transaction
from django.core.management.base import BaseCommand

from dataprofil.models import DataSiswa
from dataprofil.factories import (
    DataSiswaFactory,
)

NUM_SISWA = 50

class Command(BaseCommand):
    help = "Melakukan generate data dummy"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Menghapus data lama...")
        models = [DataSiswa]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Membuat data baru...")

        # Membuat data siswa
        for _ in range(NUM_SISWA):
            data_siswa = DataSiswaFactory()