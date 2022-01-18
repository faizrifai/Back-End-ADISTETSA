from django.contrib.auth.models import User, Group
from django.urls import reverse
from rest_framework.test import APITestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import *

from kustom_autentikasi.models import DataGuruUser

# Create your tests here.
class SetupData(APITestCase):
    def setUp(self):
        self.data_guru = {
            "NAMA_SEKOLAH": "Diaz, Hartman and Brooks",
            "NSS": 4999043407735781,
            "NPSN": 30415103387183,
            "ALAMAT_SEKOLAH": "32915 Michael Parkway Suite 113\nKennedyland, UT 01855",
            "NAMA_LENGKAP": "Ashley Garner",
            "NIK": 4316986353796738000,
            "JENIS_KELAMIN": "Laki-laki",
            "TEMPAT_LAHIR": "South Tina",
            "TANGGAL_LAHIR": "2020-12-18",
            "NAMA_IBU_KANDUNG": "Lisa Dunn",
            "ALAMAT_TEMPAT_TINGGAL": "55469 Robert Underpass\nJohnsonchester, NC 67442",
            "DUSUN": "Gregoryburgh",
            "KELURAHAN": "Smithborough",
            "KECAMATAN": "South Derek",
            "KOTA": "Malloryton",
            "PROVINSI": "Foleyborough",
            "LINTANG_1": "-58.0314815",
            "LINTANG_2": "-36.292985",
            "AGAMA": "Kristen",
            "NPWP": 4687559902746400,
            "NAMA_WAJIB_PAJAK": "Bryan Smith",
            "KEWARGANEGARAAN": "Mayotte",
            "STATUS_KAWIN": "Belum Kawin",
            "NAMA_PASANGAN": "Donna Lester",
            "PEKERJAAN_PASANGAN": "Brewing technologist",
            "PASANGAN_PNS": "Iya",
            "NIP_PASANGAN": 30113013759084,
            "STATUS_PEGAWAI": "Tidak Aktif",
            "PNS": "Tidak",
            "NIP": 4341623682038467,
            "NIY": 6011628058059454,
            "NIGB": 3532106108466521,
            "NUPTK": 4323139083424071000,
            "JENIS_PTK": "especially",
            "SK_PENGANGKATAN": "639071865054",
            "TMT_PENGANGKATAN": 180064012150155,
            "LEMBAGA_PENGANGKATAN": "Wilson, Pierce and Nichols",
            "SK_CPNS": "3520431256630650",
            "TMT_CPNS": 30484259967529,
            "TMT_PNS": 4151267166565837000,
            "PANGKAT": "['past', 'wife', 'capital']",
            "SUMBER_GAJI": "Smith LLC",
            "KARTU_PEGAWAI": "3501920063629643",
            "KARIS": "3584189563389112",
            "NO_SURAT": "348450601341900",
            "TGL_SURAT": "1980-09-29",
            "TMT_TUGAS": 180008251765058,
            "SEKOLAH_INDUK": "Letter second put yourself.",
            "LISENSI_KEPALA_SEKOLAH": "Civil parent computer offer top building.",
            "KODE_PROGRAM_KEAHLIAN": "4912005989642952",
            "JENIS_KETUNAAN": "['real', 'tax', 'art']",
            "SPESIALIS_MENANGANI": "['choose', 'brother', 'information']",
            "STATUS_AKTIF": "Tidak Aktif",
            "NO_TELP": "747.439.9197x7818",
            "EMAIL": "qshort@example.com",
        }

        self.data_admin = {
            'username': 'admin',
            'password': 'merdeka123'
        }

        # create groups
        groups = ['Siswa', 'Guru', 'Orang Tua', 'Karyawan', 'Staf Kurikulum']
        for group in groups:
            object = Group.objects.create(name=group)
            object.save()

        # create superuser
        user = User.objects.create_user(username='admin', password='merdeka123')
        user.is_superuser = True
        user.save()

        # login as superuser
        login_response = self.client.post(reverse('login'), self.data_admin)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + login_response.data['access'])

        # create data guru
        self.client.post(reverse('data_guru'), self.data_guru)

        # import data guru user to create user
        open_file = open('kurikulum/data/data_guru_user.csv', 'rb')
        uploaded_file = SimpleUploadedFile('data_guru_user.csv', open_file.read())
        data = {
            'file': uploaded_file
        }
        self.client.post(reverse('import_data_guru_user'), data, format='multipart')

        # login sebagai staf kurikulum
        self.data_staf_kurikulum = {
            'username': '4341623682038467',
            'password': 'merdeka123'
        }

        # jadikan sebagai staf kurikulum
        data_guru_user = DataGuruUser.objects.get(DATA_GURU__NIP = self.data_staf_kurikulum['username'])
        my_group = Group.objects.get(name='Staf Kurikulum')
        my_group.user_set.add(data_guru_user.USER)

        # setup filter
        TahunAjaran.objects.create(TAHUN_AJARAN_AWAL='2020', TAHUN_AJARAN_AKHIR='2021')
        DataSemester.objects.create(KE='I', NAMA='Semester 1')
        MataPelajaran.objects.create(KODE='BI', NAMA='Bahasa Indonesia')
        Jurusan.objects.create(NAMA='IPA')
        Kelas.objects.create(TAHUN_AJARAN__in=1, TINGKATAN='X', JURUSAN=1)
        NamaOfferingKelas.objects.create(NAMA='A')
        OfferingKelas.objects.create(KELAS=1, OFFERING=1)
        KategoriTataTertib.objects.create(NAMA='Pakaian')

        login_response = self.client.post(reverse('login'), self.data_staf_kurikulum)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + login_response.data['access'])

        super().setUp()

        def tearDown(self):
            super().tearDown()