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
