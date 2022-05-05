from django.db import transaction
from django.core.management.base import BaseCommand

from tata_usaha.models import *
from tata_usaha.factories import *

class Command(BaseCommand):
    help = "Melakukan generate data dummy tata usaha"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Menghapus data lama...")
        models = [
            BukuInduk, DataBeasiswaSiswa, MutasiKeluar, MutasiMasuk
        ]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Membuat data baru...")


        # Buku Induk, Mutasi Masuk, dan Mutasi Keluar
        for _ in range(60):
            BukuIndukFactory()
            MutasiKeluarFactory()
            MutasiMasukFactory()
        
        for _ in range(120):
            DataBeasiswaSiswaFactory()
        