from kustom_autentikasi.models import DataGuruUser
from .models import *
from .serializers import *
from .doc_schema import *
from rest_framework.views import Response
from rest_framework.parsers import MultiPartParser
from .models import KTSP
from .models import SilabusRPB

from rest_framework import generics, status

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
    filterset_fields = ('TAHUN_AJARAN',)
    search_fields = ('TAHUN_AJARAN__ID', 'NAMA_FILE')

    def get_serializer_class(self):
        if self.request.method == "GET":
            return KTSPListSerializer

        elif self.request.method == "POST":
            return KTSPSerializer

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

    def update(self, request, *args, **kwargs):
        try:
            return super().update(request, *args, **kwargs)
        except Exception as e:
            if ('UNIQUE' in str(e)):
                return Response(data={'error': 'Data dengan tahun ajaran yang dipilih sudah ada'}, status=status.HTTP_400_BAD_REQUEST)

            return Response(data={'error': str(e)})



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
    filterset_fields = ('MATA_PELAJARAN', 'KELAS', 'SEMESTER', 'TAHUN_AJARAN')
    search_fields = ('MATA_PELAJARAN__NAMA', 'KELAS__KODE_KELAS', 'SEMESTER__NAMA', 'TAHUN_AJARAN__TAHUN_AJARAN_AWAL', 'TAHUN_AJARAN__TAHUN_AJARAN_AKHIR')

    def get_serializer_class(self):
        if self.request.method == "GET":
            return SilabusRPBListSerializer

        elif self.request.method == "POST":
            return SilabusRPBSerializer

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
    parser_classes = (MultiPartParser,)

    queryset = SilabusRPB.objects.all()
    serializer_class = SilabusRPBSerializer

class TataTertibListView(generics.ListCreateAPIView):
    """
    get: Menampilkan Tata Tertib.
    post: Menambahkan Tata Tertib (Super Admin/ Staf Kurikulum).
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Staf Kurikulum'],
        'POST': ['Staf Kurikulum'],
    }

    queryset = TataTertib.objects.all()
    serializer_class = TataTertibSerializer
    filterset_fields = ('KETERANGAN', 'KATEGORI')
    search_fields = ('KETERANGAN', 'KATEGORI')

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class TataTertibDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    get: Menampilkan data Tata Tertib.
    put: Mengubah atribut keseluruhan data Tata Tertib.
    patch: Mengubah beberapa atribut data Tata Tertib.
    delete: Menghapus data Tata Tertib.
    """
    permission_classes = [HasGroupPermissionAny]
    required_groups = {
        'GET': ['Staf Kurikulum'],
        'PUT': ['Staf Kurikulum'],
        'PATCH': ['Staf Kurikulum'],
        'DELETE': ['Staf Kurikulum'],
    }

    queryset = TataTertib.objects.all()
    serializer_class = TataTertibSerializer

class PoinPelanggaranListView(generics.ListCreateAPIView):
    """
    get: Menampilkan Poin Pelanggaran
    post: Menambahkan Poin Pelanggaran (Super Admin/ Staf Kurikulum).
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        
        'GET': ['Siswa', 'Guru', 'Karyawan', 'Orang Tua', 'Staf Kurikulum'],
        'POST': ['Staf Kurikulum'],
    }

    queryset = PoinPelanggaran.objects.all()
    serializer_class = PoinPelanggaranSerializer

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class PoinPelanggaranDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    get: Menampilkan data Tata Tertib.
    put: Mengubah atribut keseluruhan data Tata Tertib.
    patch: Mengubah beberapa atribut data Tata Tertib.
    delete: Menghapus data Tata Tertib.
    """
    permission_classes = [HasGroupPermissionAny]
    required_groups = {
        'GET': ['Siswa', 'Guru', 'Karyawan', 'Orang Tua', 'Staf Kurikulum'],
        'PUT': ['Staf Kurikulum'],
        'PATCH': ['Staf Kurikulum'],
        'DELETE': ['Staf Kurikulum'],
    }

    queryset = PoinPelanggaran.objects.all()
    serializer_class = PoinPelanggaranSerializer

class JadwalPekanAktifListView(generics.ListAPIView):
    """
    get: Menampilkan Jadwal Pekan Aktif
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Siswa', 'Guru', 'Karyawan', 'Orang Tua', 'Staf Kurikulum'],
    }

    queryset = JadwalPekanAktif.objects.all()
    serializer_class = JadwalPekanAktifListSerializer

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class JadwalPekanAktifDetailView(generics.RetrieveAPIView):
    """
    get: Menampilkan detail Jadwal Pekan Aktif
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Siswa', 'Guru', 'Karyawan', 'Orang Tua', 'Staf Kurikulum'],
    }

    queryset = JadwalPekanAktif.objects.all()
    serializer_class = JadwalPekanAktifDetailSerializer

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class JadwalMengajarGuruListView(generics.ListAPIView):
    """
    get: Menampilkan Jadwal Mengajar (Guru).
    """
    permission_classes = [HasGroupPermissionAny]
    required_groups = {
        'GET': ['Guru'],
    }

    serializer_class = JadwalMengajarSerializer

    def get_queryset(self):
        current_user = self.request.user
        data_guru_user = DataGuruUser.objects.get(USER=current_user)
        queryset = JadwalMengajar.objects.filter(GURU=data_guru_user.DATA_GURU)
        return queryset

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class DaftarJurnalBelajarGuruListView(generics.ListAPIView):
    """
    get: Menampilkan Daftar Jurnal Belajar (Guru).
    """
    permission_classes = [HasGroupPermissionAny]
    required_groups = {
        'GET': ['Guru'],
    }

    serializer_class = DaftarJurnalBelajarGuruListSerializer

    def get_queryset(self):
        current_user = self.request.user
        data_guru_user = DataGuruUser.objects.get(USER=current_user)
        queryset = DaftarJurnalBelajar.objects.filter(GURU=data_guru_user.DATA_GURU)
        return queryset

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class JurnalBelajarGuruListView(generics.ListCreateAPIView):
    """
    get: Menampilkan Jurnal Belajar (Guru).
    """
    permission_classes = [HasGroupPermissionAny]
    required_groups = {
        'GET': ['Guru'],
        'POST': ['Guru',]
    }

    parser_classes = (MultiPartParser,)
    serializer_class = JurnalBelajarGuruSerializer

    def get_queryset(self):
        current_user = self.request.user
        data_guru_user = DataGuruUser.objects.get(USER=current_user)
        daftar_jurnal = DaftarJurnalBelajar.objects.get(pk=self.kwargs.get('pk'))
        queryset = JurnalBelajar.objects.filter(DAFTAR=daftar_jurnal, GURU=data_guru_user.DATA_GURU)
        return queryset

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return JurnalBelajarGuruListSerializer
        elif self.request.method == 'POST':
            return JurnalBelajarGuruSerializer

        return super().get_serializer_class()

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class AbsensiSiswaListView(generics.ListAPIView):
    """
    get: Menampilkan Absensi Siswa (Guru).
    """
    permission_classes = [HasGroupPermissionAny]
    required_groups = {
        'GET': ['Guru'],
    }

    parser_classes = (MultiPartParser,)
    serializer_class = AbsensiSiswaListSerializer

    def get_queryset(self):
        current_user = self.request.user
        data_guru_user = DataGuruUser.objects.get(USER=current_user)
        daftar_jurnal = DaftarJurnalBelajar.objects.get(pk=self.kwargs.get('pk'))
        queryset = JurnalBelajar.objects.filter(DAFTAR=daftar_jurnal, GURU=data_guru_user.DATA_GURU)
        return queryset

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return JurnalBelajarGuruListSerializer
        elif self.request.method == 'POST':
            return JurnalBelajarGuruSerializer

        return super().get_serializer_class()

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class TambahKelasSiswaView(generics.CreateAPIView):
    """
    post: Mendaftarkan siswa ke dalam kelas yang dipilih (Staf Kurikulum).
    """
    permission_classes = [HasGroupPermissionAny]
    required_groups = {
        'POST': ['Staf Kurikulum'],
    }

    serializer_class = TambahKelasSiswaSerializer
    queryset = KelasSiswa.objects.all()

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)