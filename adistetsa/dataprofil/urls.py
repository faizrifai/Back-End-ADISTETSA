from django.urls.conf import path

from .views import *

urlpatterns = [
    path('data_siswa', DataSiswaListView.as_view(), name='data_siswa'),
    path('data_siswa/<int:siswa_id>', DataSiswaDetailView.as_view()),
    path('data_orang_tua', DataOrangTuaListView.as_view(), name='data_orang_tua'),
    path('data_orang_tua/<int:orangtua_id>', DataOrangTuaDetailView.as_view()),
    path('data_guru', DataGuruListView.as_view(), name='data_guru'),
    path('data_guru/<int:guru_id>', DataGuruDetailView.as_view()),
    path('data_karyawan', DataKaryawanListView.as_view(), name='data_karyawan'),
    path('data_karyawan/<int:karyawan_id>', DataKaryawanDetailView.as_view()),
    path('data_guru_kompetensi', DataKompetensiGuruListView.as_view(), name='data_kompetensi_guru'),
    path('data_guru_kompetensi/<int:pk>', DataKompetensiGuruDetailView.as_view(), name='data_kompetensi_guru'),
    path('data_karyawan_kompetensi', DataKompetensiKaryawanListView.as_view(), name='data_kompetensi_karyawan'),
    path('data_karyawan_kompetensi/<int:pk>', DataKompetensiKaryawanDetailView.as_view(), name='data_kompetensi_karyawan'),
    path('data_guru_anak', DataAnakGuruListView.as_view(), name='data_guru_anak'),
    path('data_guru_anak/<int:pk>', DataAnakGuruDetailView.as_view(), name='data_guru_anak'),
    path('data_guru_beasiswa', DataBeasiswaGuruListView.as_view(), name='data_guru_beasiswa'),
    path('data_guru_beasiswa/<int:pk>', DataBeasiswaGuruDetailView.as_view(), name='data_guru_beasiswa'),
    path('data_guru_buku', DataBukuGuruListView.as_view(), name='data_guru_buku'),
    path('data_guru_buku/<int:pk>', DataBukuGuruDetailView.as_view(), name='data_guru_buku'),
    path('data_guru_diklat', DataDiklatGuruListView.as_view(), name='data_guru_diklat'),
    path('data_guru_diklat/<int:pk>', DataDiklatGuruDetailView.as_view(), name='data_guru_diklat'),
    path('data_guru_karya_tulis', DataKaryaTulisGuruListView.as_view(), name='data_guru_karya_tulis'),
    path('data_guru_karya_tulis/<int:pk>', DataKaryaTulisGuruDetailView.as_view(), name='data_guru_karya_tulis'),
    path('data_guru_kesejahteraan', DataKesejahteraanGuruListView.as_view(), name='data_guru_kesejahteraan'),
    path('data_guru_kesejahteraan/<int:pk>', DataKesejahteraanGuruDetailView.as_view(), name='data_guru_kesejahteraan'),
    path('data_guru_tunjangan', DataTunjanganGuruListView.as_view(), name='data_guru_tunjangan'),
    path('data_guru_tunjangan/<int:pk>', DataTunjanganGuruDetailView.as_view(), name='data_guru_tunjangan'),
    path('data_guru_tugas_tambahan', DataTugasTambahanGuruListView.as_view(), name='data_guru_tugas_tambahan'),
    path('data_guru_tugas_tambahan/<int:pk>', DataTugasTambahanGuruDetailView.as_view(), name='data_guru_tugas_tambahan'),
    path('data_guru_penghargaan', DataPenghargaanGuruListView.as_view(), name='data_guru_penghargaan'),
    path('data_guru_penghargaan/<int:pk>', DataPenghargaanGuruDetailView.as_view(), name='data_guru_penghargaan'),
    path('data_guru_nilai_tes', DataNilaiTesGuruListView.as_view(), name='data_guru_nilai_tes'),
    path('data_guru_nilai_tes/<int:pk>', DataNilaiTesGuruDetailView.as_view(), name='data_guru_nilai_tes'),
    path('data_guru_riwayat_gaji_berkala', DataRiwayatGajiBerkalaGuruListView.as_view(), name='data_guru_riwayat_gaji_berkala'),
    path('data_guru_riwayat_gaji_berkala/<int:pk>', DataRiwayatGajiBerkalaGuruDetailView.as_view(), name='data_guru_riwayat_gaji_berkala'),
    path('data_guru_riwayat_jabatan_struktural', DataRiwayatJabatanStrukturalGuruListView.as_view(), name='data_guru_riwayat_jabatan_struktural'),
    path('data_guru_riwayat_jabatan_struktural/<int:pk>', DataRiwayatJabatanStrukturalGuruDetailView.as_view(), name='data_guru_riwayat_jabatan_struktural'),
    path('data_guru_riwayat_kepangkatan', DataRiwayatKepangkatanGuruListView.as_view(), name='data_guru_riwayat_kepangkatan'),
    path('data_guru_riwayat_kepangkatan/<int:pk>', DataRiwayatKepangkatanGuruDetailView.as_view(), name='data_guru_riwayat_kepangkatan'),
    path('data_guru_riwayat_pendidikan_formal', DataRiwayatPendidikanFormalGuruListView.as_view(), name='data_guru_riwayat_pendidikan_formal'),
    path('data_guru_riwayat_pendidikan_formal/<int:pk>', DataRiwayatPendidikanFormalGuruDetailView.as_view(), name='data_guru_riwayat_pendidikan_formal'),
    path('data_guru_riwayat_sertifikasi', DataRiwayatSertifikasiGuruListView.as_view(), name='data_guru_riwayat_sertifikasi'),
    path('data_guru_riwayat_sertifikasi/<int:pk>', DataRiwayatSertifikasiGuruDetailView.as_view(), name='data_guru_riwayat_sertifikasi'),
    path('data_guru_riwayat_jabatan_fungsional', DataRiwayatJabatanFungsionalGuruListView.as_view(), name='data_guru_riwayat_jabatan_fungsional'),
    path('data_guru_riwayat_jabatan_fungsional/<int:pk>', DataRiwayatJabatanFungsionalGuruDetailView.as_view(), name='data_guru_riwayat_jabatan_fungsional'),
    path('data_guru_riwayat_karir', DataRiwayatKarirGuruListView.as_view(), name='data_guru_riwayat_karir'),
    path('data_guru_riwayat_karir/<int:pk>', DataRiwayatKarirGuruDetailView.as_view(), name='data_guru_riwayat_karir'),
    path('data_karyawan_anak', DataAnakKaryawanListView.as_view(), name = "data_karyawan_anak"),
    path('data_karyawan_anak/<int:pk>', DataAnakKaryawanDetailView.as_view(), name = "data_karyawan_anak"),
    path('data_karyawan_beasiswa', DataBeasiswaKaryawanListView.as_view(), name = "data_karyawan_beasiswa"),
    path('data_karyawan_beasiswa/<int:pk>', DataBeasiswaKaryawanDetailView.as_view(), name = "data_karyawan_beasiswa"),
    path('data_karyawan_buku', DataBukuKaryawanListView.as_view(), name = "data_karyawan_buku"),
    path('data_karyawan_buku/<int:pk>', DataBukuKaryawanDetailView.as_view(), name = "data_karyawan_buku"),
    path('data_karyawan_diklat', DataDiklatKaryawanListView.as_view(), name = "data_karyawan_diklat"),
    path('data_karyawan_diklat/<int:pk>', DataDiklatKaryawanDetailView.as_view(), name = "data_karyawan_diklat"),
    path('data_karyawan_karya_tulis', DataKaryaTulisKaryawanListView.as_view(), name = "data_karyawan_karya_tulis"),
    path('data_karyawan_karya_tulis/<int:pk>', DataKaryaTulisKaryawanDetailView.as_view(), name = "data_karyawan_karya_tulis"),
    path('data_karyawan_kesejahteraan', DataKesejahteraanKaryawanListView.as_view(), name = "data_karyawan_kesejahteraan"),
    path('data_karyawan_kesejahteraan/<int:pk>', DataKesejahteraanKaryawanDetailView.as_view(), name = "data_karyawan_kesejahteraan"),
    path('data_karyawan_tunjangan', DataTunjanganKaryawanListView.as_view(), name = "data_karyawan_tunjangan"),
    path('data_karyawan_tunjangan/<int:pk>', DataTunjanganKaryawanDetailView.as_view(), name = "data_karyawan_tunjangan"),
    path('data_karyawan_tugas_tambahan', DataTugasTambahanKaryawanListView.as_view(), name = "data_karyawan_tugas_tambahan"),
    path('data_karyawan_tugas_tambahan/<int:pk>', DataTugasTambahanKaryawanDetailView.as_view(), name = "data_karyawan_tugas_tambahan"),
    path('data_karyawan_penghargaan', DataPenghargaanKaryawanListView.as_view(), name = "data_karyawan_penghargaan"),
    path('data_karyawan_penghargaan/<int:pk>', DataPenghargaanKaryawanDetailView.as_view(), name = "data_karyawan_penghargaan"),
    path('data_karyawan_nilai_tes', DataNilaiTesKaryawanListView.as_view(), name = "data_karyawan_nilai_tes"),
    path('data_karyawan_nilai_tes/<int:pk>', DataNilaiTesKaryawanDetailView.as_view(), name = "data_karyawan_nilai_tes"),
    path('data_karyawan_riwayat_gaji_berkala', DataRiwayatGajiBerkalaKaryawanListView.as_view(), name = "data_karyawan_riwayat_gaji_berkala"),
    path('data_karyawan_riwayat_gaji_berkala/<int:pk>', DataRiwayatGajiBerkalaKaryawanDetailView.as_view(), name = "data_karyawan_riwayat_gaji_berkala"),
    path('data_karyawan_riwayat_jabatan_struktural', DataRiwayatJabatanStrukturalKaryawanListView.as_view(), name = "data_karyawan_riwayat_jabatan_struktural"),
    path('data_karyawan_riwayat_jabatan_struktural/<int:pk>', DataRiwayatJabatanStrukturalKaryawanDetailView.as_view(), name = "data_karyawan_riwayat_jabatan_struktural"),
    path('data_karyawan_riwayat_kepangkatan', DataRiwayatKepangkatanKaryawanListView.as_view(), name = "data_karyawan_riwayat_kepangkatan"),
    path('data_karyawan_riwayat_kepangkatan/<int:pk>', DataRiwayatKepangkatanKaryawanDetailView.as_view(), name = "data_karyawan_riwayat_kepangkatan"),
    path('data_karyawan_riwayat_pendidikan_formal', DataRiwayatPendidikanFormalKaryawanListView.as_view(), name = "data_karyawan_riwayat_pendidikan_formal"),
    path('data_karyawan_riwayat_pendidikan_formal/<int:pk>', DataRiwayatPendidikanFormalKaryawanDetailView.as_view(), name = "data_karyawan_riwayat_pendidikan_formal"),
    path('data_karyawan_riwayat_sertifikasi', DataRiwayatSertifikasiKaryawanListView.as_view(), name = "data_karyawan_riwayat_sertifikasi"),
    path('data_karyawan_riwayat_sertifikasi/<int:pk>', DataRiwayatSertifikasiKaryawanDetailView.as_view(), name = "data_karyawan_riwayat_sertifikasi"),
    path('data_karyawan_riwayat_jabatan_fungsional', DataRiwayatJabatanFungsionalKaryawanListView.as_view(), name = "data_karyawan_riwayat_jabatan_fungsional"),
    path('data_karyawan_riwayat_jabatan_fungsional/<int:pk>', DataRiwayatJabatanFungsionalKaryawanDetailView.as_view(), name = "data_karyawan_riwayat_jabatan_fungsional"),
    path('data_karyawan_riwayat_karir', DataRiwayatKarirKaryawanListView.as_view(), name = "data_karyawan_riwayat_karir"),
    path('data_karyawan_riwayat_karir/<int:pk>', DataRiwayatKarirKaryawanDetailView.as_view(), name = "data_karyawan_riwayat_karir"),
]