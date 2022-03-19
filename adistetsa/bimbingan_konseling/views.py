from django.shortcuts import render
from kustom_autentikasi.models import *
from .models import *
from .serializers import *

from rest_framework import generics, status
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView

from adistetsa.permissions import HasGroupPermissionAny, IsSuperAdmin, is_in_group

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

    parser_classes= (MultiPartParser,)

    def get_queryset(self):
        current_user = self.request.user
        if (is_in_group(current_user, 'Staf BK')):
            queryset = KatalogKonselor.objects.get(USER=current_user)
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

    # def list(self, request, *args, **kwargs):
    #     return super().list(request, *args, **kwargs)

class KatalogKonselorListView(generics.ListAPIView):
    """
    GET: Menampilan profil konselor.
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Siswa', 'Guru', 'Karyawan', 'Orang Tua'],
    }

    queryset = KatalogKonselor.objects.all()
    serializer_class = KatalogKonselorListSerializer

    def get_queryset(self):
        current_user = self.request.user
        if (not is_in_group(current_user, 'Staf BK')):
            queryset = KatalogKonselor.objects.filter(USER=current_user)
            return queryset

        return super().get_queryset()

    # def get_user(self, obj): 
    #     if (is_in_group(obj.USER, 'Staf BK')):
    #         data_guru = DataGuruUser.objects.get(USER=obj.USER).DATA_GURU
    #         queryset = DataGuru.objects.filter(NAMA=data_guru.NAMA_LENGKAP)

    #         return queryset 

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

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
        if (not is_in_group(current_user, 'Staf BK')):
            queryset = Konsultasi.objects.filter(USER=current_user)
            return queryset

        return super().get_queryset()

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

class DaftarKonsultasiDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    PUT: Mengubah semua data konsultasi.
    PATCH: Mengubah beberapa data konsultasi.
    GET: Menampilan satu data konsultasi.
    DELETE: Menghapus data konsultasi
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
        if (is_in_group(current_user, 'Orang Tua')):
            return KonsultasiDetailOrangTuaSerializer
        elif (is_in_group(current_user, 'Staf BK')):
            qs = self.get_object()
            if (is_in_group(qs.USER, 'Orang Tua')):
                return KonsultasiDetailOrangTuaSerializer
            elif (is_in_group(qs.USER, 'Siswa')):
                return KonsultasiDetailSiswaSerializer
            elif (is_in_group(qs.USER, 'Guru')):
                return KonsultasiDetailGuruSerializer
            elif (is_in_group(qs.USER, 'Karyawan')):
                return KonsultasiDetailKaryawanSerializer
        return super().get_serializer_class()
    
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

class PengajuanKonsultasiView(generics.CreateAPIView):
    """
    post: Menambahkan data Pengajuan Pengajuan Konsultasi (All Role).
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'POST': ['Siswa', 'Guru', 'Orang Tua', 'Karyawan'],
    }
    parser_classes = (MultiPartParser,)

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
    parser_classes = (MultiPartParser,)

    queryset = Konsultasi.objects.all()
    serializer_class = PengajuanKonsultasiListSerializer

    def get_queryset(self):
        current_user = self.request.user
        qs = Konsultasi.objects.filter(USER = current_user)

        return qs

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
    PUT: Mengubah semua data alumni pilihan.
    PATCH: Mengubah beberapa data daftar alumni pilihan.
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Staf BK','Alumni'],
        'PUT': ['Staf BK'],
        'PATCH': ['Staf BK', 'Alumni'],
    }

    queryset = DataAlumni.objects.all()
    serializer_class = DataAlumniDetailSerializer

    def retrieve(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

class AngketPeminatanListView(generics.ListCreateAPIView):
    """
    get: Menampilkan data daftar Angket Peminatan.
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Staf BK'],
        'Create': ['Siswa'],
    }
    
    parser_classes= (MultiPartParser,)
    queryset = PeminatanLintasMinat.objects.all()
    serializer_class = PeminatanLintasMinatListSerializer

    def get_queryset(self):
        qs = PeminatanLintasMinat.objects.filter(KATEGORI='Angket Peminatan')
        return qs

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs) 

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)  

class AngketLintasMinatListView(generics.ListCreateAPIView):
    """
    get: Menampilkan data daftar Angket Lintas Minat.
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Staf BK'],
        'Create': ['Siswa'],
    }

    parser_classes= (MultiPartParser,)
    queryset = PeminatanLintasMinat.objects.all()
    serializer_class = PeminatanLintasMinatListSerializer

    def get_queryset(self):
        qs = PeminatanLintasMinat.objects.filter(KATEGORI='Angket Lintas Minat')
        return qs
 
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

class AngketDataDiriListView(generics.ListCreateAPIView):
    """
    get: Menampilkan data daftar Angket Data Diri.
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Staf BK'],
        'Create': ['Siswa'],
    }

    queryset = PeminatanLintasMinat.objects.all()
    serializer_class = PeminatanLintasMinatListSerializer
    parser_classes= (MultiPartParser,)

    def get_queryset(self):
        qs = PeminatanLintasMinat.objects.filter(KATEGORI='Angket Data Diri')
        return qs
        
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs) 
    
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

# # Create your views here.
# def booked_event_page_view(request):
#    # getting queryset
#     currentUser = request.user
#     bookedEvents = models.BookedEvent.objects.filter(user=currentUser)
#     # adding event filter
#     filter = JurusanFilter(request.GET, queryset=bookedEvents)
#     bookedEvents = filter.qs
#     context = {'bookedEvents': bookedEvents, 'filter':filter}
#     return render(request, 'booked_events.html', context)