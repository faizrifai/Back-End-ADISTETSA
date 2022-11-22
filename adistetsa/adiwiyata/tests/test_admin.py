from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from model_bakery import baker

from adiwiyata.factories import DaftarKaderFactory

from ..admin import DaftarKaderAdmin
from ..models import DaftarKader, TabunganSampahProxy


class DaftarKaderAdminTest(TestCase):
    def setUp(self):
        DaftarKaderFactory()

        self.data_kader = DaftarKader.objects.first()

    def test_custom_functions(self):
        nis = self.data_kader.NIS.NIS
        nama = self.data_kader.NIS.NAMA
        handphone = self.data_kader.NIS.HP
        alamat = self.data_kader.NIS.ALAMAT

        r_admin = DaftarKaderAdmin
        nis_admin = r_admin.nis(self, self.data_kader)
        nama_admin = r_admin.nama(self, self.data_kader)
        handphone_admin = r_admin.handphone(self, self.data_kader)
        alamat_admin = r_admin.alamat(self, self.data_kader)

        self.assertEqual(nis, nis_admin)
        self.assertEqual(nama, nama_admin)
        self.assertEqual(handphone, handphone_admin)
        self.assertEqual(alamat, alamat_admin)


class TabunganSampahProxyTestCase(TestCase):
    def setUp(self):
        baker.make(TabunganSampahProxy)

        User.objects.create_superuser("admin", "admin@example.com", "inipassword123")

    def test_tabungansampahproxy(self):
        # login
        self.client.login(username="admin", password="inipassword123")

        # eksekusi
        r_admin = reverse("admin:adiwiyata_tabungansampahproxy_changelist")
        response = self.client.get(r_admin)
        
        # logout
        self.client.logout()

        self.assertEqual(response.status_code, 200)