from .test_setup import *

from django.urls import reverse
from rest_framework import status

class DataTestCase(SetupData):
    def test_edit_ktsp(self):
        # upload file
        open_file = open('kustom_autentikasi/data/data_karyawan_user.csv', 'rb')
        uploaded_file = SimpleUploadedFile('data_karyawan_user.csv', open_file.read())

        # data ktsp
        data = {
            'TAHUN_AJARAN': 1,
            'NAMA_FILE': uploaded_file,
        }

        response = self.client.put(reverse('ktsp', kwargs={'pk': 1}), data, format='multipart')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_ktsp(self):
        response = self.client.delete(reverse('ktsp', kwargs={'pk': 1}))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)