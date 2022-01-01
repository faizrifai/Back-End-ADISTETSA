from django.urls.conf import path

from .views import *

urlpatterns = [
    path('data_siswa', DataSiswaListView.as_view()),
    path('data_siswa/<int:siswa_id>', DataSiswaDetailView.as_view()),
    path('data_orang_tua', DataOrangTuaListView.as_view()),
    path('data_orang_tua/<int:orangtua_id>', DataOrangTuaDetailView.as_view()),
    path('data_guru', DataGuruListView.as_view()),
    path('data_guru/<int:guru_id>', DataGuruDetailView.as_view()),
    path('data_karyawan', DataKaryawanListView.as_view()),
    path('data_karyawan/<int:karyawan_id>', DataKaryawanDetailView.as_view()),
    path('data_guru_kompetensi', DataKompetensiGuruListView.as_view()),
    path('data_guru_kompetensi/<int:pk>', DataKompetensiGuruDetailView.as_view()),
    # path('data_kompetensi_karyawan', DataKompetensiKaryawanListView.as_view()),
]