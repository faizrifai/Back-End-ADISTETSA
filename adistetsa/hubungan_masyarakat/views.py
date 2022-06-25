from .filters import BukuTamuFilter
from kustom_autentikasi.models import *
from .models import *
from .serializers import *

from rest_framework.reverse import reverse
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from utility.permissions import HasGroupPermissionAny, IsSuperAdmin

# Create model
class LogUKSModel:
    def __init__(self, id, nama, jenis_ptk, tanggal, detail_url):
        self.ID = id
        self.NAMA = nama
        self.JENIS_PTK = jenis_ptk
        self.TANGGAL = tanggal
        self.DETAIL_URL = detail_url

class BukuTamuModel:
    def __init__(self, id, nama, instansi_asal, alamat, no_hp, hari, tanggal, jam, keperluan):
        self.ID = id
        self.NAMA = nama
        self.INSTANSI_ASAL = instansi_asal
        self.ALAMAT = alamat
        self.NO_HP = no_hp
        self.HARI = hari
        self.TANGGAL = tanggal
        self.JAM = jam
        self.KEPERLUAN = keperluan

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
        qs_log_karyawan = LogUKSKaryawan.objects.all()

        qs_combined = []
        query_params = self.request.query_params

        for data in qs_log_siswa:
            new_data = LogUKSModel(
                id = data.ID,
                nama = str(data.NAMA),
                jenis_ptk = data.JENIS_PTK,
                tanggal = data.TANGGAL,
                detail_url = reverse('detail_log_uks_siswa', kwargs={'pk': data.ID})
            )
            qs_combined.append(new_data)

        for data in qs_log_tendik:
            new_data = LogUKSModel(
                id = data.ID,
                nama = str(data.NAMA),
                jenis_ptk = data.JENIS_PTK,
                tanggal = data.TANGGAL,
                detail_url = reverse('detail_log_uks_tendik', kwargs={'pk': data.ID})
            )
            qs_combined.append(new_data)

        for data in qs_log_karyawan:
            new_data = LogUKSModel(
                id = data.ID,
                nama = str(data.NAMA),
                jenis_ptk = data.JENIS_PTK,
                tanggal = data.TANGGAL,
                detail_url = reverse('detail_log_uks_karyawan', kwargs={'pk': data.ID})
            )
            qs_combined.append(new_data)
        
        if query_params.get('TANGGAL') and not query_params.get('NAMA'):
            param = query_params.get('TANGGAL')
            if param == '1': # Terbaru
                qs_combined.sort(key=lambda x: x.TANGGAL, reverse=True)
            elif param == '2': # Terlama
                qs_combined.sort(key=lambda x: x.TANGGAL)

        elif query_params.get('NAMA') and not query_params.get('TANGGAL'):
            param = query_params.get('NAMA')
            if param == '1': # Z - A
                qs_combined.sort(key=lambda x: x.NAMA, reverse=True)
            elif param == '2': # A - Z
                qs_combined.sort(key=lambda x: x.NAMA)

        elif query_params.get('NAMA') and query_params.get('TANGGAL'):
            param_nama = query_params.get('NAMA')
            param_tanggal = query_params.get('TANGGAL')
            reverse_nama = param_nama == '1'
            reverse_tanggal = param_tanggal == '1'

            qs_combined.sort(key=lambda x: x.NAMA, reverse=reverse_nama)
            qs_combined.sort(key=lambda x: x.TANGGAL, reverse=reverse_tanggal)

        else:
            pass

        if query_params.get('JENIS_PTK'):
            qs_combined = filter(lambda x: x.JENIS_PTK == query_params.get('JENIS_PTK'), qs_combined)

        if query_params.get('search'):
            # cannot search if filter exists
            # if query_params.get('TANGGAL') or query_params.get('NAMA') or query_params.get('JENIS_PTK'):
            #     pass
            # else:
            # qs_combined = filter(lambda x: x.NAMA.lower().startswith(query_params.get('search').lower()), qs_combined)
            qs_combined = filter(lambda x: query_params.get('search').lower() in x.NAMA.lower(), qs_combined)

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

class LogUKSDetailKaryawanView(generics.RetrieveAPIView):
    """
    get: Menampilkan detail log UKS (Staf Humas).
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Staf Humas'],
    }

    serializer_class = LogUKSDetailKaryawanSerializer
    queryset = LogUKSKaryawan.objects.all()

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

class TambahLogUKSKaryawanView(generics.CreateAPIView):
    """
    post: Menambahkan log UKS Karyawan (Staf Humas).
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'POST': ['Staf Humas'],
    }

    serializer_class = TambahLogUKSKaryawanSerializer
    queryset = LogUKSKaryawan.objects.all()

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

    def get_serializer_class(self):
        if self.request.method == "GET":
            return BukuTamuListSerializer

        elif self.request.method == "POST":
            return BukuTamuPostSerializer
    
    def list(self, request, *args, **kwargs):
        qs = BukuTamu.objects.all()

        qs_combined = []
        query_params = self.request.query_params

        for data in qs:
            new_data = BukuTamuModel(
                id = data.ID,
                nama = data.NAMA,
                instansi_asal = data.INSTANSI_ASAL,
                alamat = data.ALAMAT,
                no_hp = data.NO_HP,
                hari = data.HARI,
                tanggal = data.TANGGAL,
                jam = data.JAM,
                keperluan = data.KEPERLUAN
            )
            qs_combined.append(new_data)
        
        if query_params.get('TANGGAL') and not query_params.get('NAMA'):
            param = query_params.get('TANGGAL')
            if param == '1': # Terbaru
                qs_combined.sort(key=lambda x: x.TANGGAL, reverse=True)
            elif param == '2': # Terlama
                qs_combined.sort(key=lambda x: x.TANGGAL)

        elif query_params.get('NAMA') and not query_params.get('TANGGAL'):
            param = query_params.get('NAMA')
            if param == '1': # Z - A
                qs_combined.sort(key=lambda x: x.NAMA, reverse=True)
            elif param == '2': # A - Z
                qs_combined.sort(key=lambda x: x.NAMA)

        elif query_params.get('NAMA') and query_params.get('TANGGAL'):
            param_nama = query_params.get('NAMA')
            param_tanggal = query_params.get('TANGGAL')
            reverse_nama = param_nama == '1'
            reverse_tanggal = param_tanggal == '1'

            qs_combined.sort(key=lambda x: x.NAMA, reverse=reverse_nama)
            qs_combined.sort(key=lambda x: x.TANGGAL, reverse=reverse_tanggal)

        else:
            pass

        if query_params.get('search'):
            qs_combined = filter(lambda x: x.NAMA.lower().startswith(query_params.get('search').lower()), qs_combined)

        serializer = BukuTamuListSerializer(qs_combined, many=True)

        new_data = {}
        new_data['results'] = list(serializer.data)

        return Response(new_data)

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

class DataSiswaListView(generics.ListAPIView):
    """
    get: Menampilkan daftar siswa (Staf Humas).
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Staf Humas'],
    }

    serializer_class = DataSiswaSerializer
    queryset = KelasSiswa.objects.all()
    
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class DataGuruListView(generics.ListAPIView):
    """
    get: Menampilkan daftar guru (Staf Humas).
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Staf Humas'],
    }

    serializer_class = DataGuruTendikSerializer
    queryset = DataGuru.objects.all()
    
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class DataKaryawanListView(generics.ListAPIView):
    """
    get: Menampilkan daftar karyawan (Staf Humas).
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Staf Humas'],
    }

    serializer_class = DataKaryawanSerializer
    queryset = DataKaryawan.objects.all()
    
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)