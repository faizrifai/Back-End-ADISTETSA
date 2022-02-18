from kustom_autentikasi.models import *
from .models import *
from .serializers import *
from rest_framework.views import Response
from rest_framework.parsers import MultiPartParser

from rest_framework import generics, status

from adistetsa.permissions import HasGroupPermissionAny, IsSuperAdmin, is_in_group
from kurikulum.serializers import PoinPelanggaranSerializer
# Create your views here.

class PengajuanLaporanPelanggaranListView(generics.ListCreateAPIView):
    """
    get: Menampilkan data daftar Pengajuan Laporan Pelanggaran (All Role).
    post: Menambahkan data Pengajuan Laporan Pelanggaran (All Role).
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Siswa', 'Guru', 'Orang Tua', 'Karyawan'],
        'POST': ['Siswa', 'Guru', 'Orang Tua', 'Karyawan'],
    }
    parser_classes = (MultiPartParser,)

    queryset = PengajuanLaporanPelanggaran.objects.all()
    serializer_class = PengajuanLaporanPelanggaranSerializer

    def get_serializer_class(self):
        if self.request.method == "GET":
            return PengajuanLaporanPelanggaranListSerializer

        elif self.request.method == "POST":
            return PengajuanLaporanPelanggaranSerializer

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class RiwayatLaporanPelanggaranListView(generics.ListAPIView):
    """
    get: Menampilkan data Riwayat Laporan Pelanggaran (Siswa).
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Siswa'],
    }

    queryset = RiwayatLaporanPelanggaran.objects.all()
    serializer_class = RiwayatLaporanPelanggaranSerializer

    def get_serializer_class(self):
        if self.request.method == "GET":
            return RiwayatLaporanPelanggaranListSerializer

    def get_queryset(self):
        current_user = self.request.user
        if (is_in_group(current_user, 'Siswa')):
            data_siswa_user = DataSiswaUser.objects.get(USER=current_user)
            queryset = RiwayatLaporanPelanggaran.objects.filter(DATA_SISWA=data_siswa_user.DATA_SISWA)

            return queryset

        return super().get_queryset()

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class PengajuanProgramKebaikanListView(generics.ListCreateAPIView):
    """
    get: Menampilkan data daftar Pengajuan Program Kebaikan.
    post: Menambahkan data Pengajuan Program Kebaikan.
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Siswa'],
        'POST': ['Siswa'],
    }
    parser_classes = (MultiPartParser,)

    queryset = PengajuanProgramKebaikan.objects.all()
    serializer_class = PengajuanProgramKebaikanSerializer

    def get_serializer_class(self):
        if self.request.method == "GET":
            return PengajuanProgramKebaikanListSerializer

        elif self.request.method == "POST":
            return PengajuanProgramKebaikanSerializer

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class RiwayatProgramKebaikanListView(generics.ListAPIView):
    """
    get: Menampilkan data Riwayat Laporan Pelanggaran.
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Siswa'],
    }

    queryset = RiwayatProgramKebaikan.objects.all()
    serializer_class = RiwayatProgramKebaikanSerializer

    def get_serializer_class(self):
        if self.request.method == "GET":
            return RiwayatProgramKebaikanListSerializer

    def get_queryset(self):
        current_user = self.request.user
        if (is_in_group(current_user, 'Siswa')):
            data_siswa_user = DataSiswaUser.objects.get(USER=current_user)
            queryset = RiwayatProgramKebaikan.objects.filter(DATA_SISWA=data_siswa_user.DATA_SISWA)

            return queryset

        return super().get_queryset()

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class DaftarSiswaListView(generics.ListAPIView):
    """
    get: Menampilkan daftar siswa (All Role).
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Siswa', 'Guru', 'Karyawan', 'Orang Tua'],
    }

    queryset = DataSiswa.objects.all()
    serializer_class = DaftarSiswaListSerializer
    filterset_fields = ('NIS', 'NAMA')
    search_fields = ('NIS', 'NAMA')

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class DataPelanggaranListView(generics.ListAPIView):
    """
    get: Menampilkan data pelanggaran (All Role).
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Siswa', 'Guru', 'Karyawan', 'Orang Tua'],
    }

    queryset = PoinPelanggaran.objects.all()
    serializer_class = PoinPelanggaranSerializer
    search_fields = ['KETERANGAN', 'POIN']

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)