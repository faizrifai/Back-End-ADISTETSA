from django.db import transaction
from django.core.management.base import BaseCommand

from kurikulum.models import *
from kurikulum.factories import *
from kesiswaan.models import KatalogEkskul

class Command(BaseCommand):
    help = "Melakukan generate data dummy dependensi kurikulum"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Menghapus data lama...")
        models = [
            DataSemester, TahunAjaran, MataPelajaran,
            Jurusan, NamaOfferingKelas, WaktuPelajaran,
            KatalogEkskul
        ]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Membuat data baru...")

        # Tahun Ajaran
        for i in range(5):
            TahunAjaran.objects.create(TAHUN_AJARAN_AWAL=2018+i, TAHUN_AJARAN_AKHIR=2019+i)

        # Semester
        DataSemester.objects.create(KE='I')
        DataSemester.objects.create(KE='II')

        # Mata Pelajaran
        mata_pelajaran = [
            {'KODE': 'BI', 'NAMA': 'Bahasa Indonesia'},
            {'KODE': 'BING', 'NAMA': 'Bahasa Inggris'},
            {'KODE': 'MTK', 'NAMA': 'Matematika'},
            {'KODE': 'BIO', 'NAMA': 'Biologi'},
            {'KODE': 'KIM', 'NAMA': 'Kimia'},
            {'KODE': 'FIS', 'NAMA': 'Fisika'},
            {'KODE': 'GEO', 'NAMA': 'Geografi'}
        ]

        for data in mata_pelajaran:
            MataPelajaran.objects.create(**data)

        # Jurusan
        Jurusan.objects.create(NAMA='MIPA')
        Jurusan.objects.create(NAMA='IPS')
        Jurusan.objects.create(NAMA='BAHASA')

        # Nama Offering Kelas
        NamaOfferingKelas.objects.create(NAMA='A')
        NamaOfferingKelas.objects.create(NAMA='B')
        NamaOfferingKelas.objects.create(NAMA='C')
        NamaOfferingKelas.objects.create(NAMA='D')
        NamaOfferingKelas.objects.create(NAMA='E')
        NamaOfferingKelas.objects.create(NAMA='F')

        # Waktu Pelajaran
        waktu_pelajaran = [
            {'WAKTU_MULAI': '07:00', 'WAKTU_BERAKHIR': '08:00', 'JAM_KE': 1},
            {'WAKTU_MULAI': '08:15', 'WAKTU_BERAKHIR': '09:15', 'JAM_KE': 2},
            {'WAKTU_MULAI': '09:30', 'WAKTU_BERAKHIR': '10:30', 'JAM_KE': 3},
            {'WAKTU_MULAI': '11:00', 'WAKTU_BERAKHIR': '12:00', 'JAM_KE': 4},
            {'WAKTU_MULAI': '12:15', 'WAKTU_BERAKHIR': '13:15', 'JAM_KE': 5},
            {'WAKTU_MULAI': '13:45', 'WAKTU_BERAKHIR': '14:45', 'JAM_KE': 6}
        ]

        for data in waktu_pelajaran:
            WaktuPelajaran.objects.create(**data)

        # Ekskul Pramuka
        KatalogEkskul.objects.create(NAMA='PRAMUKA', KATEGORI='Wajib', DESKRIPSI='Ekskul wajib untuk semua siswa')
