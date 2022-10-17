from os import stat
from .test_setup import *

from django.urls import reverse
from rest_framework import status


class PerpustakaanTestCase(SetupData):
    def setUp(self):
        self.pengajuan = {
            "BUKU": [1, 2],
            "TANGGAL_PENGAJUAN": "2022-09-08",
            "JANGKA_PEMINJAMAN": "Jangka Pendek",
        }

        return super().setUp()

    def test_get_katalog_buku(self):
        response = self.client.get(reverse("katalog_buku"))

        self.assertEqual(response.data["count"], 1)

    def test_get_katalog_buku_tersedia(self):
        response = self.client.get(reverse("katalog_buku_tersedia"))

        self.assertEqual(response.data["count"], 5)

    def test_pengajuan_peminjaman_siswa(self):
        # login sebagai siswa
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.siswa_token)

        response = self.client.post(
            reverse("pengajuan_peminjaman_siswa"), self.pengajuan
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_pengajuan_peminjaman_siswa_disetujui(self):
        # login sebagai siswa
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.siswa_token)

        # tambah pengajuan
        self.client.post(reverse("pengajuan_peminjaman_siswa"), self.pengajuan)

        # setujui pengajuan
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.admin_token)
        self.client.get(reverse("acc_pengajuan_peminjaman_siswa", kwargs={"pk": 1}))

        response = self.client.get(reverse("riwayat_peminjaman_siswa"))

        self.assertEqual(response.data["count"], 1)

    def test_pengajuan_peminjaman_siswa_ditolak(self):
        # login sebagai siswa
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.siswa_token)

        # tambah pengajuan
        self.client.post(reverse("pengajuan_peminjaman_siswa"), self.pengajuan)

        # tolak pengajuan
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.admin_token)
        response = self.client.get(
            reverse("tolak_pengajuan_peminjaman_siswa", kwargs={"pk": 1})
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_pengajuan_peminjaman_guru(self):
        # login sebagai guru
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.guru_token)

        response = self.client.post(
            reverse("pengajuan_peminjaman_guru"), self.pengajuan
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_pengajuan_peminjaman_guru_disetujui(self):
        # login sebagai guru
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.guru_token)

        # tambah pengajuan
        self.client.post(reverse("pengajuan_peminjaman_guru"), self.pengajuan)

        # setujui pengajuan
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.admin_token)
        self.client.get(reverse("acc_pengajuan_peminjaman_guru", kwargs={"pk": 1}))

        response = self.client.get(reverse("riwayat_peminjaman_guru"))

        self.assertEqual(response.data["count"], 1)

    def test_pengajuan_peminjaman_guru_ditolak(self):
        # login sebagai guru
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.guru_token)

        # tambah pengajuan
        self.client.post(reverse("pengajuan_peminjaman_guru"), self.pengajuan)

        # tolak pengajuan
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.admin_token)
        response = self.client.get(
            reverse("tolak_pengajuan_peminjaman_guru", kwargs={"pk": 1})
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_buku_tidak_tersedia_siswa(self):
        # login sebagai siswa
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.siswa_token)

        # pengajuan 2x
        self.client.post(reverse("pengajuan_peminjaman_siswa"), self.pengajuan)
        response = self.client.post(
            reverse("pengajuan_peminjaman_siswa"), self.pengajuan
        )

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_buku_tidak_tersedia_guru(self):
        # login sebagai guru
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.guru_token)

        # pengajuan 2x
        self.client.post(reverse("pengajuan_peminjaman_guru"), self.pengajuan)
        response = self.client.post(
            reverse("pengajuan_peminjaman_guru"), self.pengajuan
        )

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
