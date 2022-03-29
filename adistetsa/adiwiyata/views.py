from re import I
from urllib import request
from kustom_autentikasi.models import *
from .models import *
from .serializers import *

from rest_framework import generics, status
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView

from adistetsa.permissions import HasGroupPermissionAny, IsSuperAdmin, is_in_group

# Create your views here.
class SanitasiDrainaseListView(generics.ListAPIView):
    """
    get: Mendapatkan list Sanitasi Drainase (All Role).
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Siswa', 'Guru', 'Orang Tua', 'Karyawan'],
    }

    queryset = SanitasiDrainase.objects.all()
    serializer_class = SanitasiDrainaseListSerializer

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

class JaringanKerjaListView(generics.ListAPIView):
    """
    get: Mendapatkan list Jaringan Kerja (All Role).
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Siswa', 'Guru', 'Orang Tua', 'Karyawan'],
    }

    queryset = JaringanKerja.objects.all()
    serializer_class = JaringanKerjaListSerializer

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

class PublikasiListView(generics.ListAPIView):
    """
    get: Mendapatkan list Publikasi (All Role).
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Siswa', 'Guru', 'Orang Tua', 'Karyawan'],
    }

    queryset = Publikasi.objects.all()
    serializer_class = PublikasiListSerializer

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

class DaftarKaderListView(generics.ListAPIView):
    """
    get: Mendapatkan list Daftar Kader (All Role).
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Siswa', 'Guru', 'Orang Tua', 'Karyawan'],
    }

    queryset = DaftarKader.objects.all()
    serializer_class = KaderListSerializer

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

class KegiatanKaderListView(generics.ListAPIView):
    """
    get: Mendapatkan list Kegiatan Kader (All Role).
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Siswa', 'Guru', 'Orang Tua', 'Karyawan'],
    }

    queryset = KegiatanKader.objects.all()
    serializer_class = KegiatanKaderListSerializer

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

class KonservasiEnergiListView(generics.ListAPIView):
    """
    get: Mendapatkan list Konservaso Energi (All Role).
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Siswa', 'Guru', 'Orang Tua', 'Karyawan'],
    }

    queryset = Konservasi.objects.all()
    serializer_class = KonservasiListSerializer

    def get_queryset(self):
        qs = Konservasi.objects.filter(KATEGORI='Energi')
        return qs
        

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

class KonservasiAirListView(generics.ListAPIView):
    """
    get: Mendapatkan list Konservasi Air (All Role).
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Siswa', 'Guru', 'Orang Tua', 'Karyawan'],
    }

    queryset = Konservasi.objects.all()
    serializer_class = KonservasiListSerializer

    def get_queryset(self):
        qs = Konservasi.objects.filter(KATEGORI='Air')
        return qs
        

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

class PembibitanPohonListView(generics.ListAPIView):
    """
    get: Mendapatkan list Pembibitan Pohon (All Role).
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Siswa', 'Guru', 'Orang Tua', 'Karyawan'],
    }

    queryset = PembibitanPohon.objects.all()
    serializer_class = PembibitanPohonListSerializer

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

class PemeliharaanPohonListView(generics.ListAPIView):
    """
    get: Mendapatkan list Pemeliharaan Pohon (All Role).
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Siswa', 'Guru', 'Orang Tua', 'Karyawan'],
    }

    queryset = PemeliharaanPohon.objects.all()
    serializer_class = PemeliharaanPohonListSerializer

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

class KaryaInovatifListView(generics.ListAPIView):
    """
    get: Mendapatkan list Karya Inovatif (All Role).
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Siswa', 'Guru', 'Orang Tua', 'Karyawan'],
    }

    queryset = KaryaInovatif.objects.all()
    serializer_class = KaryaInovatifListSerializer

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

class PenerapanPRLHListView(generics.ListAPIView):
    """
    get: Mendapatkan list Penerapan PRLH (All Role).
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Siswa', 'Guru', 'Orang Tua', 'Karyawan'],
    }

    queryset = PenerapanPRLH.objects.all()
    serializer_class = PenerapanPRLHListSerializer

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

class ReuseReduceRecycleListView(generics.ListAPIView):
    """
    get: Mendapatkan list Reuse Reduce Recycle (All Role).
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Siswa', 'Guru', 'Orang Tua', 'Karyawan'],
    }

    queryset = ReuseReduceRecycle.objects.all()
    serializer_class = ReuseReduceRecycleListSerializer

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

class PemeliharaanSampahListView(generics.ListAPIView):
    """
    get: Mendapatkan list Pemeliharaan Sampah (All Role).
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Siswa', 'Guru', 'Orang Tua', 'Karyawan'],
    }

    queryset = PemeliharaanSampah.objects.all()
    serializer_class = PemeliharaanSampahListSerializer

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)