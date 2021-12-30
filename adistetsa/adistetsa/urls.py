from django.contrib import admin
from django.urls import include, path

from rest_framework import routers

from dataprofil import views

urlpatterns = [
    path('admin', admin.site.urls),
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
]
