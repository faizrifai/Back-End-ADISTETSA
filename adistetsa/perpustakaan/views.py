from kustom_autentikasi.models import *
from .models import *
from .serializers import *
# from .doc_schema import *
from rest_framework.parsers import MultiPartParser

from rest_framework import generics

from adistetsa.permissions import HasGroupPermissionAny, IsSuperAdmin


# Create your views here. 
class KatalogBukuListView(generics.ListAPIView):
    """
    get: Menampilkan daftar KatalogBuku.
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Staf Perpustakaan'],
    }

    queryset = KatalogBuku.objects.all()
    serializer_class = KatalogBukuListSerializer


    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

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