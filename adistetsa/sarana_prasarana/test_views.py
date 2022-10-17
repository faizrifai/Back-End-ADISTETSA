from .test_setup import *

from django.urls import reverse
from rest_framework import status


class SaranaPrasaranaTestCase(SetupData):
    def setUp(self):
        super().setUp()

        open_file = open("kustom_autentikasi/data/data_karyawan_user.csv", "rb")
        uploaded_file = SimpleUploadedFile("data_karyawan_user.csv", open_file.read())

        self.pengajuan_sarana = {
            "NAMA_PEMINJAM": "Afdhal",
            "NO_TELEPON": "081132320404",
            "ALAT": "1,2",
            "KEGIATAN": "Baca tulis",
            "TANGGAL_PENGGUNAAN": "2022-02-02",
            "TANGGAL_PENGEMBALIAN": "2022-02-03",
            "KETERANGAN": "Dibutuhkan pulpen untuk menulis pada acara baca tulis",
            "TANDA_TANGAN": uploaded_file,
        }

        self.pengajuan_ruangan = {
            "PENGGUNA": "Afdhal",
            "NO_HP": "081132324040",
            "KEGIATAN": "Lomba Basket",
            "RUANGAN": 1,
            "TANGGAL_PEMAKAIAN": "2022-02-02",
            "TANGGAL_BERAKHIR": "2022-02-03",
            "JAM_PENGGUNAAN": "09:00",
            "JAM_BERAKHIR": "09:30",
            "JENIS_PEMINJAMAN": "Jangka Pendek",
            "KETERANGAN": "Dibutuhkan pulpen untuk menulis pada acara baca tulis",
            "TANDA_TANGAN": uploaded_file,
        }

    def test_get_katalog_ruangan(self):
        response = self.client.get(reverse("katalog_ruangan"))

        self.assertEqual(response.data["count"], 1)

    def test_get_katalog_sarana(self):
        response = self.client.get(reverse("katalog_sarana"))

        self.assertEqual(response.data["count"], 2)

    def test_pengajuan_peminjaman_ruangan(self):
        # login sebagai siswa
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.siswa_token)

        response = self.client.post(
            reverse("pengajuan_peminjaman_ruangan"), self.pengajuan_ruangan
        )
        print(response.data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_pengajuan_peminjaman_ruangan_disetujui(self):
        # login sebagai siswa
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.siswa_token)

        # tambah pengajuan
        self.client.post(
            reverse("pengajuan_peminjaman_ruangan"), self.pengajuan_ruangan
        )

        # setujui pengajuan
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.admin_token)
        self.client.get(reverse("acc_pengajuan_peminjaman_ruangan", kwargs={"pk": 1}))

        # login sebagai siswa
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.siswa_token)
        # p = self.client.get(reverse('pengajuan_peminjaman_ruangan'))
        # print(p.data)

        response = self.client.get(reverse("riwayat_peminjaman_ruangan"))

        self.assertEqual(response.data["count"], 1)

    def test_pengajuan_peminjaman_ruangan_ditolak(self):
        # login sebagai siswa
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.siswa_token)

        # tambah pengajuan
        self.client.post(
            reverse("pengajuan_peminjaman_ruangan"), self.pengajuan_ruangan
        )

        # tolak pengajuan
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.admin_token)
        response = self.client.get(
            reverse("tolak_pengajuan_peminjaman_ruangan", kwargs={"pk": 1})
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_pengajuan_peminjaman_barang(self):
        # login sebagai guru
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.guru_token)

        response = self.client.post(
            reverse("pengajuan_peminjaman_barang"), self.pengajuan_sarana
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_pengajuan_peminjaman_barang_disetujui(self):
        # login sebagai guru
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.guru_token)

        # tambah pengajuan
        self.client.post(reverse("pengajuan_peminjaman_barang"), self.pengajuan_sarana)

        # setujui pengajuan
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.admin_token)
        self.client.get(reverse("acc_pengajuan_peminjaman_barang", kwargs={"pk": 1}))

        # login sebagai guru
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.guru_token)

        response = self.client.get(reverse("riwayat_peminjaman_barang"))

        self.assertEqual(response.data["count"], 1)

    def test_pengajuan_peminjaman_barang_ditolak(self):
        # login sebagai guru
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.guru_token)

        # tambah pengajuan
        self.client.post(reverse("pengajuan_peminjaman_barang"), self.pengajuan_sarana)

        # tolak pengajuan
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.admin_token)
        response = self.client.get(
            reverse("tolak_pengajuan_peminjaman_barang", kwargs={"pk": 1})
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_ruangan_tidak_tersedia(self):
        # login sebagai siswa
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.siswa_token)

        # pengajuan 2x
        self.client.post(
            reverse("pengajuan_peminjaman_ruangan"), self.pengajuan_ruangan
        )
        response = self.client.post(
            reverse("pengajuan_peminjaman_ruangan"), self.pengajuan_ruangan
        )

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_sarana_tidak_tersedia(self):
        # login sebagai guru
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.guru_token)

        # pengajuan 2x
        self.client.post(reverse("pengajuan_peminjaman_barang"), self.pengajuan_sarana)
        response = self.client.post(
            reverse("pengajuan_peminjaman_barang"), self.pengajuan_sarana
        )

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
