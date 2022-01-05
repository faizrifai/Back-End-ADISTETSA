from django.contrib.auth.models import User, Group
from django.urls import reverse
from rest_framework.test import APITestCase
from django.core.files.uploadedfile import SimpleUploadedFile

# Create your tests here.
class SetupData(APITestCase):
    def setUp(self):
        self.data_karyawan = {
            "NAMA_SEKOLAH": "Johnson, Houston and Perez",
            "NSS": 4520672340051299300,
            "NPSN": 4828311034040611,
            "ALAMAT_SEKOLAH": "1068 Williams Drive\nLisaburgh, MO 42852",
            "NAMA_LENGKAP": "Stephen Daugherty",
            "NIK": 4127223898104425,
            "JENIS_KELAMIN": "Laki-laki",
            "TEMPAT_LAHIR": "Lake Denise",
            "TANGGAL_LAHIR": "2011-05-25",
            "NAMA_IBU_KANDUNG": "David Hart",
            "ALAMAT_TEMPAT_TINGGAL": "48659 Whitney View\nNew Scott, OK 75270",
            "DUSUN": "New Ruthport",
            "KELURAHAN": "Lake Mistymouth",
            "KECAMATAN": "South Amyberg",
            "KOTA": "Browningside",
            "PROVINSI": "New Danielburgh",
            "LINTANG_1": "-52.270452",
            "LINTANG_2": "-19.7324905",
            "AGAMA": "Budha",
            "NPWP": 4707538934969475,
            "NAMA_WAJIB_PAJAK": "Jennifer Gross",
            "KEWARGANEGARAAN": "Mexico",
            "STATUS_KAWIN": "Kawin",
            "NAMA_PASANGAN": "Alan Simmons",
            "PEKERJAAN_PASANGAN": "Multimedia programmer",
            "PASANGAN_PNS": "Iya",
            "NIP_PASANGAN": 180073163740219,
            "STATUS_PEGAWAI": "Tidak Aktif",
            "PNS": "Tidak",
            "NIP": 2706913373216115,
            "NIY": 2714219439352278,
            "NIGB": 4118668413138665,
            "NUPTK": 4909434152003640000,
            "JENIS_PTK": "same",
            "SK_PENGANGKATAN": "180083959753524",
            "TMT_PENGANGKATAN": 36912513967954,
            "LEMBAGA_PENGANGKATAN": "Lozano Inc",
            "SK_CPNS": "2715021000898419",
            "TMT_CPNS": 3507270547637356,
            "TMT_PNS": 4938607349807,
            "PANGKAT": "['player', 'able', 'detail']",
            "SUMBER_GAJI": "Rollins, Ferrell and Walker",
            "KARTU_PEGAWAI": "4506049871559157895",
            "KARIS": "3550858342848008",
            "NO_SURAT": "213108731628172",
            "TGL_SURAT": "1991-10-12",
            "TMT_TUGAS": 180079010761936,
            "SEKOLAH_INDUK": "Field environment specific defense arm.",
            "LISENSI_KEPALA_SEKOLAH": "Serious brother whether yourself she phone.",
            "KODE_PROGRAM_KEAHLIAN": "4947113233334696",
            "JENIS_KETUNAAN": "['guy', 'close', 'plant']",
            "SPESIALIS_MENANGANI": "['quality', 'clear', 'red']",
            "STATUS_AKTIF": "Aktif",
            "NO_TELP": "(159)782-8296",
            "EMAIL": "russelljennifer@example.org"
        }

        self.data_kompetensi = {
            "BIDANG_STUDI": "Bahasa Indonesia",
            "URUTAN": "Pertama"
        }

        self.data_admin = {
            'username': 'admin',
            'password': 'merdeka123'
        }

        # create groups
        groups = ['Siswa', 'Guru', 'Orang Tua', 'Karyawan']
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

        # create data karyawan
        self.client.post(reverse('data_karyawan'), self.data_karyawan)

        # import data karyawan user to create user
        open_file = open('kustom_autentikasi/data/data_karyawan_user.csv', 'rb')
        uploaded_file = SimpleUploadedFile('data_karyawan_user.csv', open_file.read())
        data = {
            'file': uploaded_file
        }
        self.client.post(reverse('import_data_karyawan_user'), data, format='multipart')

        # login as karyawan
        self.data_karyawan_user = {
            'username': 'stephen_daugherty_2011',
            'password': 'merdeka123'
        }

        login_response = self.client.post(reverse('login'), self.data_karyawan_user)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + login_response.data['access'])

        super().setUp()

        def tearDown(self):
            super().tearDown()