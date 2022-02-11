from django.urls.conf import path

from .views import *

urlpatterns = [
    path('sarpras/katalog_sarana', KatalogSaranaListView.as_view(), name='katalog_sarana'),
    path('sarpras/pengajuan_peminjaman_barang', PengajuanPeminjamanBarangListView.as_view(), name='pengajuan_peminjaman_barang'),
    path('sarpras/riwayat_peminjaman_barang', RiwayatPeminjamanBarangListView.as_view(), name='riwayat_peminjaman_barang'),
    path('sarpras/acc_pengajuan_peminjaman_barang/<int:pk>', AccPengajuanPeminjamanBarangView.as_view(), name='acc_pengajuan_peminjaman_barang'),
    path('sarpras/tolak_pengajuan_peminjaman_barang/<int:pk>', TolakPengajuanPeminjamanBarangView.as_view(), name='tolak_pengajuan_peminjaman_barang'),
    path('sarpras/katalog_ruangan', KatalogRuanganListView.as_view(), name='katalog_ruangan'),
    path('sarpras/pengajuan_peminjaman_ruangan', PengajuanPeminjamanRuanganListView.as_view(), name='pengajuan_peminjaman_ruangan'),
    path('sarpras/riwayat_peminjaman_ruangan', RiwayatPeminjamanRuanganListView.as_view(), name='riwayat_peminjaman_ruangan'),
    path('sarpras/acc_pengajuan_peminjaman_ruangan/<int:pk>', AccPengajuanPeminjamanRuanganView.as_view(), name='acc_pengajuan_peminjaman_ruangan'),
    path('sarpras/tolak_pengajuan_peminjaman_ruangan/<int:pk>', TolakPengajuanPeminjamanRuanganView.as_view(), name='tolak_pengajuan_peminjaman_ruangan'),
]