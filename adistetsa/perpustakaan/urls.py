from django.urls.conf import path

from .views import *
#from .filter_views import *
#from .import_views import *

urlpatterns = [
    path('perpustakaan/katalog_buku', KatalogBukuListView.as_view(), name='katalog_buku'),
    path('perpustakaan/katalog_buku_copy', KatalogBukuCopyListView.as_view(), name='katalog_buku'),
    path('perpustakaan/katalog_buku_copy/<int:pk>', KatalogBukuCopyDetailView.as_view(), name='katalog_buku'),
    path('perpustakaan/pengajuan_peminjaman_guru', PengajuanPeminjamanGuruListView.as_view(), name='pengajuan_peminjaman_guru'),
    path('perpustakaan/pengajuan_peminjaman_guru/<int:pk>', PengajuanPeminjamanGuruDetailView.as_view(), name='pengajuan_peminjaman_guru'),
    path('perpustakaan/riwayat_peminjaman_guru', RiwayatPeminjamanGuruListView.as_view(), name='riwayat_peminjaman_guru'),
    path('perpustakaan/riwayat_peminjaman_guru/<int:pk>', RiwayatPeminjamanGuruDetailView.as_view(), name='riwayat_peminjaman_guru'),
]