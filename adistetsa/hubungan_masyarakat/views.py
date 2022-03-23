from .filters import BukuTamuFilter
from kustom_autentikasi.models import *
from .models import *
from .serializers import *

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from adistetsa.permissions import HasGroupPermissionAny, IsSuperAdmin

# Create model
class LogUKSModel:
    def __init__(self, id, nama, jenis_ptk, tanggal, detail_url):
        self.ID = id
        self.NAMA = nama
        self.JENIS_PTK = jenis_ptk
        self.TANGGAL = tanggal
        self.DETAIL_URL = detail_url

# Create your views here. 
class LogUKSListView(APIView):
    """
    get: Menampilkan daftar log UKS (Staf Humas).
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Staf Humas'],
    }

    def get(self, request, *args, **kwargs):
        """
        Menampilkan daftar log UKS (Staf Humas).
        """

        qs_log_siswa = LogUKSSiswa.objects.all()
        qs_log_tendik = LogUKSTendik.objects.all()

        qs_combined = []
        query_params = self.request.query_params

        for data in qs_log_siswa:
            new_data = LogUKSModel(
                id = data.ID,
                nama = data.NAMA,
                jenis_ptk = data.JENIS_PTK,
                tanggal = data.TANGGAL,
                detail_url = reverse('detail_log_uks_siswa', kwargs={'pk': data.ID})
            )
            qs_combined.append(new_data)

        for data in qs_log_tendik:
            new_data = LogUKSModel(
                id = data.ID,
                nama = data.NAMA,
                jenis_ptk = data.JENIS_PTK,
                tanggal = data.TANGGAL,
                detail_url = reverse('detail_log_uks_tendik', kwargs={'pk': data.ID})
            )
            qs_combined.append(new_data)
        
        if query_params.get('TANGGAL'):
            param = query_params.get('TANGGAL')
            if param == '1': # Terbaru
                qs_combined.sort(key=lambda x: x.TANGGAL, reverse=True)
            elif param == '2': # Terlama
                qs_combined.sort(key=lambda x: x.TANGGAL)

        if query_params.get('NAMA'):
            param = query_params.get('NAMA')
            if param == '1': # Z - A
                qs_combined.sort(key=lambda x: x.NAMA, reverse=True)
            elif param == '2': # A - Z
                qs_combined.sort(key=lambda x: x.NAMA)

        if query_params.get('JENIS_PTK'):
            qs_combined = filter(lambda x: x.JENIS_PTK == query_params.get('JENIS_PTK'), qs_combined)

        if query_params.get('search'):
            # cannot search if filter exists
            if query_params.get('TANGGAL') or query_params.get('NAMA') or query_params.get('JENIS_PTK'):
                pass
            else:
                qs_combined = filter(lambda x: x.NAMA.lower().startswith(query_params.get('search').lower()), qs_combined)

        serializer = LogUKSListSerializer(qs_combined, many=True)

        return Response(serializer.data)

class LogUKSDetailSiswaView(generics.RetrieveAPIView):
    """
    get: Menampilkan detail log UKS (Staf Humas).
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Staf Humas'],
    }

    serializer_class = LogUKSDetailSiswaSerializer
    queryset = LogUKSSiswa.objects.all()

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

class LogUKSDetailTendikView(generics.RetrieveAPIView):
    """
    get: Menampilkan detail log UKS (Staf Humas).
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Staf Humas'],
    }

    serializer_class = LogUKSDetailTendikSerializer
    queryset = LogUKSTendik.objects.all()

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

class TambahLogUKSSiswaView(generics.CreateAPIView):
    """
    post: Menambahkan log UKS Siswa (Staf Humas).
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'POST': ['Staf Humas'],
    }

    serializer_class = TambahLogUKSSiswaSerializer
    queryset = LogUKSSiswa.objects.all()

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

class TambahLogUKSTendikView(generics.CreateAPIView):
    """
    post: Menambahkan log UKS Tendik (Staf Humas).
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'POST': ['Staf Humas'],
    }

    serializer_class = TambahLogUKSTendikSerializer
    queryset = LogUKSTendik.objects.all()

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

class BukuTamuListView(generics.ListCreateAPIView):
    """
    get: Menampilkan daftar tamu (Staf Humas).
    post: Menambahkan data tamu (Staf Humas).
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Staf Humas'],
        'POST': ['Staf Humas'],
    }

    serializer_class = BukuTamuListSerializer
    queryset = BukuTamu.objects.all()
    search_fields = ('NAMA', )
    filterset_class = BukuTamuFilter
    
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

class BukuTamuDetailView(generics.RetrieveAPIView):
    """
    get: Menampilkan detail tamu (Staf Humas).
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Staf Humas'],
    }

    serializer_class = BukuTamuListSerializer
    queryset = BukuTamu.objects.all()
    
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)