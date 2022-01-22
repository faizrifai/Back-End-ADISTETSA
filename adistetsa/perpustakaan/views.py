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
    get: Menampilkan daftar KatalogBuku.
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Staf Perpustakaan', 'Guru', 'Siswa'],
    }

    queryset = KatalogBuku.objects.all()
    serializer_class = KatalogBukuListSerializer


    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

class KatalogBukuCopyListView(generics.ListAPIView):
    """
    get: Menampilkan daftar KatalogBuku.
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Staf Perpustakaan', 'Guru', 'Siswa'],
    }

    queryset = KatalogBukuCopy.objects.all()
    serializer_class = KatalogBukuCopyListSerializer


    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

class KatalogBukuCopyDetailView(generics.UpdateAPIView):
    """
    get: Menampilkan daftar KatalogBuku.
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'PUT': ['Staf Perpustakaan'],
        'PATCH': ['Staf Perpustakaan'],
    }

    queryset = KatalogBukuCopy.objects.all()
    serializer_class = KatalogBukuCopyListSerializer

class PengajuanPeminjamanGuruListView(generics.ListCreateAPIView):
    """
    get: Menampilkan daftar peminjaman guru.
    post: Membuat pengajuan peminjaman guru
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Staf Perpustakaan', 'Guru'],
        'POST': ['Staf Perpustakaan', 'Guru'],
    }

    queryset = PengajuanPeminjamanGuru.objects.all()
    serializer_class = PengajuanPeminjamanGuruListSerializer

    def get_serializer_class(self):
        if self.request.method == "GET":
            return PengajuanPeminjamanGuruListSerializer

        elif self.request.method == "POST":
            return PengajuanPeminjamanGuruSerializer

    def get_queryset(self):
        current_user = self.request.user
        if (is_in_group(current_user, 'Guru')):
            data_guru_user = DataGuruUser.objects.get(USER=current_user)
            queryset = PengajuanPeminjamanGuru.objects.filter(DATA_GURU=data_guru_user.DATA_GURU)
            return queryset

        return super().get_queryset()

    def get_data_guru(self):
        user = self.request.user
        data_guru = DataGuruUser.objects.get(USER=user).DATA_GURU

        return data_guru        
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.validated_data['DATA_GURU_id'] = self.get_data_guru().ID

        return super(PengajuanPeminjamanGuruListView, self).perform_create(serializer)

class PengajuanPeminjamanGuruDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    get: Menampilkan daftar pengajuan peminjaman guru.
    put: Mengubah pengajuan peminjaman guru.
    patch: Mengubah beberapa pengajuan peminjaman guru.
    delete: menghapus daftar pengajuan peminjaman guru.
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Staf Perpustakaan'],
        'PUT': ['Staf Perpustakaan'],
        'PATCH': ['Staf Perpustakaan'],
        'DELETE': ['Staf Perpustakaan'],      
    }

    queryset = PengajuanPeminjamanGuru.objects.all()
    serializer_class = PengajuanPeminjamanGuruListSerializer

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

class RiwayatPeminjamanGuruDetailView(generics.RetrieveUpdateAPIView):
    """
    get: Menampilkan daftar riwayat peminjaman guru.
    put: Mengubah riwayat peminjaman guru
    patch: Mengubah beberapa field riwayat peminjaman guru
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Staf Perpustakaan'],
        'PUT': ['Staf Perpustakaan'],
        'PATCH': ['Staf Perpustakaan'], 
    }

    queryset = RiwayatPeminjamanGuru.objects.all()
    serializer_class = RiwayatPeminjamanGuruListSerializer
    
class PengajuanPeminjamanSiswaListView(generics.ListAPIView):
    """
    get: Menampilkan daftar KatalogBuku.
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Staf Perpustakaan', 'Siswa'],
        'POST': ['Staf Perpustakaan', 'Siswa'],
    }

    queryset = PengajuanPeminjamanSiswa.objects.all()
    serializer_class = PengajuanPeminjamanSiswaSerializer


    def get_queryset(self):
        current_user = self.request.user
        if (is_in_group(user, 'Siswa')):
            data_siswa_user = DataSiswaUser.objects.get(USER=current_user)
            queryset = PengajuanPeminjamanSiswa.objects.filter(NIS=data_siswa_user.DATA_SISWA)
            return queryset

        super().get_queryset()


    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class PengajuanPeminjamanSiswaDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    get: Menampilkan data Tata Tertib.
    put: Mengubah atribut keseluruhan data Tata Tertib.
    patch: Mengubah beberapa atribut data Tata Tertib.
    delete: Menghapus data Tata Tertib.
    """
    permission_classes = [HasGroupPermissionAny]
    required_groups = {
        'GET': ['Siswa', 'Staf Perpustakaan'],
        'PUT': ['Staf Perpustakaan', 'Siswa'],
        'PATCH': ['Staf Perpustakaan', 'Siswa'],
        'DELETE': ['Staf Perpustakaan', 'Siswa'],
    }

    queryset = PengajuanPeminjamanSiswa.objects.all()
    serializer_class = PengajuanPeminjamanSiswaSerializer


    def get_queryset(self):
        current_user = self.request.user
        if (is_in_group(user, 'Siswa')):
            data_siswa_user = DataSiswaUser.objects.get(USER=current_user)
            queryset = RiwayatPeminjamanSiswa.objects.filter(NIS=data_siswa_user.DATA_SISWA)
            return queryset

        super().get_queryset()


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