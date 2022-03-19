from django.urls.conf import path

from .views import *

urlpatterns = [
    path('bimbingan_konseling/profil_konselor', ProfilKonselorView.as_view(), name='profil_konselor'),
    path('bimbingan_konseling/katalog_konselor', KatalogKonselorListView.as_view(), name='katalog_konselor'),
    path('bimbingan_konseling/daftar_konsultasi', DaftarKonsultasiListView.as_view(), name='daftar_konsultasi'),
    path('bimbingan_konseling/daftar_konsultasi/<int:pk>', DaftarKonsultasiDetailView.as_view(), name='daftar_konsultasi'),
    path('bimbingan_konseling/daftar_alumni', DaftarAlumniListView.as_view(), name='daftar_alumni'),
    path('bimbingan_konseling/daftar_alumni/<int:pk>', DaftarAlumniDetailView.as_view(), name='daftar_alumni'),
    path('bimbingan_konseling/angket_peminatan', AngketPeminatanListView.as_view(), name='angket_peminatan'),
    path('bimbingan_konseling/angket_peminatan', AngketLintasMinatListView.as_view(), name='angket_peminatan'),
    path('bimbingan_konseling/angket_peminatan', AngketDataDiriListView.as_view(), name='angket_peminatan'),
    path('bimbingan_konseling/pengajuan_konsultasi/<int:id_konselor>', PengajuanKonsultasiView.as_view(), name='pengajuan_konsultasi'),
    path('bimbingan_konseling/pengajuan_konsultasi_list_sendiri', PengajuanKonsultasiNonStafListView.as_view(), name='pengajuan_konsultasi_lis_sendiri'),
]