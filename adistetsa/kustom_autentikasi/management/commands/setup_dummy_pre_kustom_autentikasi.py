from django.db import transaction
from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group


class Command(BaseCommand):
    help = "Melakukan generate data dummy pre kustom autentikasi"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Membuat data baru...")

        # Membuat Grup
        Group.objects.update_or_create(name="Siswa")
        Group.objects.update_or_create(name="Guru")
        Group.objects.update_or_create(name="Orang Tua")
        Group.objects.update_or_create(name="Karyawan")
        Group.objects.update_or_create(name="Pelatih")
        Group.objects.update_or_create(name="Staf Adiwiyata")
        Group.objects.update_or_create(name="Staf BK")
        Group.objects.update_or_create(name="Staf PPDB")
        Group.objects.update_or_create(name="Staf Humas")
        Group.objects.update_or_create(name="Staf Kesiswaan")
        Group.objects.update_or_create(name="Staf Keuangan")
        Group.objects.update_or_create(name="Staf Kurikulum")
        Group.objects.update_or_create(name="Staf Perpustakaan")
        Group.objects.update_or_create(name="Staf Sarpras")
        Group.objects.update_or_create(name="Staf TU")
        Group.objects.update_or_create(name="Staf UPM")
