from .models import *
from .serializers import *
from .doc_schema import *
from rest_framework.parsers import MultiPartParser
from .models import KTSP
from .models import SilabusRPB

from rest_framework import generics

from adistetsa.permissions import HasGroupPermissionAny, IsSuperAdmin

# Create your views here. 
class KTSPListView(generics.ListCreateAPIView):
    """
    get: Menampilkan daftar KTSP.
    post: Menambahkan data KTSP (Super Admin/ Staf Kurikulum).
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Staf Kurikulum'],
        'POST': ['Staf Kurikulum'],
    }
    parser_classes= (MultiPartParser,)

    queryset = KTSP.objects.all()
    serializer_class = KTSPSerializer

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class KTSPDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    get: Menampilkan data KTSP.
    put: Mengubah atribut keseluruhan data KTSP.
    patch: Mengubah beberapa atribut data KTSP.
    delete: Menghapus data KTSP.
    """
    permission_classes = [HasGroupPermissionAny]
    required_groups = {
        'GET': ['Staf Kurikulum'],
        'PUT': ['Staf Kurikulum'],
        'PATCH': ['Staf Kurikulum'],
        'DELETE': ['Staf Kurikulum'],
    }
    parser_classes= (MultiPartParser,)

    queryset = KTSP.objects.all()
    serializer_class = KTSPSerializer


class SilabusRPBListView(generics.ListCreateAPIView):
    """
    get: Menampilkan daftar Silabus RPB.
    post: Menambahkan data Silabus RPB (Super Admin/ Staf Kurikulum).
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Staf Kurikulum'],
        'POST': ['Staf Kurikulum'],
    }
    parser_classes= (MultiPartParser,)

    queryset = SilabusRPB.objects.all()
    serializer_class = SilabusRPBSerializer

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class SilabusRPBDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    get: Menampilkan data Silabus RPB.
    put: Mengubah atribut keseluruhan data Silabus RPB.
    patch: Mengubah beberapa atribut data Silabus RPB.
    delete: Menghapus data Silabus RPB.
    """
    permission_classes = [HasGroupPermissionAny]
    required_groups = {
        'GET': ['Staf Kurikulum'],
        'PUT': ['Staf Kurikulum'],
        'PATCH': ['Staf Kurikulum'],
        'DELETE': ['Staf Kurikulum'],
    }
    parser_classes= (MultiPartParser,)

    queryset = SilabusRPB.objects.all()
    serializer_class = SilabusRPBSerializer