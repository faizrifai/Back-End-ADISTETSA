from django.urls.conf import path

from .views import *

urlpatterns = [
    path('bimbingan_konseling/profil_konselor', ProfilKonselorView.as_view(), name='profil_konselor'),
    path('bimbingan_konseling/katalog_konselor', KatalogKonselorListView.as_view(), name='katalog_konselor'),
    path('bimbingan_konseling/katalog_konselor/<int:pk>', KatalogKonselorDetailView.as_view(), name='katalog_konselor'),
    path('bimbingan_konseling/daftar_konsultasi', DaftarKonsultasiListView.as_view(), name='daftar_konsultasi'),
    path('bimbingan_konseling/daftar_konsultasi/<int:pk>', DaftarKonsultasiDetailView.as_view(), name='daftar_konsultasi'),
    path('bimbingan_konseling/daftar_alumni', DaftarAlumniListView.as_view(), name='daftar_alumni'),
    path('bimbingan_konseling/daftar_alumni/<int:pk>', DaftarAlumniDetailView.as_view(), name='daftar_alumni'),
    path('bimbingan_konseling/angket_peminatan', AngketPeminatanListView.as_view(), name='angket_peminatan'),
    path('bimbingan_konseling/angket_peminatan_siswa', AngketPeminatanSiswaDetailView.as_view(), name='angket_peminatan'),
    path('bimbingan_konseling/angket_lintas_minat', AngketLintasMinatListView.as_view(), name='angket_lintas_minat'),
    path('bimbingan_konseling/angket_lintas_minat_siswa', AngketLintasMinatSiswaDetailView.as_view(), name='angket_lintas_minat'),
    path('bimbingan_konseling/angket_data_diri', AngketDataDiriListView.as_view(), name='angket_data_diri'),
    path('bimbingan_konseling/angket_data_diri_siswa', AngketDataDiriSiswaDetailView.as_view(), name='angket_data_diri'),
    path('bimbingan_konseling/pengajuan_konsultasi/<int:id_konselor>', PengajuanKonsultasiView.as_view(), name='pengajuan_konsultasi'),
    path('bimbingan_konseling/pengajuan_konsultasi', PengajuanKonsultasiNonStafListView.as_view(), name='pengajuan_konsultasi'),
    path('bimbingan_konseling/parameter_jurusan', ParameterJurusanListView.as_view(), name='parameter_jurusan'),
    path('bimbingan_konseling/parameter_kelas', ParameterKelasListView.as_view(), name='parameter_kelas'),
]