from django.db import transaction
from django.core.management.base import BaseCommand

from bimbingan_konseling.models import *
from bimbingan_konseling.factories import *

NUM_DATA = 10

class Command(BaseCommand):
    help = "Melakukan generate data dummy pre bimbingan konseling"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Menghapus data lama...")
        models = [
            KatalogKonselor
        ]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Membuat data katalog konselor...")

        for _ in range(NUM_DATA):
            KatalogKonselorFactory()