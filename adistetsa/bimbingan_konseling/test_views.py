from django.test import override_settings
from kurikulum.models import MataPelajaran
from rest_framework.test import APITestCase
from utility.test_utility import *

from .factories import KatalogKonselorFactory
from .models import KatalogKonselor

import shutil

TEST_DIR = "test_data"


class TestKurikulum(APITestCase):
    @classmethod
    @override_settings(MEDIA_ROOT=(TEST_DIR + "/media"))
    def setUpClass(self):
        super().setUpClass()

        buatRole()
        self.data_login_guru = generateUserGuru(["Staf BK"])
        KatalogKonselor.objects.create(
            USER=DataGuruUser.objects.last().USER,
            NAMA=DataGuruUser.objects.last().DATA_GURU.NAMA_LENGKAP,
            KOMPETENSI="Bahasa Indonesia",
            ALUMNUS="SMAN 4 Malang",
            WHATSAPP="https://wa.me/081134503493",
            CONFERENCE="https://meet.google.com",
        )

        # Buat dummy guru BK
        for _ in range(10):
            generateUserGuru(["Staf BK"])

        # Mata Pelajaran
        mata_pelajaran = [
            {"KODE": "BI", "NAMA": "Bahasa Indonesia"},
            {"KODE": "BING", "NAMA": "Bahasa Inggris"},
            {"KODE": "MTK", "NAMA": "Matematika"},
            {"KODE": "BIO", "NAMA": "Biologi"},
            {"KODE": "KIM", "NAMA": "Kimia"},
            {"KODE": "FIS", "NAMA": "Fisika"},
            {"KODE": "GEO", "NAMA": "Geografi"},
        ]

        for data in mata_pelajaran:
            MataPelajaran.objects.create(**data)

    def tearDown(self):
        print("\nDeleting temporary files...\n")
        try:
            shutil.rmtree(TEST_DIR)
        except OSError:
            pass

    @override_settings(MEDIA_ROOT=(TEST_DIR + "/media"))
    def test_get_profil_konselor(self):
        loginWithUserData(self, self.data_login_guru)
        response = self.client.get(reverse("profil_konselor"))

        print(response.data)

    # @override_settings(MEDIA_ROOT=(TEST_DIR + '/media'))
    # def test_edit_ktsp(self):
    #     # data ktsp
    #     update_data = {
    #         'TAHUN_AJARAN': 2,
    #     }

    #     loginWithUserData(self, self.data_login_guru)
    #     testUpdateWithFileView(self, 'ktsp', KTSPFactory, update_data, 'NAMA_FILE')

    # @override_settings(MEDIA_ROOT=(TEST_DIR + '/media'))
    # def test_delete_ktsp(self):
    #     loginWithUserData(self, self.data_login_guru)
    #     testDeleteView(self, 'ktsp', KTSPFactory, 10)
