from .test_setup import *

from django.urls import reverse
from rest_framework import status


class DataTestCase(SetupData):
    def test_pengajuan_laporan_pelanggaran(self):
        response = self.client.post(
            reverse("pengajuan_laporan_pelanggaran"), self.pengajuan
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_riwayat_laporan_pelanggaran(self):
        # add pengajuan
        response = self.client.post(
            reverse("pengajuan_laporan_pelanggaran"), self.pengajuan
        )

        # setujui
        pengajuan = PengajuanLaporanPelanggaran.objects.get(pk=1)
        pengajuan.STATUS_PENGAJUAN = "Disetujui"
        pengajuan.save()

        # get riwayat
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.siswa_token)
        response = self.client.get(reverse("riwayat_laporan_pelanggaran"))

        self.assertEqual(response.data["count"], 1)

    def test_pengajuan_program_kebaikan(self):
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.siswa_token)
        response = self.client.post(
            reverse("pengajuan_program_kebaikan"), self.pengajuan_kebaikan
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_riwayat_program_kebaikan(self):
        # add pengajuan
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.siswa_token)
        response = self.client.post(
            reverse("pengajuan_program_kebaikan"), self.pengajuan_kebaikan
        )

        # setujui
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.guru_token)
        pengajuan = PengajuanProgramKebaikan.objects.get(pk=1)
        pengajuan.STATUS_PENGAJUAN = "Disetujui"
        pengajuan.save()

        # get riwayat
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.siswa_token)
        response = self.client.get(reverse("riwayat_program_kebaikan"))

        self.assertEqual(response.data["count"], 1)
