from kustom_autentikasi.models import *
from kurikulum.models import Jurusan, NamaOfferingKelas
from rest_framework import generics, status
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView

from .filters import AngketFilter
from .models import *
from .serializers import *

from utility.permissions import HasGroupPermissionAny, IsSuperAdmin, is_in_group

class ProfilKonselorView(APIView):
    """
    GET: Menampilan profil konselor.
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Staf BK'],
        'PATCH': ['Staf BK'],
    }

    queryset = KatalogKonselor.objects.all()
    serializer_class = KonselorDetailSerializer

    parser_classes = (MultiPartParser,)

    def get_queryset(self):
        current_user = self.request.user
        if (is_in_group(current_user, 'Staf BK')):
            try:
                queryset = KatalogKonselor.objects.get(USER=current_user)
            except KatalogKonselor.DoesNotExist:
                data_guru_user = DataGuruUser.objects.get(USER=current_user)
                queryset = KatalogKonselor.objects.create(
                USER = data_guru_user.USER,
                NAMA = data_guru_user.DATA_GURU.NAMA_LENGKAP,
                KOMPETENSI = '',
                ALUMNUS = '',
                WHATSAPP = 'https://wa.me/',
                CONFERENCE = 'https://meet.google.com'
                )

            return queryset

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class
        response = serializer(queryset).data
        return Response(response)

    def patch(self, request, format=None):
        queryset = self.get_queryset()
        roleSerializer = self.serializer_class
        serializer = roleSerializer(queryset, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class KatalogKonselorListView(generics.ListAPIView):
    """
    GET: Menampilan profil konselor.
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Siswa', 'Guru', 'Karyawan', 'Orang Tua'],
    }

    queryset = KatalogKonselor.objects.all().order_by('NAMA')
    serializer_class = KatalogKonselorListSerializer
    search_fields = ('NAMA',)

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

class KatalogKonselorDetailView(generics.RetrieveAPIView):
    """
    GET: Menampilkan detail konselor.
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Siswa', 'Guru', 'Karyawan', 'Orang Tua'],
    }

    queryset = KatalogKonselor.objects.all()
    serializer_class = KatalogKonselorDetailSerializer

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

class DaftarKonsultasiListView(generics.ListAPIView):
    """
    get: Menampilkan daftar konsultasi.
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Staf BK'],
    }

    queryset = Konsultasi.objects.all()
    serializer_class = KonsultasiListSerializer

    def get_queryset(self):
        current_user = self.request.user
        query_params = self.request.query_params

        if query_params.get('search'):
            data_siswa_user = DataSiswaUser.objects.filter(DATA_SISWA__NAMA__icontains=query_params.get('search'))
            data_guru_user = DataGuruUser.objects.filter(DATA_GURU__NAMA_LENGKAP__icontains=query_params.get('search'))
            data_karyawan_user = DataKaryawanUser.objects.filter(DATA_KARYAWAN__NAMA_LENGKAP__icontains=query_params.get('search'))

            print(data_siswa_user)

            ids = []
            for data in data_siswa_user:
                ids.append(data.USER.pk)

            for data in data_guru_user:
                ids.append(data.USER.pk)

            for data in data_karyawan_user:
                ids.append(data.USER.pk)

            queryset = Konsultasi.objects.filter(USER__pk__in=ids)

            if (is_in_group(current_user, 'Staf BK')):
                queryset = queryset.filter(KONSELOR__USER=current_user)
            else:
                queryset = queryset.filter(USER=current_user)

            return queryset.order_by('-TANGGAL_KONSULTASI')

        if (not is_in_group(current_user, 'Staf BK')):
            queryset = Konsultasi.objects.filter(USER=current_user)

            return queryset.order_by('-TANGGAL_KONSULTASI')

        return super().get_queryset().filter(KONSELOR__USER=current_user).order_by('-TANGGAL_KONSULTASI')

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

class DaftarKonsultasiDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    PUT: Mengubah semua data konsultasi.
    PATCH: Mengubah beberapa data konsultasi.
    GET: Menampilan satu data konsultasi.
    DELETE: Menghapus data konsultasi.
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Staf BK', 'Siswa', 'Guru', 'Orang Tua', 'Karyawan'],
        'PUT': ['Staf BK'],
        'PATCH': ['Staf BK', 'Siswa', 'Guru', 'Orang Tua', 'Karyawan'],
        'DELETE': ['Staf BK', 'Siswa', 'Guru', 'Orang Tua', 'Karyawan'],
    }

    queryset = Konsultasi.objects.all()
    serializer_class = KonsultasiDetailSerializer

    def get_serializer_class(self):
        current_user = self.request.user
        if (is_in_group(current_user, 'Staf BK')):
            qs = self.get_object()
            if (is_in_group(qs.USER, 'Orang Tua')):
                return KonsultasiDetailOrangTuaSerializer
            elif (is_in_group(qs.USER, 'Siswa')):
                return KonsultasiDetailSiswaSerializer
            elif (is_in_group(qs.USER, 'Guru')):
                return KonsultasiDetailGuruSerializer
            elif (is_in_group(qs.USER, 'Karyawan')):
                return KonsultasiDetailKaryawanSerializer
        else:
            if (is_in_group(current_user, 'Orang Tua')):
                return KonsultasiDetailOrangTuaSerializer
            elif (is_in_group(current_user, 'Siswa')):
                return KonsultasiDetailSiswaSerializer
            elif (is_in_group(current_user, 'Guru')):
                return KonsultasiDetailGuruSerializer
            elif (is_in_group(current_user, 'Karyawan')):
                return KonsultasiDetailKaryawanSerializer

        return super().get_serializer_class()

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

class PengajuanKonsultasiView(generics.ListCreateAPIView):
    """
    post: Menambahkan data Pengajuan Pengajuan Konsultasi (All Role).
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'POST': ['Siswa', 'Guru', 'Orang Tua', 'Karyawan'],
    }

    queryset = Konsultasi.objects.all()
    serializer_class = KonsultasiDetailSerializer

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

class PengajuanKonsultasiNonStafListView(generics.ListAPIView):
    """
    get: Mendapatkan status pengajuan saat ini (All Role).
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Siswa', 'Guru', 'Orang Tua', 'Karyawan'],
    }

    queryset = Konsultasi.objects.all().order_by('-TANGGAL_KONSULTASI')
    serializer_class = PengajuanKonsultasiListSerializer
    search_fields = ('KONSELOR__NAMA',)

    def get_queryset(self):
        current_user = self.request.user
        qs = Konsultasi.objects.filter(USER = current_user)

        return qs.order_by('-TANGGAL_KONSULTASI')

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

class DaftarAlumniListView(generics.ListAPIView):
    """
    get: Menampilkan daftar alumni.
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Staf BK', 'Alumni'],
    }

    queryset = DataAlumni.objects.all()
    serializer_class = DataAlumniListSerializer
    search_fields = ('NAMA_SISWA', 'NISN')

    def get_queryset(self):
        current_user = self.request.user
        if (not is_in_group(current_user, 'Staf BK')):
            data_siswa = DataSiswaUser.objects.get(USER=current_user).DATA_SISWA
            queryset = DataAlumni.objects.filter(NIS=data_siswa.NIS)

            return queryset

        return super().get_queryset()

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

class DaftarAlumniDetailView(generics.RetrieveUpdateAPIView):
    """
    get: Menampilkan daftar alumni pilihan.
    put: Mengubah semua data alumni pilihan.
    patch: Mengubah beberapa data daftar alumni pilihan.
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Staf BK', 'Alumni'],
        'PUT': ['Staf BK'],
        'PATCH': ['Staf BK', 'Alumni'],
    }

    queryset = DataAlumni.objects.all()
    serializer_class = DataAlumniDetailSerializer

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

class AngketPeminatanListView(generics.ListAPIView):
    """
    get: Menampilkan data daftar Angket Peminatan.
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Staf BK'],
    }

    parser_classes = (MultiPartParser,)
    queryset = PeminatanLintasMinat.objects.all()
    serializer_class = PeminatanLintasMinatListSerializer
    filter_class = AngketFilter
    search_fields = ('KELAS_SISWA__NIS__NAMA',)

    def get_queryset(self):
        qs = PeminatanLintasMinat.objects.filter(KATEGORI='Angket Peminatan')
        return qs

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

class AngketPeminatanSiswaDetailView(APIView):
    """
    get: Melihat data Angket Peminatan
    patch: Mengedit data Angket Peminatan
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Siswa'],
        'PATCH': ['Siswa'],
    }

    parser_classes = (MultiPartParser,)
    queryset = PeminatanLintasMinat.objects.all()
    serializer_class = PeminatanLintasMinatListSerializer
    search_fields = ('KELAS_SISWA__NIS__NAMA',)

    def get_queryset(self):
        current_user = self.request.user
        if (is_in_group(current_user, 'Siswa')):
            data_siswa = DataSiswaUser.objects.get(USER=current_user).DATA_SISWA
            kelas_siswa = KelasSiswa.objects.filter(NIS=data_siswa, KELAS__KELAS__TINGKATAN='X').first()
            try:
                queryset = PeminatanLintasMinat.objects.get(KELAS_SISWA=kelas_siswa, KATEGORI='Angket Peminatan')
            except PeminatanLintasMinat.DoesNotExist:
                queryset = PeminatanLintasMinat.objects.create(KELAS_SISWA=kelas_siswa, KATEGORI='Angket Peminatan')

            return queryset

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class
        response = serializer(queryset).data
        return Response(response)

    def patch(self, request, format=None):
        queryset = self.get_queryset()
        roleSerializer = self.serializer_class
        serializer = roleSerializer(queryset, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AngketLintasMinatListView(generics.ListAPIView):
    """
    get: Menampilkan data daftar Angket Lintas Minat.
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Staf BK'],
    }

    parser_classes = (MultiPartParser,)
    queryset = PeminatanLintasMinat.objects.all()
    serializer_class = PeminatanLintasMinatListSerializer
    filter_class = AngketFilter
    search_fields = ('KELAS_SISWA__NIS__NAMA',)

    def get_queryset(self):
        qs = PeminatanLintasMinat.objects.filter(KATEGORI='Angket Lintas Minat')
        return qs

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

class AngketLintasMinatSiswaDetailView(APIView):
    """
    get: Melihat data Angket Lintas Minat
    patch: Mengedit data Angket Lintas Minat
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Siswa'],
        'PATCH': ['Siswa'],
    }

    parser_classes = (MultiPartParser,)
    queryset = PeminatanLintasMinat.objects.all()
    serializer_class = PeminatanLintasMinatListSerializer

    def get_queryset(self):
        current_user = self.request.user
        if (is_in_group(current_user, 'Siswa')):
            data_siswa = DataSiswaUser.objects.get(USER=current_user).DATA_SISWA
            kelas_siswa = KelasSiswa.objects.filter(NIS=data_siswa, KELAS__KELAS__TINGKATAN='X').first()
            try:
                queryset = PeminatanLintasMinat.objects.get(KELAS_SISWA=kelas_siswa, KATEGORI='Angket Lintas Minat')
            except PeminatanLintasMinat.DoesNotExist:
                queryset = PeminatanLintasMinat.objects.create(KELAS_SISWA=kelas_siswa, KATEGORI='Angket Lintas Minat')

            return queryset

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class
        response = serializer(queryset).data
        return Response(response)

    def patch(self, request, format=None):
        queryset = self.get_queryset()
        roleSerializer = self.serializer_class
        serializer = roleSerializer(queryset, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AngketDataDiriListView(generics.ListAPIView):
    """
    get: Menampilkan data daftar Angket Data Diri.
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Staf BK'],
    }

    queryset = PeminatanLintasMinat.objects.all()
    serializer_class = PeminatanLintasMinatListSerializer
    parser_classes= (MultiPartParser,)
    filter_class = AngketFilter
    search_fields = ('KELAS_SISWA__NIS__NAMA',)

    def get_queryset(self):
        qs = PeminatanLintasMinat.objects.filter(KATEGORI='Angket Data Diri')
        return qs

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

class AngketDataDiriSiswaDetailView(APIView):
    """
    get: Melihat data Angket Data Diri
    patch: Mengedit data Angket Data Diri
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Siswa'],
        'PATCH': ['Siswa'],
    }

    parser_classes = (MultiPartParser,)
    queryset = PeminatanLintasMinat.objects.all()
    serializer_class = PeminatanLintasMinatListSerializer

    def get_queryset(self):
        current_user = self.request.user
        if (is_in_group(current_user, 'Siswa')):
            data_siswa = DataSiswaUser.objects.get(USER=current_user).DATA_SISWA
            kelas_siswa = KelasSiswa.objects.filter(NIS=data_siswa, KELAS__KELAS__TINGKATAN='X').first()
            try:
                queryset = PeminatanLintasMinat.objects.get(KELAS_SISWA=kelas_siswa, KATEGORI='Angket Data Diri')
            except PeminatanLintasMinat.DoesNotExist:
                queryset = PeminatanLintasMinat.objects.create(KELAS_SISWA=kelas_siswa, KATEGORI='Angket Data Diri')

            return queryset

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class
        response = serializer(queryset).data
        return Response(response)

    def patch(self, request, format=None):
        queryset = self.get_queryset()
        roleSerializer = self.serializer_class
        serializer = roleSerializer(queryset, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ParameterJurusanListView(generics.ListAPIView):
    """
    GET: Menampilan parameter untuk filter jurusan.
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Staf BK'],
    }

    queryset = Jurusan.objects.all()
    serializer_class = ParameterJurusanListSerializer

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

class ParameterKelasListView(generics.ListAPIView):
    """
    GET: Menampilan parameter untuk filter kelas.
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Staf BK'],
    }

    queryset = NamaOfferingKelas.objects.all()
    serializer_class = ParameterKelasListSerializer

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)