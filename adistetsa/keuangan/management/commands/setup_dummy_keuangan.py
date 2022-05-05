from django.db import transaction
from django.core.management.base import BaseCommand

from keuangan.models import *
from keuangan.factories import *

import random

class Command(BaseCommand):
    help = "Melakukan generate data dummy Keuangan, pastikan def save di komen sementara lur wkwkwk"
    
    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Menghapus data lama...")
        models = [
            Pembayaran,
        ]
        for m in models:
            m.objects.all().delete()
            
        self.stdout.write("Membuat data baru...")
        
        for _ in range(100):
            PembayaranFactory()