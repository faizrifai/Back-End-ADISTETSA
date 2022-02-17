from kustom_autentikasi.models import *
from .models import *
from .serializers import *
from .utility import check_buku_tersedia

from rest_framework import generics, status
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView

from adistetsa.permissions import HasGroupPermissionAny, IsSuperAdmin, is_in_group


# Create your views here. 
class KatalogBukuListView(generics.ListAPIView):
    """
    get: Menampilkan daftar katalog buku.
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Staf Perpustakaan', 'Guru', 'Siswa'],
    }

    queryset = KatalogBuku.objects.all()
    serializer_class = KatalogBukuListSerializer
    search_fields = ('JUDUL', 'KODE_AUTHOR__NAMA_AUTHOR', 'BAHASA__BAHASA', 'KODE_TIPE__NAMA_TIPE', 'TAHUN_TERBIT__TAHUN_TERBIT')

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class KatalogBukuDetailView(generics.RetrieveAPIView):
    """
    get: Menampilkan detail buku.
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Staf Perpustakaan', 'Guru', 'Siswa'],
    }

    queryset = KatalogBuku.objects.all()
    serializer_class = KatalogBukuListSerializer

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class KatalogBukuTersediaListView(generics.ListAPIView):
    """
    get: Menampilkan daftar katalog buku yang bisa dipinjam.
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Staf Perpustakaan', 'Guru', 'Siswa'],
    }

    queryset = KatalogBukuCopy.objects.all()
    serializer_class = KatalogBukuCopySerializer
    search_fields = (
        'DATA_DONASI__REGISTER_DONASI__JUDUL',
        'DATA_DONASI__REGISTER_DONASI__KODE_AUTHOR__NAMA_AUTHOR',
        'DATA_DONASI__REGISTER_DONASI__BAHASA__BAHASA',
        'DATA_DONASI__REGISTER_DONASI__KODE_TIPE__NAMA_TIPE',
        'DATA_DONASI__REGISTER_DONASI__TAHUN_TERBIT__TAHUN_TERBIT'
    )

    def get_queryset(self):
        queryset = KatalogBukuCopy.objects.filter(STATUS='Sudah Dikembalikan')

        return queryset

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class PengajuanPeminjamanSiswaListView(generics.ListCreateAPIView):
    """
    get: Menampilkan daftar pengajuan peminjaman (Siswa).
    post: Membuat pengajuan peminjaman (Siswa).
    """

    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Siswa'],
        'POST': ['Siswa'],
    }

    parser_classes = (MultiPartParser,)
    queryset = PengajuanPeminjamanSiswa.objects.all()
    serializer_class = PengajuanPeminjamanSiswaSerializer
    search_fields = ('BUKU__DATA_DONASI__REGISTER_DONASI__JUDUL', 'STATUS_PENGAJUAN', 'NIS__NIS', 'NIS__NAMA',)

    def get_queryset(self):
        current_user = self.request.user
        if (is_in_group(current_user, 'Siswa')):
            data_siswa_user = DataSiswaUser.objects.get(USER=current_user)
            queryset = PengajuanPeminjamanSiswa.objects.filter(NIS=data_siswa_user.DATA_SISWA)
            return queryset

        return super().get_queryset()

    def get_serializer_class(self):
        current_user = self.request.user
        if (is_in_group(current_user, 'Siswa')):
            if self.request.method == 'GET':
                return PengajuanPeminjamanSiswaListSerializer
            elif self.request.method == "POST":
                return PengajuanPeminjamanSiswaSerializer

        return super().get_serializer_class()

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
        
    def create(self, request, *args, **kwargs):
        buku = request.data['BUKU']

        if (check_buku_tersedia(buku)):
            return super().create(request, *args, **kwargs)
        else:
            return Response(data={'error': 'Buku yang dipilih tidak tersedia untuk dipinjam.'}, status=status.HTTP_404_NOT_FOUND)


class PengajuanPeminjamanSiswaDetailView(generics.RetrieveAPIView):
    """
    get: Menampilkan detail pengajuan peminjaman (Siswa).
    """

    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Siswa'],
    }

    queryset = PengajuanPeminjamanSiswa.objects.all()
    serializer_class = PengajuanPeminjamanSiswaListSerializer

    def get_queryset(self):
        current_user = self.request.user
        if (is_in_group(current_user, 'Siswa')):
            data_siswa_user = DataSiswaUser.objects.get(USER=current_user)
            queryset = PengajuanPeminjamanSiswa.objects.filter(NIS=data_siswa_user.DATA_SISWA)
            return queryset

        return super().get_queryset()


class PengajuanPeminjamanSiswaAdminListView(generics.ListAPIView):
    """
    get: Menampilkan daftar pengajuan peminjaman (Staf Perpustakaan).
    """

    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Staf Perpustakaan'],
    }

    queryset = PengajuanPeminjamanSiswa.objects.all()
    serializer_class = PengajuanPeminjamanSiswaAdminSerializer
    search_fields = ('BUKU__DATA_DONASI__REGISTER_DONASI__JUDUL', 'STATUS_PENGAJUAN', 'NIS__NIS', 'NIS__NAMA',)

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class PengajuanPeminjamanSiswaAdminDetailView(generics.RetrieveAPIView):
    """
    get: Menampilkan detail pengajuan peminjaman (Staf Perpustakaan).
    """

    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Staf Perpustakaan'],
        'POST': ['Staf Perpustakaan'],
    }

    queryset = PengajuanPeminjamanSiswa.objects.all()
    serializer_class = PengajuanPeminjamanSiswaAdminSerializer

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class PengajuanPeminjamanGuruListView(generics.ListCreateAPIView):
    """
    get: Menampilkan daftar pengajuan peminjaman (Guru).
    post: Membuat pengajuan peminjaman (Guru).
    """

    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Guru'],
        'POST': ['Guru'],
    }

    parser_classes = (MultiPartParser,)
    queryset = PengajuanPeminjamanGuru.objects.all()
    serializer_class = PengajuanPeminjamanGuruSerializer
    search_fields = ('BUKU__DATA_DONASI__REGISTER_DONASI__JUDUL', 'STATUS_PENGAJUAN', 'DATA_GURU__NIK', 'DATA_GURU__NAMA_LENGKAP',)

    def get_queryset(self):
        current_user = self.request.user
        if (is_in_group(current_user, 'Guru')):
            data_guru_user = DataGuruUser.objects.get(USER=current_user)
            queryset = PengajuanPeminjamanGuru.objects.filter(DATA_GURU=data_guru_user.DATA_GURU)
            return queryset

        return super().get_queryset()

    def get_serializer_class(self):
        current_user = self.request.user
        if (is_in_group(current_user, 'Guru')):
            if self.request.method == 'GET':
                return PengajuanPeminjamanGuruListSerializer
            elif self.request.method == "POST":
                return PengajuanPeminjamanGuruSerializer

        return super().get_serializer_class()


    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
        
    def create(self, request, *args, **kwargs):
        buku = request.data['BUKU']

        if (check_buku_tersedia(buku)):
            return super().create(request, *args, **kwargs)
        else:
            return Response(data={'error': 'Buku yang dipilih tidak tersedia untuk dipinjam.'}, status=status.HTTP_404_NOT_FOUND)


class PengajuanPeminjamanGuruDetailView(generics.RetrieveAPIView):
    """
    get: Menampilkan detail pengajuan peminjaman (Guru).
    """

    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Guru'],
    }

    queryset = PengajuanPeminjamanSiswa.objects.all()
    serializer_class = PengajuanPeminjamanGuruListSerializer

    def get_queryset(self):
        current_user = self.request.user
        if (is_in_group(current_user, 'Guru')):
            data_guru_user = DataGuruUser.objects.get(USER=current_user)
            queryset = PengajuanPeminjamanGuru.objects.filter(DATA_GURU=data_guru_user.DATA_GURU)
            return queryset

        return super().get_queryset()


class PengajuanPeminjamanGuruAdminListView(generics.ListAPIView):
    """
    get: Menampilkan daftar pengajuan peminjaman (Staf Perpustakaan).
    """

    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Staf Perpustakaan'],
        'POST': ['Staf Perpustakaan'],
    }

    queryset = PengajuanPeminjamanGuru.objects.all()
    serializer_class = PengajuanPeminjamanGuruAdminSerializer
    search_fields = ('BUKU__DATA_DONASI__REGISTER_DONASI__JUDUL', 'STATUS_PENGAJUAN', 'DATA_GURU__NIK', 'DATA_GURU__NAMA_LENGKAP',)

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class PengajuanPeminjamanGuruAdminDetailView(generics.RetrieveAPIView):
    """
    get: Menampilkan detail pengajuan peminjaman (Staf Perpustakaan).
    """

    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Staf Perpustakaan'],
        'POST': ['Staf Perpustakaan'],
    }

    queryset = PengajuanPeminjamanGuru.objects.all()
    serializer_class = PengajuanPeminjamanGuruAdminSerializer

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class RiwayatPeminjamanSiswaListView(generics.ListAPIView):
    """
    get: Menampilkan daftar riwayat peminjaman siswa (Siswa).
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Siswa'],
    }

    queryset = RiwayatPeminjamanSiswa.objects.all()
    serializer_class = RiwayatPeminjamanSiswaSerializer
    search_fields = ('BUKU__DATA_DONASI__REGISTER_DONASI__JUDUL', 'STATUS_PEMINJAMAN', 'NIS__NIS', 'NIS__NAMA', 'JANGKA_PEMINJAMAN')

    def get_queryset(self):
        current_user = self.request.user
        if (is_in_group(current_user, 'Siswa')):
            data_siswa_user = DataSiswaUser.objects.get(USER=current_user)
            queryset = RiwayatPeminjamanSiswa.objects.filter(NIS=data_siswa_user.DATA_SISWA)
            return queryset

        return super().get_queryset()

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class RiwayatPeminjamanSiswaDetailView(generics.RetrieveAPIView):
    """
    get: Menampilkan detail riwayat peminjaman siswa (Siswa).
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Siswa'],
    }

    queryset = RiwayatPeminjamanSiswa.objects.all()
    serializer_class = RiwayatPeminjamanSiswaSerializer

    def get_queryset(self):
        current_user = self.request.user
        if (is_in_group(current_user, 'Siswa')):
            data_siswa_user = DataSiswaUser.objects.get(USER=current_user)
            queryset = RiwayatPeminjamanSiswa.objects.filter(NIS=data_siswa_user.DATA_SISWA)
            return queryset

        return super().get_queryset()

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class RiwayatPeminjamanSiswaAdminListView(generics.ListAPIView):
    """
    get: Menampilkan daftar riwayat peminjaman siswa (Staf Perpustakaan).
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Staf Perpustakaan'],
    }

    queryset = RiwayatPeminjamanSiswa.objects.all()
    serializer_class = RiwayatPeminjamanSiswaAdminSerializer
    search_fields = ('BUKU__DATA_DONASI__REGISTER_DONASI__JUDUL', 'STATUS_PEMINJAMAN', 'NIS__NIS', 'NIS__NAMA', 'JANGKA_PEMINJAMAN')

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class RiwayatPeminjamanSiswaAdminDetailView(generics.RetrieveAPIView):
    """
    get: Menampilkan detail riwayat peminjaman siswa (Staf Perpustakaan).
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Staf Perpustakaan'],
    }

    queryset = RiwayatPeminjamanSiswa.objects.all()
    serializer_class = RiwayatPeminjamanSiswaAdminSerializer

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs) 


class RiwayatPeminjamanGuruListView(generics.ListAPIView):
    """
    get: Menampilkan daftar riwayat peminjaman guru (Guru).
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Guru'],
    }

    queryset = RiwayatPeminjamanGuru.objects.all()
    serializer_class = RiwayatPeminjamanGuruSerializer
    search_fields = ('BUKU__DATA_DONASI__REGISTER_DONASI__JUDUL', 'STATUS_PEMINJAMAN', 'DATA_GURU__NIK', 'DATA_GURU__NAMA_LENGKAP', 'JANGKA_PEMINJAMAN')

    def get_queryset(self):
        current_user = self.request.user
        if (is_in_group(current_user, 'Guru')):
            data_guru_user = DataGuruUser.objects.get(USER=current_user)
            queryset = RiwayatPeminjamanGuru.objects.filter(DATA_GURU=data_guru_user.DATA_GURU)
            return queryset

        return super().get_queryset()

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class RiwayatPeminjamanGuruDetailView(generics.RetrieveAPIView):
    """
    get: Menampilkan detail riwayat peminjaman guru (Guru).
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Guru'],
    }

    queryset = RiwayatPeminjamanGuru.objects.all()
    serializer_class = RiwayatPeminjamanGuruSerializer

    def get_queryset(self):
        current_user = self.request.user
        if (is_in_group(current_user, 'Guru')):
            data_guru_user = DataGuruUser.objects.get(USER=current_user)
            queryset = RiwayatPeminjamanGuru.objects.filter(DATA_GURU=data_guru_user.DATA_GURU)
            return queryset

        return super().get_queryset()

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class RiwayatPeminjamanGuruAdminListView(generics.ListAPIView):
    """
    get: Menampilkan daftar riwayat peminjaman guru (Staf Perpustakaan).
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Staf Perpustakaan'],
    }

    queryset = RiwayatPeminjamanGuru.objects.all()
    serializer_class = RiwayatPeminjamanGuruAdminSerializer
    search_fields = ('BUKU__DATA_DONASI__REGISTER_DONASI__JUDUL', 'STATUS_PEMINJAMAN', 'DATA_GURU__NIK', 'DATA_GURU__NAMA_LENGKAP', 'JANGKA_PEMINJAMAN')

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class RiwayatPeminjamanGuruAdminDetailView(generics.ListAPIView):
    """
    get: Menampilkan detail riwayat peminjaman guru (Staf Perpustakaan).
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Staf Perpustakaan'],
    }

    queryset = RiwayatPeminjamanGuru.objects.all()
    serializer_class = RiwayatPeminjamanGuruAdminSerializer

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class AccPengajuanPeminjamanSiswaView(APIView):
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Staf Perpustakaan'],
    }

    def get(self, request, pk, format=None):
        """
        Menampilkan status pengajuan peminjaman siswa berhasil disetujui (Staf Perpustakaan).
        """
        try:
            obj = PengajuanPeminjamanSiswa.objects.get(pk=pk)
            obj.STATUS_PENGAJUAN = 'Disetujui'
            obj.save()

            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            return Response(data={'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class AccPengajuanPeminjamanSiswaView(APIView):
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Staf Perpustakaan'],
    }

    def get(self, request, pk, format=None):
        """
        Menampilkan status pengajuan peminjaman siswa berhasil disetujui (Staf Perpustakaan).
        """
        try:
            obj = PengajuanPeminjamanSiswa.objects.get(pk=pk)
            obj.STATUS_PENGAJUAN = 'Disetujui'
            obj.save()

            return Response(data={'status': 'Berhasil menyetujui permintaan peminjaman'},status=status.HTTP_200_OK)
        except Exception as e:
            return Response(data={'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class AccPengajuanPeminjamanGuruView(APIView):
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Staf Perpustakaan'],
    }

    def get(self, request, pk, format=None):
        """
        Menampilkan status pengajuan peminjaman guru berhasil disetujui (Staf Perpustakaan).
        """
        try:
            obj = PengajuanPeminjamanGuru.objects.get(pk=pk)
            obj.STATUS_PENGAJUAN = 'Disetujui'
            obj.save()

            return Response(data={'status': 'Berhasil menyetujui permintaan peminjaman'},status=status.HTTP_200_OK)
        except Exception as e:
            return Response(data={'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class TolakPengajuanPeminjamanSiswaView(APIView):
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Staf Perpustakaan'],
    }

    def get(self, request, pk, format=None):
        """
        Menampilkan status pengajuan peminjaman siswa berhasil ditolak (Staf Perpustakaan).
        """
        try:
            obj = PengajuanPeminjamanSiswa.objects.get(pk=pk)
            obj.STATUS_PENGAJUAN = 'Ditolak'
            obj.save()

            return Response(data={'status': 'Berhasil menolak permintaan peminjaman'},status=status.HTTP_200_OK)
        except Exception as e:
            return Response(data={'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class TolakPengajuanPeminjamanGuruView(APIView):
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Staf Perpustakaan'],
    }

    def get(self, request, pk, format=None):
        """
        Menampilkan status pengajuan peminjaman guru berhasil ditolak (Staf Perpustakaan).
        """
        try:
            obj = PengajuanPeminjamanGuru.objects.get(pk=pk)
            obj.STATUS_PENGAJUAN = 'Ditolak'
            obj.save()

            return Response(data={'status': 'Berhasil menolak permintaan peminjaman'},status=status.HTTP_200_OK)
        except Exception as e:
            return Response(data={'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)