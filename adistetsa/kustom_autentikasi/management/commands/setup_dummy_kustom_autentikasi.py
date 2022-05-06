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
            User, DataSiswaUser, DataGuruUser, DataOrangTuaUser,
            DataKaryawanUser, DataPelatihUser
        ]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Membuat data baru...")

        data_siswa = DataSiswa.objects.all()
        data_guru = DataGuru.objects.all()
        data_karyawan = DataKaryawan.objects.all()
        data_orang_tua = DataOrangTua.objects.all()
        data_pelatih = DataPelatih.objects.all()
        
        staf = [
            'Staf Adiwiyata', 'Staf BK', 'Staf PPDB', 'Staf Humas',
            'Staf Kesiswaan', 'Staf Keuangan', 'Staf Kurikulum', 'Staf Perpustakaan',
            'Staf Sarpras', 'Staf TU', 'Staf UPM'
        ]

        for i in range(len(data_siswa)):
            # Data Siswa User
            siswa = data_siswa[i]

            username = str(siswa.NIS)
            password = 'merdeka123'

            try:
                user = User.objects.get(username=username)
                user.delete()
            except:
                pass
        
            new_user = User.objects.create_user(username, siswa.EMAIL, password)

            grup_siswa = Group.objects.get(name='Siswa')
            grup_siswa.user_set.add(new_user)

            DataSiswaUser.objects.create(USER=new_user, DATA_SISWA=siswa)

        for i in range(len(data_guru)):
            # Data Guru User
            guru = data_guru[i]

            username = (guru.NAMA_LENGKAP + '_' + str(guru.TANGGAL_LAHIR.year)).lower().replace(' ', '_')
            password = 'merdeka123'

            new_user = User.objects.create_user(username, guru.EMAIL, password)

            grup_guru = Group.objects.get(name='Guru')
            grup_guru.user_set.add(new_user)

            pilih_staf = random.choices(staf, k=2)
            for data in pilih_staf:
                grup = Group.objects.get(name=data)
                grup.user_set.add(new_user)

            DataGuruUser.objects.create(USER=new_user, DATA_GURU=guru)

        for i in range(len(data_karyawan)):
            # Data Karyawan User
            karyawan = data_karyawan[i]

            username = (karyawan.NAMA_LENGKAP + '_' + str(karyawan.TANGGAL_LAHIR.year)).lower().replace(' ', '_')
            password = 'merdeka123'

            new_user = User.objects.create_user(username, karyawan.EMAIL, password)

            grup_karyawan = Group.objects.get(name='Karyawan')
            grup_karyawan.user_set.add(new_user)

            pilih_staf = random.choices(staf, k=2)
            for data in pilih_staf:
                grup = Group.objects.get(name=data)
                grup.user_set.add(new_user)

            DataKaryawanUser.objects.create(USER=new_user, DATA_KARYAWAN=karyawan)

        for i in range(len(data_orang_tua)):
            # Data Orang Tua User
            orang_tua = data_orang_tua[i]

            username = (orang_tua.NAMA_AYAH + '_' + str(orang_tua.TAHUN_LAHIR_AYAH.year)).lower().replace(' ', '_')
            password = 'merdeka123'

            new_user = User.objects.create_user(username=username, password=password)

            grup_orang_tua = Group.objects.get(name='Orang Tua')
            grup_orang_tua.user_set.add(new_user)

            DataOrangTuaUser.objects.create(USER=new_user, DATA_ORANG_TUA=orang_tua)

        for i in range(len(data_pelatih)):
            # Data Pelatih User
            pelatih = data_pelatih[i]

            username = (pelatih.NAMA).lower().replace(' ', '_')
            password = 'merdeka123'

            new_user = User.objects.create_user(username=username, password=password)

            grup_pelatih = Group.objects.get(name='Pelatih')
            grup_pelatih.user_set.add(new_user)

            DataPelatihUser.objects.create(USER=new_user, DATA_PELATIH=pelatih)