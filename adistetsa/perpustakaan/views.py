from venv import create
from kustom_autentikasi.models import *
from .models import *
from .serializers import *
# from .doc_schema import *
from rest_framework.parsers import MultiPartParser

from rest_framework import generics

from adistetsa.permissions import HasGroupPermissionAny, IsSuperAdmin, is_in_group


# Create your views here. 
class KatalogBukuListView(generics.ListAPIView):
    """
    get: Menampilkan daftar katalog buku.
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Staf Perpustakaan', 'Guru', 'Siswa'],
    }

    queryset = KatalogBuku.objects.all()
    serializer_class = KatalogBukuListSerializer
    search_fields = ('JUDUL', 'KODE_AUTHOR__NAMA_AUTHOR', 'BAHASA__BAHASA', 'TIPE_MEDIA__NAMA_MEDIA', 'KODE_TIPE__NAMA_TIPE', 'TAHUN_TERBIT__TAHUN_TERBIT')

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class KatalogBukuTersediaListView(generics.ListAPIView):
    """
    get: Menampilkan daftar katalog buku yang bisa dipinjam.
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Staf Perpustakaan', 'Guru', 'Siswa'],
    }

    queryset = KatalogBukuCopy.objects.all()
    serializer_class = KatalogBukuCopySerializer
    search_fields = (
        'DATA_DONASI__REGISTER_DONASI__JUDUL',
        'DATA_DONASI__REGISTER_DONASI__KODE_AUTHOR__NAMA_AUTHOR',
        'DATA_DONASI__REGISTER_DONASI__BAHASA__BAHASA',
        'DATA_DONASI__REGISTER_DONASI__TIPE_MEDIA__NAMA_MEDIA',
        'DATA_DONASI__REGISTER_DONASI__KODE_TIPE__NAMA_TIPE',
        'DATA_DONASI__REGISTER_DONASI__TAHUN_TERBIT__TAHUN_TERBIT'
    )

    def get_queryset(self):
        queryset = KatalogBukuCopy.objects.filter(STATUS='Sudah Dikembalikan')

        return queryset

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class PengajuanPeminjamanSiswaListView(generics.ListCreateAPIView):
    """
    get: Menampilkan daftar pengajuan peminjaman (Staf Perpustakaan, Siswa).
    post: Membuat pengajuan peminjaman (Siswa).
    """

    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Staf Perpustakaan', 'Siswa'],
        'POST': ['Siswa'],
    }

    queryset = PengajuanPeminjamanSiswa.objects.all()
    serializer_class = PengajuanPeminjamanSiswaSerializer
    search_fields = ('STATUS_PENGAJUAN')

    def get_queryset(self):
        current_user = self.request.user
        if (is_in_group(current_user, 'Siswa')):
            data_siswa_user = DataSiswaUser.objects.get(USER=current_user)
            queryset = PengajuanPeminjamanSiswa.objects.filter(NIS=data_siswa_user.DATA_SISWA)
            return queryset

        return super().get_queryset()

    def get_serializer_class(self):
        current_user = self.request.user
        if (is_in_group(current_user, 'Siswa')):
            return PengajuanPeminjamanSiswaSerializer
        elif (is_in_group(current_user, 'Staf Perpustakaan')):
            return PengajuanPeminjamanSiswaAdminSerializer

        return super().get_serializer_class()


    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
        
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class PengajuanPeminjamanGuruListView(generics.ListCreateAPIView):
    """
    get: Menampilkan daftar pengajuan peminjaman (Staf Perpustakaan, Guru).
    post: Membuat pengajuan peminjaman (Guru).
    """

    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Staf Perpustakaan', 'Guru'],
        'POST': ['Guru'],
    }

    queryset = PengajuanPeminjamanGuru.objects.all()
    serializer_class = PengajuanPeminjamanGuruSerializer
    search_fields = ('STATUS_PENGAJUAN')

    def get_queryset(self):
        current_user = self.request.user
        if (is_in_group(current_user, 'Guru')):
            data_guru_user = DataGuruUser.objects.get(USER=current_user)
            queryset = PengajuanPeminjamanGuru.objects.filter(DATA_GURU=data_guru_user.DATA_GURU)
            return queryset

        return super().get_queryset()

    def get_serializer_class(self):
        current_user = self.request.user
        if (is_in_group(current_user, 'Guru')):
            return PengajuanPeminjamanGuruSerializer
        elif (is_in_group(current_user, 'Staf Perpustakaan')):
            return PengajuanPeminjamanGuruAdminSerializer

        return super().get_serializer_class()


    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
        
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class RiwayatPeminjamanGuruListView(generics.ListAPIView):
    """
    get: Menampilkan daftar riwayat peminjaman guru.
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Staf Perpustakaan', 'Guru'],
    }

    queryset = RiwayatPeminjamanGuru.objects.all()
    serializer_class = RiwayatPeminjamanGuruListSerializer

    def get_queryset(self):
        current_user = self.request.user
        if (is_in_group(current_user, 'Guru')):
            data_guru_user = DataGuruUser.objects.get(USER=current_user)
            queryset = RiwayatPeminjamanGuru.objects.filter(DATA_GURU=data_guru_user.DATA_GURU)
            return queryset

        return super().get_queryset()

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class RiwayatPeminjamanSiswaListView(generics.ListAPIView):
    """
    get: Menampilkan daftar KatalogBuku.
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Staf Perpustakaan'],
        'POST': ['Staf Perpustakaan'],
    }

    queryset = RiwayatPeminjamanSiswa.objects.all()
    serializer_class = RiwayatPeminjamanSiswaSerializer


    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class RiwayatPeminjamanSiswaDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    get: Menampilkan data Tata Tertib.
    put: Mengubah atribut keseluruhan data Tata Tertib.
    patch: Mengubah beberapa atribut data Tata Tertib.
    delete: Menghapus data Tata Tertib.
    """
    permission_classes = [HasGroupPermissionAny]
    required_groups = {
        'GET': ['Siswa', 'Staf Perpustakaan'],
        'PUT': ['Staf Perpustakaan'],
        'PATCH': ['Staf Perpustakaan'],
    }

    queryset = RiwayatPeminjamanSiswa.objects.all()
    serializer_class = RiwayatPeminjamanSiswaSerializer


    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs) 