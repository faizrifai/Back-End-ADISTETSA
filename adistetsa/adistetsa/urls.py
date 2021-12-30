from django.contrib import admin
from django.urls import include, path

from rest_framework import routers

from dataprofil import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', views.HomeView.as_view()),
    path('api-token-auth', views.ObtainAuthTokenView.as_view()),
    path('data_siswa', views.DataSiswaListView.as_view()),
    path('data_siswa/<int:pk>', views.DataSiswaDetailView.as_view()),
    path('api-token-auth', views.ObtainAuthTokenView.as_view()),
    path('data_orang_tua', views.DataOrangTuaSiswaListView.as_view()),
    path('data_orang_tua/<int:pk>', views.DataOrangTuaDetailView.as_view()),
    path('data_karyawan', views.DataKaryawanListView.as_view()),
    path('data_karyawan/<int:pk>', views.DataKaryawanDetailView.as_view()),
    path('data_guru', views.DataGuruListView.as_view()),
    path('data_guru/<int:pk>', views.DataGuruDetailView.as_view()),
    path('data_kompetensi_guru', views.DataKompetensiGuruListView.as_view()),
    path('data_kompetensi_guru/<int:pk>', views.DataKompetensiGuruDetailView.as_view()),
    path('data_kompetensi_karyawan', views.DataKompetensiKaryawanListView.as_view()),
    path('data_kompetensi_karyawan/<int:pk>', views.DataKompetensiKaryawanDetailView.as_view()),
    path('data_anak_guru', views.DataAnakGuruListView.as_view()),
    path('data_anak_guru/owner/<int:id>', views.DataBeasiswaGuruView.as_view()),
    path('data_anak_guru/<int:pk>', views.DataAnakGuruDetailView.as_view()),
    path('data_anak_karyawan', views.DataAnakKaryawanListView.as_view()),
    path('data_anak_karyawan/<int:pk>', views.DataAnakKaryawanDetailView.as_view()),
    path('data_beasiswa_guru', views.DataBeasiswaGuruListView.as_view()),
    path('data_beasiswa_guru/owner/<int:id>', views.DataBeasiswaGuruView.as_view()),
    path('data_beasiswa_guru/<int:id>/<int:pk>', views.DataBeasiswaGuru2View.as_view()),
    path('data_beasiswa_karyawan', views.DataBeasiswaKaryawanListView.as_view()),
    path('data_beasiswa_karyawan/<int:pk>', views.DataBeasiswaKaryawanDetailView.as_view()),
]
