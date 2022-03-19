from django.urls.conf import path

from .views import *

urlpatterns = [
    path('tata_usaha/katalog_sarana', KatalogSaranaListView.as_view(), name='katalog_sarana'),
    path('sarpras/pengajuan_peminjaman_barang', PengajuanPeminjamanBarangListView.as_view(), name='pengajuan_peminjaman_barang'),
    path('sarpras/pengajuan_peminjaman_barang/<int:pk>', PengajuanPeminjamanBarangDetailView.as_view(), name='pengajuan_peminjaman_barang'),
    path('sarpras/pengajuan_peminjaman_barang_admin', PengajuanPeminjamanBarangAdminListView.as_view(), name='pengajuan_peminjaman_barang_admin'),
    path('sarpras/pengajuan_peminjaman_barang_admin/<int:pk>', PengajuanPeminjamanBarangAdminDetailView.as_view(), name='pengajuan_peminjaman_barang_admin'),
    path('sarpras/riwayat_peminjaman_barang', RiwayatPeminjamanBarangListView.as_view(), name='riwayat_peminjaman_barang'),
]