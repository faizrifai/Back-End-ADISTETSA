from .models import TahunAjaran, DataSemester, Kelas, MataPelajaran
from .filter_serializers import *

from rest_framework import generics
from rest_framework.parsers import MultiPartParser

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
    parser_classes= (MultiPartParser,)

    queryset = DataSemester.objects.all()
    serializer_class = SemesterSerializer


class TahunAjaranListView(generics.ListAPIView):
    """
    get: Menampilkan daftar tahun ajaran (Super Admin/ Staf Kurikulum).
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Staf Kurikulum'],
    }
    parser_classes= (MultiPartParser,)

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
    parser_classes= (MultiPartParser,)

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
    parser_classes= (MultiPartParser,)

    queryset = MataPelajaran.objects.all()
    serializer_class = MataPelajaranSerializer