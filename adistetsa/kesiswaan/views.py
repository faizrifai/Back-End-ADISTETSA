from kustom_autentikasi.models import *
from .models import *
from .serializers import *
from rest_framework.views import Response
from rest_framework.parsers import MultiPartParser

from rest_framework import generics, status

from adistetsa.permissions import HasGroupPermissionAny, IsSuperAdmin
# Create your views here.

class PengajuanLaporanPelanggaranListView(generics.ListCreateAPIView):
    """
    get: Menampilkan data daftar Pengajuan Laporan Pelanggaran.
    post: Menambahkan data Pengajuan Laporan Pelanggaran.
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Siswa, Guru, Orang Tua, Karyawan'],
        'POST': ['Siswa, Guru, Orang Tua, Karyawan'],
    }
    parser_classes= (MultiPartParser,)

    queryset = PengajuanLaporanPelanggaran.objects.all()
    serializer_class = PengajuanLaporanPelanggaranSerializer
    # filterset_fields = ('TAHUN_AJARAN',)
    # search_fields = ('TAHUN_AJARAN__ID', 'NAMA_FILE')

    def get_serializer_class(self):
        if self.request.method == "GET":
            return PengajuanLaporanPelanggaranListSerializer

        elif self.request.method == "POST":
            return PengajuanLaporanPelanggaranSerializer

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class PengajuanLaporanPelanggaranDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    get: Menampilkan data Pengajuan Laporan Pelanggaran.
    put: Mengubah atribut keseluruhan data Pengajuan Laporan Pelanggaran.
    patch: Mengubah beberapa atribut data Pengajuan Laporan Pelanggaran.
    delete: Menghapus data Pengajuan Laporan Pelanggaran.
    """
    permission_classes = [HasGroupPermissionAny]
    required_groups = {
        'GET': ['Staf Kesiswaan'],
        'PUT': ['Staf Kesiswaan'],
        'PATCH': ['Staf Kesiswaan'],
        'DELETE': ['Staf Kesiswaan'],
    }
    parser_classes= (MultiPartParser,)

    queryset = PengajuanLaporanPelanggaran.objects.all()
    serializer_class = PengajuanLaporanPelanggaranSerializer


class PelanggaranSiswaListView(generics.ListAPIView):
    """
    get: Menampilkan data Pelanggaran Siswa.
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Staf Kesiswaan'],
    }

    queryset = PelanggaranSiswa.objects.all()
    serializer_class = PelanggaranSiswaSerializer
    # filterset_fields = ('KETERANGAN', 'KATEGORI')
    # search_fields = ('KETERANGAN', 'KATEGORI')
    def get_serializer_class(self):
        if self.request.method == "GET":
            return PelanggaranSiswaListSerializer

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class RiwayatLaporanPelanggaranListView(generics.ListAPIView):
    """
    get: Menampilkan data Riwayat Laporan Pelanggaran.
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Staf Kesiswaan'],
    }

    queryset = RiwayatLaporanPelanggaran.objects.all()
    serializer_class = RiwayatLaporanPelanggaranSerializer
    # filterset_fields = ('KETERANGAN', 'KATEGORI')
    # search_fields = ('KETERANGAN', 'KATEGORI')
    def get_serializer_class(self):
        if self.request.method == "GET":
            return RiwayatLaporanPelanggaranListSerializer

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

class KategoriProgramKebaikanListView(generics.ListCreateAPIView):
    """
    get: Menampilkan data Riwayat Laporan Pelanggaran.
    post: Menambahkan data Riwayat Laporan Pelanggaran.
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Staf Kesiswaan'],
    }

    queryset = KategoriProgramKebaikan.objects.all()
    serializer_class = KategoriProgramKebaikanSerializer
    # filterset_fields = ('KETERANGAN', 'KATEGORI')
    # search_fields = ('KETERANGAN', 'KATEGORI')

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

class KategoriProgramKebaikanDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    get: Menampilkan data Riwayat Laporan Pelanggaran.
    put: Mengubah data Riwayat Laporan Pelanggaran.
    patch: Mengubah beberapa atribut data Riwayat Laporan Pelanggaran.
    delete: Menghapus data Riwayat Laporan Pelanggaran.
    """
    permission_classes = [HasGroupPermissionAny]
    required_groups = {
        'GET': ['Staf Kesiswaan'],
        'PUT': ['Staf Kesiswaan'],
        'PATCH': ['Staf Kesiswaan'],
        'DELETE': ['Staf Kesiswaan'],
    }

    queryset = KategoriProgramKebaikan.objects.all()
    serializer_class = KategoriProgramKebaikanSerializer

class ProgramKebaikanListView(generics.ListCreateAPIView):
    """
    get: Menampilkan data Pelanggaran Siswa.
    post: 
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Staf Kesiswaan', 'Siswa'],
        'POST': ['Staf Kesiswaaan']
    }

    queryset = ProgramKebaikan.objects.all()
    serializer_class = ProgramKebaikanSerializer
    # filterset_fields = ('KETERANGAN', 'KATEGORI')
    # search_fields = ('KETERANGAN', 'KATEGORI')
    def get_serializer_class(self):
        if self.request.method == "GET":
            return ProgramKebaikanListSerializer
        if self.request.method == "POST":
            return ProgramKebaikanSerializer

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

class ProgramKebaikanDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    get: Menampilkan data Program Kebaikan.
    put: Mengubah data Program Kebaikan.
    patch: Mengubah beberapa atribut data Program Kebaikan.
    delete: Menghapus data Program Kebaikan.
    """
    permission_classes = [HasGroupPermissionAny]
    required_groups = {
        'GET': ['Staf Kesiswaan'],
        'PUT': ['Staf Kesiswaan'],
        'PATCH': ['Staf Kesiswaan'],
        'DELETE': ['Staf Kesiswaan'],
    }

    queryset = ProgramKebaikan.objects.all()
    serializer_class = ProgramKebaikanSerializer

class PengajuanProgramKebaikanListView(generics.ListCreateAPIView):
    """
    get: Menampilkan data daftar Pengajuan Program Kebaikan.
    post: Menambahkan data Pengajuan Program Kebaikan.
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Staf Kesiswaan', 'Siswa'],
        'POST': ['Staf Kesiswaan', 'Siswa'],
    }
    parser_classes= (MultiPartParser,)

    queryset = PengajuanProgramKebaikan.objects.all()
    serializer_class = PengajuanProgramKebaikanSerializer
    # filterset_fields = ('TAHUN_AJARAN',)
    # search_fields = ('TAHUN_AJARAN__ID', 'NAMA_FILE')

    def get_serializer_class(self):
        if self.request.method == "GET":
            return PengajuanProgramKebaikanListSerializer

        elif self.request.method == "POST":
            return PengajuanProgramKebaikanSerializer

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class PengajuanProgramKebaikanDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    get: Menampilkan data Pengajuan Program Kebaikan.
    put: Mengubah atribut keseluruhan data PengajuanProgramKebaikan.
    patch: Mengubah beberapa atribut data PengajuanProgramKebaikan.
    delete: Menghapus data PengajuanProgramKebaikan.
    """
    permission_classes = [HasGroupPermissionAny]
    required_groups = {
        'GET': ['Staf Kesiswaan'],
        'PUT': ['Staf Kesiswaan'],
        'PATCH': ['Staf Kesiswaan'],
        'DELETE': ['Staf Kesiswaan'],
    }
    parser_classes= (MultiPartParser,)

    queryset = PengajuanProgramKebaikan.objects.all()
    serializer_class = PengajuanProgramKebaikanSerializer

class RiwayatProgramKebaikanListView(generics.ListAPIView):
    """
    get: Menampilkan data Riwayat Laporan Pelanggaran.
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Staf Kesiswaan'],
    }

    queryset = RiwayatProgramKebaikan.objects.all()
    serializer_class = RiwayatProgramKebaikanSerializer
    # filterset_fields = ('KETERANGAN', 'KATEGORI')
    # search_fields = ('KETERANGAN', 'KATEGORI')
    def get_serializer_class(self):
        if self.request.method == "GET":
            return RiwayatProgramKebaikanListSerializer

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
