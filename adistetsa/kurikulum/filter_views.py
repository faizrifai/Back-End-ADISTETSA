from .models import TahunAjaran, DataSemester, Kelas, MataPelajaran, JadwalPekanEfektifSemester
from .filter_serializers import *

from rest_framework import generics

from adistetsa.permissions import HasGroupPermissionAny, IsSuperAdmin

# Create your views here. 
class SemesterListView(generics.ListAPIView):
    """
    get: Menampilkan daftar semester (Super Admin/ Staf Kurikulum).
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Staf Kurikulum'],
    }

    queryset = DataSemester.objects.all()
    serializer_class = SemesterSerializer


class TahunAjaranListView(generics.ListAPIView):
    """
    get: Menampilkan daftar tahun ajaran (Guru, Pelatih).
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Guru', 'Pelatih'],
    }

    queryset = TahunAjaran.objects.all()
    serializer_class = TahunAjaranSerializer


class KelasListView(generics.ListAPIView):
    """
    get: Menampilkan daftar kelas (Super Admin/ Staf Kurikulum).
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Staf Kurikulum'],
    }

    queryset = Kelas.objects.all()
    serializer_class = KelasSerializer


class MataPelajaranListView(generics.ListAPIView):
    """
    get: Menampilkan daftar mata pelajaran (Super Admin/ Staf Kurikulum).
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Staf Kurikulum'],
    }

    queryset = MataPelajaran.objects.all()
    serializer_class = MataPelajaranSerializer


class KategoriTataTertibListView(generics.ListAPIView):
    """
    get: Menampilkan daftar mata pelajaran (Super Admin/ Staf Kurikulum).
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Staf Kurikulum'],
    }

    queryset = KategoriTataTertib.objects.all()
    serializer_class = KategoriTataTertibSerializer


class JadwalPekanEfektifSemesterListView(generics.ListCreateAPIView):
    """
    get: Menampilkan daftar pekan efektif per semester (Super Admin/ Staf Kurikulum).
    post: Menambah data pekan efektif per semester (Super Admin/ Staf Kurikulum).
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Staf Kurikulum'],
        'POST': ['Staf Kurikulum'],
    }

    queryset = JadwalPekanEfektifSemester.objects.all()
    serializer_class = JadwalPekanEfektifSemesterSerializer


class JadwalPekanEfektifSemesterDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    get: Menampilkan pekan efektif per semester (Super Admin/ Staf Kurikulum).
    put: Mengubah semua atribut pekan efektif per semester (Super Admin/ Staf Kurikulum).
    patch: Mengubah beberapa atribut pekan efektif per semester (Super Admin/ Staf Kurikulum).
    delete: Menghapus pekan efektif per semester (Super Admin/ Staf Kurikulum).
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Staf Kurikulum'],
        'PUT': ['Staf Kurikulum'],
        'PATCH': ['Staf Kurikulum'],
        'DELETE': ['Staf Kurikulum'],
    }

    queryset = JadwalPekanEfektifSemester.objects.all()
    serializer_class = JadwalPekanEfektifSemesterSerializer


class JadwalPekanTidakEfektifListView(generics.ListCreateAPIView):
    """
    get: Menampilkan daftar pekan tidak efektif (Super Admin/ Staf Kurikulum).
    post: Menambah data pekan tidak efektif (Super Admin/ Staf Kurikulum).
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Staf Kurikulum'],
        'POST': ['Staf Kurikulum'],
    }

    queryset = JadwalPekanTidakEfektif.objects.all()
    serializer_class = JadwalPekanTidakEfektifSerializer


class JadwalPekanTidakEfektifDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    get: Menampilkan pekan tidak efektif (Super Admin/ Staf Kurikulum).
    put: Mengubah semua atribut pekan tidak efektif (Super Admin/ Staf Kurikulum).
    patch: Mengubah beberapa atribut pekan tidak efektif (Super Admin/ Staf Kurikulum).
    delete: Menghapus pekan tidak efektif (Super Admin/ Staf Kurikulum).
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Staf Kurikulum'],
        'PUT': ['Staf Kurikulum'],
        'PATCH': ['Staf Kurikulum'],
        'DELETE': ['Staf Kurikulum'],
    }

    queryset = JadwalPekanTidakEfektif.objects.all()
    serializer_class = JadwalPekanTidakEfektifSerializer


class KelasSiswaListView(generics.ListAPIView):
    """
    get: Menampilkan daftar kelas siswa (Super Admin/ Staf Kurikulum).
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Staf Kurikulum'],
    }

    queryset = KelasSiswa.objects.all()
    serializer_class = KelasSiswaSerializer
    filterset_fields = ('NIS', 'KELAS')
    search_fields = ('NIS__NIS', 'NIS__NAMA', 'KELAS__KELAS__KODE_KELAS')
