from django.contrib.auth.models import User, Group
from django.urls import reverse
from rest_framework.test import APITestCase
from django.core.files.uploadedfile import SimpleUploadedFile

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

        self.data_kompetensi = {
            "BIDANG_STUDI": "Bahasa Indonesia",
            "URUTAN": "Pertama"
        }

        self.data_anak = {
        'STATUS': "Hidup",
        'JENJANG': "SMA",
        'NISN': 12349876,
        'NAMA': "Leo",
        'JENIS_KELAMIN': "Laki-laki",
        'TEMPAT_LAHIR': "Bumi",
        'TANGGAL_LAHIR': "2000-01-11",
        'TAHUN_MASUK': "2000",     
        }

        self.data_beasiswa = {
        'JENIS': "sada",
        'PENYELANGGARA': "gdfg",
        'DARI_TAHUN': "gdgfd",
        'SAMPAI_TAHUN': "fdgfd",
        'MASIH_MENERIMA': "dfgfd",
        }

        self.data_buku = {
        'JUDUL_BUKU': "eqweq",
        'TAHUN_BUKU': "qweq",
        'PENERBIT_BUKU': "eqweqw",
        }

        self.data_diklat = {
        'JENIS_DIKLAT': "qweqw",
        'NAMA': "qweqw",
        'PENYELENGGARA': "qweqw",
        'TAHUN': "wqeqw",
        'PERAN': "wqeqwe",
        }

        self.data_karya_tulis = {
        'JUDUL': "wqeqwe",
        'TAHUN': "qweqwe",
        'PUBLIKASI': "qweqwe",
        'KETERANGAN': "dfvfd",
        }

        self.data_kesejahteraan = {
        'JENIS': "sdfdsf",
        'NAMA': "dsfdsf",
        'PENYELENGGARA': "sdfdsf",
        'DARI_TAHUN': "dsfdsf",
        'SAMPAI_TAHUN': "ghfhgf",
        'STATUS': "jhgjhg",
        }

        self.data_tunjangan = {
        'JENIS': "dfbdfb",
        'NAMA': "dfbfdb",
        'INSTANSI': "dfbfd",
        'SUMBER_DANA': "bdfbfdb",
        'DARI_TAHUN': "dfbfdbfd",
        'SAMPAI_TAHUN': "dfbfdbf",
        'NOMINAL': "dfbfdb",
        'STATUS': "ghgh",
        }

        self.data_tugas_tambahan = {
        'JABATAN_PTK': "dsfdsf",
        'JPM': "dsfds",
        'NO_SK': "sdfsdf",
        'TMT_TAMBAHAN': "ghfg",
        'TST_TAMBAHAN': "fghgfh",
        }

        self.data_penghargaan = {
        'TINGKAT_PENGHARGAAN': "hfghgf",
        'JENIS_PENGHARGAAN': "fdgfdg",
        'NAMA': "dfgfdg",
        'TAHUN': "dfgfdg",
        'INSTANSI': "dfgfdg",
        }

        self.data_nilai_tes = {
        'JENIS': "dfsdf",
        'NAMA': "dsfdsf",
        'PENYELENGGARA': "dsfdsfs",
        'TAHUN': "sdfsdfds",
        'SKOR': "sdfsdfsd",
        }

        self.data_riwayat_gaji_berkala = {
        'PANGKAT_GOLONGAN': "fdgfdg",
        'NO_SK': "fdgfdg",
        'TANGGAL_SK': "2000-02-20",
        'TMT_KGB': "dfgfdg",
        'TAHUN_MK': "fdsfs",
        'BULAN_MK': "dsfdsf",
        'GAJI_POKOK': "dsfsdf",
        }

        self.data_riwayat_jabatan_struktural = {
        'JABATAN_PTK': "fsdfds",
        'SK_STRUKTURAL': "sdfdsf",
        'TMT_JABATAN': "sdfdsf",
        }

        self.data_riwayat_kepangkatan = {
        'PANGKAT_GOLONGAN': "dsfsdf",
        'NO_SK': "dsfdsf",
        'TANGGAL_SK': "2000-02-20",
        'PANGKAT_GOLONGAN': "dvdf",
        'MK_TAHUN': "nbv",
        'MK_BULAN': "rdfvc",
        }

        self.data_riwayat_pendidikan_formal = {
        'BIDANG_STUDI': "fsdfs",
        'JENJANG': "dsfsdfs",
        'GELAR': "dsfsdf",
        'SATUAN': "sdfdsfds",
        'FAKULTAS': "dsfds",
        'KEPENDIDIKAN': "dsfds",
        'KEPENDUDUKAN': "dsfds",
        'TAHUN_MASUK': "sdfsdf",
        'TAHUN_LULUS': "dsfsd",
        'NIM': "dsfds",
        'MASIH': "dsfsd",
        'SMT': "sdfs",
        'IPK': "sdfds",
        }

        self.data_riwayat_sertifikasi = {
        'JENIS_SERTIFIKASI': "fsdfds",
        'NO_SERTIFIKASI': "sdfdsfs",
        'TAHUN_SERTIFIKASI': "sdfdsf",
        'BIDANG_STUDI': "dsfdsf",
        'NO_REGISTRASI': "sdfdsf",
        'NO_PESERTA': "sdfdsf",
        }

        self.data_riwayat_jabatan_fungsional = {
        'JABATAN_FUNGSIONAL': "sdfdsf",
        'SK_JABATAN_FUNGSIONAL': "sdfds",
        'TMT_JABATAN': "dsfdsf",
        }

        self.data_riwayat_karir = {
        'JENJANG': "sdfdsf",
        'JENIS_LEMBAGA': "sdfds",
        'STS_KEPEGAWAIAN': "dsfdsf",
        'JENIS_PTK': "fsdfsd",
        'LEMBAGA': "dsfdsf",
        'NO_SK_KERJA': "fsdfds",
        'TGL_SK_KERJA': "2000-02-20",
        'TMT_KERJA': "dfsdsf",
        'TST_KERJA': "dsfdsf",
        'TEMPAT_KERJA': "sdfdsf",
        'TTD_SK_KERJA': "dsfdsf",
        'MAPEL_DIAJARKAN': "dsfsdf",
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

        # create data guru
        self.client.post(reverse('data_guru'), self.data_guru)

        # import data guru user to create user
        open_file = open('kustom_autentikasi/data/data_guru_user.csv', 'rb')
        uploaded_file = SimpleUploadedFile('data_guru_user.csv', open_file.read())
        data = {
            'file': uploaded_file
        }
        self.client.post(reverse('import_data_guru_user'), data, format='multipart')

        # login as guru
        self.data_guru_user = {
            'username': '4341623682038467',
            'password': 'merdeka123'
        }

        login_response = self.client.post(reverse('login'), self.data_guru_user)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + login_response.data['access'])

        super().setUp()

        def tearDown(self):
            super().tearDown()