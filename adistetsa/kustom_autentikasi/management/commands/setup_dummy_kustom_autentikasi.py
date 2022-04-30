from django.db import transaction
from django.core.management.base import BaseCommand

from kustom_autentikasi.models import *

import random

total_user = 20

class Command(BaseCommand):
    help = "Melakukan generate data dummy kustom_autentikasi"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Menghapus data lama...")
        models = [
            DataSiswaUser, DataGuruUser, DataOrangTuaUser,
            DataKaryawanUser, DataPelatihUser
        ]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Membuat data baru...")

        data_siswa = DataSiswa.objects.all()
        data_guru = DataGuru.objects.all()
        data_karyawan = DataKaryawan.objects.all()
        data_orang_tua = DataOrangTua.objects.all()
        
        staf = [
            'Staf Adiwiyata', 'Staf BK', 'Staf PPDB', 'Staf Humas',
            'Staf Kesiswaan', 'Staf Keuangan', 'Staf Kurikulum', 'Staf Perpustakaan',
            'Staf Sarpras', 'Staf TU', 'Staf UPM'
        ]

        for i in range(total_user):
            # Data Siswa User
            siswa = data_siswa[i]

            username = str(siswa.NIS)
            password = 'merdeka123'

            try:
                user = User.objects.get(username=username)
                user.delete()
            except:
                pass
        
            new_user = User.objects.get_or_create(username=username, password=password, email=siswa.EMAIL)

            grup_siswa = Group.objects.get(name='Siswa')
            grup_siswa.user_set.add(new_user[0])

            DataSiswaUser.objects.create(USER=new_user[0], DATA_SISWA=siswa)

            # Data Guru User
            guru = data_guru[i]

            username = (guru.NAMA_LENGKAP + '_' + str(guru.TANGGAL_LAHIR.year)).lower().replace(' ', '_')
            password = 'merdeka123'

            try:
                user = User.objects.get(username=username)
                user.delete()
            except:
                pass
        
            new_user = User.objects.get_or_create(username=username, password=password, email=guru.EMAIL)

            grup_guru = Group.objects.get(name='Guru')
            grup_guru.user_set.add(new_user[0])

            pilih_staf = random.choices(staf, k=2)
            for data in pilih_staf:
                grup = Group.objects.get(name=data)
                grup.user_set.add(new_user[0])

            DataGuruUser.objects.create(USER=new_user[0], DATA_GURU=guru)

            # Data Karyawan User
            karyawan = data_karyawan[i]

            username = (karyawan.NAMA_LENGKAP + '_' + str(karyawan.TANGGAL_LAHIR.year)).lower().replace(' ', '_')
            password = 'merdeka123'

            try:
                user = User.objects.get(username=username)
                user.delete()
            except:
                pass
        
            new_user = User.objects.get_or_create(username=username, password=password, email=karyawan.EMAIL)

            grup_karyawan = Group.objects.get(name='Karyawan')
            grup_karyawan.user_set.add(new_user[0])

            pilih_staf = random.choices(staf, k=2)
            for data in pilih_staf:
                grup = Group.objects.get(name=data)
                grup.user_set.add(new_user[0])

            DataKaryawanUser.objects.create(USER=new_user[0], DATA_KARYAWAN=karyawan)

            # Data Orang Tua User
            orang_tua = data_orang_tua[i]

            username = (orang_tua.NAMA_AYAH + '_' + str(orang_tua.TAHUN_LAHIR_AYAH.year)).lower().replace(' ', '_')
            password = 'merdeka123'

            try:
                user = User.objects.get(username=username)
                user.delete()
            except:
                pass
        
            new_user = User.objects.get_or_create(username=username, password=password)

            grup_orang_tua = Group.objects.get(name='Orang Tua')
            grup_orang_tua.user_set.add(new_user[0])

            DataOrangTuaUser.objects.create(USER=new_user[0], DATA_ORANG_TUA=orang_tua)