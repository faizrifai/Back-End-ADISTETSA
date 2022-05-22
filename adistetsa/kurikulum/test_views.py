import shutil

from django.test import override_settings
from rest_framework.test import APITestCase
from utility.test_utility import *

from kurikulum.factories import KTSPFactory
from kurikulum.models import TahunAjaran

TEST_DIR = 'test_data'


class TestKurikulum(APITestCase):
    @classmethod
    @override_settings(MEDIA_ROOT=(TEST_DIR + '/media'))
    def setUpClass(self):
        super().setUpClass()

        TahunAjaran.objects.create(
            TAHUN_AJARAN_AWAL=2020, TAHUN_AJARAN_AKHIR=2021)
        TahunAjaran.objects.create(
            TAHUN_AJARAN_AWAL=2021, TAHUN_AJARAN_AKHIR=2022)

        buatRole()
        self.data_login_guru = generateUserGuru(['Staf Kurikulum'])

    def tearDown(self):
        print("\nDeleting temporary files...\n")
        try:
            shutil.rmtree(TEST_DIR)
        except OSError:
            pass

    @override_settings(MEDIA_ROOT=(TEST_DIR + '/media'))
    def test_post_ktsp(self):
        # data ktsp
        post_data = {
            'TAHUN_AJARAN': 1,
        }

        loginWithUserData(self, self.data_login_guru)
        testPostWithFileView(self, 'ktsp', post_data, 'NAMA_FILE')

    @override_settings(MEDIA_ROOT=(TEST_DIR + '/media'))
    def test_edit_ktsp(self):
        # data ktsp
        update_data = {
            'TAHUN_AJARAN': 2,
        }

        loginWithUserData(self, self.data_login_guru)
        testUpdateWithFileView(self, 'ktsp', KTSPFactory,
                               update_data, 'NAMA_FILE')

    @override_settings(MEDIA_ROOT=(TEST_DIR + '/media'))
    def test_delete_ktsp(self):
        loginWithUserData(self, self.data_login_guru)
        testDeleteView(self, 'ktsp', KTSPFactory, 10)
