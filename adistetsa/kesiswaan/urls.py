from django.urls.conf import path
from .views import *

urlpatterns = [
    path('kesiswaan/pengajuan_laporan_pelanggaran', PengajuanLaporanPelanggaranListView.as_view(), name='pengajuan_laporan_pelanggaran'),
    path('kesiswaan/riwayat_laporan_pelanggaran', RiwayatLaporanPelanggaranListView.as_view(), name='riwayat_laporan_pelanggaran'),
    path('kesiswaan/pengajuan_program_kebaikan', PengajuanProgramKebaikanListView.as_view(), name='pengajuan_program_kebaikan'),
    path('kesiswaan/riwayat_program_kebaikan', RiwayatProgramKebaikanListView.as_view(), name='riwayat_program_kebaikan'),
    path('kesiswaan/daftar_siswa', DaftarSiswaListView.as_view(), name='daftar_siswa'),
    path('kesiswaan/data_pelanggaran', DataPelanggaranListView.as_view(), name='data_pelanggaran'),
    path('kesiswaan/data_kebaikan', DataKebaikanListView.as_view(), name='data_kebaikan'),
    path('kesiswaan/pelanggaran_saya', PelanggaranSayaListView.as_view(), name='pelanggaran_saya'),
    path('kesiswaan/katalog_ekskul', KatalogEkskulListView.as_view(), name='katalog_ekskul'),
    path('kesiswaan/katalog_ekskul/<int:pk>', KatalogEkskulDetailView.as_view(), name='katalog_ekskul'),
    path('kesiswaan/ajukan_ekskul/<int:id_katalog_ekskul>', AjukanEkskulListView.as_view(), name='ajukan_ekskul'),
    path('kesiswaan/pengajuan_ekskul', PengajuanEkskulListView.as_view(), name='pengajuan_ekskul'),
    path('kesiswaan/pengajuan_ekskul/<int:pk>', PengajuanEkskulDetailView.as_view(), name='pengajuan_ekskul'),
    path('kesiswaan/acc_pengajuan_ekskul/<int:pk>', AccPengajuanEkskulView.as_view(), name='acc_pengajuan_ekskul'),
    path('kesiswaan/ekskul_saya', EkskulSayaListView.as_view(), name='ekskul_saya'),
    path('kesiswaan/daftar_anggota/<int:id_katalog_ekskul>', DaftarAnggotaListView.as_view(), name='daftar_anggota'),
    path('kesiswaan/detail_anggota/<int:pk>', DaftarAnggotaDetailView.as_view(), name='detail_anggota'),
    path('kesiswaan/jadwal_ekskul', JadwalEkskulListView.as_view(), name='jadwal_ekskul'),
    path('kesiswaan/daftar_jurnal_ekskul', DaftarJurnalEkskulListView.as_view(), name='daftar_jurnal_ekskul'),
    path('kesiswaan/jurnal_ekskul_pertemuan/<int:id_daftar_jurnal_ekskul>', JurnalEkskulListView.as_view(), name='jurnal_ekskul_pertemuan'),
    path('kesiswaan/isi_jurnal_ekskul/<int:id_daftar_jurnal_ekskul>', IsiJurnalEkskulListView.as_view(), name='isi_jurnal_ekskul'),
    path('kesiswaan/presensi_ekskul/<int:id_jurnal_ekskul_pertemuan>', PresensiEkskulListView.as_view(), name='presensi_ekskul'),
    path('kesiswaan/detail_presensi_ekskul/<int:pk>', PresensiEkskulDetailView.as_view(), name='detail_presensi_ekskul'),
]