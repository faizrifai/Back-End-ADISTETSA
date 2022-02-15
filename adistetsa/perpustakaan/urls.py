from django.urls.conf import path

from .views import *

urlpatterns = [
    path('perpustakaan/katalog_buku', KatalogBukuListView.as_view(), name='katalog_buku'),
    path('perpustakaan/katalog_buku/<str:pk>', KatalogBukuDetailView.as_view(), name='katalog_buku'),
    path('perpustakaan/katalog_buku_tersedia', KatalogBukuTersediaListView.as_view(), name='katalog_buku_tersedia'),
    path('perpustakaan/pengajuan_peminjaman_siswa', PengajuanPeminjamanSiswaListView.as_view(), name='pengajuan_peminjaman_siswa'),
    path('perpustakaan/pengajuan_peminjaman_siswa/<int:pk>', PengajuanPeminjamanSiswaDetailView.as_view(), name='pengajuan_peminjaman_siswa'),
    path('perpustakaan/pengajuan_peminjaman_siswa_admin', PengajuanPeminjamanSiswaAdminListView.as_view(), name='pengajuan_peminjaman_siswa_admin'),
    path('perpustakaan/pengajuan_peminjaman_siswa_admin/<int:pk>', PengajuanPeminjamanSiswaAdminDetailView.as_view(), name='pengajuan_peminjaman_siswa_admin'),
    path('perpustakaan/pengajuan_peminjaman_guru', PengajuanPeminjamanGuruListView.as_view(), name='pengajuan_peminjaman_guru'),
    path('perpustakaan/pengajuan_peminjaman_guru/<int:pk>', PengajuanPeminjamanGuruDetailView.as_view(), name='pengajuan_peminjaman_guru'),
    path('perpustakaan/pengajuan_peminjaman_guru_admin', PengajuanPeminjamanGuruAdminListView.as_view(), name='pengajuan_peminjaman_guru_admin'),
    path('perpustakaan/pengajuan_peminjaman_guru_admin/<int:pk>', PengajuanPeminjamanGuruAdminDetailView.as_view(), name='pengajuan_peminjaman_guru_admin'),
    path('perpustakaan/riwayat_peminjaman_siswa', RiwayatPeminjamanSiswaListView.as_view(), name='riwayat_peminjaman_siswa'),
    path('perpustakaan/riwayat_peminjaman_siswa/<int:pk>', RiwayatPeminjamanSiswaDetailView.as_view(), name='riwayat_peminjaman_siswa'),
    path('perpustakaan/riwayat_peminjaman_siswa_admin', RiwayatPeminjamanSiswaAdminListView.as_view(), name='riwayat_peminjaman_siswa_admin'),
    path('perpustakaan/riwayat_peminjaman_siswa_admin<int:pk>', RiwayatPeminjamanSiswaAdminDetailView.as_view(), name='riwayat_peminjaman_siswa_admin'),
    path('perpustakaan/riwayat_peminjaman_guru', RiwayatPeminjamanGuruListView.as_view(), name='riwayat_peminjaman_guru'),
    path('perpustakaan/riwayat_peminjaman_guru/<int:pk>', RiwayatPeminjamanGuruDetailView.as_view(), name='riwayat_peminjaman_guru'),
    path('perpustakaan/riwayat_peminjaman_guru_admin', RiwayatPeminjamanGuruAdminListView.as_view(), name='riwayat_peminjaman_guru_admin'),
    path('perpustakaan/riwayat_peminjaman_guru_admin/<int:pk>', RiwayatPeminjamanGuruAdminDetailView.as_view(), name='riwayat_peminjaman_guru_admin'),
    path('perpustakaan/acc_pengajuan_peminjaman_siswa/<int:pk>', AccPengajuanPeminjamanSiswaView.as_view(), name='acc_pengajuan_peminjaman_siswa'),
    path('perpustakaan/acc_pengajuan_peminjaman_guru/<int:pk>', AccPengajuanPeminjamanGuruView.as_view(), name='acc_pengajuan_peminjaman_guru'),
    path('perpustakaan/tolak_pengajuan_peminjaman_siswa/<int:pk>', TolakPengajuanPeminjamanSiswaView.as_view(), name='tolak_pengajuan_peminjaman_siswa'),
    path('perpustakaan/tolak_pengajuan_peminjaman_guru/<int:pk>', TolakPengajuanPeminjamanGuruView.as_view(), name='tolak_pengajuan_peminjaman_guru'),
]