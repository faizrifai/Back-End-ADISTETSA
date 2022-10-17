from django.contrib.auth.models import User
from django.test import override_settings
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from utility.test_utility import testListView, testListViewWithSearch

import shutil

from .factories import (
    SanitasiDrainaseFactory,
    PublikasiFactory,
    KonservasiFactory,
    JaringanKerjaFactory,
    KegiatanKaderFactory,
    PembibitanPohonFactory,
    PemeliharaanPohonFactory,
    PemeliharaanSampahFactory,
    PenanamanPohonFactory,
    PenerapanPRLHFactory,
    KaryaInovatifFactory,
    ReuseReduceRecycleFactory,
)
from .models import (
    SanitasiDrainase,
    JaringanKerja,
    Publikasi,
    Konservasi,
    KegiatanKader,
    PembibitanPohon,
    PemeliharaanPohon,
    PemeliharaanSampah,
    PenanamanPohon,
    PenerapanPRLH,
    KaryaInovatif,
    ReuseReduceRecycle,
    TabunganSampah,
)

TEST_DIR = "test_data"

# Create your tests here.
class TestAdiwiyata(APITestCase):
    @override_settings(MEDIA_ROOT=(TEST_DIR + "/media"))
    def setUp(self):
        # create superuser
        user = User.objects.create_user(username="admin", password="merdeka123")
        user.is_superuser = True
        user.save()

        self.data_admin = {"username": "admin", "password": "merdeka123"}

        # login as superuser
        login_response = self.client.post(reverse("login"), self.data_admin)
        self.client.credentials(
            HTTP_AUTHORIZATION="Bearer " + login_response.data["access"]
        )

    def tearDown(self):
        print("\nDeleting temporary files...\n")
        try:
            shutil.rmtree(TEST_DIR)
        except OSError:
            pass

    @override_settings(MEDIA_ROOT=(TEST_DIR + "/media"))
    def testSanitasi(self):
        testListViewWithSearch(
            self,
            "sanitasi_drainase",
            SanitasiDrainaseFactory,
            10,
            SanitasiDrainase,
            "NAMA_KEGIATAN",
        )

    @override_settings(MEDIA_ROOT=(TEST_DIR + "/media"))
    def testJaringanKerja(self):
        testListViewWithSearch(
            self,
            "jaringan_kerja",
            JaringanKerjaFactory,
            10,
            JaringanKerja,
            "NAMA_KEGIATAN",
        )

    @override_settings(MEDIA_ROOT=(TEST_DIR + "/media"))
    def testPublikasi(self):
        testListViewWithSearch(
            self, "publikasi", PublikasiFactory, 10, Publikasi, "NAMA_KEGIATAN"
        )

    @override_settings(MEDIA_ROOT=(TEST_DIR + "/media"))
    def testKegiatanKader(self):
        testListViewWithSearch(
            self,
            "kegiatan_kader",
            KegiatanKaderFactory,
            10,
            KegiatanKader,
            "NAMA_KEGIATAN",
        )

    @override_settings(MEDIA_ROOT=(TEST_DIR + "/media"))
    def testKonservasiEnergi(self):
        response = testListViewWithSearch(
            self,
            "konservasi_energi",
            KonservasiFactory,
            10,
            Konservasi,
            "NAMA_KEGIATAN",
            False,
        )

        self.assertEqual(
            len(response.data["results"]),
            len(Konservasi.objects.filter(KATEGORI="Energi")),
        )

    @override_settings(MEDIA_ROOT=(TEST_DIR + "/media"))
    def testKonservasiAir(self):
        response = testListViewWithSearch(
            self,
            "konservasi_air",
            KonservasiFactory,
            10,
            Konservasi,
            "NAMA_KEGIATAN",
            False,
        )

        self.assertEqual(
            len(response.data["results"]),
            len(Konservasi.objects.filter(KATEGORI="Air")),
        )

    @override_settings(MEDIA_ROOT=(TEST_DIR + "/media"))
    def testPembibitanPohon(self):
        testListViewWithSearch(
            self,
            "pembibitan_pohon",
            PembibitanPohonFactory,
            10,
            PembibitanPohon,
            "NAMA_KEGIATAN",
        )

    @override_settings(MEDIA_ROOT=(TEST_DIR + "/media"))
    def testPemeliharaanPohon(self):
        testListViewWithSearch(
            self,
            "pemeliharaan_pohon",
            PemeliharaanPohonFactory,
            10,
            PemeliharaanPohon,
            "NAMA_KEGIATAN",
        )

    @override_settings(MEDIA_ROOT=(TEST_DIR + "/media"))
    def testInovatif(self):
        testListViewWithSearch(
            self, "inovatif", KaryaInovatifFactory, 10, KaryaInovatif, "NAMA_INOVATOR"
        )

    @override_settings(MEDIA_ROOT=(TEST_DIR + "/media"))
    def testPRLH(self):
        testListViewWithSearch(
            self, "prlh", PenerapanPRLHFactory, 10, PenerapanPRLH, "NAMA_KEGIATAN"
        )

    @override_settings(MEDIA_ROOT=(TEST_DIR + "/media"))
    def test3R(self):
        testListViewWithSearch(
            self,
            "reuse_reduce_recycle",
            ReuseReduceRecycleFactory,
            10,
            ReuseReduceRecycle,
            "NAMA_KEGIATAN",
        )

    @override_settings(MEDIA_ROOT=(TEST_DIR + "/media"))
    def testPemeliharaanSampah(self):
        testListViewWithSearch(
            self,
            "pemeliharaan_sampah",
            PemeliharaanSampahFactory,
            10,
            PemeliharaanSampah,
            "NAMA_KEGIATAN",
        )

    @override_settings(MEDIA_ROOT=(TEST_DIR + "/media"))
    def testPenanamanPohon(self):
        testListViewWithSearch(
            self,
            "penanaman_pohon",
            PenanamanPohonFactory,
            10,
            PenanamanPohon,
            "NAMA_KEGIATAN",
        )

    @override_settings(MEDIA_ROOT=(TEST_DIR + "/media"))
    def testTabunganSampah(self):
        response = testListView(self, "tabungan_sampah", TabunganSampah, 10, False)
        self.assertEqual(len(response.data["results"]), 12)

        response_tahun = self.client.get(reverse("tabungan_sampah_tahun"))
        self.assertEqual(response_tahun.status_code, status.HTTP_200_OK)
