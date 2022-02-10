from .test_setup import *

from django.urls import reverse
from rest_framework import status

class DataTestCase(SetupData):
   def test_pengajuan_laporan_pelanggaran(self):
       response = self.client.post(reverse('pengajuan_laporan_pelanggaran'), self.pengajuan)

       self.assertEqual(response.status_code, status.HTTP_201_CREATED)