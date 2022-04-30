from django.db import transaction
from django.core.management.base import BaseCommand

from adiwiyata.models import *
from adiwiyata.factories import *

NUM_DATA = 10

class Command(BaseCommand):
    help = "Melakukan generate data dummy adiwiyata"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Menghapus data lama...")
        models = [
            SanitasiDrainase, JaringanKerja, Publikasi, DaftarKader,
            KegiatanKader, Konservasi, PenanamanPohon, PembibitanPohon,
            PemeliharaanPohon, KaryaInovatif, PenerapanPRLH, ReuseReduceRecycle,
            PemeliharaanSampah, TabunganSampah
        ]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Membuat data baru...")

        # Membuat data
        for _ in range(NUM_DATA):
            SanitasiDrainaseFactory()
            JaringanKerjaFactory()
            PublikasiFactory()
            DaftarKaderFactory()
            KegiatanKaderFactory()
            KonservasiFactory()
            PenanamanPohonFactory()
            PembibitanPohonFactory()
            PemeliharaanPohonFactory()
            KaryaInovatifFactory()
            PenerapanPRLHFactory()
            ReuseReduceRecycleFactory()
            PemeliharaanSampahFactory()
            TabunganSampahFactory()