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

        self.data_anak = {
        'STATUS': "Aktif",
        'JENJANG': "SMA",
        'NISN': "2123165464",
        'NAMA': "Afdhal",
        'JENIS_KELAMIN': "Perempuan",
        'TEMPAT_LAHIR': "Malang",
        'TANGGAL_LAHIR': "2000-11-30",
        'TAHUN_MASUK': "2020", 
        }

        self.data_beasiswa = {
        'JENIS': "Aktif",
        'PENYELANGGARA': "SMA",
        'DARI_TAHUN': "2123165464",
        'SAMPAI_TAHUN': "Afdhal",
        'MASIH_MENERIMA': "Perempuan",
        }

        self.data_buku = {
        'JUDUL_BUKU': "Aktif",
        'TAHUN_BUKU': "2021",
        'PENERBIT_BUKU': "Afdhal",
        }

        self.data_diklat = {
        'JENIS_DIKLAT': "gatau",
        'NAMA': "Afdhal",
        'PENYELENGGARA': "Tau",
        'TAHUN': "2022",
        'PERAN': "Aktor",
        }

        self.data_karya_tulis = {
        'JUDUL': "Aktif",
        'TAHUN': "Afdhal",
        'PUBLIKASI': "Tau",
        'KETERANGAN': "2021",
        }

        self.data_kesejahteraan = {
        'JENIS': "Aktif",
        'NAMA': "Afdhal",
        'PENYELENGGARA': "Tau",
        'DARI_TAHUN': "2021",
        'SAMPAI_TAHUN': "2022",
        'STATUS': "Aktif",
        }

        self.data_tunjangan = {
        'JENIS': "Aktif",
        'NAMA': "Afdhal",
        'INSTANSI': "UM",
        'SUMBER_DANA': "UM",
        'DARI_TAHUN': "2022",
        'SAMPAI_TAHUN': "20223",
        'NOMINAL': "2022",
        'STATUS': "Aktif",
        }

        self.data_tugas_tambahan = {
        'JABATAN_PTK': "Dosen",
        'JPM': "Afdhal",
        'NO_SK': "132",
        'TMT_TAMBAHAN': "1233",
        'TST_TAMBAHAN': "2022",
        }

        self.data_penghargaan = {
        'TINGKAT_PENGHARGAAN': "Dosen",
        'JENIS_PENGHARGAAN': "Gatau",
        'NAMA': "Afdhal",
        'TAHUN': "1233",
        'INSTANSI': "um",
        }

        self.data_nilai_tes = {
        'JENIS': "Dosen",
        'NAMA': "Gatau",
        'PENYELENGGARA': "Afdhal",
        'TAHUN': "1233",
        'SKOR': "99",
        }

        self.data_riwayat_gaji_berkala = {
        'PANGKAT_GOLONGAN': "Dosen",
        'NO_SK': "Gatau",
        'TANGGAL_SK': "2020-07-18",
        'TMT_KGB': "1233",
        'TAHUN_MK': "2020",
        'BULAN_MK': "Juli",
        'GAJI_POKOK': "99",
        }

        self.data_riwayat_jabatan_struktural = {
        'JABATAN_PTK': "Dosen",
        'SK_STRUKTURAL': "Gatau",
        'TMT_JABATAN': "gg",
        }

        self.data_riwayat_kepangkatan = {
        'PANGKAT_GOLONGAN': "Mhs",
        'NO_SK': "231654651",
        'TANGGAL_SK': "2020-10-10",
        'PANGKAT_GOLONGAN': "Dosen",
        'MK_TAHUN': "2022",
        'MK_BULAN': "Juli",
        }

        self.data_karyawan_riwayat_pendidikan_formal = {
        'BIDANG_STUDI': "MTK",
        'JENJANG': "231654651",
        'GELAR': "S10",
        'SATUAN': "Dosen",
        'FAKULTAS': "ft",
        'KEPENDIDIKAN': "ya",
        'KEPENDUDUKAN': "mlg",
        'TAHUN_MASUK': "2020",
        'TAHUN_LULUS': "2021",
        'NIM': "123561651",
        'MASIH': "ya",
        'SMT': "15",        
        'IP': "4",
        }

        self.data_riwayat_sertifikasi = {
        'JENIS_SERTIFIKASI': "Mhs",
        'NO_SERTIFIKASI': "231654651",
        'TAHUN_SERTIFIKASI': "2020-10-10",
        'BIDANG_STUDI': "Dosen",
        'NO_REGISTRASI': "2022",
        'NO_PESERTA': "12132123",
        }

        self.data_riwayat_jabatan_fungsional = {
        'JABATAN_FUNGSIONAL': "Mhs",
        'SK_JABATAN_FUNGSIONAL': "231654651",
        'TMT_JABATAN': "sadsadsadsad",
        }

        self.data_riwayat_karir = {
        'JENJANG': "asdadsaddsa",
        'JENIS_LEMBAGA': "asdadsaddsa",
        'STS_KEPEGAWAIAN': "asdadsaddsa",
        'JENIS_PTK': "asdadsaddsa",
        'LEMBAGA': "asdadsaddsa",
        'NO_SK_KERJA': "12312313",
        'TGL_SK_KERJA': "2020-12-12",
        'TMT_KERJA': "sadsadsa",
        'TST_KERJA': "asdadsaddsa",
        'TEMPAT_KERJA': "asdadsaddsa",
        'TTD_SK_KERJA': "asdadsaddsa",
        'MAPEL_DIAJARKAN': "ya",
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