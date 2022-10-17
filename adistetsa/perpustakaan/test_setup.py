from django.contrib.auth.models import User, Group
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from rest_framework.test import APITestCase

from .models import *

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

        self.data_admin = {"username": "admin", "password": "merdeka123"}

        # create groups
        groups = ["Siswa", "Guru", "Orang Tua", "Karyawan", "Staf Perpustakaan"]
        for group in groups:
            object = Group.objects.create(name=group)
            object.save()

        # create superuser
        user = User.objects.create_user(username="admin", password="merdeka123")
        user.is_superuser = True
        user.save()

        # login as superuser
        login_response = self.client.post(reverse("login"), self.data_admin)
        self.admin_token = login_response.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.admin_token)

        # menambah siswa
        self.client.post(reverse("data_siswa"), self.data_siswa)
        open_file = open("kustom_autentikasi/data/data_siswa_user.csv", "rb")
        uploaded_file = SimpleUploadedFile("data_siswa_user.csv", open_file.read())
        data = {"file": uploaded_file}
        self.client.post(reverse("import_data_siswa_user"), data, format="multipart")

        # token siswa
        self.login_siswa = {"username": "30117680196686", "password": "merdeka123"}
        login_response = self.client.post(reverse("login"), self.login_siswa)
        self.siswa_token = login_response.data["access"]

        # menambah guru
        self.client.post(reverse("data_guru"), self.data_guru)
        open_file = open("kustom_autentikasi/data/data_guru_user.csv", "rb")
        uploaded_file = SimpleUploadedFile("data_guru_user.csv", open_file.read())
        data = {"file": uploaded_file}
        self.client.post(reverse("import_data_guru_user"), data, format="multipart")

        # token guru
        self.login_guru = {"username": "4341623682038467", "password": "merdeka123"}
        login_response = self.client.post(reverse("login"), self.login_guru)
        self.guru_token = login_response.data["access"]

        # menambah katalog buku
        self.bahasa = {"KODE_BAHASA": "ID", "BAHASA": "Indonesia"}
        bahasa = TipeBahasa.objects.create(**self.bahasa)

        self.kode_media = {"KODE_MEDIA": "PR", "NAMA_MEDIA": "Printed"}
        tipe_media = TipeMedia.objects.create(**self.kode_media)

        self.kode_tipe = {
            "KODE_TIPE": "Ct",
            "NAMA_TIPE": "Cetakan",
            "LAMA_PINJAM": "3 hari",
            "DENDA": "10000",
        }
        tipe_buku = TipeBuku.objects.create(**self.kode_tipe)

        self.kode_author = {"KODE_AUTHOR": "A", "NAMA_AUTHOR": "Afdhal"}
        author = Author.objects.create(**self.kode_author)

        self.tahun_terbit = {
            "TAHUN_TERBIT": 2022,
        }
        tahun_terbit = TahunTerbit.objects.create(**self.tahun_terbit)

        self.kode_lokasi = {"KODE_LOKASI": "SMU4", "NAMA_LOKASI": "SMA Negeri 4 Malang"}
        lokasi = Lokasi.objects.create(**self.kode_lokasi)

        self.lokasi_spesifik = {
            "LOKASI_SPESIFIK": "SMU4",
            "NAMA": "SMA Negeri 4 Malang",
        }
        lokasi_spesifik = LokasiSpesifik.objects.create(**self.lokasi_spesifik)

        self.operator_code = {
            "KODE_OPERATOR": User.objects.get(pk=1),
            "UNIT": "Perpustakaan",
        }
        operator = Operator.objects.create(**self.operator_code)

        self.katalog_buku = {
            "REGISTER": "12345",
            "ISBN": "9050-3030-2020",
            "JUDUL": "Ini adalah buku",
            "VOLUME": "1",
            "EDISI": "1",
            "BAHASA": bahasa,
            "KODE_MEDIA": tipe_media,
            "KODE_TIPE": tipe_buku,
            "NOMER_DEWEY": "1111",
            "KODE_AUTHOR": author,
            "KODE_JUDUL": "IAB",
            "TAHUN_TERBIT": tahun_terbit,
            "KOTA_PENERBIT": "Malang",
            "PENERBIT": "Erlangga",
            "DESKRIPSI_FISIK": "Bagus",
            "INDEX": "1",
            "BIBLIOGRAPHY": "1",
            "KODE_LOKASI": lokasi,
            "LOKASI_SPESIFIK": lokasi_spesifik,
            "HARGA": "15000",
            "DATA_ENTRY": "2022-02-02",
            "OPERATOR_CODE": operator,
        }
        katalog_buku = KatalogBuku.objects.create(**self.katalog_buku)

        # menambah data donasi dan katalog buku copy
        self.pendanaan = {"KODE_PENDANAAN": "AB", "NAMA_PENDANAAN": "Amal Jariyah"}
        pendanaan = Pendanaan.objects.create(**self.pendanaan)

        self.donasi_buku = {
            "REGISTER_DONASI": katalog_buku,
            "DUPLIKAT": 5,
            "KODE_DONASI": pendanaan,
            "TANGGAL_PENERIMAAN": "2022-02-02",
            "CATATAN_DONASI": "Semoga membawa berkah",
        }
        DonasiBuku.objects.create(**self.donasi_buku)

        super().setUp()

        def tearDown(self):
            super().tearDown()
