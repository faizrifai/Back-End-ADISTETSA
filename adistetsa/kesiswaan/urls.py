from django.urls.conf import path
from .views import *

urlpatterns = [
    path('kesiswaan/pengajuan_laporan_pelanggaran', PengajuanLaporanPelanggaranListView.as_view(), name='pengajuan_laporan_pelanggaran'),
    path('kesiswaan/riwayat_laporan_pelanggaran', RiwayatLaporanPelanggaranListView.as_view(), name='riwayat_laporan_pelanggaran'),
    path('kesiswaan/pengajuan_program_kebaikan', PengajuanProgramKebaikanListView.as_view(), name='pengajuan_program_kebaikan'),
    path('kesiswaan/riwayat_program_kebaikan', RiwayatProgramKebaikanListView.as_view(), name='riwayat_program_kebaikan'),
    path('kesiswaan/daftar_siswa', DaftarSiswaListView.as_view(), name='daftar_siswa'),
    path('kesiswaan/data_pelanggaran', DataPelanggaranListView.as_view(), name='data_pelanggaran'),
    path('kesiswaan/data_kebaikan', DataKebaikanListView.as_view(), name='data_kebaikan')
]