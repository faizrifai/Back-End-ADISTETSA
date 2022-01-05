from .test_guru_setup import *

from django.urls import reverse
from rest_framework import status

class CreateDataTestCase(SetupData):
    def test_create_data_kompetensi(self):
        response = self.client.post(reverse('data_kompetensi_guru'), self.data_kompetensi)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_edit_data_kompetensi(self):
        # add data kompetensi
        self.client.post(reverse('data_kompetensi_guru'), self.data_kompetensi)

        # test edit data
        patch_response = self.client.patch(reverse('data_kompetensi_guru', kwargs={'pk': 1}), self.data_kompetensi)
        put_response = self.client.put(reverse('data_kompetensi_guru', kwargs={'pk': 1}), self.data_kompetensi)

        self.assertEqual(patch_response.status_code, status.HTTP_200_OK)
        self.assertEqual(put_response.status_code, status.HTTP_200_OK)

    def test_delete_data_kompetensi(self):
        # add data kompetensi
        self.client.post(reverse('data_kompetensi_guru'), self.data_kompetensi)

        # test delete data
        response = self.client.delete(reverse('data_kompetensi_guru', kwargs={'pk': 1}))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)