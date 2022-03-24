from django.urls.conf import path

from .views import *

urlpatterns = [
    path('hubungan_masyarakat/log_uks', LogUKSListView.as_view(), name='log_uks'),
    path('hubungan_masyarakat/detail_log_uks_siswa/<int:pk>', LogUKSDetailSiswaView.as_view(), name='detail_log_uks_siswa'),
    path('hubungan_masyarakat/detail_log_uks_tendik/<int:pk>', LogUKSDetailTendikView.as_view(), name='detail_log_uks_tendik'),
    path('hubungan_masyarakat/tambah_log_uks_siswa', TambahLogUKSSiswaView.as_view(), name='tambah_log_uks_siswa'),
    path('hubungan_masyarakat/tambah_log_uks_tendik', TambahLogUKSTendikView.as_view(), name='tambah_log_uks_tendik'),
    path('hubungan_masyarakat/buku_tamu', BukuTamuListView.as_view(), name='buku_tamu'),
    path('hubungan_masyarakat/buku_tamu/<int:pk>', BukuTamuDetailView.as_view(), name='buku_tamu'),
]