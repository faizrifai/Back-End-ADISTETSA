from django.db import transaction
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand

from bimbingan_konseling.models import *
from bimbingan_konseling.factories import *

NUM_DATA = 10

class Command(BaseCommand):
    help = "Melakukan generate data dummy adiwiyata"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Menghapus data lama...")
        models = [
            DataAlumni, PeminatanLintasMinat, Konsultasi,
        ]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Membuat data baru...")

        # Membuat data peminatan lintas minat
        kelas_siswa = KelasSiswa.objects.all()
        total_data = len(kelas_siswa)
        if total_data > 10:
            total_data = 10

        file = ContentFile(b'Hello world!', name='angket.txt')

        for i in range(total_data):
            PeminatanLintasMinat.objects.create(
                KELAS_SISWA = kelas_siswa[i],
                KATEGORI='Angket Peminatan',
                FILE=file,
            )
            PeminatanLintasMinat.objects.create(
                KELAS_SISWA = kelas_siswa[i],
                KATEGORI='Angket Lintas Minat',
                FILE=file,
            )
            PeminatanLintasMinat.objects.create(
                KELAS_SISWA = kelas_siswa[i],
                KATEGORI='Angket Data Diri',
                FILE=file,
            )

        if len(KatalogKonselor.objects.all()) > 0:
            self.stdout.write("Membuat data baru...")
            for _ in range(NUM_DATA):
                DataAlumniFactory()
                KonsultasiFactory()
        else:
            self.stdout.write("Membuat data katalog konselor...")
            for _ in range(NUM_DATA):
                KatalogKonselor.objects.all().delete()
                KatalogKonselorFactory()