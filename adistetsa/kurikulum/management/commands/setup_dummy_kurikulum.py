from django.db import transaction
from django.core.management.base import BaseCommand

from kurikulum.models import *
from kurikulum.factories import *

from inspect import isclass

NUM_DATA = 10

class Command(BaseCommand):
    help = "Melakukan generate data dummy kurikulum"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Menghapus data lama...")
        models = [
            NilaiRaport
        ]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Membuat data baru...")

        # Membuat data
        for _ in range(NUM_DATA):
            NilaiRaportFactory()
