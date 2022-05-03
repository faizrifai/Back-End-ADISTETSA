from django.db import transaction
from django.core.management.base import BaseCommand


from unit_penjamin_mutu.models import *
from unit_penjamin_mutu.factories import *

import random 

class Command(BaseCommand):
    help = "Melakukan generate data dummy Perpustakaan"
    
    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Menghapus data lama...")
        models = [
            PembagianTugasGuruBK, PembagianTugasGuruTIK, PembagianTugasPokokTambahanTendik, RincianTugasPokokTambahanTendik, TugasTambahanKepanitiaanTendik
        ]
        for m in models:
            m.objects.all().delete()
            
        self.stdout.write("Membuat data baru...")
        
        data_kelas = OfferingKelas.objects.all()
            
        for _ in range(10):
            n = random.randint(2, 4)
            sampel = random.choices(data_kelas, k=n)
            
            PembagianTugasBKFactory(data_kelas = sampel)
        
        for _ in range(10):
            n = random.randint(2, 4)
            sampel = random.choices(data_kelas, k=n)
            
            PembagianTugasTIKFactory(data_kelas = sampel)
        
        for _ in range(100):
            PembagianTugasPokokTambahanTendikFactory()
            
        for _ in range(100): 
            RincianTugasPokokTambahanTendikFactory()
            
        for _ in range(100):
            TugasTambahanKepanitiaanTendikFactory()
        
        
      