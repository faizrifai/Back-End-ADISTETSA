from .models import *
from .serializers import *
from .doc_filters import *
from kustom_autentikasi.models import DataGuruUser

from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema

from adistetsa.permissions import HasGroupPermissionAny, IsSuperAdmin, is_in_group

# Create your views here.

class DataSiswaListView(generics.ListCreateAPIView):
    """
    get: Menampilkan seluruh daftar siswa (Super Admin/ Staf PPDB/ Staf Kurikulum).
    post: Menambahkan data siswa (Super Admin/ Staf PPDB/ Staf Kurikulum).
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'get': ['Staf PPDB', 'Staf Kurikulum'],
        'post': ['Staf PPDB', 'Staf Kurikulum'],
    }
    queryset = DataSiswa.objects.all()
    serializer_class = DataSiswaSerializer


class DataSiswaDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    get: Menampilkan data salah satu siswa (Super Admin/ Staf PPDB/ Staf Kurikulum).
    put: Mengganti seluruh atribut data siswa (Super Admin/ Staf PPDB/ Staf Kurikulum).
    patch: Mengganti beberapa atribut data siswa (Super Admin/ Staf PPDB/ Staf Kurikulum).
    delete: Menghapus data siswa (Super Admin/ Staf PPDB/ Staf Kurikulum)
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'get': ['Staf PPDB', 'Staf Kurikulum'],
        'post': ['Staf PPDB', 'Staf Kurikulum'],
    }
    queryset = DataSiswa.objects.all()
    serializer_class = DataSiswaSerializer
    lookup_url_kwarg = 'siswa_id'


class DataOrangTuaListView(generics.ListCreateAPIView):
    """
    get: Menampilkan seluruh daftar orang tua (Super Admin/ Staf PPDB).
    post: Menambahkan data orang tua (Super Admin/ Staf PPDB).
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'get': ['Staf PPDB'],
        'post': ['Staf PPDB'],
    }
    queryset = DataOrangTua.objects.all()
    serializer_class = DataOrangTuaSerializer


class DataOrangTuaDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    get: Menampilkan data salah satu orang tua (Super Admin/ Staf PPDB).
    put: Mengganti seluruh atribut data orang tua (Super Admin/ Staf PPDB).
    patch: Mengganti beberapa atribut data orang tua (Super Admin/ Staf PPDB).
    delete: Menghapus data orang tua (Super Admin/ Staf PPDB)
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'get': ['Staf PPDB'],
        'post': ['Staf PPDB'],
    }
    queryset = DataOrangTua.objects.all()
    serializer_class = DataOrangTuaSerializer
    lookup_url_kwarg = 'orangtua_id'


class DataGuruListView(generics.ListCreateAPIView):
    """
    get: Menampilkan seluruh daftar guru (Super Admin/ Staf PPDB).
    post: Menambahkan data guru (Super Admin/ Staf PPDB).
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'get': ['Staf PPDB'],
        'post': ['Staf PPDB'],
    }
    queryset = DataGuru.objects.all()
    serializer_class = DataGuruSerializer


class DataGuruDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    get: Menampilkan data salah satu guru (Super Admin/ Staf PPDB).
    put: Mengganti seluruh atribut data guru (Super Admin/ Staf PPDB).
    patch: Mengganti beberapa atribut data guru (Super Admin/ Staf PPDB).
    delete: Menghapus data guru (Super Admin/ Staf PPDB)
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'get': ['Staf PPDB'],
        'post': ['Staf PPDB'],
    }
    queryset = DataGuru.objects.all()
    serializer_class = DataGuruSerializer
    lookup_url_kwarg = 'guru_id'


class DataKaryawanListView(generics.ListCreateAPIView):
    """
    get: Menampilkan seluruh daftar karyawan (Super Admin/ Staf PPDB).
    post: Menambahkan data karyawan (Super Admin/ Staf PPDB).
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'get': ['Staf PPDB'],
        'post': ['Staf PPDB'],
    }
    queryset = DataKaryawan.objects.all()
    serializer_class = DataKaryawanSerializer


class DataKaryawanDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    get: Menampilkan data salah satu karyawan (Super Admin/ Staf PPDB).
    put: Mengganti seluruh atribut data karyawan (Super Admin/ Staf PPDB).
    patch: Mengganti beberapa atribut data karyawan (Super Admin/ Staf PPDB).
    delete: Menghapus data karyawan (Super Admin/ Staf PPDB)
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'get': ['Staf PPDB'],
        'post': ['Staf PPDB'],
    }
    queryset = DataKaryawan.objects.all()
    serializer_class = DataKaryawanSerializer
    lookup_url_kwarg = 'karyawan_id'


class DataKompetensiGuruListView(generics.ListCreateAPIView):
    """
    get: Menampilkan daftar kompetensi guru (Guru).
    post: Menambahkan data kompetensi guru (Guru).
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Guru'],
        'POST': ['Guru'],
    }
    serializer_class = DataKompetensiGuruSerializer

    def get_data_guru(self):
        user = self.request.user
        data_guru = DataGuruUser.objects.get(USER=user).DATA_GURU

        return data_guru

    def get_queryset(self):
        data_guru = self.get_data_guru()

        return DataKompetensiGuru.objects.filter(OWNER=data_guru.ID)

    def perform_create(self, serializer):
        serializer.validated_data['OWNER_id'] = self.get_data_guru().ID
        return super(DataKompetensiGuruListView, self).perform_create(serializer)


class DataKompetensiGuruDetailView(APIView):
    """
    get: Menampilkan daftar kompetensi guru (Guru).
    put: Mengubah atribut keseluruhan data kompetensi guru (Guru).
    patch: Mengubah beberapa atribut data kompetensi guru (Guru).
    delete: Menghapus data kompetensi guru (Guru).
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Guru'],
        'PUT': ['Guru'],
        'PATCH': ['Guru'],
        'DELETE': ['Guru'],
    }
    serializer_class = DataKompetensiGuruSerializer

    def get_queryset(self, pk):
        user = self.request.user
        data_guru = DataGuruUser.objects.get(USER=user).DATA_GURU

        return DataKompetensiGuru.objects.get(pk=pk, OWNER=data_guru.ID)

    def get(self, request, pk, *args, **kwargs):
        queryset = self.get_queryset(pk)
        serializer = self.serializer_class
        response = serializer(queryset).data

        return Response(response)

    def put(self, request, pk, format=None):
        queryset = self.get_queryset(pk)
        serializer = self.serializer_class(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        queryset = self.get_queryset(pk)
        serializer = self.serializer_class(queryset, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        queryset = self.get_queryset(pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)