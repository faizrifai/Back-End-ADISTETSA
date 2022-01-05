from .test_karyawan_setup import *

from django.urls import reverse
from rest_framework import status

class CreateDataKompetensiCase(SetupData):
    def test_create_data_kompetensi(self):
        response = self.client.post(reverse('data_kompetensi_karyawan'), self.data_kompetensi)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_edit_data_kompetensi(self):
        # add data kompetensi
        self.client.post(reverse('data_kompetensi_karyawan'), self.data_kompetensi)

        # test edit data
        patch_response = self.client.patch(reverse('data_kompetensi_karyawan', kwargs={'pk': 1}), self.data_kompetensi)
        put_response = self.client.put(reverse('data_kompetensi_karyawan', kwargs={'pk': 1}), self.data_kompetensi)

        self.assertEqual(patch_response.status_code, status.HTTP_200_OK)
        self.assertEqual(put_response.status_code, status.HTTP_200_OK)

    def test_delete_data_kompetensi(self):
        # add data kompetensi
        self.client.post(reverse('data_kompetensi_karyawan'), self.data_kompetensi)

        # test delete data
        response = self.client.delete(reverse('data_kompetensi_karyawan', kwargs={'pk': 1}))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class CreateDataAnakCase(SetupData):
    def test_create_data_anak(self):
        response = self.client.post(reverse('data_karyawan_anak'), self.data_anak)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_edit_data_anak(self):
        # add data 
        self.client.post(reverse('data_karyawan_anak'), self.data_anak)

        # test edit data
        patch_response = self.client.patch(reverse('data_karyawan_anak', kwargs={'pk': 1}), self.data_anak)
        put_response = self.client.put(reverse('data_karyawan_anak', kwargs={'pk': 1}), self.data_anak)

        self.assertEqual(patch_response.status_code, status.HTTP_200_OK)
        self.assertEqual(put_response.status_code, status.HTTP_200_OK)

    def test_delete_data_anak(self):
        # add data 
        self.client.post(reverse('data_karyawan_anak'), self.data_anak)

        # test delete data
        response = self.client.delete(reverse('data_karyawan_anak', kwargs={'pk': 1}))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class CreateDataBeasiswaCase(SetupData):
    def test_create_data_beasiswa(self):
        response = self.client.post(reverse('data_karyawan_beasiswa'), self.data_beasiswa)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_edit_data_beasiswa(self):
        # add data 
        self.client.post(reverse('data_karyawan_beasiswa'), self.data_beasiswa)

        # test edit data
        patch_response = self.client.patch(reverse('data_karyawan_beasiswa', kwargs={'pk': 1}), self.data_beasiswa)
        put_response = self.client.put(reverse('data_karyawan_beasiswa', kwargs={'pk': 1}), self.data_beasiswa)

        self.assertEqual(patch_response.status_code, status.HTTP_200_OK)
        self.assertEqual(put_response.status_code, status.HTTP_200_OK)

    def test_delete_data_beasiswa(self):
        # add data 
        self.client.post(reverse('data_karyawan_beasiswa'), self.data_beasiswa)

        # test delete data
        response = self.client.delete(reverse('data_karyawan_beasiswa', kwargs={'pk': 1}))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class CreateDataBukuCase(SetupData):
    def test_create_data_buku(self):
        response = self.client.post(reverse('data_karyawan_buku'), self.data_buku)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_edit_data_buku(self):
        # add data 
        self.client.post(reverse('data_karyawan_buku'), self.data_buku)

        # test edit data
        patch_response = self.client.patch(reverse('data_karyawan_buku', kwargs={'pk': 1}), self.data_buku)
        put_response = self.client.put(reverse('data_karyawan_buku', kwargs={'pk': 1}), self.data_buku)

        self.assertEqual(patch_response.status_code, status.HTTP_200_OK)
        self.assertEqual(put_response.status_code, status.HTTP_200_OK)

    def test_delete_data_buku(self):
        # add data 
        self.client.post(reverse('data_karyawan_buku'), self.data_buku)

        # test delete data
        response = self.client.delete(reverse('data_karyawan_buku', kwargs={'pk': 1}))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class CreateDataDiklatCase(SetupData):
    def test_create_data_diklat(self):
        response = self.client.post(reverse('data_karyawan_diklat'), self.data_diklat)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_edit_data_diklat(self):
        # add data 
        self.client.post(reverse('data_karyawan_diklat'), self.data_diklat)

        # test edit data
        patch_response = self.client.patch(reverse('data_karyawan_diklat', kwargs={'pk': 1}), self.data_diklat)
        put_response = self.client.put(reverse('data_karyawan_diklat', kwargs={'pk': 1}), self.data_diklat)

        self.assertEqual(patch_response.status_code, status.HTTP_200_OK)
        self.assertEqual(put_response.status_code, status.HTTP_200_OK)

    def test_delete_data_diklat(self):
        # add data 
        self.client.post(reverse('data_karyawan_diklat'), self.data_diklat)

        # test delete data
        response = self.client.delete(reverse('data_karyawan_diklat', kwargs={'pk': 1}))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class CreateDataKaryaTulisCase(SetupData):
    def test_create_data_karya_tulis(self):
        response = self.client.post(reverse('data_karyawan_karya_tulis'), self.data_karya_tulis)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_edit_data_karya_tulis(self):
        # add data 
        self.client.post(reverse('data_karyawan_karya_tulis'), self.data_karya_tulis)

        # test edit data
        patch_response = self.client.patch(reverse('data_karyawan_karya_tulis', kwargs={'pk': 1}), self.data_karya_tulis)
        put_response = self.client.put(reverse('data_karyawan_karya_tulis', kwargs={'pk': 1}), self.data_karya_tulis)

        self.assertEqual(patch_response.status_code, status.HTTP_200_OK)
        self.assertEqual(put_response.status_code, status.HTTP_200_OK)

    def test_delete_data_karya_tulis(self):
        # add data 
        self.client.post(reverse('data_karyawan_karya_tulis'), self.data_karya_tulis)

        # test delete data
        response = self.client.delete(reverse('data_karyawan_karya_tulis', kwargs={'pk': 1}))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class CreatedataKesejahteraanCase(SetupData):
    def test_create_data_karyawan_kesejahteraan(self):
        response = self.client.post(reverse('data_karyawan_kesejahteraan'), self.data_kesejahteraan)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_edit_data_karyawan_kesejahteraan(self):
        # add data 
        self.client.post(reverse('data_karyawan_kesejahteraan'), self.data_kesejahteraan)

        # test edit data
        patch_response = self.client.patch(reverse('data_karyawan_kesejahteraan', kwargs={'pk': 1}), self.data_kesejahteraan)
        put_response = self.client.put(reverse('data_karyawan_kesejahteraan', kwargs={'pk': 1}), self.data_kesejahteraan)

        self.assertEqual(patch_response.status_code, status.HTTP_200_OK)
        self.assertEqual(put_response.status_code, status.HTTP_200_OK)

    def test_delete_data_karyawan_kesejahteraan(self):
        # add data 
        self.client.post(reverse('data_karyawan_kesejahteraan'), self.data_kesejahteraan)

        # test delete data
        response = self.client.delete(reverse('data_karyawan_kesejahteraan', kwargs={'pk': 1}))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class CreateDataTunjanganCase(SetupData):
    def test_create_data_tunjangan(self):
        response = self.client.post(reverse('data_karyawan_tunjangan'), self.data_tunjangan)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_edit_data_tunjangan(self):
        # add data 
        self.client.post(reverse('data_karyawan_tunjangan'), self.data_tunjangan)

        # test edit data
        patch_response = self.client.patch(reverse('data_karyawan_tunjangan', kwargs={'pk': 1}), self.data_tunjangan)
        put_response = self.client.put(reverse('data_karyawan_tunjangan', kwargs={'pk': 1}), self.data_tunjangan)

        self.assertEqual(patch_response.status_code, status.HTTP_200_OK)
        self.assertEqual(put_response.status_code, status.HTTP_200_OK)

    def test_delete_data_tunjangan(self):
        # add data 
        self.client.post(reverse('data_karyawan_tunjangan'), self.data_tunjangan)

        # test delete data
        response = self.client.delete(reverse('data_karyawan_tunjangan', kwargs={'pk': 1}))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class CreateDataTugasTambahanCase(SetupData):
    def test_create_data_tugas_tambahan(self):
        response = self.client.post(reverse('data_karyawan_tugas_tambahan'), self.data_tugas_tambahan)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_edit_data_tugas_tambahan(self):
        # add data 
        self.client.post(reverse('data_karyawan_tugas_tambahan'), self.data_tugas_tambahan)

        # test edit data
        patch_response = self.client.patch(reverse('data_karyawan_tugas_tambahan', kwargs={'pk': 1}), self.data_tugas_tambahan)
        put_response = self.client.put(reverse('data_karyawan_tugas_tambahan', kwargs={'pk': 1}), self.data_tugas_tambahan)

        self.assertEqual(patch_response.status_code, status.HTTP_200_OK)
        self.assertEqual(put_response.status_code, status.HTTP_200_OK)

    def test_delete_data_tugas_tambahan(self):
        # add data 
        self.client.post(reverse('data_karyawan_tugas_tambahan'), self.data_tugas_tambahan)

        # test delete data
        response = self.client.delete(reverse('data_karyawan_tugas_tambahan', kwargs={'pk': 1}))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class CreateDataPenghargaanCase(SetupData):
    def test_create_data_penghargaan(self):
        response = self.client.post(reverse('data_karyawan_penghargaan'), self.data_penghargaan)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_edit_data_penghargaan(self):
        # add data 
        self.client.post(reverse('data_karyawan_penghargaan'), self.data_penghargaan)

        # test edit data
        patch_response = self.client.patch(reverse('data_karyawan_penghargaan', kwargs={'pk': 1}), self.data_penghargaan)
        put_response = self.client.put(reverse('data_karyawan_penghargaan', kwargs={'pk': 1}), self.data_penghargaan)

        self.assertEqual(patch_response.status_code, status.HTTP_200_OK)
        self.assertEqual(put_response.status_code, status.HTTP_200_OK)

    def test_delete_data_penghargaan(self):
        # add data 
        self.client.post(reverse('data_karyawan_penghargaan'), self.data_penghargaan)

        # test delete data
        response = self.client.delete(reverse('data_karyawan_penghargaan', kwargs={'pk': 1}))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class CreateDataNilaiTesCase(SetupData):
    def test_create_data_nilai_tes(self):
        response = self.client.post(reverse('data_karyawan_nilai_tes'), self.data_nilai_tes)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_edit_data_nilai_tes(self):
        # add data 
        self.client.post(reverse('data_karyawan_nilai_tes'), self.data_nilai_tes)

        # test edit data
        patch_response = self.client.patch(reverse('data_karyawan_nilai_tes', kwargs={'pk': 1}), self.data_nilai_tes)
        put_response = self.client.put(reverse('data_karyawan_nilai_tes', kwargs={'pk': 1}), self.data_nilai_tes)

        self.assertEqual(patch_response.status_code, status.HTTP_200_OK)
        self.assertEqual(put_response.status_code, status.HTTP_200_OK)

    def test_delete_data_nilai_tes(self):
        # add data 
        self.client.post(reverse('data_karyawan_nilai_tes'), self.data_nilai_tes)

        # test delete data
        response = self.client.delete(reverse('data_karyawan_nilai_tes', kwargs={'pk': 1}))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class CreateDataRiwayatGajiBerkalaCase(SetupData):
    def test_create_data_riwayat_gaji_berkala(self):
        response = self.client.post(reverse('data_karyawan_riwayat_gaji_berkala'), self.data_riwayat_gaji_berkala)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_edit_data_riwayat_gaji_berkala(self):
        # add data 
        self.client.post(reverse('data_karyawan_riwayat_gaji_berkala'), self.data_riwayat_gaji_berkala)

        # test edit data
        patch_response = self.client.patch(reverse('data_karyawan_riwayat_gaji_berkala', kwargs={'pk': 1}), self.data_riwayat_gaji_berkala)
        put_response = self.client.put(reverse('data_karyawan_riwayat_gaji_berkala', kwargs={'pk': 1}), self.data_riwayat_gaji_berkala)

        self.assertEqual(patch_response.status_code, status.HTTP_200_OK)
        self.assertEqual(put_response.status_code, status.HTTP_200_OK)

    def test_delete_data_riwayat_gaji_berkala(self):
        # add data 
        self.client.post(reverse('data_karyawan_riwayat_gaji_berkala'), self.data_riwayat_gaji_berkala)

        # test delete data
        response = self.client.delete(reverse('data_karyawan_riwayat_gaji_berkala', kwargs={'pk': 1}))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class CreateDataRiwayatJabatanStrukturalCase(SetupData):
    def test_create_data_riwayat_jabatan_struktural(self):
        response = self.client.post(reverse('data_karyawan_riwayat_jabatan_struktural'), self.data_riwayat_jabatan_struktural)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_edit_data_riwayat_jabatan_struktural(self):
        # add data 
        self.client.post(reverse('data_karyawan_riwayat_jabatan_struktural'), self.data_riwayat_jabatan_struktural)

        # test edit data
        patch_response = self.client.patch(reverse('data_karyawan_riwayat_jabatan_struktural', kwargs={'pk': 1}), self.data_riwayat_jabatan_struktural)
        put_response = self.client.put(reverse('data_karyawan_riwayat_jabatan_struktural', kwargs={'pk': 1}), self.data_riwayat_jabatan_struktural)

        self.assertEqual(patch_response.status_code, status.HTTP_200_OK)
        self.assertEqual(put_response.status_code, status.HTTP_200_OK)

    def test_delete_data_riwayat_jabatan_struktural(self):
        # add data 
        self.client.post(reverse('data_karyawan_riwayat_jabatan_struktural'), self.data_riwayat_jabatan_struktural)

        # test delete data
        response = self.client.delete(reverse('data_karyawan_riwayat_jabatan_struktural', kwargs={'pk': 1}))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class CreateDataRiwayatKepangkatanCase(SetupData):
    def test_create_data_karyawan_riwayat_kepangkatan(self):
        response = self.client.post(reverse('data_karyawan_riwayat_kepangkatan'), self.data_riwayat_kepangkatan)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_edit_data_karyawan_riwayat_kepangkatan(self):
        # add data 
        self.client.post(reverse('data_karyawan_riwayat_kepangkatan'), self.data_riwayat_kepangkatan)

        # test edit data
        patch_response = self.client.patch(reverse('data_karyawan_riwayat_kepangkatan', kwargs={'pk': 1}), self.data_riwayat_kepangkatan)
        put_response = self.client.put(reverse('data_karyawan_riwayat_kepangkatan', kwargs={'pk': 1}), self.data_riwayat_kepangkatan)

        self.assertEqual(patch_response.status_code, status.HTTP_200_OK)
        self.assertEqual(put_response.status_code, status.HTTP_200_OK)

    def test_delete_data_karyawan_riwayat_kepangkatan(self):
        # add data 
        self.client.post(reverse('data_karyawan_riwayat_kepangkatan'), self.data_riwayat_kepangkatan)

        # test delete data
        response = self.client.delete(reverse('data_karyawan_riwayat_kepangkatan', kwargs={'pk': 1}))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class CreateDataRiwayatPendidikanFormalCase(SetupData):
    def test_create_data_karyawan_riwayat_pendidikan_formal(self):
        response = self.client.post(reverse('data_karyawan_riwayat_pendidikan_formal'), self.data_karyawan_riwayat_pendidikan_formal)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_edit_data_karyawan_riwayat_pendidikan_formal(self):
        # add data 
        self.client.post(reverse('data_karyawan_riwayat_pendidikan_formal'), self.data_karyawan_riwayat_pendidikan_formal)

        # test edit data
        patch_response = self.client.patch(reverse('data_karyawan_riwayat_pendidikan_formal', kwargs={'pk': 1}), self.data_karyawan_riwayat_pendidikan_formal)
        put_response = self.client.put(reverse('data_karyawan_riwayat_pendidikan_formal', kwargs={'pk': 1}), self.data_karyawan_riwayat_pendidikan_formal)

        self.assertEqual(patch_response.status_code, status.HTTP_200_OK)
        self.assertEqual(put_response.status_code, status.HTTP_200_OK)

    def test_delete_data_karyawan_riwayat_pendidikan_formal(self):
        # add data 
        self.client.post(reverse('data_karyawan_riwayat_pendidikan_formal'), self.data_karyawan_riwayat_pendidikan_formal)

        # test delete data
        response = self.client.delete(reverse('data_karyawan_riwayat_pendidikan_formal', kwargs={'pk': 1}))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class CreateDataRiwayatSertifikasiCase(SetupData):
    def test_create_data_karyawan_riwayat_sertifikasi(self):
        response = self.client.post(reverse('data_karyawan_riwayat_sertifikasi'), self.data_riwayat_sertifikasi)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_edit_data_karyawan_riwayat_sertifikasi(self):
        # add data 
        self.client.post(reverse('data_karyawan_riwayat_sertifikasi'), self.data_riwayat_sertifikasi)

        # test edit data
        patch_response = self.client.patch(reverse('data_karyawan_riwayat_sertifikasi', kwargs={'pk': 1}), self.data_riwayat_sertifikasi)
        put_response = self.client.put(reverse('data_karyawan_riwayat_sertifikasi', kwargs={'pk': 1}), self.data_riwayat_sertifikasi)

        self.assertEqual(patch_response.status_code, status.HTTP_200_OK)
        self.assertEqual(put_response.status_code, status.HTTP_200_OK)

    def test_delete_data_karyawan_riwayat_sertifikasi(self):
        # add data 
        self.client.post(reverse('data_karyawan_riwayat_sertifikasi'), self.data_riwayat_sertifikasi)

        # test delete data
        response = self.client.delete(reverse('data_karyawan_riwayat_sertifikasi', kwargs={'pk': 1}))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class CreateDataRiwayatSertifikasiCase(SetupData):
    def test_create_data_karyawan_riwayat_sertifikasi(self):
        response = self.client.post(reverse('data_karyawan_riwayat_sertifikasi'), self.data_riwayat_sertifikasi)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_edit_data_karyawan_riwayat_sertifikasi(self):
        # add data 
        self.client.post(reverse('data_karyawan_riwayat_sertifikasi'), self.data_riwayat_sertifikasi)

        # test edit data
        patch_response = self.client.patch(reverse('data_karyawan_riwayat_sertifikasi', kwargs={'pk': 1}), self.data_riwayat_sertifikasi)
        put_response = self.client.put(reverse('data_karyawan_riwayat_sertifikasi', kwargs={'pk': 1}), self.data_riwayat_sertifikasi)

        self.assertEqual(patch_response.status_code, status.HTTP_200_OK)
        self.assertEqual(put_response.status_code, status.HTTP_200_OK)

    def test_delete_data_karyawan_riwayat_sertifikasi(self):
        # add data 
        self.client.post(reverse('data_karyawan_riwayat_sertifikasi'), self.data_riwayat_sertifikasi)

        # test delete data
        response = self.client.delete(reverse('data_karyawan_riwayat_sertifikasi', kwargs={'pk': 1}))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class CreatedataRiwayatJabatanFungsionalCase(SetupData):
    def test_create_data_karyawan_riwayat_jabatan_fungsional(self):
        response = self.client.post(reverse('data_karyawan_riwayat_jabatan_fungsional'), self.data_riwayat_jabatan_fungsional)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_edit_data_karyawan_riwayat_jabatan_fungsional(self):
        # add data 
        self.client.post(reverse('data_karyawan_riwayat_jabatan_fungsional'), self.data_riwayat_jabatan_fungsional)

        # test edit data
        patch_response = self.client.patch(reverse('data_karyawan_riwayat_jabatan_fungsional', kwargs={'pk': 1}), self.data_riwayat_jabatan_fungsional)
        put_response = self.client.put(reverse('data_karyawan_riwayat_jabatan_fungsional', kwargs={'pk': 1}), self.data_riwayat_jabatan_fungsional)

        self.assertEqual(patch_response.status_code, status.HTTP_200_OK)
        self.assertEqual(put_response.status_code, status.HTTP_200_OK)

    def test_delete_data_karyawan_riwayat_jabatan_fungsional(self):
        # add data 
        self.client.post(reverse('data_karyawan_riwayat_jabatan_fungsional'), self.data_riwayat_jabatan_fungsional)

        # test delete data
        response = self.client.delete(reverse('data_karyawan_riwayat_jabatan_fungsional', kwargs={'pk': 1}))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class CreatedataRiwayatKarirCase(SetupData):
    def test_create_data_karyawan_riwayat_karir(self):
        response = self.client.post(reverse('data_karyawan_riwayat_karir'), self.data_riwayat_karir)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_edit_data_karyawan_riwayat_karir(self):
        # add data 
        self.client.post(reverse('data_karyawan_riwayat_karir'), self.data_riwayat_karir)

        # test edit data
        patch_response = self.client.patch(reverse('data_karyawan_riwayat_karir', kwargs={'pk': 1}), self.data_riwayat_karir)
        put_response = self.client.put(reverse('data_karyawan_riwayat_karir', kwargs={'pk': 1}), self.data_riwayat_karir)

        self.assertEqual(patch_response.status_code, status.HTTP_200_OK)
        self.assertEqual(put_response.status_code, status.HTTP_200_OK)

    def test_delete_data_karyawan_riwayat_karir(self):
        # add data 
        self.client.post(reverse('data_karyawan_riwayat_karir'), self.data_riwayat_karir)

        # test delete data
        response = self.client.delete(reverse('data_karyawan_riwayat_karir', kwargs={'pk': 1}))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
