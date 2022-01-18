from .test_setup import *

from django.urls import reverse
from rest_framework import status

class DataTestCase(SetupData):
    def test_create_ktsp(self):
        # file upload
        open_file = open('kustom_autentikasi/data/data_karyawan_user.csv', 'rb')
        uploaded_file = SimpleUploadedFile('data_karyawan_user.csv', open_file.read())

        # data ktsp
        data = {
            'TAHUN_AJARAN': 1,
            'NAMA_FILE': uploaded_file,
        }

        # create data ktsp
        response = self.client.post(reverse('ktsp'), data, format='multipart')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_edit_ktsp(self):
        response = self.client.get(reverse('ktsp'))

        print(response.data)