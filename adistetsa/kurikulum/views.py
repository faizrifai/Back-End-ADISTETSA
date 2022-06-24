from rest_framework import generics, status
from rest_framework.parsers import MultiPartParser
from rest_framework.views import Response
from utility.permissions import HasGroupPermissionAny, IsSuperAdmin

from .custom_filter import DaftarJurnalBelajarFilter, JadwalMengajarGuruFilter
from .doc_schema import *
from .models import *
from .serializers import *

# Create your views here.


class KTSPListView(generics.ListCreateAPIView):
    """
    get: Menampilkan daftar KTSP.
    post: Menambahkan data KTSP (Super Admin/ Staf Kurikulum).
    """
    permission_classes = [IsSuperAdmin | HasGroupPermissionAny]
    required_groups = {
        'GET': ['Staf Kurikulum'],
        'POST': ['Staf Kurikulum'],
    }
    parser_classes = (MultiPartParser,)

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
    parser_classes = (MultiPartParser,)

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
    permission_classes = [IsSuperAdmin | HasGroupPermissionAny]
    required_groups = {
        'GET': ['Staf Kurikulum'],
        'POST': ['Staf Kurikulum'],
    }
    parser_classes = (MultiPartParser,)

    queryset = SilabusRPB.objects.all()
    serializer_class = SilabusRPBSerializer
    filterset_fields = ('MATA_PELAJARAN', 'KELAS', 'SEMESTER', 'TAHUN_AJARAN')
    search_fields = ('MATA_PELAJARAN__NAMA', 'KELAS__KODE_KELAS', 'SEMESTER__NAMA',
                     'TAHUN_AJARAN__TAHUN_AJARAN_AWAL', 'TAHUN_AJARAN__TAHUN_AJARAN_AKHIR')

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


class PoinPelanggaranListView(generics.ListCreateAPIView):
    """
    get: Menampilkan Poin Pelanggaran
    post: Menambahkan Poin Pelanggaran (Super Admin/ Staf Kurikulum).
    """
    permission_classes = [IsSuperAdmin | HasGroupPermissionAny]
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
    permission_classes = [IsSuperAdmin | HasGroupPermissionAny]
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
    permission_classes = [IsSuperAdmin | HasGroupPermissionAny]
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
    filter_class = JadwalMengajarGuruFilter
    search_fields = ('GURU__NAMA_LENGKAP', 'TAHUN_AJARAN__TAHUN_AJARAN_AWAL',
                     'TAHUN_AJARAN__TAHUN_AJARAN_AKHIR', 'SEMESTER__KE', 'KELAS__KELAS__KODE_KELAS', 'MATA_PELAJARAN__NAMA')

    def get_queryset(self):
        current_user = self.request.user
        data_guru_user = apps.get_model('kustom_autentikasi', 'DataGuruUser').objects.get(USER=current_user)
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
    search_fields = ['MATA_PELAJARAN__NAMA', 'GURU__NAMA_LENGKAP',
                     'KELAS__KELAS__KODE_KELAS', 'KELAS__OFFERING__NAMA']
    filter_class = DaftarJurnalBelajarFilter

    def get_queryset(self):
        current_user = self.request.user
        data_guru_user = apps.get_model('kustom_autentikasi', 'DataGuruUser').objects.get(USER=current_user)

        queryset = DaftarJurnalBelajar.objects.filter(
            GURU=data_guru_user.DATA_GURU)

        return queryset

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class JurnalBelajarGuruListView(generics.ListCreateAPIView):
    """
    get: Menampilkan daftar pertemuan (Guru).
    post: Mengisi jurnal pertemuan (Guru).
    """
    permission_classes = [HasGroupPermissionAny]
    required_groups = {
        'GET': ['Guru'],
        'POST': ['Guru']
    }

    parser_classes = (MultiPartParser,)
    serializer_class = JurnalBelajarGuruSerializer
    search_fields = ('PERTEMUAN', 'TANGGAL_MENGAJAR', 'DESKRIPSI_MATERI')

    def get_queryset(self):
        current_user = self.request.user
        data_guru_user = apps.get_model('kustom_autentikasi', 'DataGuruUser').objects.get(USER=current_user)
        daftar_jurnal = DaftarJurnalBelajar.objects.get(
            pk=self.kwargs.get('id_jurnal_belajar_mengajar'))
        queryset = JurnalBelajar.objects.filter(
            DAFTAR=daftar_jurnal, GURU=data_guru_user.DATA_GURU)

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


class JurnalBelajarGuruDetailView(generics.RetrieveAPIView):
    """
    get: Menampilkan detail pertemuan (Guru).
    """
    permission_classes = [HasGroupPermissionAny]
    required_groups = {
        'GET': ['Guru'],
    }

    serializer_class = JurnalBelajarGuruListSerializer

    def get_queryset(self):
        current_user = self.request.user
        data_guru_user = apps.get_model('kustom_autentikasi', 'DataGuruUser').objects.get(USER=current_user)
        queryset = JurnalBelajar.objects.filter(GURU=data_guru_user.DATA_GURU)

        return queryset

    def retrieve(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class AbsensiSiswaListView(generics.ListAPIView):
    """
    get: Menampilkan presensi siswa (Guru).
    """
    permission_classes = [HasGroupPermissionAny]
    required_groups = {
        'GET': ['Guru'],
    }

    parser_classes = (MultiPartParser,)
    serializer_class = AbsensiSiswaListSerializer
    search_fields = ('NIS__NAMA',)

    def get_queryset(self):
        queryset = AbsensiSiswa.objects.filter(
            JURNAL_BELAJAR_id=self.kwargs.get('id_jurnal_belajar_pertemuan'))
        return queryset

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return AbsensiSiswaListSerializer

        return super().get_serializer_class()

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class AbsensiSiswaDetailView(generics.RetrieveUpdateAPIView):
    """
    get: Menampilkan detail presensi siswa (Guru).
    patch: Mengubah keterangan presensi siswa (Guru).
    """
    permission_classes = [HasGroupPermissionAny]
    required_groups = {
        'GET': ['Guru'],
        'PATCH': ['Guru']
    }

    # parser_classes = (MultiPartParser,)
    serializer_class = AbsensiSiswaListSerializer
    queryset = AbsensiSiswa.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return AbsensiSiswaListSerializer
        elif self.request.method == 'PATCH':
            return AbsensiSiswaSerializer

        return super().get_serializer_class()

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)


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
