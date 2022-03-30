from django.db.models import Sum
from kurikulum.enums import ENUM_BULAN
from kustom_autentikasi.models import *
from .models import *
from .serializers import *

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

import datetime as dt

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
    search_fields = ('NAMA_KEGIATAN',)

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
    search_fields = ('NAMA_KEGIATAN',)

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
    search_fields = ('NAMA_KEGIATAN',)

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
    search_fields = ('NIS__NAMA', 'NIS__NIS')

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
    search_fields = ('NAMA_KEGIATAN',)

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
    search_fields = ('NAMA_KEGIATAN',)

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
    search_fields = ('NAMA_KEGIATAN',)

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
    search_fields = ('NAMA_KEGIATAN',)

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
    search_fields = ('NAMA_KEGIATAN',)

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
    search_fields = ('NAMA_INOVATOR', 'NAMA_KARYA_INOVATIF', 'JENIS')

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
    search_fields = ('NAMA_KEGIATAN', 'PESERTA')

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
    search_fields = ('NAMA_KEGIATAN', 'PIHAK_TERLIBAT')

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
    search_fields = ('NAMA_KEGIATAN',)

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

class PenanamanPohonListView(generics.ListAPIView):
    """
    get: Mendapatkan list Penanaman Pohon (All Role).
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Siswa', 'Guru', 'Orang Tua', 'Karyawan'],
    }

    queryset = PenanamanPohon.objects.all()
    serializer_class = PenanamanPohonListSerializer
    search_fields = ('NAMA_KEGIATAN',)

    def list(self, request, *args, **kwargs):
        response = super().list(request, args, kwargs)
        new_data = response.data
        new_data.update({
            'TOTAL_POHON': PenanamanPohon.objects.all().aggregate(Sum('JUMLAH'))['JUMLAH__sum'],
        })
        response.data = new_data

        return response

class TabunganSampahModel(object):
    def __init__(self, bulan, sampah_kering, sampah_basah, total_tabungan):
        self.bulan = bulan
        self.sampah_kering = sampah_kering
        self.sampah_basah = sampah_basah
        self.total_tabungan = total_tabungan

class FilterTahunListView(APIView):
    """
    GET: Menampilan daftar tahun untuk filter Tabungan Sampah.
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Siswa', 'Guru', 'Orang Tua', 'Karyawan'],
    }

    def get(self, request, *args, **kwargs):
        qs = TabunganSampah.objects.all()

        # initialize years
        years = []
        for data in qs:
            years.append({'TAHUN': data.TANGGAL.year})

        years = sorted(years, key=lambda d: d['TAHUN']) 

        return Response(years)

class TabunganSampahListView(APIView):
    """
    get: Mendapatkan list Tabungan Sampah (All Role).
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Siswa', 'Guru', 'Orang Tua', 'Karyawan'],
    }

    def get_queryset(self):
        daftar_bulan = [
            'Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni',
            'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember'
        ]

        tahun = self.request.query_params.get('TAHUN')
        if tahun:
            qs = TabunganSampah.objects.filter(TANGGAL__year=tahun)
        else:
            now = dt.datetime.now()
            qs = TabunganSampah.objects.filter(TANGGAL__year=now.year)

        data = []

        for bulan in daftar_bulan:
            sampah_kering = 0
            sampah_basah = 0
            total_tabungan = 0

            data.append(
                TabunganSampahModel(
                    bulan = bulan,
                    sampah_kering = sampah_kering,
                    sampah_basah = sampah_basah,
                    total_tabungan = total_tabungan
                )
            )
            
        for record in qs:
            for o in data:
                if o.bulan == ENUM_BULAN[record.TANGGAL.month-1][0]:
                    if record.KATEGORI == 'Basah':
                        o.sampah_basah += int(record.JUMLAH)
                    elif record.KATEGORI == 'Kering':
                        o.sampah_kering += int(record.JUMLAH)

                    o.total_tabungan = o.sampah_basah + o.sampah_kering

        return data

    def get(self, request, format=None):
        data = self.get_queryset()

        tahun = self.request.query_params.get('TAHUN')
        if tahun:
            filter_tahun = tahun
        else:
            now = dt.datetime.now()
            filter_tahun = now.year

        sampah_kering = TabunganSampah.objects.filter(TANGGAL__year=filter_tahun, KATEGORI='Kering').aggregate(Sum('JUMLAH'))['JUMLAH__sum'],
        sampah_basah = TabunganSampah.objects.filter(TANGGAL__year=filter_tahun, KATEGORI='Basah').aggregate(Sum('JUMLAH'))['JUMLAH__sum'],
        total_tabungan = TabunganSampah.objects.filter(TANGGAL__year=filter_tahun).aggregate(Sum('JUMLAH'))['JUMLAH__sum'],

        if not sampah_kering[0]:
            sampah_kering = (0,)
        
        if not sampah_basah[0]:
            sampah_basah = (0,)

        if not total_tabungan[0]:
            total_tabungan = (0,)

        serializer = TabunganSampahListSerializer(data, many=True)

        new_data = {}
        new_data['results'] = list(serializer.data)
        new_data['SAMPAH_KERING'] = sampah_kering[0]
        new_data['SAMPAH_BASAH'] =  sampah_basah[0]
        new_data['TOTAL_TABUNGAN'] =  total_tabungan[0]
        
        return Response(new_data)