from django.urls.conf import path

from .views import *
#from .filter_views import *
#from .import_views import *

urlpatterns = [
    path('perpustakaan/katalog_buku', KatalogBukuListView.as_view(), name='katalog_buku'),
    path('perpustakaan/pengajuan_peminjaman_siswa', PengajuanPeminjamanSiswaListView.as_view(), name='pengajuan_peminjaman_siswa'),
    path('perpustakaan/pengajuan_peminjaman_siswa/<int:pk>', PengajuanPeminjamanSiswaDetailView.as_view(), name='pengajuan_peminjaman_siswa'),
    path('perpustakaan/riwayat_peminjaman_siswa', RiwayatPeminjamanSiswaListView.as_view(), name='riwayat_peminjaman_siswa'),
    path('perpustakaan/riwayat_peminjaman_siswa/<int:pk>', RiwayatPeminjamanSiswaDetailView.as_view(), name='riwayat_peminjaman_siswa'),
]