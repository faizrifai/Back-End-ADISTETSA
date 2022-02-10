from django.urls.conf import path
from .views import *

urlpatterns = [
    path('kesiswaan/pengajuan_laporan_pelanggaran', PengajuanLaporanPelanggaranListView.as_view(), name='pengajuan_laporan_pelanggaran'),
    path('kesiswaan/pengajuan_laporan_pelanggaran/<int:pk>', PengajuanLaporanPelanggaranDetailView.as_view(), name='pengajuan_laporan_pelanggaran'),
    path('kesiswaan/pelanggaran_siswa', PelanggaranSiswaListView.as_view(), name='pelanggaran_siswa'),
    path('kesiswaan/riwayat_laporan_pelanggaran', RiwayatLaporanPelanggaranListView.as_view(), name='riwayat_laporan_pelanggaran'),
    path('kesiswaan/kategori_program_kebaikan', KategoriProgramKebaikanListView.as_view(), name='kategori_program_kebaikan'),
    path('kesiswaan/kategori_program_kebaikan/<int:pk>', KategoriProgramKebaikanDetailView.as_view(), name='kategori_program_kebaikan'),
    path('kesiswaan/program_kebaikan', ProgramKebaikanListView.as_view(), name='program_kebaikan'),
    path('kesiswaan/program_kebaikan/<int:pk>', ProgramKebaikanDetailView.as_view(), name='program_kebaikan'),
    path('kesiswaan/pengajuan_program_kebaikan', PengajuanProgramKebaikanListView.as_view(), name='pengajuan_program_kebaikan'),
    path('kesiswaan/pengajuan_program_kebaikan/<int:pk>', PengajuanProgramKebaikanDetailView.as_view(), name='pengajuan_program_kebaikan'),
    path('kesiswaan/riwayat_program_kebaikan', RiwayatProgramKebaikanListView.as_view(), name='riwayat_program_kebaikan'),
]