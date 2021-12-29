import random

from django.db import transaction
from django.core.management.base import BaseCommand

from dataprofil.models import *
from dataprofil.factories import (
    DataSiswaFactory,
    DataOrangTuaFactory,
    DataGuruFactory,
    DataKaryawanFactory,
)

NUM_SISWA = 50
NUM_ORANG_TUA = 50
NUM_GURU = 50
NUM_KARYAWAN = 50

class Command(BaseCommand):
    help = "Melakukan generate data dummy"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Menghapus data lama...")
        models = [DataSiswa, DataOrangTua, DataGuru, DataKaryawan]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Membuat data baru...")

        # Membuat data siswa
        for _ in range(NUM_SISWA):
            data_siswa = DataSiswaFactory()
            
        # Membuat data orang tua
        for _ in range(NUM_ORANG_TUA):
            data_orang_tua = DataOrangTuaFactory()
            
        for _ in range(NUM_GURU):
            data_guru = DataGuruFactory()
            
        for _ in range(NUM_KARYAWAN):
            data_karyawan = DataKaryawanFactory()