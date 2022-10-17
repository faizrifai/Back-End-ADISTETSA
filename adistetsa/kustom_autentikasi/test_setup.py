from django.contrib.auth.models import User, Group
from django.urls import reverse
from rest_framework.test import APITestCase


# Create your tests here.
class SetupData(APITestCase):
    def setUp(self):
        self.data_siswa = {
            "NIS": 30117680196686,
            "NISN": 3012342234833,
            "NAMA": "Becky Sanders",
            "NIPD": 213171464447798,
            "JENIS_KELAMIN": "Perempuan",
            "TEMPAT_LAHIR": "Port Kylechester",
            "TANGGAL_LAHIR": "2010-08-17",
            "NIK": 4002422974503,
            "AGAMA": "Budha",
            "ALAMAT": "27102 Deanna Oval Apt. 856\nLake Dorothy, ND 87225",
            "RT": 644,
            "RW": 635,
            "DUSUN": "Lake Ericside",
            "KELURAHAN": "Riveraton",
            "KECAMATAN": "West Markfort",
            "KODE_POS": 73140,
            "JENIS_TINGGAL": "Mandiri",
            "EMAIL": "",
            "SKHUN": "",
            "PENERIMA_KPS": "Iya",
            "ROMBEL_SAAT_INI": "",
            "NO_PESERTA_UJIAN_NASIONAL": "",
            "NO_SERI_IJAZAH": "",
            "PENERIMA_KIP": "Iya",
            "NO_REGRISTASI_AKTA_LAHIR": "",
            "BANK": "",
            "NO_REKENING_BANK": "",
            "REKENING_ATAS_NAMA": "",
            "LAYAK_PIP": "Iya",
            "KEBUTUHAN_KHUSUS": "",
            "ANAK_KE": "",
            "LINTANG": "",
            "BUJUR": "",
        }

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
            "EMAIL": "russelljennifer@example.org",
        }

        self.data_orang_tua = {
            "NIK_AYAH": 503808910908,
            "NAMA_AYAH": "Nicholas Mckay",
            "TAHUN_LAHIR_AYAH": "2012-07-12",
            "JENJANG_PENDIDIKAN_AYAH": "D4",
            "PEKERJAAN_AYAH": "Financial risk analyst",
            "PENGHASILAN_AYAH": "Rp 5.000.000; Ke Atas",
            "NIK_IBU": 4226239700435,
            "NAMA_IBU": "Joyce Bradley",
            "TAHUN_LAHIR_IBU": "1974-01-17",
            "JENJANG_PENDIDIKAN_IBU": "D4",
            "PEKERJAAN_IBU": "Wellsite geologist",
            "PENGHASILAN_IBU": "Rp 500.000;- RP 1.500.000;",
            "NIK_WALI": 3550827822703793,
            "NAMA_WALI": "Amy Watson",
            "TAHUN_LAHIR_WALI": "2006-02-13",
            "JENJANG_PENDIDIKAN_WALI": "Tidak Bersekolah",
            "PEKERJAAN_WALI": "Industrial buyer",
            "PENGHASILAN_WALI": "Rp 3.500.000;- Rp 5.000.000;",
            "DATA_ANAK": [],
        }

        self.data_kompetensi = {"BIDANG_STUDI": "Bahasa Indonesia", "URUTAN": "Pertama"}

        self.data_admin = {"username": "admin", "password": "merdeka123"}

        # create groups
        groups = ["Siswa", "Guru", "Orang Tua", "Karyawan"]
        for group in groups:
            object = Group.objects.create(name=group)
            object.save()

        # create superuser
        user = User.objects.create_user(username="admin", password="merdeka123")
        user.is_superuser = True
        user.save()

        # login as superuser
        login_response = self.client.post(reverse("login"), self.data_admin)
        self.client.credentials(
            HTTP_AUTHORIZATION="Bearer " + login_response.data["access"]
        )

        super().setUp()

        def tearDown(self):
            super().tearDown()
