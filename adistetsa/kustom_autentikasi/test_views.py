from dataprofil.models import DataSiswa
from .models import DataSiswaUser
from .test_setup import *

from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework import status

class CreateDataTestCase(SetupData):
    def test_create_data_siswa(self):
        # create data siswa
        response = self.client.post(reverse('data_siswa'), self.data_siswa)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_data_guru(self):
        # create data guru
        response = self.client.post(reverse('data_guru'), self.data_guru)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_data_karyawan(self):
        # create data karyawan
        response = self.client.post(reverse('data_karyawan'), self.data_karyawan)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_data_orang_tua(self):
        # create data orang tua
        response = self.client.post(reverse('data_orang_tua'), self.data_orang_tua)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class CreateDataUserTestCase(SetupData):
    def test_create_data_siswa_user(self):
        # create data siswa
        data_siswa_response = self.client.post(reverse('data_siswa'), self.data_siswa)

        # upload file to import
        open_file = open('kustom_autentikasi/data/data_siswa_user.csv', 'rb')
        uploaded_file = SimpleUploadedFile('data_siswa_user.csv', open_file.read())
        data = {
            'file': uploaded_file
        }
        response = self.client.post(reverse('import_data_siswa_user'), data, format='multipart')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_data_guru_user(self):
        # create data guru
        data_guru_response = self.client.post(reverse('data_guru'), self.data_guru)

        # upload file to import
        open_file = open('kustom_autentikasi/data/data_guru_user.csv', 'rb')
        uploaded_file = SimpleUploadedFile('data_guru_user.csv', open_file.read())
        data = {
            'file': uploaded_file
        }
        response = self.client.post(reverse('import_data_guru_user'), data, format='multipart')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_data_karyawan_user(self):
        # create data karyawan
        data_guru_response = self.client.post(reverse('data_karyawan'), self.data_karyawan)

        # upload file to import
        open_file = open('kustom_autentikasi/data/data_karyawan_user.csv', 'rb')
        uploaded_file = SimpleUploadedFile('data_karyawan_user.csv', open_file.read())
        data = {
            'file': uploaded_file
        }
        response = self.client.post(reverse('import_data_karyawan_user'), data, format='multipart')

        self.assertEqual(response.status_code, status.HTTP_200_OK)