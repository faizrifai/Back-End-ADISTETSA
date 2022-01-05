from .models import *
from .serializers import *
from .doc_schema import *
from kustom_autentikasi.models import DataGuruUser, DataKaryawanUser

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
        'GET': ['Staf PPDB', 'Staf Kurikulum', 'Guru'],
        'POST': ['Staf PPDB', 'Staf Kurikulum', 'Guru'],
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
        'GET': ['Staf PPDB', 'Staf Kurikulum', 'Guru'],
        'PUT': ['Staf PPDB', 'Staf Kurikulum', 'Guru'],
        'PATCH': ['Staf PPDB', 'Staf Kurikulum', 'Guru'],
        'DELETE': ['Staf PPDB', 'Staf Kurikulum', 'Guru'],
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
        'GET': ['Staf PPDB'],
        'POST': ['Staf PPDB'],
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
        'GET': ['Staf PPDB'],
        'PUT': ['Staf PPDB'],
        'PATCH': ['Staf PPDB'],
        'DELETE': ['Staf PPDB'],
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
        'GET': ['Staf PPDB'],
        'POST': ['Staf PPDB'],
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
        'GET': ['Staf PPDB'],
        'PUT': ['Staf PPDB'],
        'PATCH': ['Staf PPDB'],
        'DELETE': ['Staf PPDB'],
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
        'GET': ['Staf PPDB'],
        'POST': ['Staf PPDB'],
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
        'GET': ['Staf PPDB'],
        'PUT': ['Staf PPDB'],
        'PATCH': ['Staf PPDB'],
        'DELETE': ['Staf PPDB'],
    }
    queryset = DataKaryawan.objects.all()
    serializer_class = DataKaryawanSerializer
    lookup_url_kwarg = 'karyawan_id'


class DataKompetensiGuruListView(generics.ListCreateAPIView):
    """
    get: Menampilkan daftar kompetensi guru (Guru).
    post: Menambahkan data kompetensi guru (Guru).
    """
    permission_classes = [HasGroupPermissionAny]
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
    permission_classes = [HasGroupPermissionAny]
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

        return DataKompetensiGuru.objects.get(pk=self.kwargs['pk'], OWNER=data_guru.ID)

    def get(self, request, pk, *args, **kwargs):
        queryset = self.get_queryset(pk)
        serializer = self.serializer_class
        response = serializer(queryset).data

        return Response(response)

    @swagger_auto_schema(
        request_body=schema_datakompetensiguru,
        responses={'200': 'Berhasil mengupdate data kompetensi guru', '400': 'Bad Request',}
    )
    def put(self, request, pk, format=None):
        queryset = self.get_queryset(pk)
        serializer = self.serializer_class(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        request_body=schema_datakompetensiguru,
        responses={'200': 'Berhasil mengupdate data kompetensi guru', '400': 'Bad Request',}
    )
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


class DataKompetensiKaryawanListView(generics.ListCreateAPIView):
    """
    get: Menampilkan daftar kompetensi karyawan (Karyawan).
    post: Menambahkan data kompetensi karyawan (Karyawan).
    """
    permission_classes = [HasGroupPermissionAny]
    required_groups = {
        'GET': ['Karyawan'],
        'POST': ['Karyawan'],
    }
    serializer_class = DataKompetensiKaryawanSerializer

    def get_data_karyawan(self):
        user = self.request.user
        data_karyawan = DataKaryawanUser.objects.get(USER=user).DATA_KARYAWAN

        return data_karyawan

    def get_queryset(self):
        data_karyawan = self.get_data_karyawan()

        return DataKompetensiKaryawan.objects.filter(OWNER=data_karyawan.ID)

    def perform_create(self, serializer):
        serializer.validated_data['OWNER_id'] = self.get_data_karyawan().ID

        return super(DataKompetensiKaryawanListView, self).perform_create(serializer)


class DataKompetensiKaryawanDetailView(APIView):
    """
    get: Menampilkan daftar kompetensi karyawan (Karyawan).
    put: Mengubah atribut keseluruhan data kompetensi karyawan (Karyawan).
    patch: Mengubah beberapa atribut data kompetensi karyawan (Karyawan).
    delete: Menghapus data kompetensi karyawan (Karyawan).
    """
    permission_classes = [HasGroupPermissionAny]
    required_groups = {
        'GET': ['Karyawan'],
        'PUT': ['Karyawan'],
        'PATCH': ['Karyawan'],
        'DELETE': ['Karyawan'],
    }
    serializer_class = DataKompetensiKaryawanSerializer

    def get_queryset(self, pk):
        user = self.request.user
        data_karyawan = DataKaryawanUser.objects.get(USER=user).DATA_KARYAWAN

        return DataKompetensiKaryawan.objects.get(pk=self.kwargs['pk'], OWNER=data_karyawan.ID)

    def get(self, request, pk, *args, **kwargs):
        queryset = self.get_queryset(pk)
        serializer = self.serializer_class
        response = serializer(queryset).data

        return Response(response)

    @swagger_auto_schema(
        request_body=schema_datakompetensikaryawan,
        responses={'200': 'Berhasil mengupdate data kompetensi karyawan', '400': 'Bad Request',}
    )
    def put(self, request, pk, format=None):
        queryset = self.get_queryset(pk)
        serializer = self.serializer_class(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        request_body=schema_datakompetensikaryawan,
        responses={'200': 'Berhasil mengupdate data kompetensi karyawan', '400': 'Bad Request',}
    )
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
        

class DataAnakGuruListView(generics.ListCreateAPIView):
    """
    get: Menampilkan daftar anak guru (Guru).
    post: Menambahkan data anak guru (Guru).
    """
    permission_classes = [HasGroupPermissionAny]
    required_groups = {
        'GET': ['Guru'],
        'POST': ['Guru'],
    }
    serializer_class = DataAnakGuruSerializer

    def get_data_guru(self):
        user = self.request.user
        data_guru = DataGuruUser.objects.get(USER=user).DATA_GURU

        return data_guru

    def get_queryset(self):
        data_guru = self.get_data_guru()

        return DataAnakGuru.objects.filter(OWNER=data_guru.ID)

    def perform_create(self, serializer):
        serializer.validated_data['OWNER_id'] = self.get_data_guru().ID

        return super(DataAnakGuruListView, self).perform_create(serializer)


class DataAnakGuruDetailView(APIView):
    """
    get: Menampilkan daftar anak guru (Guru).
    put: Mengubah atribut keseluruhan data anak guru (Guru).
    patch: Mengubah beberapa atribut data anak guru (Guru).
    delete: Menghapus data anak guru (Guru).
    """
    permission_classes = [HasGroupPermissionAny]
    required_groups = {
        'GET': ['Guru'],
        'PUT': ['Guru'],
        'PATCH': ['Guru'],
        'DELETE': ['Guru'],
    }
    serializer_class = DataAnakGuruSerializer

    def get_queryset(self, pk):
        user = self.request.user
        data_guru = DataGuruUser.objects.get(USER=user).DATA_GURU

        return DataAnakGuru.objects.get(pk=self.kwargs['pk'], OWNER=data_guru.ID)

    def get(self, request, pk, *args, **kwargs):
        queryset = self.get_queryset(pk)
        serializer = self.serializer_class
        response = serializer(queryset).data

        return Response(response)

    @swagger_auto_schema(
        request_body=schema_dataanakguru,
        responses={'200': 'Berhasil mengupdate data anak guru', '400': 'Bad Request',}
    )
    def put(self, request, pk, format=None):
        queryset = self.get_queryset(pk)
        serializer = self.serializer_class(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        request_body=schema_dataanakguru,
        responses={'200': 'Berhasil mengupdate data anak guru', '400': 'Bad Request',}
    )
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


class DataBeasiswaGuruListView(generics.ListCreateAPIView):
    """
    get: Menampilkan daftar beasiswa guru (Guru).
    post: Menambahkan data beasiswa guru (Guru).
    """
    permission_classes = [HasGroupPermissionAny]
    required_groups = {
        'GET': ['Guru'],
        'POST': ['Guru'],
    }
    serializer_class = DataBeasiswaGuruSerializer

    def get_data_guru(self):
        user = self.request.user
        data_guru = DataGuruUser.objects.get(USER=user).DATA_GURU

        return data_guru

    def get_queryset(self):
        data_guru = self.get_data_guru()

        return DataBeasiswaGuru.objects.filter(OWNER=data_guru.ID)

    def perform_create(self, serializer):
        serializer.validated_data['OWNER_id'] = self.get_data_guru().ID

        return super(DataBeasiswaGuruListView, self).perform_create(serializer)


class DataBeasiswaGuruDetailView(APIView):
    """
    get: Menampilkan daftar beasiswa guru (Guru).
    put: Mengubah atribut keseluruhan data beasiswa guru (Guru).
    patch: Mengubah beberapa atribut data beasiswa guru (Guru).
    delete: Menghapus data beasiswa guru (Guru).
    """
    permission_classes = [HasGroupPermissionAny]
    required_groups = {
        'GET': ['Guru'],
        'PUT': ['Guru'],
        'PATCH': ['Guru'],
        'DELETE': ['Guru'],
    }
    serializer_class = DataBeasiswaGuruSerializer

    def get_queryset(self, pk):
        user = self.request.user
        data_guru = DataGuruUser.objects.get(USER=user).DATA_GURU

        return DataBeasiswaGuru.objects.get(pk=self.kwargs['pk'], OWNER=data_guru.ID)

    def get(self, request, pk, *args, **kwargs):
        queryset = self.get_queryset(pk)
        serializer = self.serializer_class
        response = serializer(queryset).data

        return Response(response)

    @swagger_auto_schema(
        request_body=schema_databeasiswaguru,
        responses={'200': 'Berhasil mengupdate data beasiswa guru', '400': 'Bad Request',}
    )
    def put(self, request, pk, format=None):
        queryset = self.get_queryset(pk)
        serializer = self.serializer_class(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        request_body=schema_databeasiswaguru,
        responses={'200': 'Berhasil mengupdate data beasiswa guru', '400': 'Bad Request',}
    )
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

class DataBukuGuruListView(generics.ListCreateAPIView):
        """
        get: Menampilkan daftar buku guru (Guru).
        post: Menambahkan data buku guru (Guru).
        """
        permission_classes = [HasGroupPermissionAny]
        required_groups = {
            'GET': ['Guru'],
            'POST': ['Guru'],
        }
        serializer_class = DataBukuGuruSerializer

        def get_data_guru(self):
            user = self.request.user
            data_guru = DataGuruUser.objects.get(USER=user).DATA_GURU

            return data_guru

        def get_queryset(self):
            data_guru = self.get_data_guru()

            return DataBukuGuru.objects.filter(OWNER=data_guru.ID)

        def perform_create(self, serializer):
            serializer.validated_data['OWNER_id'] = self.get_data_guru().ID

            return super(DataBukuGuruListView, self).perform_create(serializer)


class DataBukuGuruDetailView(APIView):
        """
        get: Menampilkan daftar buku guru (Guru).
        put: Mengubah atribut keseluruhan data buku guru (Guru).
        patch: Mengubah beberapa atribut data buku guru (Guru).
        delete: Menghapus data buku guru (Guru).
        """
        permission_classes = [HasGroupPermissionAny]
        required_groups = {
            'GET': ['Guru'],
            'PUT': ['Guru'],
            'PATCH': ['Guru'],
            'DELETE': ['Guru'],
        }
        serializer_class = DataBukuGuruSerializer

        def get_queryset(self, pk):
            user = self.request.user
            data_guru = DataGuruUser.objects.get(USER=user).DATA_GURU

            return DataBukuGuru.objects.get(pk=self.kwargs['pk'], OWNER=data_guru.ID)

        def get(self, request, pk, *args, **kwargs):
            queryset = self.get_queryset(pk)
            serializer = self.serializer_class
            response = serializer(queryset).data

            return Response(response)

        @swagger_auto_schema(
            request_body=schema_databukuguru,
            responses={'200': 'Berhasil mengupdate data buku guru', '400': 'Bad Request',}
        )
        def put(self, request, pk, format=None):
            queryset = self.get_queryset(pk)
            serializer = self.serializer_class(queryset, data=request.data)
            if serializer.is_valid():
                serializer.save()

                return Response(serializer.data)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        @swagger_auto_schema(
            request_body=schema_databukuguru,
            responses={'200': 'Berhasil mengupdate data buku guru', '400': 'Bad Request',}
        )
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

class DataDiklatGuruListView(generics.ListCreateAPIView):
        """
        get: Menampilkan daftar diklat guru (Guru).
        post: Menambahkan data diklat guru (Guru).
        """
        permission_classes = [HasGroupPermissionAny]
        required_groups = {
            'GET': ['Guru'],
            'POST': ['Guru'],
        }
        serializer_class = DataDiklatGuruSerializer

        def get_data_guru(self):
            user = self.request.user
            data_guru = DataGuruUser.objects.get(USER=user).DATA_GURU

            return data_guru

        def get_queryset(self):
            data_guru = self.get_data_guru()

            return DataDiklatGuru.objects.filter(OWNER=data_guru.ID)

        def perform_create(self, serializer):
            serializer.validated_data['OWNER_id'] = self.get_data_guru().ID

            return super(DataDiklatGuruListView, self).perform_create(serializer)


class DataDiklatGuruDetailView(APIView):
        """
        get: Menampilkan daftar diklat guru (Guru).
        put: Mengubah atribut keseluruhan data diklat guru (Guru).
        patch: Mengubah beberapa atribut data diklat guru (Guru).
        delete: Menghapus data diklat guru (Guru).
        """
        permission_classes = [HasGroupPermissionAny]
        required_groups = {
            'GET': ['Guru'],
            'PUT': ['Guru'],
            'PATCH': ['Guru'],
            'DELETE': ['Guru'],
        }
        serializer_class = DataDiklatGuruSerializer

        def get_queryset(self, pk):
            user = self.request.user
            data_guru = DataGuruUser.objects.get(USER=user).DATA_GURU

            return DataDiklatGuru.objects.get(pk=self.kwargs['pk'], OWNER=data_guru.ID)

        def get(self, request, pk, *args, **kwargs):
            queryset = self.get_queryset(pk)
            serializer = self.serializer_class
            response = serializer(queryset).data

            return Response(response)

        @swagger_auto_schema(
            request_body=schema_datadiklatguru,
            responses={'200': 'Berhasil mengupdate data diklat guru', '400': 'Bad Request',}
        )
        def put(self, request, pk, format=None):
            queryset = self.get_queryset(pk)
            serializer = self.serializer_class(queryset, data=request.data)
            if serializer.is_valid():
                serializer.save()

                return Response(serializer.data)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        @swagger_auto_schema(
            request_body=schema_datadiklatguru,
            responses={'200': 'Berhasil mengupdate data diklat guru', '400': 'Bad Request',}
        )
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



class DataKaryaTulisGuruListView(generics.ListCreateAPIView):
        """
        get: Menampilkan daftar karya tulis guru (Guru).
        post: Menambahkan data karya tulis guru (Guru).
        """
        permission_classes = [HasGroupPermissionAny]
        required_groups = {
            'GET': ['Guru'],
            'POST': ['Guru'],
        }
        serializer_class = DataKaryaTulisGuruSerializer

        def get_data_guru(self):
            user = self.request.user
            data_guru = DataGuruUser.objects.get(USER=user).DATA_GURU

            return data_guru

        def get_queryset(self):
            data_guru = self.get_data_guru()

            return DataKaryaTulisGuru.objects.filter(OWNER=data_guru.ID)

        def perform_create(self, serializer):
            serializer.validated_data['OWNER_id'] = self.get_data_guru().ID

            return super(DataKaryaTulisGuruListView, self).perform_create(serializer)


class DataKaryaTulisGuruDetailView(APIView):
        """
        get: Menampilkan daftar karya tulis guru (Guru).
        put: Mengubah atribut keseluruhan data karya tulis guru (Guru).
        patch: Mengubah beberapa atribut data karya tulis guru (Guru).
        delete: Menghapus data karya tulis guru (Guru).
        """
        permission_classes = [HasGroupPermissionAny]
        required_groups = {
            'GET': ['Guru'],
            'PUT': ['Guru'],
            'PATCH': ['Guru'],
            'DELETE': ['Guru'],
        }
        serializer_class = DataKaryaTulisGuruSerializer

        def get_queryset(self, pk):
            user = self.request.user
            data_guru = DataGuruUser.objects.get(USER=user).DATA_GURU

            return DataKaryaTulisGuru.objects.get(pk=self.kwargs['pk'], OWNER=data_guru.ID)

        def get(self, request, pk, *args, **kwargs):
            queryset = self.get_queryset(pk)
            serializer = self.serializer_class
            response = serializer(queryset).data

            return Response(response)

        @swagger_auto_schema(
            request_body=schema_datakaryatulisguru,
            responses={'200': 'Berhasil mengupdate data karyatulis guru', '400': 'Bad Request',}
        )
        def put(self, request, pk, format=None):
            queryset = self.get_queryset(pk)
            serializer = self.serializer_class(queryset, data=request.data)
            if serializer.is_valid():
                serializer.save()

                return Response(serializer.data)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        @swagger_auto_schema(
            request_body=schema_datakaryatulisguru,
            responses={'200': 'Berhasil mengupdate data karyatulis guru', '400': 'Bad Request',}
        )
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


class DataKaryaTulisGuruListView(generics.ListCreateAPIView):
        """
        get: Menampilkan daftar karya tulis guru (Guru).
        post: Menambahkan data karya tulis guru (Guru).
        """
        permission_classes = [HasGroupPermissionAny]
        required_groups = {
            'GET': ['Guru'],
            'POST': ['Guru'],
        }
        serializer_class = DataKaryaTulisGuruSerializer

        def get_data_guru(self):
            user = self.request.user
            data_guru = DataGuruUser.objects.get(USER=user).DATA_GURU

            return data_guru

        def get_queryset(self):
            data_guru = self.get_data_guru()

            return DataKaryaTulisGuru.objects.filter(OWNER=data_guru.ID)

        def perform_create(self, serializer):
            serializer.validated_data['OWNER_id'] = self.get_data_guru().ID

            return super(DataKaryaTulisGuruListView, self).perform_create(serializer)


class DataKaryaTulisGuruDetailView(APIView):
        """
        get: Menampilkan daftar karya tulis guru (Guru).
        put: Mengubah atribut keseluruhan data karya tulis guru (Guru).
        patch: Mengubah beberapa atribut data karya tulis guru (Guru).
        delete: Menghapus data karya tulis guru (Guru).
        """
        permission_classes = [HasGroupPermissionAny]
        required_groups = {
            'GET': ['Guru'],
            'PUT': ['Guru'],
            'PATCH': ['Guru'],
            'DELETE': ['Guru'],
        }
        serializer_class = DataKaryaTulisGuruSerializer

        def get_queryset(self, pk):
            user = self.request.user
            data_guru = DataGuruUser.objects.get(USER=user).DATA_GURU

            return DataKaryaTulisGuru.objects.get(pk=self.kwargs['pk'], OWNER=data_guru.ID)

        def get(self, request, pk, *args, **kwargs):
            queryset = self.get_queryset(pk)
            serializer = self.serializer_class
            response = serializer(queryset).data

            return Response(response)

        @swagger_auto_schema(
            request_body=schema_datakaryatulisguru,
            responses={'200': 'Berhasil mengupdate data karyatulis guru', '400': 'Bad Request',}
        )
        def put(self, request, pk, format=None):
            queryset = self.get_queryset(pk)
            serializer = self.serializer_class(queryset, data=request.data)
            if serializer.is_valid():
                serializer.save()

                return Response(serializer.data)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        @swagger_auto_schema(
            request_body=schema_datakaryatulisguru,
            responses={'200': 'Berhasil mengupdate data karyatulis guru', '400': 'Bad Request',}
        )
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

class DataKesejahteraanGuruListView(generics.ListCreateAPIView):
        """
        get: Menampilkan daftar karya tulis guru (Guru).
        post: Menambahkan data karya tulis guru (Guru).
        """
        permission_classes = [HasGroupPermissionAny]
        required_groups = {
            'GET': ['Guru'],
            'POST': ['Guru'],
        }
        serializer_class = DataKesejahteraanGuruSerializer

        def get_data_guru(self):
            user = self.request.user
            data_guru = DataGuruUser.objects.get(USER=user).DATA_GURU

            return data_guru

        def get_queryset(self):
            data_guru = self.get_data_guru()

            return DataKesejahteraanGuru.objects.filter(OWNER=data_guru.ID)

        def perform_create(self, serializer):
            serializer.validated_data['OWNER_id'] = self.get_data_guru().ID

            return super(DataKesejahteraanGuruListView, self).perform_create(serializer)


class DataKesejahteraanGuruDetailView(APIView):
        """
        get: Menampilkan daftar karya tulis guru (Guru).
        put: Mengubah atribut keseluruhan data karya tulis guru (Guru).
        patch: Mengubah beberapa atribut data karya tulis guru (Guru).
        delete: Menghapus data karya tulis guru (Guru).
        """
        permission_classes = [HasGroupPermissionAny]
        required_groups = {
            'GET': ['Guru'],
            'PUT': ['Guru'],
            'PATCH': ['Guru'],
            'DELETE': ['Guru'],
        }
        serializer_class = DataKesejahteraanGuruSerializer

        def get_queryset(self, pk):
            user = self.request.user
            data_guru = DataGuruUser.objects.get(USER=user).DATA_GURU

            return DataKesejahteraanGuru.objects.get(pk=self.kwargs['pk'], OWNER=data_guru.ID)

        def get(self, request, pk, *args, **kwargs):
            queryset = self.get_queryset(pk)
            serializer = self.serializer_class
            response = serializer(queryset).data

            return Response(response)

        @swagger_auto_schema(
            request_body=schema_datakesejahteraanguru,
            responses={'200': 'Berhasil mengupdate data kesejahteraan guru', '400': 'Bad Request',}
        )
        def put(self, request, pk, format=None):
            queryset = self.get_queryset(pk)
            serializer = self.serializer_class(queryset, data=request.data)
            if serializer.is_valid():
                serializer.save()

                return Response(serializer.data)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        @swagger_auto_schema(
            request_body=schema_datakesejahteraanguru,
            responses={'200': 'Berhasil mengupdate data kesejahteraan guru', '400': 'Bad Request',}
        )
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

class DataTunjanganGuruListView(generics.ListCreateAPIView):
        """
        get: Menampilkan daftar karya tulis guru (Guru).
        post: Menambahkan data karya tulis guru (Guru).
        """
        permission_classes = [HasGroupPermissionAny]
        required_groups = {
            'GET': ['Guru'],
            'POST': ['Guru'],
        }
        serializer_class = DataTunjanganGuruSerializer

        def get_data_guru(self):
            user = self.request.user
            data_guru = DataGuruUser.objects.get(USER=user).DATA_GURU

            return data_guru

        def get_queryset(self):
            data_guru = self.get_data_guru()

            return DataTunjanganGuru.objects.filter(OWNER=data_guru.ID)

        def perform_create(self, serializer):
            serializer.validated_data['OWNER_id'] = self.get_data_guru().ID

            return super(DataTunjanganGuruListView, self).perform_create(serializer)


class DataTunjanganGuruDetailView(APIView):
        """
        get: Menampilkan daftar karya tulis guru (Guru).
        put: Mengubah atribut keseluruhan data karya tulis guru (Guru).
        patch: Mengubah beberapa atribut data karya tulis guru (Guru).
        delete: Menghapus data karya tulis guru (Guru).
        """
        permission_classes = [HasGroupPermissionAny]
        required_groups = {
            'GET': ['Guru'],
            'PUT': ['Guru'],
            'PATCH': ['Guru'],
            'DELETE': ['Guru'],
        }
        serializer_class = DataTunjanganGuruSerializer

        def get_queryset(self, pk):
            user = self.request.user
            data_guru = DataGuruUser.objects.get(USER=user).DATA_GURU

            return DataTunjanganGuru.objects.get(pk=self.kwargs['pk'], OWNER=data_guru.ID)

        def get(self, request, pk, *args, **kwargs):
            queryset = self.get_queryset(pk)
            serializer = self.serializer_class
            response = serializer(queryset).data

            return Response(response)

        @swagger_auto_schema(
            request_body=schema_datatunjanganguru,
            responses={'200': 'Berhasil mengupdate data tunjangan guru', '400': 'Bad Request',}
        )
        def put(self, request, pk, format=None):
            queryset = self.get_queryset(pk)
            serializer = self.serializer_class(queryset, data=request.data)
            if serializer.is_valid():
                serializer.save()

                return Response(serializer.data)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        @swagger_auto_schema(
            request_body=schema_datatunjanganguru,
            responses={'200': 'Berhasil mengupdate data tunjangan guru', '400': 'Bad Request',}
        )
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

class DataTugasTambahanGuruListView(generics.ListCreateAPIView):
        """
        get: Menampilkan daftar karya tulis guru (Guru).
        post: Menambahkan data karya tulis guru (Guru).
        """
        permission_classes = [HasGroupPermissionAny]
        required_groups = {
            'GET': ['Guru'],
            'POST': ['Guru'],
        }
        serializer_class = DataTugasTambahanGuruSerializer

        def get_data_guru(self):
            user = self.request.user
            data_guru = DataGuruUser.objects.get(USER=user).DATA_GURU

            return data_guru

        def get_queryset(self):
            data_guru = self.get_data_guru()

            return DataTugasTambahanGuru.objects.filter(OWNER=data_guru.ID)

        def perform_create(self, serializer):
            serializer.validated_data['OWNER_id'] = self.get_data_guru().ID

            return super(DataTugasTambahanGuruListView, self).perform_create(serializer)


class DataTugasTambahanGuruDetailView(APIView):
        """
        get: Menampilkan daftar karya tulis guru (Guru).
        put: Mengubah atribut keseluruhan data karya tulis guru (Guru).
        patch: Mengubah beberapa atribut data karya tulis guru (Guru).
        delete: Menghapus data karya tulis guru (Guru).
        """
        permission_classes = [HasGroupPermissionAny]
        required_groups = {
            'GET': ['Guru'],
            'PUT': ['Guru'],
            'PATCH': ['Guru'],
            'DELETE': ['Guru'],
        }
        serializer_class = DataTugasTambahanGuruSerializer

        def get_queryset(self, pk):
            user = self.request.user
            data_guru = DataGuruUser.objects.get(USER=user).DATA_GURU

            return DataTugasTambahanGuru.objects.get(pk=self.kwargs['pk'], OWNER=data_guru.ID)

        def get(self, request, pk, *args, **kwargs):
            queryset = self.get_queryset(pk)
            serializer = self.serializer_class
            response = serializer(queryset).data

            return Response(response)

        @swagger_auto_schema(
            request_body=schema_datatugastambahanguru,
            responses={'200': 'Berhasil mengupdate data tugastambahan guru', '400': 'Bad Request',}
        )
        def put(self, request, pk, format=None):
            queryset = self.get_queryset(pk)
            serializer = self.serializer_class(queryset, data=request.data)
            if serializer.is_valid():
                serializer.save()

                return Response(serializer.data)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        @swagger_auto_schema(
            request_body=schema_datatugastambahanguru,
            responses={'200': 'Berhasil mengupdate data tugastambahan guru', '400': 'Bad Request',}
        )
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

class DataPenghargaanGuruListView(generics.ListCreateAPIView):
        """
        get: Menampilkan daftar karya tulis guru (Guru).
        post: Menambahkan data karya tulis guru (Guru).
        """
        permission_classes = [HasGroupPermissionAny]
        required_groups = {
            'GET': ['Guru'],
            'POST': ['Guru'],
        }
        serializer_class = DataPenghargaanGuruSerializer

        def get_data_guru(self):
            user = self.request.user
            data_guru = DataGuruUser.objects.get(USER=user).DATA_GURU

            return data_guru

        def get_queryset(self):
            data_guru = self.get_data_guru()

            return DataPenghargaanGuru.objects.filter(OWNER=data_guru.ID)

        def perform_create(self, serializer):
            serializer.validated_data['OWNER_id'] = self.get_data_guru().ID

            return super(DataPenghargaanGuruListView, self).perform_create(serializer)


class DataPenghargaanGuruDetailView(APIView):
        """
        get: Menampilkan daftar karya tulis guru (Guru).
        put: Mengubah atribut keseluruhan data karya tulis guru (Guru).
        patch: Mengubah beberapa atribut data karya tulis guru (Guru).
        delete: Menghapus data karya tulis guru (Guru).
        """
        permission_classes = [HasGroupPermissionAny]
        required_groups = {
            'GET': ['Guru'],
            'PUT': ['Guru'],
            'PATCH': ['Guru'],
            'DELETE': ['Guru'],
        }
        serializer_class = DataPenghargaanGuruSerializer

        def get_queryset(self, pk):
            user = self.request.user
            data_guru = DataGuruUser.objects.get(USER=user).DATA_GURU

            return DataPenghargaanGuru.objects.get(pk=self.kwargs['pk'], OWNER=data_guru.ID)

        def get(self, request, pk, *args, **kwargs):
            queryset = self.get_queryset(pk)
            serializer = self.serializer_class
            response = serializer(queryset).data

            return Response(response)

        @swagger_auto_schema(
            request_body=schema_datapenghargaanguru,
            responses={'200': 'Berhasil mengupdate data penghargaan guru', '400': 'Bad Request',}
        )
        def put(self, request, pk, format=None):
            queryset = self.get_queryset(pk)
            serializer = self.serializer_class(queryset, data=request.data)
            if serializer.is_valid():
                serializer.save()

                return Response(serializer.data)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        @swagger_auto_schema(
            request_body=schema_datapenghargaanguru,
            responses={'200': 'Berhasil mengupdate data penghargaan guru', '400': 'Bad Request',}
        )
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

class DataNilaiTesGuruListView(generics.ListCreateAPIView):
        """
        get: Menampilkan daftar karya tulis guru (Guru).
        post: Menambahkan data karya tulis guru (Guru).
        """
        permission_classes = [HasGroupPermissionAny]
        required_groups = {
            'GET': ['Guru'],
            'POST': ['Guru'],
        }
        serializer_class = DataNilaiTesGuruSerializer

        def get_data_guru(self):
            user = self.request.user
            data_guru = DataGuruUser.objects.get(USER=user).DATA_GURU

            return data_guru

        def get_queryset(self):
            data_guru = self.get_data_guru()

            return DataNilaiTesGuru.objects.filter(OWNER=data_guru.ID)

        def perform_create(self, serializer):
            serializer.validated_data['OWNER_id'] = self.get_data_guru().ID

            return super(DataNilaiTesGuruListView, self).perform_create(serializer)


class DataNilaiTesGuruDetailView(APIView):
        """
        get: Menampilkan daftar karya tulis guru (Guru).
        put: Mengubah atribut keseluruhan data karya tulis guru (Guru).
        patch: Mengubah beberapa atribut data karya tulis guru (Guru).
        delete: Menghapus data karya tulis guru (Guru).
        """
        permission_classes = [HasGroupPermissionAny]
        required_groups = {
            'GET': ['Guru'],
            'PUT': ['Guru'],
            'PATCH': ['Guru'],
            'DELETE': ['Guru'],
        }
        serializer_class = DataNilaiTesGuruSerializer

        def get_queryset(self, pk):
            user = self.request.user
            data_guru = DataGuruUser.objects.get(USER=user).DATA_GURU

            return DataNilaiTesGuru.objects.get(pk=self.kwargs['pk'], OWNER=data_guru.ID)

        def get(self, request, pk, *args, **kwargs):
            queryset = self.get_queryset(pk)
            serializer = self.serializer_class
            response = serializer(queryset).data

            return Response(response)

        @swagger_auto_schema(
            request_body=schema_datanilaitesguru,
            responses={'200': 'Berhasil mengupdate data nilaites guru', '400': 'Bad Request',}
        )
        def put(self, request, pk, format=None):
            queryset = self.get_queryset(pk)
            serializer = self.serializer_class(queryset, data=request.data)
            if serializer.is_valid():
                serializer.save()

                return Response(serializer.data)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        @swagger_auto_schema(
            request_body=schema_datanilaitesguru,
            responses={'200': 'Berhasil mengupdate data nilaites guru', '400': 'Bad Request',}
        )
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

class DataRiwayatGajiBerkalaGuruListView(generics.ListCreateAPIView):
        """
        get: Menampilkan daftar karya tulis guru (Guru).
        post: Menambahkan data karya tulis guru (Guru).
        """
        permission_classes = [HasGroupPermissionAny]
        required_groups = {
            'GET': ['Guru'],
            'POST': ['Guru'],
        }
        serializer_class = DataRiwayatGajiBerkalaGuruSerializer

        def get_data_guru(self):
            user = self.request.user
            data_guru = DataGuruUser.objects.get(USER=user).DATA_GURU

            return data_guru

        def get_queryset(self):
            data_guru = self.get_data_guru()

            return DataRiwayatGajiBerkalaGuru.objects.filter(OWNER=data_guru.ID)

        def perform_create(self, serializer):
            serializer.validated_data['OWNER_id'] = self.get_data_guru().ID

            return super(DataRiwayatGajiBerkalaGuruListView, self).perform_create(serializer)


class DataRiwayatGajiBerkalaGuruDetailView(APIView):
        """
        get: Menampilkan daftar karya tulis guru (Guru).
        put: Mengubah atribut keseluruhan data karya tulis guru (Guru).
        patch: Mengubah beberapa atribut data karya tulis guru (Guru).
        delete: Menghapus data karya tulis guru (Guru).
        """
        permission_classes = [HasGroupPermissionAny]
        required_groups = {
            'GET': ['Guru'],
            'PUT': ['Guru'],
            'PATCH': ['Guru'],
            'DELETE': ['Guru'],
        }
        serializer_class = DataRiwayatGajiBerkalaGuruSerializer

        def get_queryset(self, pk):
            user = self.request.user
            data_guru = DataGuruUser.objects.get(USER=user).DATA_GURU

            return DataRiwayatGajiBerkalaGuru.objects.get(pk=self.kwargs['pk'], OWNER=data_guru.ID)

        def get(self, request, pk, *args, **kwargs):
            queryset = self.get_queryset(pk)
            serializer = self.serializer_class
            response = serializer(queryset).data

            return Response(response)

        @swagger_auto_schema(
            request_body=schema_datariwayatgajiberkalaguru,
            responses={'200': 'Berhasil mengupdate data riwayatgajiberkala guru', '400': 'Bad Request',}
        )
        def put(self, request, pk, format=None):
            queryset = self.get_queryset(pk)
            serializer = self.serializer_class(queryset, data=request.data)
            if serializer.is_valid():
                serializer.save()

                return Response(serializer.data)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        @swagger_auto_schema(
            request_body=schema_datariwayatgajiberkalaguru,
            responses={'200': 'Berhasil mengupdate data riwayatgajiberkala guru', '400': 'Bad Request',}
        )
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

class DataRiwayatJabatanStrukturalGuruListView(generics.ListCreateAPIView):
        """
        get: Menampilkan daftar karya tulis guru (Guru).
        post: Menambahkan data karya tulis guru (Guru).
        """
        permission_classes = [HasGroupPermissionAny]
        required_groups = {
            'GET': ['Guru'],
            'POST': ['Guru'],
        }
        serializer_class = DataRiwayatJabatanStrukturalGuruSerializer

        def get_data_guru(self):
            user = self.request.user
            data_guru = DataGuruUser.objects.get(USER=user).DATA_GURU

            return data_guru

        def get_queryset(self):
            data_guru = self.get_data_guru()

            return DataRiwayatJabatanStrukturalGuru.objects.filter(OWNER=data_guru.ID)

        def perform_create(self, serializer):
            serializer.validated_data['OWNER_id'] = self.get_data_guru().ID

            return super(DataRiwayatJabatanStrukturalGuruListView, self).perform_create(serializer)


class DataRiwayatJabatanStrukturalGuruDetailView(APIView):
        """
        get: Menampilkan daftar karya tulis guru (Guru).
        put: Mengubah atribut keseluruhan data karya tulis guru (Guru).
        patch: Mengubah beberapa atribut data karya tulis guru (Guru).
        delete: Menghapus data karya tulis guru (Guru).
        """
        permission_classes = [HasGroupPermissionAny]
        required_groups = {
            'GET': ['Guru'],
            'PUT': ['Guru'],
            'PATCH': ['Guru'],
            'DELETE': ['Guru'],
        }
        serializer_class = DataRiwayatJabatanStrukturalGuruSerializer

        def get_queryset(self, pk):
            user = self.request.user
            data_guru = DataGuruUser.objects.get(USER=user).DATA_GURU

            return DataRiwayatJabatanStrukturalGuru.objects.get(pk=self.kwargs['pk'], OWNER=data_guru.ID)

        def get(self, request, pk, *args, **kwargs):
            queryset = self.get_queryset(pk)
            serializer = self.serializer_class
            response = serializer(queryset).data

            return Response(response)

        @swagger_auto_schema(
            request_body=schema_datariwayatjabatanstrukturalguru,
            responses={'200': 'Berhasil mengupdate data riwayatjabatanstruktural guru', '400': 'Bad Request',}
        )
        def put(self, request, pk, format=None):
            queryset = self.get_queryset(pk)
            serializer = self.serializer_class(queryset, data=request.data)
            if serializer.is_valid():
                serializer.save()

                return Response(serializer.data)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        @swagger_auto_schema(
            request_body=schema_datariwayatjabatanstrukturalguru,
            responses={'200': 'Berhasil mengupdate data riwayatjabatanstruktural guru', '400': 'Bad Request',}
        )
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

class DataRiwayatKepangkatanGuruListView(generics.ListCreateAPIView):
        """
        get: Menampilkan daftar karya tulis guru (Guru).
        post: Menambahkan data karya tulis guru (Guru).
        """
        permission_classes = [HasGroupPermissionAny]
        required_groups = {
            'GET': ['Guru'],
            'POST': ['Guru'],
        }
        serializer_class = DataRiwayatKepangkatanGuruSerializer

        def get_data_guru(self):
            user = self.request.user
            data_guru = DataGuruUser.objects.get(USER=user).DATA_GURU

            return data_guru

        def get_queryset(self):
            data_guru = self.get_data_guru()

            return DataRiwayatKepangkatanGuru.objects.filter(OWNER=data_guru.ID)

        def perform_create(self, serializer):
            serializer.validated_data['OWNER_id'] = self.get_data_guru().ID

            return super(DataRiwayatKepangkatanGuruListView, self).perform_create(serializer)


class DataRiwayatKepangkatanGuruDetailView(APIView):
        """
        get: Menampilkan daftar karya tulis guru (Guru).
        put: Mengubah atribut keseluruhan data karya tulis guru (Guru).
        patch: Mengubah beberapa atribut data karya tulis guru (Guru).
        delete: Menghapus data karya tulis guru (Guru).
        """
        permission_classes = [HasGroupPermissionAny]
        required_groups = {
            'GET': ['Guru'],
            'PUT': ['Guru'],
            'PATCH': ['Guru'],
            'DELETE': ['Guru'],
        }
        serializer_class = DataRiwayatKepangkatanGuruSerializer

        def get_queryset(self, pk):
            user = self.request.user
            data_guru = DataGuruUser.objects.get(USER=user).DATA_GURU

            return DataRiwayatKepangkatanGuru.objects.get(pk=self.kwargs['pk'], OWNER=data_guru.ID)

        def get(self, request, pk, *args, **kwargs):
            queryset = self.get_queryset(pk)
            serializer = self.serializer_class
            response = serializer(queryset).data

            return Response(response)

        @swagger_auto_schema(
            request_body=schema_datariwayatkepangkatanguru,
            responses={'200': 'Berhasil mengupdate data riwayatkepangkatan guru', '400': 'Bad Request',}
        )
        def put(self, request, pk, format=None):
            queryset = self.get_queryset(pk)
            serializer = self.serializer_class(queryset, data=request.data)
            if serializer.is_valid():
                serializer.save()

                return Response(serializer.data)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        @swagger_auto_schema(
            request_body=schema_datariwayatkepangkatanguru,
            responses={'200': 'Berhasil mengupdate data riwayatkepangkatan guru', '400': 'Bad Request',}
        )
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

class DataRiwayatPendidikanFormalGuruListView(generics.ListCreateAPIView):
        """
        get: Menampilkan daftar karya tulis guru (Guru).
        post: Menambahkan data karya tulis guru (Guru).
        """
        permission_classes = [HasGroupPermissionAny]
        required_groups = {
            'GET': ['Guru'],
            'POST': ['Guru'],
        }
        serializer_class = DataRiwayatPendidikanFormalGuruSerializer

        def get_data_guru(self):
            user = self.request.user
            data_guru = DataGuruUser.objects.get(USER=user).DATA_GURU

            return data_guru

        def get_queryset(self):
            data_guru = self.get_data_guru()

            return DataRiwayatPendidikanFormalGuru.objects.filter(OWNER=data_guru.ID)

        def perform_create(self, serializer):
            serializer.validated_data['OWNER_id'] = self.get_data_guru().ID

            return super(DataRiwayatPendidikanFormalGuruListView, self).perform_create(serializer)


class DataRiwayatPendidikanFormalGuruDetailView(APIView):
        """
        get: Menampilkan daftar karya tulis guru (Guru).
        put: Mengubah atribut keseluruhan data karya tulis guru (Guru).
        patch: Mengubah beberapa atribut data karya tulis guru (Guru).
        delete: Menghapus data karya tulis guru (Guru).
        """
        permission_classes = [HasGroupPermissionAny]
        required_groups = {
            'GET': ['Guru'],
            'PUT': ['Guru'],
            'PATCH': ['Guru'],
            'DELETE': ['Guru'],
        }
        serializer_class = DataRiwayatPendidikanFormalGuruSerializer

        def get_queryset(self, pk):
            user = self.request.user
            data_guru = DataGuruUser.objects.get(USER=user).DATA_GURU

            return DataRiwayatPendidikanFormalGuru.objects.get(pk=self.kwargs['pk'], OWNER=data_guru.ID)

        def get(self, request, pk, *args, **kwargs):
            queryset = self.get_queryset(pk)
            serializer = self.serializer_class
            response = serializer(queryset).data

            return Response(response)

        @swagger_auto_schema(
            request_body=schema_datariwayatpendidikanformalguru,
            responses={'200': 'Berhasil mengupdate data riwayatpendidikanformal guru', '400': 'Bad Request',}
        )
        def put(self, request, pk, format=None):
            queryset = self.get_queryset(pk)
            serializer = self.serializer_class(queryset, data=request.data)
            if serializer.is_valid():
                serializer.save()

                return Response(serializer.data)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        @swagger_auto_schema(
            request_body=schema_datariwayatpendidikanformalguru,
            responses={'200': 'Berhasil mengupdate data riwayatpendidikanformal guru', '400': 'Bad Request',}
        )
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


class DataRiwayatSertifikasiGuruListView(generics.ListCreateAPIView):
        """
        get: Menampilkan daftar karya tulis guru (Guru).
        post: Menambahkan data karya tulis guru (Guru).
        """
        permission_classes = [HasGroupPermissionAny]
        required_groups = {
            'GET': ['Guru'],
            'POST': ['Guru'],
        }
        serializer_class = DataRiwayatSertifikasiGuruSerializer

        def get_data_guru(self):
            user = self.request.user
            data_guru = DataGuruUser.objects.get(USER=user).DATA_GURU

            return data_guru

        def get_queryset(self):
            data_guru = self.get_data_guru()

            return DataRiwayatSertifikasiGuru.objects.filter(OWNER=data_guru.ID)

        def perform_create(self, serializer):
            serializer.validated_data['OWNER_id'] = self.get_data_guru().ID

            return super(DataRiwayatSertifikasiGuruListView, self).perform_create(serializer)


class DataRiwayatSertifikasiGuruDetailView(APIView):
        """
        get: Menampilkan daftar karya tulis guru (Guru).
        put: Mengubah atribut keseluruhan data karya tulis guru (Guru).
        patch: Mengubah beberapa atribut data karya tulis guru (Guru).
        delete: Menghapus data karya tulis guru (Guru).
        """
        permission_classes = [HasGroupPermissionAny]
        required_groups = {
            'GET': ['Guru'],
            'PUT': ['Guru'],
            'PATCH': ['Guru'],
            'DELETE': ['Guru'],
        }
        serializer_class = DataRiwayatSertifikasiGuruSerializer

        def get_queryset(self, pk):
            user = self.request.user
            data_guru = DataGuruUser.objects.get(USER=user).DATA_GURU

            return DataRiwayatSertifikasiGuru.objects.get(pk=self.kwargs['pk'], OWNER=data_guru.ID)

        def get(self, request, pk, *args, **kwargs):
            queryset = self.get_queryset(pk)
            serializer = self.serializer_class
            response = serializer(queryset).data

            return Response(response)

        @swagger_auto_schema(
            request_body=schema_datariwayatsertifikasiguru,
            responses={'200': 'Berhasil mengupdate data riwayatsertifikasi guru', '400': 'Bad Request',}
        )
        def put(self, request, pk, format=None):
            queryset = self.get_queryset(pk)
            serializer = self.serializer_class(queryset, data=request.data)
            if serializer.is_valid():
                serializer.save()

                return Response(serializer.data)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        @swagger_auto_schema(
            request_body=schema_datariwayatsertifikasiguru,
            responses={'200': 'Berhasil mengupdate data riwayatsertifikasi guru', '400': 'Bad Request',}
        )
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

class DataRiwayatJabatanFungsionalGuruListView(generics.ListCreateAPIView):
        """
        get: Menampilkan daftar karya tulis guru (Guru).
        post: Menambahkan data karya tulis guru (Guru).
        """
        permission_classes = [HasGroupPermissionAny]
        required_groups = {
            'GET': ['Guru'],
            'POST': ['Guru'],
        }
        serializer_class = DataRiwayatJabatanFungsionalGuruSerializer

        def get_data_guru(self):
            user = self.request.user
            data_guru = DataGuruUser.objects.get(USER=user).DATA_GURU

            return data_guru

        def get_queryset(self):
            data_guru = self.get_data_guru()

            return DataRiwayatJabatanFungsionalGuru.objects.filter(OWNER=data_guru.ID)

        def perform_create(self, serializer):
            serializer.validated_data['OWNER_id'] = self.get_data_guru().ID

            return super(DataRiwayatJabatanFungsionalGuruListView, self).perform_create(serializer)


class DataRiwayatJabatanFungsionalGuruDetailView(APIView):
        """
        get: Menampilkan daftar karya tulis guru (Guru).
        put: Mengubah atribut keseluruhan data karya tulis guru (Guru).
        patch: Mengubah beberapa atribut data karya tulis guru (Guru).
        delete: Menghapus data karya tulis guru (Guru).
        """
        permission_classes = [HasGroupPermissionAny]
        required_groups = {
            'GET': ['Guru'],
            'PUT': ['Guru'],
            'PATCH': ['Guru'],
            'DELETE': ['Guru'],
        }
        serializer_class = DataRiwayatJabatanFungsionalGuruSerializer

        def get_queryset(self, pk):
            user = self.request.user
            data_guru = DataGuruUser.objects.get(USER=user).DATA_GURU

            return DataRiwayatJabatanFungsionalGuru.objects.get(pk=self.kwargs['pk'], OWNER=data_guru.ID)

        def get(self, request, pk, *args, **kwargs):
            queryset = self.get_queryset(pk)
            serializer = self.serializer_class
            response = serializer(queryset).data

            return Response(response)

        @swagger_auto_schema(
            request_body=schema_datariwayatjabatanfungsionalguru,
            responses={'200': 'Berhasil mengupdate data riwayatjabatanfungsional guru', '400': 'Bad Request',}
        )
        def put(self, request, pk, format=None):
            queryset = self.get_queryset(pk)
            serializer = self.serializer_class(queryset, data=request.data)
            if serializer.is_valid():
                serializer.save()

                return Response(serializer.data)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        @swagger_auto_schema(
            request_body=schema_datariwayatjabatanfungsionalguru,
            responses={'200': 'Berhasil mengupdate data riwayatjabatanfungsional guru', '400': 'Bad Request',}
        )
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

class DataRiwayatKarirGuruListView(generics.ListCreateAPIView):
        """
        get: Menampilkan daftar karya tulis guru (Guru).
        post: Menambahkan data karya tulis guru (Guru).
        """
        permission_classes = [HasGroupPermissionAny]
        required_groups = {
            'GET': ['Guru'],
            'POST': ['Guru'],
        }
        serializer_class = DataRiwayatKarirGuruSerializer

        def get_data_guru(self):
            user = self.request.user
            data_guru = DataGuruUser.objects.get(USER=user).DATA_GURU

            return data_guru

        def get_queryset(self):
            data_guru = self.get_data_guru()

            return DataRiwayatKarirGuru.objects.filter(OWNER=data_guru.ID)

        def perform_create(self, serializer):
            serializer.validated_data['OWNER_id'] = self.get_data_guru().ID

            return super(DataRiwayatKarirGuruListView, self).perform_create(serializer)


class DataRiwayatKarirGuruDetailView(APIView):
        """
        get: Menampilkan daftar karya tulis guru (Guru).
        put: Mengubah atribut keseluruhan data karya tulis guru (Guru).
        patch: Mengubah beberapa atribut data karya tulis guru (Guru).
        delete: Menghapus data karya tulis guru (Guru).
        """
        permission_classes = [HasGroupPermissionAny]
        required_groups = {
            'GET': ['Guru'],
            'PUT': ['Guru'],
            'PATCH': ['Guru'],
            'DELETE': ['Guru'],
        }
        serializer_class = DataRiwayatKarirGuruSerializer

        def get_queryset(self, pk):
            user = self.request.user
            data_guru = DataGuruUser.objects.get(USER=user).DATA_GURU

            return DataRiwayatKarirGuru.objects.get(pk=self.kwargs['pk'], OWNER=data_guru.ID)

        def get(self, request, pk, *args, **kwargs):
            queryset = self.get_queryset(pk)
            serializer = self.serializer_class
            response = serializer(queryset).data

            return Response(response)

        @swagger_auto_schema(
            request_body=schema_datariwayatkarirguru,
            responses={'200': 'Berhasil mengupdate data riwayatkarir guru', '400': 'Bad Request',}
        )
        def put(self, request, pk, format=None):
            queryset = self.get_queryset(pk)
            serializer = self.serializer_class(queryset, data=request.data)
            if serializer.is_valid():
                serializer.save()

                return Response(serializer.data)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        @swagger_auto_schema(
            request_body=schema_datariwayatkarirguru,
            responses={'200': 'Berhasil mengupdate data riwayatkarir guru', '400': 'Bad Request',}
        )
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

class DataAnakKaryawanListView(generics.ListCreateAPIView):
    """
    get: Menampilkan seluruh daftar Anak karyawan (Super Admin/ Karyawan).
    post: Menambahkan data Anak karyawan (Super Admin/ Karyawan).
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Karyawan'],
        'POST': ['Karyawan'],
    }
    queryset = DataAnakKaryawan.objects.all()
    serializer_class = DataAnakKaryawanSerializer

    def get_data_karyawan(self):
        user = self.request.user
        data_karyawan = DataKaryawanUser.objects.get(USER=user).DATA_KARYAWAN

        return data_karyawan

    def get_queryset(self):
        data_karyawan = self.get_data_karyawan()

        return DataAnakKaryawan.objects.filter(OWNER=data_karyawan.ID)

    def perform_create(self, serializer):
        serializer.validated_data['OWNER_id'] = self.get_data_karyawan().ID

        return super(DataAnakKaryawanListView, self).perform_create(serializer)

class DataAnakKaryawanDetailView(APIView):
    """
    get: Menampilkan daftar Data Anak Karyawan (Karyawan).
    put: Mengubah atribut keseluruhan Data Anak Karyawan (Karyawan).
    patch: Mengubah beberapa atribut Data Anak Karyawan (Karyawan).
    delete: Menghapus Data Anak Karyawan (Karyawan).
    """
    permission_classes = [HasGroupPermissionAny]
    required_groups = {
        'GET': ['Karyawan'],
        'PUT': ['Karyawan'],
        'PATCH': ['Karyawan'],
        'DELETE': ['Karyawan'],
    }
    serializer_class = DataAnakKaryawanSerializer

    def get_queryset(self, pk):
        user = self.request.user
        data_karyawan = DataKaryawanUser.objects.get(USER=user).DATA_KARYAWAN
        return DataAnakKaryawan.objects.get(pk=self.kwargs['pk'], OWNER= data_karyawan.ID)

    def get(self, request, pk, *args, **kwargs):
        queryset = self.get_queryset(pk)
        serializer = self.serializer_class
        response = serializer(queryset).data

        return Response(response)

    @swagger_auto_schema(
        request_body=schema_dataanakkaryawan,
        responses={'200': 'Berhasil mengupdate data anak karyawan', '400': 'Bad Request',}
    )
    def put(self, request, pk, format=None):
        queryset = self.get_queryset(pk)
        serializer = self.serializer_class(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        request_body=schema_dataanakkaryawan,
        responses={'200': 'Berhasil mengupdate data anak karyawan', '400': 'Bad Request',}
    )
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

class DataBeasiswaKaryawanListView(generics.ListCreateAPIView):
    """
    get: Menampilkan seluruh daftar beasiswa karyawan (Super Admin/ Karyawan).
    post: Menambahkan data beasiswa karyawan (Super Admin/ Karyawan).
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Karyawan'],
        'POST': ['Karyawan'],
    }
    queryset = DataBeasiswaKaryawan.objects.all()
    serializer_class = DataBeasiswaKaryawanSerializer

    def get_data_karyawan(self):
        user = self.request.user
        data_karyawan = DataKaryawanUser.objects.get(USER=user).DATA_KARYAWAN

        return data_karyawan

    def get_queryset(self):
        data_karyawan = self.get_data_karyawan()

        return DataBeasiswaKaryawan.objects.filter(OWNER=data_karyawan.ID)

    def perform_create(self, serializer):
        serializer.validated_data['OWNER_id'] = self.get_data_karyawan().ID

        return super(DataBeasiswaKaryawanListView, self).perform_create(serializer)

class DataBeasiswaKaryawanDetailView(APIView):
    """
    get: Menampilkan daftar Data Anak Karyawan (Karyawan).
    put: Mengubah atribut keseluruhan Data Anak Karyawan (Karyawan).
    patch: Mengubah beberapa atribut Data Anak Karyawan (Karyawan).
    delete: Menghapus Data Anak Karyawan (Karyawan).
    """
    permission_classes = [HasGroupPermissionAny]
    required_groups = {
        'GET': ['Karyawan'],
        'PUT': ['Karyawan'],
        'PATCH': ['Karyawan'],
        'DELETE': ['Karyawan'],
    }
    serializer_class = DataBeasiswaKaryawanSerializer

    def get_queryset(self,pk):
        user = self.request.user
        data_karyawan = DataKaryawanUser.objects.get(USER=user).DATA_KARYAWAN
        return DataBeasiswaKaryawan.objects.get(pk=self.kwargs['pk'], OWNER= data_karyawan.ID)

    def get(self, request, pk, *args, **kwargs):
        queryset = self.get_queryset(pk)
        serializer = self.serializer_class
        response = serializer(queryset).data

        return Response(response)

    @swagger_auto_schema(
        request_body=schema_databeasiswakaryawan,
        responses={'200': 'Berhasil mengupdate data beasiswa karyawan', '400': 'Bad Request',}
    )
    def put(self, request, pk, format=None):
        queryset = self.get_queryset(pk)
        serializer = self.serializer_class(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        request_body=schema_databeasiswakaryawan,
        responses={'200': 'Berhasil mengupdate data beasiswa karyawan', '400': 'Bad Request',}
    )
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

class DataBukuKaryawanListView(generics.ListCreateAPIView):
    """
    get: Menampilkan seluruh daftar buku karyawan (Super Admin/ Karyawan).
    post: Menambahkan data buku karyawan (Super Admin/ Karyawan).
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Karyawan'],
        'POST': ['Karyawan'],
    }
    queryset = DataBukuKaryawan.objects.all()
    serializer_class = DataBukuKaryawanSerializer

    def get_data_karyawan(self):
        user = self.request.user
        data_karyawan = DataKaryawanUser.objects.get(USER=user).DATA_KARYAWAN

        return data_karyawan

    def get_queryset(self):
        data_karyawan = self.get_data_karyawan()

        return DataBukuKaryawan.objects.filter(OWNER=data_karyawan.ID)

    def perform_create(self, serializer):
        serializer.validated_data['OWNER_id'] = self.get_data_karyawan().ID

        return super(DataBukuKaryawanListView, self).perform_create(serializer)

class DataBukuKaryawanDetailView(APIView):
    """
    get: Menampilkan daftar Data Buku Karyawan (Karyawan).
    put: Mengubah atribut keseluruhan Data Buku Karyawan (Karyawan).
    patch: Mengubah beberapa atribut Data Buku Karyawan (Karyawan).
    delete: Menghapus Data Buku Karyawan (Karyawan).
    """
    permission_classes = [HasGroupPermissionAny]
    required_groups = {
        'GET': ['Karyawan'],
        'PUT': ['Karyawan'],
        'PATCH': ['Karyawan'],
        'DELETE': ['Karyawan'],
    }
    serializer_class = DataBukuKaryawanSerializer

    def get_queryset(self,pk):
        user = self.request.user
        data_karyawan = DataKaryawanUser.objects.get(USER=user).DATA_KARYAWAN
        return DataBukuKaryawan.objects.get(pk=self.kwargs['pk'], OWNER= data_karyawan.ID)

    def get(self, request, pk, *args, **kwargs):
        queryset = self.get_queryset(pk)
        serializer = self.serializer_class
        response = serializer(queryset).data

        return Response(response)

    @swagger_auto_schema(
        request_body=schema_databukukaryawan,
        responses={'200': 'Berhasil mengupdate data buku karyawan', '400': 'Bad Request',}
    )
    def put(self, request, pk, format=None):
        queryset = self.get_queryset(pk)
        serializer = self.serializer_class(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        request_body=schema_databukukaryawan,
        responses={'200': 'Berhasil mengupdate data buku karyawan', '400': 'Bad Request',}
    )
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

class DataDiklatKaryawanListView(generics.ListCreateAPIView):
    """
    get: Menampilkan seluruh daftar diklat karyawan (Super Admin/ Karyawan).
    post: Menambahkan data diklat karyawan (Super Admin/ Karyawan).
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Karyawan'],
        'POST': ['Karyawan'],
    }
    queryset = DataDiklatKaryawan.objects.all()
    serializer_class = DataDiklatKaryawanSerializer

    def get_data_karyawan(self):
        user = self.request.user
        data_karyawan = DataKaryawanUser.objects.get(USER=user).DATA_KARYAWAN

        return data_karyawan

    def get_queryset(self):
        data_karyawan = self.get_data_karyawan()

        return DataDiklatKaryawan.objects.filter(OWNER=data_karyawan.ID)

    def perform_create(self, serializer):
        serializer.validated_data['OWNER_id'] = self.get_data_karyawan().ID

        return super(DataDiklatKaryawanListView, self).perform_create(serializer)

class DataDiklatKaryawanDetailView(APIView):
    """
    get: Menampilkan daftar Data Diklat Karyawan (Karyawan).
    put: Mengubah atribut keseluruhan Data Diklat Karyawan (Karyawan).
    patch: Mengubah beberapa atribut Data Diklat Karyawan (Karyawan).
    delete: Menghapus Data Diklat Karyawan (Karyawan).
    """
    permission_classes = [HasGroupPermissionAny]
    required_groups = {
        'GET': ['Karyawan'],
        'PUT': ['Karyawan'],
        'PATCH': ['Karyawan'],
        'DELETE': ['Karyawan'],
    }
    serializer_class = DataDiklatKaryawanSerializer

    def get_queryset(self,pk):
        user = self.request.user
        data_karyawan = DataKaryawanUser.objects.get(USER=user).DATA_KARYAWAN
        return DataDiklatKaryawan.objects.get(pk=self.kwargs['pk'], OWNER= data_karyawan.ID)

    def get(self, request, pk, *args, **kwargs):
        queryset = self.get_queryset(pk)
        serializer = self.serializer_class
        response = serializer(queryset).data

        return Response(response)

    @swagger_auto_schema(
        request_body=schema_datadiklatkaryawan,
        responses={'200': 'Berhasil mengupdate data diklat karyawan', '400': 'Bad Request',}
    )
    def put(self, request, pk, format=None):
        queryset = self.get_queryset(pk)
        serializer = self.serializer_class(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        request_body=schema_datadiklatkaryawan,
        responses={'200': 'Berhasil mengupdate data diklat karyawan', '400': 'Bad Request',}
    )
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

class DataKaryaTulisKaryawanListView(generics.ListCreateAPIView):
    """
    get: Menampilkan seluruh daftar karya tulis karyawan (Super Admin/ Karyawan).
    post: Menambahkan data karya tulis karyawan (Super Admin/ Karyawan).
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Karyawan'],
        'POST': ['Karyawan'],
    }
    queryset = DataKaryaTulisKaryawan.objects.all()
    serializer_class = DataKaryaTulisKaryawanSerializer

    def get_data_karyawan(self):
        user = self.request.user
        data_karyawan = DataKaryawanUser.objects.get(USER=user).DATA_KARYAWAN

        return data_karyawan

    def get_queryset(self):
        data_karyawan = self.get_data_karyawan()

        return DataKaryaTulisKaryawan.objects.filter(OWNER=data_karyawan.ID)

    def perform_create(self, serializer):
        serializer.validated_data['OWNER_id'] = self.get_data_karyawan().ID

        return super(DataKaryaTulisKaryawanListView, self).perform_create(serializer)

class DataKaryaTulisKaryawanDetailView(APIView):
    """
    get: Menampilkan daftar Data KaryaTulis Karyawan (Karyawan).
    put: Mengubah atribut keseluruhan Data KaryaTulis Karyawan (Karyawan).
    patch: Mengubah beberapa atribut Data KaryaTulis Karyawan (Karyawan).
    delete: Menghapus Data KaryaTulis Karyawan (Karyawan).
    """
    permission_classes = [HasGroupPermissionAny]
    required_groups = {
        'GET': ['Karyawan'],
        'PUT': ['Karyawan'],
        'PATCH': ['Karyawan'],
        'DELETE': ['Karyawan'],
    }
    serializer_class = DataKaryaTulisKaryawanSerializer

    def get_queryset(self,pk):
        user = self.request.user
        data_karyawan = DataKaryawanUser.objects.get(USER=user).DATA_KARYAWAN
        return DataKaryaTulisKaryawan.objects.get(pk=self.kwargs['pk'], OWNER= data_karyawan.ID)

    def get(self, request, pk, *args, **kwargs):
        queryset = self.get_queryset(pk)
        serializer = self.serializer_class
        response = serializer(queryset).data

        return Response(response)

    @swagger_auto_schema(
        request_body=schema_datakaryatuliskaryawan,
        responses={'200': 'Berhasil mengupdate data karya tulis karyawan', '400': 'Bad Request',}
    )
    def put(self, request, pk, format=None):
        queryset = self.get_queryset(pk)
        serializer = self.serializer_class(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        request_body=schema_datakaryatuliskaryawan,
        responses={'200': 'Berhasil mengupdate data karya tulis karyawan', '400': 'Bad Request',}
    )
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

class DataKesejahteraanKaryawanListView(generics.ListCreateAPIView):
    """
    get: Menampilkan seluruh daftar Kesejahteraan karyawan (Super Admin/ Karyawan).
    post: Menambahkan data Kesejahteraan karyawan (Super Admin/ Karyawan).
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Karyawan'],
        'POST': ['Karyawan'],
    }
    queryset = DataKesejahteraanKaryawan.objects.all()
    serializer_class = DataKesejahteraanKaryawanSerializer

    def get_data_karyawan(self):
        user = self.request.user
        data_karyawan = DataKaryawanUser.objects.get(USER=user).DATA_KARYAWAN

        return data_karyawan

    def get_queryset(self):
        data_karyawan = self.get_data_karyawan()

        return DataKesejahteraanKaryawan.objects.filter(OWNER=data_karyawan.ID)

    def perform_create(self, serializer):
        serializer.validated_data['OWNER_id'] = self.get_data_karyawan().ID

        return super(DataKesejahteraanKaryawanListView, self).perform_create(serializer)

class DataKesejahteraanKaryawanDetailView(APIView):
    """
    get: Menampilkan daftar Data Kesejahteraan Karyawan (Karyawan).
    put: Mengubah atribut keseluruhan Data Kesejahteraan Karyawan (Karyawan).
    patch: Mengubah beberapa atribut Data Kesejahteraan Karyawan (Karyawan).
    delete: Menghapus Data Kesejahteraan Karyawan (Karyawan).
    """
    permission_classes = [HasGroupPermissionAny]
    required_groups = {
        'GET': ['Karyawan'],
        'PUT': ['Karyawan'],
        'PATCH': ['Karyawan'],
        'DELETE': ['Karyawan'],
    }
    serializer_class = DataKesejahteraanKaryawanSerializer

    def get_queryset(self,pk):
        user = self.request.user
        data_karyawan = DataKaryawanUser.objects.get(USER=user).DATA_KARYAWAN
        return DataKesejahteraanKaryawan.objects.get(pk=self.kwargs['pk'], OWNER= data_karyawan.ID)

    def get(self, request, pk, *args, **kwargs):
        queryset = self.get_queryset(pk)
        serializer = self.serializer_class
        response = serializer(queryset).data

        return Response(response)

    @swagger_auto_schema(
        request_body=schema_datakesejahteraankaryawan,
        responses={'200': 'Berhasil mengupdate data kesejahteraan karyawan', '400': 'Bad Request',}
    )
    def put(self, request, pk, format=None):
        queryset = self.get_queryset(pk)
        serializer = self.serializer_class(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        request_body=schema_datakesejahteraankaryawan,
        responses={'200': 'Berhasil mengupdate data kesejahteraan karyawan', '400': 'Bad Request',}
    )
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

class DataTunjanganKaryawanListView(generics.ListCreateAPIView):
    """
    get: Menampilkan seluruh daftar Tunjangan karyawan (Super Admin/ Karyawan).
    post: Menambahkan data Tunjangan karyawan (Super Admin/ Karyawan).
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Karyawan'],
        'POST': ['Karyawan'],
    }
    queryset = DataTunjanganKaryawan.objects.all()
    serializer_class = DataTunjanganKaryawanSerializer

    def get_data_karyawan(self):
        user = self.request.user
        data_karyawan = DataKaryawanUser.objects.get(USER=user).DATA_KARYAWAN

        return data_karyawan

    def get_queryset(self):
        data_karyawan = self.get_data_karyawan()

        return DataTunjanganKaryawan.objects.filter(OWNER=data_karyawan.ID)

    def perform_create(self, serializer):
        serializer.validated_data['OWNER_id'] = self.get_data_karyawan().ID

        return super(DataTunjanganKaryawanListView, self).perform_create(serializer)

class DataTunjanganKaryawanDetailView(APIView):
    """
    get: Menampilkan daftar Data Tunjangan Karyawan (Karyawan).
    put: Mengubah atribut keseluruhan Data Tunjangan Karyawan (Karyawan).
    patch: Mengubah beberapa atribut Data Tunjangan Karyawan (Karyawan).
    delete: Menghapus Data Tunjangan Karyawan (Karyawan).
    """
    permission_classes = [HasGroupPermissionAny]
    required_groups = {
        'GET': ['Karyawan'],
        'PUT': ['Karyawan'],
        'PATCH': ['Karyawan'],
        'DELETE': ['Karyawan'],
    }
    serializer_class = DataTunjanganKaryawanSerializer

    def get_queryset(self,pk):
        user = self.request.user
        data_karyawan = DataKaryawanUser.objects.get(USER=user).DATA_KARYAWAN
        return DataTunjanganKaryawan.objects.get(pk=self.kwargs['pk'], OWNER= data_karyawan.ID)

    def get(self, request, pk, *args, **kwargs):
        queryset = self.get_queryset(pk)
        serializer = self.serializer_class
        response = serializer(queryset).data

        return Response(response)

    @swagger_auto_schema(
        request_body=schema_datatunjangankaryawan,
        responses={'200': 'Berhasil mengupdate data tunjangan karyawan', '400': 'Bad Request',}
    )
    def put(self, request, pk, format=None):
        queryset = self.get_queryset(pk)
        serializer = self.serializer_class(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        request_body=schema_datatunjangankaryawan,
        responses={'200': 'Berhasil mengupdate data tunjangan karyawan', '400': 'Bad Request',}
    )
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

class DataTugasTambahanKaryawanListView(generics.ListCreateAPIView):
    """
    get: Menampilkan seluruh daftar Tunjangan karyawan (Super Admin/ Karyawan).
    post: Menambahkan data Tunjangan karyawan (Super Admin/ Karyawan).
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Karyawan'],
        'POST': ['Karyawan'],
    }
    queryset = DataTugasTambahanKaryawan.objects.all()
    serializer_class = DataTugasTambahanKaryawanSerializer

    def get_data_karyawan(self):
        user = self.request.user
        data_karyawan = DataKaryawanUser.objects.get(USER=user).DATA_KARYAWAN

        return data_karyawan

    def get_queryset(self):
        data_karyawan = self.get_data_karyawan()

        return DataTugasTambahanKaryawan.objects.filter(OWNER=data_karyawan.ID)

    def perform_create(self, serializer):
        serializer.validated_data['OWNER_id'] = self.get_data_karyawan().ID

        return super(DataTugasTambahanKaryawanListView, self).perform_create(serializer)

class DataTugasTambahanKaryawanDetailView(APIView):
    """
    get: Menampilkan daftar Data TugasTambahan Karyawan (Karyawan).
    put: Mengubah atribut keseluruhan Data TugasTambahan Karyawan (Karyawan).
    patch: Mengubah beberapa atribut Data TugasTambahan Karyawan (Karyawan).
    delete: Menghapus Data TugasTambahan Karyawan (Karyawan).
    """
    permission_classes = [HasGroupPermissionAny]
    required_groups = {
        'GET': ['Karyawan'],
        'PUT': ['Karyawan'],
        'PATCH': ['Karyawan'],
        'DELETE': ['Karyawan'],
    }
    serializer_class = DataTugasTambahanKaryawanSerializer

    def get_queryset(self,pk):
        user = self.request.user
        data_karyawan = DataKaryawanUser.objects.get(USER=user).DATA_KARYAWAN
        return DataTugasTambahanKaryawan.objects.get(pk=self.kwargs['pk'], OWNER= data_karyawan.ID)

    def get(self, request, pk, *args, **kwargs):
        queryset = self.get_queryset(pk)
        serializer = self.serializer_class
        response = serializer(queryset).data

        return Response(response)

    @swagger_auto_schema(
        request_body=schema_datatugastambahankaryawan,
        responses={'200': 'Berhasil mengupdate data tugas tambahan karyawan', '400': 'Bad Request',}
    )
    def put(self, request, pk, format=None):
        queryset = self.get_queryset(pk)
        serializer = self.serializer_class(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        request_body=schema_datatugastambahankaryawan,
        responses={'200': 'Berhasil mengupdate data tugas tambahan karyawan', '400': 'Bad Request',}
    )
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

class DataPenghargaanKaryawanListView(generics.ListCreateAPIView):
    """
    get: Menampilkan seluruh daftar Penghargaan karyawan (Super Admin/ Karyawan).
    post: Menambahkan data Penghargaan karyawan (Super Admin/ Karyawan).
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Karyawan'],
        'POST': ['Karyawan'],
    }
    queryset = DataPenghargaanKaryawan.objects.all()
    serializer_class = DataPenghargaanKaryawanSerializer

    def get_data_karyawan(self):
        user = self.request.user
        data_karyawan = DataKaryawanUser.objects.get(USER=user).DATA_KARYAWAN

        return data_karyawan

    def get_queryset(self):
        data_karyawan = self.get_data_karyawan()

        return DataPenghargaanKaryawan.objects.filter(OWNER=data_karyawan.ID)

    def perform_create(self, serializer):
        serializer.validated_data['OWNER_id'] = self.get_data_karyawan().ID

        return super(DataPenghargaanKaryawanListView, self).perform_create(serializer)

class DataPenghargaanKaryawanDetailView(APIView):
    """
    get: Menampilkan daftar Data Penghargaan Karyawan (Karyawan).
    put: Mengubah atribut keseluruhan Data Penghargaan Karyawan (Karyawan).
    patch: Mengubah beberapa atribut Data Penghargaan Karyawan (Karyawan).
    delete: Menghapus Data Penghargaan Karyawan (Karyawan).
    """
    permission_classes = [HasGroupPermissionAny]
    required_groups = {
        'GET': ['Karyawan'],
        'PUT': ['Karyawan'],
        'PATCH': ['Karyawan'],
        'DELETE': ['Karyawan'],
    }
    serializer_class = DataPenghargaanKaryawanSerializer

    def get_queryset(self,pk):
        user = self.request.user
        data_karyawan = DataKaryawanUser.objects.get(USER=user).DATA_KARYAWAN
        return DataPenghargaanKaryawan.objects.get(pk=self.kwargs['pk'], OWNER= data_karyawan.ID)

    def get(self, request, pk, *args, **kwargs):
        queryset = self.get_queryset(pk)
        serializer = self.serializer_class
        response = serializer(queryset).data

        return Response(response)

    @swagger_auto_schema(
        request_body=schema_datapenghargaankaryawan,
        responses={'200': 'Berhasil mengupdate data Penghargaan karyawan', '400': 'Bad Request',}
    )
    def put(self, request, pk, format=None):
        queryset = self.get_queryset(pk)
        serializer = self.serializer_class(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        request_body=schema_datapenghargaankaryawan,
        responses={'200': 'Berhasil mengupdate data tugas tambahan karyawan', '400': 'Bad Request',}
    )
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

class DataNilaiTesKaryawanListView(generics.ListCreateAPIView):
    """
    get: Menampilkan seluruh daftar NilaiTes karyawan (Super Admin/ Karyawan).
    post: Menambahkan data NilaiTes karyawan (Super Admin/ Karyawan).
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Karyawan'],
        'POST': ['Karyawan'],
    }
    queryset = DataNilaiTesKaryawan.objects.all()
    serializer_class = DataNilaiTesKaryawanSerializer

    def get_data_karyawan(self):
        user = self.request.user
        data_karyawan = DataKaryawanUser.objects.get(USER=user).DATA_KARYAWAN

        return data_karyawan

    def get_queryset(self):
        data_karyawan = self.get_data_karyawan()

        return DataNilaiTesKaryawan.objects.filter(OWNER=data_karyawan.ID)

    def perform_create(self, serializer):
        serializer.validated_data['OWNER_id'] = self.get_data_karyawan().ID

        return super(DataNilaiTesKaryawanListView, self).perform_create(serializer)

class DataNilaiTesKaryawanDetailView(APIView):
    """
    get: Menampilkan daftar Data TesKaryawan Karyawan (Karyawan).
    put: Mengubah atribut keseluruhan Data TesKaryawan Karyawan (Karyawan).
    patch: Mengubah beberapa atribut Data TesKaryawan Karyawan (Karyawan).
    delete: Menghapus Data TesKaryawan Karyawan (Karyawan).
    """
    permission_classes = [HasGroupPermissionAny]
    required_groups = {
        'GET': ['Karyawan'],
        'PUT': ['Karyawan'],
        'PATCH': ['Karyawan'],
        'DELETE': ['Karyawan'],
    }
    serializer_class = DataNilaiTesKaryawanSerializer

    def get_queryset(self,pk):
        user = self.request.user
        data_karyawan = DataKaryawanUser.objects.get(USER=user).DATA_KARYAWAN
        return DataNilaiTesKaryawan.objects.get(pk=self.kwargs['pk'], OWNER= data_karyawan.ID)

    def get(self, request, pk, *args, **kwargs):
        queryset = self.get_queryset(pk)
        serializer = self.serializer_class
        response = serializer(queryset).data

        return Response(response)

    @swagger_auto_schema(
        request_body=schema_datanilaiteskaryawan,
        responses={'200': 'Berhasil mengupdate data nilai tes karyawan', '400': 'Bad Request',}
    )
    def put(self, request, pk, format=None):
        queryset = self.get_queryset(pk)
        serializer = self.serializer_class(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        request_body=schema_datanilaiteskaryawan,
        responses={'200': 'Berhasil mengupdate data nilai tes karyawan', '400': 'Bad Request',}
    )
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

class DataRiwayatGajiBerkalaKaryawanListView(generics.ListCreateAPIView):
    """
    get: Menampilkan seluruh daftar Riwayat Gaji Berkala karyawan (Super Admin/ Karyawan).
    post: Menambahkan data Riwayat Gaji Berkala karyawan (Super Admin/ Karyawan).
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Karyawan'],
        'POST': ['Karyawan'],
    }
    queryset = DataRiwayatGajiBerkalaKaryawan.objects.all()
    serializer_class = DataRiwayatGajiBerkalaKaryawanSerializer

    def get_data_karyawan(self):
        user = self.request.user
        data_karyawan = DataKaryawanUser.objects.get(USER=user).DATA_KARYAWAN

        return data_karyawan

    def get_queryset(self):
        data_karyawan = self.get_data_karyawan()

        return DataRiwayatGajiBerkalaKaryawan.objects.filter(OWNER=data_karyawan.ID)

    def perform_create(self, serializer):
        serializer.validated_data['OWNER_id'] = self.get_data_karyawan().ID

        return super(DataRiwayatGajiBerkalaKaryawanListView, self).perform_create(serializer)

class DataRiwayatGajiBerkalaKaryawanDetailView(APIView):
    """
    get: Menampilkan daftar Data Riwayat Gaji Berkala Karyawan (Karyawan).
    put: Mengubah atribut keseluruhan Data Riwayat Gaji Berkala Karyawan (Karyawan).
    patch: Mengubah beberapa atribut Data Riwayat Gaji Berkala Karyawan (Karyawan).
    delete: Menghapus Data Riwayat Gaji Berkala Karyawan (Karyawan).
    """
    permission_classes = [HasGroupPermissionAny]
    required_groups = {
        'GET': ['Karyawan'],
        'PUT': ['Karyawan'],
        'PATCH': ['Karyawan'],
        'DELETE': ['Karyawan'],
    }
    serializer_class = DataRiwayatGajiBerkalaKaryawanSerializer

    def get_queryset(self,pk):
        user = self.request.user
        data_karyawan = DataKaryawanUser.objects.get(USER=user).DATA_KARYAWAN
        return DataRiwayatGajiBerkalaKaryawan.objects.get(pk=self.kwargs['pk'], OWNER= data_karyawan.ID)

    def get(self, request, pk, *args, **kwargs):
        queryset = self.get_queryset(pk)
        serializer = self.serializer_class
        response = serializer(queryset).data

        return Response(response)

    @swagger_auto_schema(
        request_body=schema_datariwayatgajiberkalakaryawan,
        responses={'200': 'Berhasil mengupdate data riwayat gaji berkala karyawan', '400': 'Bad Request',}
    )
    def put(self, request, pk, format=None):
        queryset = self.get_queryset(pk)
        serializer = self.serializer_class(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        request_body=schema_datariwayatgajiberkalakaryawan,
        responses={'200': 'Berhasil mengupdate data riwayat gaji berkala karyawan', '400': 'Bad Request',}
    )
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

class DataRiwayatJabatanStrukturalKaryawanListView(generics.ListCreateAPIView):
    """
    get: Menampilkan seluruh daftar Riwayat Jabatan Struktural karyawan (Super Admin/ Karyawan).
    post: Menambahkan data Riwayat Jabatan Struktural karyawan (Super Admin/ Karyawan).
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Karyawan'],
        'POST': ['Karyawan'],
    }
    queryset = DataRiwayatJabatanStrukturalKaryawan.objects.all()
    serializer_class = DataRiwayatJabatanStrukturalKaryawanSerializer

    def get_data_karyawan(self):
        user = self.request.user
        data_karyawan = DataKaryawanUser.objects.get(USER=user).DATA_KARYAWAN

        return data_karyawan

    def get_queryset(self):
        data_karyawan = self.get_data_karyawan()

        return DataRiwayatJabatanStrukturalKaryawan.objects.filter(OWNER=data_karyawan.ID)

    def perform_create(self, serializer):
        serializer.validated_data['OWNER_id'] = self.get_data_karyawan().ID

        return super(DataRiwayatJabatanStrukturalKaryawanListView, self).perform_create(serializer)

class DataRiwayatJabatanStrukturalKaryawanDetailView(APIView):
    """
    get: Menampilkan daftar Data Riwayat Jabatan Struktural Karyawan (Karyawan).
    put: Mengubah atribut keseluruhan Data Riwayat Jabatan Struktural Karyawan (Karyawan).
    patch: Mengubah beberapa atribut Data Riwayat Jabatan Struktural Karyawan (Karyawan).
    delete: Menghapus Data Riwayat Jabatan Struktural Karyawan (Karyawan).
    """
    permission_classes = [HasGroupPermissionAny]
    required_groups = {
        'GET': ['Karyawan'],
        'PUT': ['Karyawan'],
        'PATCH': ['Karyawan'],
        'DELETE': ['Karyawan'],
    }
    serializer_class = DataRiwayatJabatanStrukturalKaryawanSerializer

    def get_queryset(self,pk):
        user = self.request.user
        data_karyawan = DataKaryawanUser.objects.get(USER=user).DATA_KARYAWAN
        return DataRiwayatJabatanStrukturalKaryawan.objects.get(pk=self.kwargs['pk'], OWNER= data_karyawan.ID)

    def get(self, request, pk, *args, **kwargs):
        queryset = self.get_queryset(pk)
        serializer = self.serializer_class
        response = serializer(queryset).data

        return Response(response)

    @swagger_auto_schema(
        request_body=schema_datariwayatjabatanstrukturalkaryawan,
        responses={'200': 'Berhasil mengupdate data riwayat jabatan struktural karyawan', '400': 'Bad Request',}
    )
    def put(self, request, pk, format=None):
        queryset = self.get_queryset(pk)
        serializer = self.serializer_class(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        request_body=schema_datariwayatjabatanstrukturalkaryawan,
        responses={'200': 'Berhasil mengupdate data riwayat jabatan struktural karyawan', '400': 'Bad Request',}
    )
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

class DataRiwayatKepangkatanKaryawanListView(generics.ListCreateAPIView):
    """
    get: Menampilkan seluruh daftar Riwayat Kepangkatan karyawan (Super Admin/ Karyawan).
    post: Menambahkan data Riwayat Kepangkatan karyawan (Super Admin/ Karyawan).
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Karyawan'],
        'POST': ['Karyawan'],
    }
    queryset = DataRiwayatKepangkatanKaryawan.objects.all()
    serializer_class = DataRiwayatKepangkatanKaryawanSerializer

    def get_data_karyawan(self):
        user = self.request.user
        data_karyawan = DataKaryawanUser.objects.get(USER=user).DATA_KARYAWAN

        return data_karyawan

    def get_queryset(self):
        data_karyawan = self.get_data_karyawan()

        return DataRiwayatKepangkatanKaryawan.objects.filter(OWNER=data_karyawan.ID)

    def perform_create(self, serializer):
        serializer.validated_data['OWNER_id'] = self.get_data_karyawan().ID

        return super(DataRiwayatKepangkatanKaryawanListView, self).perform_create(serializer)

class DataRiwayatKepangkatanKaryawanDetailView(APIView):
    """
    get: Menampilkan daftar Data Riwayat Kepangkatan Karyawan (Karyawan).
    put: Mengubah atribut keseluruhan Data Riwayat Kepangkatan Karyawan (Karyawan).
    patch: Mengubah beberapa atribut Data Riwayat Kepangkatanl Karyawan (Karyawan).
    delete: Menghapus Data Riwayat Kepangkatan Karyawan (Karyawan).
    """
    permission_classes = [HasGroupPermissionAny]
    required_groups = {
        'GET': ['Karyawan'],
        'PUT': ['Karyawan'],
        'PATCH': ['Karyawan'],
        'DELETE': ['Karyawan'],
    }
    serializer_class = DataRiwayatKepangkatanKaryawanSerializer

    def get_queryset(self,pk):
        user = self.request.user
        data_karyawan = DataKaryawanUser.objects.get(USER=user).DATA_KARYAWAN
        return DataRiwayatKepangkatanKaryawan.objects.get(pk=self.kwargs['pk'], OWNER= data_karyawan.ID)

    def get(self, request, pk, *args, **kwargs):
        queryset = self.get_queryset(pk)
        serializer = self.serializer_class
        response = serializer(queryset).data

        return Response(response)

    @swagger_auto_schema(
        request_body=schema_datariwayatkepangkatankaryawan,
        responses={'200': 'Berhasil mengupdate data riwayat kepangkatan karyawan', '400': 'Bad Request',}
    )
    def put(self, request, pk, format=None):
        queryset = self.get_queryset(pk)
        serializer = self.serializer_class(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        request_body=schema_datariwayatkepangkatankaryawan,
        responses={'200': 'Berhasil mengupdate data riwayat kepangkatan karyawan', '400': 'Bad Request',}
    )
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

class DataRiwayatPendidikanFormalKaryawanListView(generics.ListCreateAPIView):
    """
    get: Menampilkan seluruh daftar Riwayat Pendidikan Formal karyawan (Super Admin/ Karyawan).
    post: Menambahkan data Riwayat Pendidikan Formal karyawan (Super Admin/ Karyawan).
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Karyawan'],
        'POST': ['Karyawan'],
    }
    queryset = DataRiwayatPendidikanFormalKaryawan.objects.all()
    serializer_class = DataRiwayatPendidikanFormalKaryawanSerializer

    def get_data_karyawan(self):
        user = self.request.user
        data_karyawan = DataKaryawanUser.objects.get(USER=user).DATA_KARYAWAN

        return data_karyawan

    def get_queryset(self):
        data_karyawan = self.get_data_karyawan()

        return DataRiwayatPendidikanFormalKaryawan.objects.filter(OWNER=data_karyawan.ID)

    def perform_create(self, serializer):
        serializer.validated_data['OWNER_id'] = self.get_data_karyawan().ID

        return super(DataRiwayatPendidikanFormalKaryawanListView, self).perform_create(serializer)

class DataRiwayatPendidikanFormalKaryawanDetailView(APIView):
    """
    get: Menampilkan daftar Data Riwayat Pendidikan Formal Karyawan (Karyawan).
    put: Mengubah atribut keseluruhan Data Riwayat Pendidikan Formal Karyawan (Karyawan).
    patch: Mengubah beberapa atribut Data Riwayat Pendidikan Formal Karyawan (Karyawan).
    delete: Menghapus Data Riwayat Pendidikan Formal Karyawan (Karyawan).
    """
    permission_classes = [HasGroupPermissionAny]
    required_groups = {
        'GET': ['Karyawan'],
        'PUT': ['Karyawan'],
        'PATCH': ['Karyawan'],
        'DELETE': ['Karyawan'],
    }
    serializer_class = DataRiwayatPendidikanFormalKaryawanSerializer

    def get_queryset(self,pk):
        user = self.request.user
        data_karyawan = DataKaryawanUser.objects.get(USER=user).DATA_KARYAWAN
        return DataRiwayatPendidikanFormalKaryawan.objects.get(pk=self.kwargs['pk'], OWNER= data_karyawan.ID)

    def get(self, request, pk, *args, **kwargs):
        queryset = self.get_queryset(pk)
        serializer = self.serializer_class
        response = serializer(queryset).data

        return Response(response)

    @swagger_auto_schema(
        request_body=schema_datariwayatpendidikanformalkaryawan,
        responses={'200': 'Berhasil mengupdate data riwayat pendidikan formal karyawan', '400': 'Bad Request',}
    )
    def put(self, request, pk, format=None):
        queryset = self.get_queryset(pk)
        serializer = self.serializer_class(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        request_body=schema_datariwayatpendidikanformalkaryawan,
        responses={'200': 'Berhasil mengupdate data riwayat pendidikan formal karyawan', '400': 'Bad Request',}
    )
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

class DataRiwayatSertifikasiKaryawanListView(generics.ListCreateAPIView):
    """
    get: Menampilkan seluruh daftar Riwayat Sertifikasi karyawan (Super Admin/ Karyawan).
    post: Menambahkan data Riwayat Sertifikasi karyawan (Super Admin/ Karyawan).
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Karyawan'],
        'POST': ['Karyawan'],
    }
    queryset = DataRiwayatSertifikasiKaryawan.objects.all()
    serializer_class = DataRiwayatSertifikasiKaryawanSerializer

    def get_data_karyawan(self):
        user = self.request.user
        data_karyawan = DataKaryawanUser.objects.get(USER=user).DATA_KARYAWAN

        return data_karyawan

    def get_queryset(self):
        data_karyawan = self.get_data_karyawan()

        return DataRiwayatSertifikasiKaryawan.objects.filter(OWNER=data_karyawan.ID)

    def perform_create(self, serializer):
        serializer.validated_data['OWNER_id'] = self.get_data_karyawan().ID

        return super(DataRiwayatSertifikasiKaryawanListView, self).perform_create(serializer)

class DataRiwayatSertifikasiKaryawanDetailView(APIView):
    """
    get: Menampilkan daftar Data Riwayat Sertifikasi Karyawan (Karyawan).
    put: Mengubah atribut keseluruhan Data Riwayat Sertifikasi Karyawan (Karyawan).
    patch: Mengubah beberapa atribut Data Riwayat Sertifikasi Karyawan (Karyawan).
    delete: Menghapus Data Riwayat Sertifikasi Karyawan (Karyawan).
    """
    permission_classes = [HasGroupPermissionAny]
    required_groups = {
        'GET': ['Karyawan'],
        'PUT': ['Karyawan'],
        'PATCH': ['Karyawan'],
        'DELETE': ['Karyawan'],
    }
    serializer_class = DataRiwayatSertifikasiKaryawanSerializer

    def get_queryset(self,pk):
        user = self.request.user
        data_karyawan = DataKaryawanUser.objects.get(USER=user).DATA_KARYAWAN
        return DataRiwayatSertifikasiKaryawan.objects.get(pk=self.kwargs['pk'], OWNER= data_karyawan.ID)

    def get(self, request, pk, *args, **kwargs):
        queryset = self.get_queryset(pk)
        serializer = self.serializer_class
        response = serializer(queryset).data

        return Response(response)

    @swagger_auto_schema(
        request_body=schema_datariwayatsertifikasikaryawan,
        responses={'200': 'Berhasil mengupdate data riwayat sertifikasi karyawan', '400': 'Bad Request',}
    )
    def put(self, request, pk, format=None):
        queryset = self.get_queryset(pk)
        serializer = self.serializer_class(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        request_body=schema_datariwayatsertifikasikaryawan,
        responses={'200': 'Berhasil mengupdate data riwayat sertifikasi karyawan', '400': 'Bad Request',}
    )
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

class DataRiwayatJabatanFungsionalKaryawanListView(generics.ListCreateAPIView):
    """
    get: Menampilkan seluruh daftar Riwayat Jabatan Fungsional karyawan (Super Admin/ Karyawan).
    post: Menambahkan data Riwayat Jabatan Fungsional karyawan (Super Admin/ Karyawan).
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Karyawan'],
        'POST': ['Karyawan'],
    }
    queryset = DataRiwayatJabatanFungsionalKaryawan.objects.all()
    serializer_class = DataRiwayatJabatanFungsionalKaryawanSerializer

    def get_data_karyawan(self):
        user = self.request.user
        data_karyawan = DataKaryawanUser.objects.get(USER=user).DATA_KARYAWAN

        return data_karyawan

    def get_queryset(self):
        data_karyawan = self.get_data_karyawan()

        return DataRiwayatJabatanFungsionalKaryawan.objects.filter(OWNER=data_karyawan.ID)

    def perform_create(self, serializer):
        serializer.validated_data['OWNER_id'] = self.get_data_karyawan().ID

        return super(DataRiwayatJabatanFungsionalKaryawanListView, self).perform_create(serializer)

class DataRiwayatJabatanFungsionalKaryawanDetailView(APIView):
    """
    get: Menampilkan daftar Data Riwayat Jabatan Fungsional Karyawan (Karyawan).
    put: Mengubah atribut keseluruhan Data Riwayat Jabatan Fungsional Karyawan (Karyawan).
    patch: Mengubah beberapa atribut Data Riwayat Jabatan Fungsional Karyawan (Karyawan).
    delete: Menghapus Data Riwayat Jabatan Fungsional Karyawan (Karyawan).
    """
    permission_classes = [HasGroupPermissionAny]
    required_groups = {
        'GET': ['Karyawan'],
        'PUT': ['Karyawan'],
        'PATCH': ['Karyawan'],
        'DELETE': ['Karyawan'],
    }
    serializer_class = DataRiwayatJabatanFungsionalKaryawanSerializer

    def get_queryset(self,pk):
        user = self.request.user
        data_karyawan = DataKaryawanUser.objects.get(USER=user).DATA_KARYAWAN
        return DataRiwayatJabatanFungsionalKaryawan.objects.get(pk=self.kwargs['pk'], OWNER= data_karyawan.ID)

    def get(self, request, pk, *args, **kwargs):
        queryset = self.get_queryset(pk)
        serializer = self.serializer_class
        response = serializer(queryset).data

        return Response(response)

    @swagger_auto_schema(
        request_body=schema_datariwayatjabatanfungsionalkaryawan,
        responses={'200': 'Berhasil mengupdate data riwayat jabatan fungsional karyawan', '400': 'Bad Request',}
    )
    def put(self, request, pk, format=None):
        queryset = self.get_queryset(pk)
        serializer = self.serializer_class(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        request_body=schema_datariwayatjabatanfungsionalkaryawan,
        responses={'200': 'Berhasil mengupdate data riwayat riwayat jabatan fungsional', '400': 'Bad Request',}
    )
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

class DataRiwayatKarirKaryawanListView(generics.ListCreateAPIView):
    """
    get: Menampilkan seluruh daftar Riwayat Karir karyawan (Super Admin/ Karyawan).
    post: Menambahkan data Riwayat Karir karyawan (Super Admin/ Karyawan).
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Karyawan'],
        'POST': ['Karyawan'],
    }
    queryset = DataRiwayatKarirKaryawan.objects.all()
    serializer_class = DataRiwayatKarirKaryawanSerializer

    def get_data_karyawan(self):
        user = self.request.user
        data_karyawan = DataKaryawanUser.objects.get(USER=user).DATA_KARYAWAN

        return data_karyawan

    def get_queryset(self):
        data_karyawan = self.get_data_karyawan()

        return DataRiwayatKarirKaryawan.objects.filter(OWNER=data_karyawan.ID)

    def perform_create(self, serializer):
        serializer.validated_data['OWNER_id'] = self.get_data_karyawan().ID

        return super(DataRiwayatKarirKaryawanListView, self).perform_create(serializer)

class DataRiwayatKarirKaryawanDetailView(APIView):
    """
    get: Menampilkan daftar Data Riwayat Karir Karyawan (Karyawan).
    put: Mengubah atribut keseluruhan Data Riwayat Karir Karyawan (Karyawan).
    patch: Mengubah beberapa atribut Data Riwayat Karir Karyawan (Karyawan).
    delete: Menghapus Data Riwayat Karir Karyawan (Karyawan).
    """
    permission_classes = [HasGroupPermissionAny]
    required_groups = {
        'GET': ['Karyawan'],
        'PUT': ['Karyawan'],
        'PATCH': ['Karyawan'],
        'DELETE': ['Karyawan'],
    }
    serializer_class = DataRiwayatKarirKaryawanSerializer

    def get_queryset(self,pk):
        user = self.request.user
        data_karyawan = DataKaryawanUser.objects.get(USER=user).DATA_KARYAWAN
        return DataRiwayatKarirKaryawan.objects.get(pk=self.kwargs['pk'], OWNER= data_karyawan.ID)

    def get(self, request, pk, *args, **kwargs):
        queryset = self.get_queryset(pk)
        serializer = self.serializer_class
        response = serializer(queryset).data

        return Response(response)

    @swagger_auto_schema(
        request_body=schema_datariwayatkarirkaryawan,
        responses={'200': 'Berhasil mengupdate data riwayat karir karyawan', '400': 'Bad Request',}
    )
    def put(self, request, pk, format=None):
        queryset = self.get_queryset(pk)
        serializer = self.serializer_class(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        request_body=schema_datariwayatkarirkaryawan,
        responses={'200': 'Berhasil mengupdate data riwayat riwayat karir', '400': 'Bad Request',}
    )
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