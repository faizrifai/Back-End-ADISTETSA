from kustom_autentikasi.models import *
from .models import *
from .serializers import *
from .utility import check_ruangan_tersedia, check_sarana_tersedia

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from rest_framework.views import APIView

from utility.permissions import HasGroupPermissionAny, IsSuperAdmin, is_in_group


# Create your views here.
class KatalogSaranaListView(generics.ListAPIView):
    """
    get: Menampilkan daftar katalog barang.
    """

    permission_classes = [IsSuperAdmin | HasGroupPermissionAny]
    required_groups = {
        "GET": ["Guru", "Siswa", "Karyawan"],
    }

    def get_queryset(self):
        queryset = Sarana.objects.all()
        return queryset.filter(STATUS="Sudah Dikembalikan")

    queryset = Sarana.objects.all()
    serializer_class = KatalogSaranaSerializer
    search_fields = ("NAMA", "JENIS__KATEGORI", "STATUS")

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class KatalogSaranaAdminListView(generics.ListAPIView):
    """
    get: Menampilkan daftar katalog barang untuk Staf.
    """

    permission_classes = [IsSuperAdmin | HasGroupPermissionAny]
    required_groups = {
        "GET": ["Staf Sarpras"],
    }

    queryset = Sarana.objects.all()
    serializer_class = KatalogSaranaSerializer
    search_fields = ("NAMA", "JENIS__KATEGORI", "STATUS")

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class PengajuanPeminjamanBarangListView(generics.ListCreateAPIView):
    """
    get: Menampilkan daftar pengajuan peminjaman (Siswa).
    post: Membuat pengajuan peminjaman (Siswa).
    """

    permission_classes = [IsSuperAdmin | HasGroupPermissionAny]
    required_groups = {
        "GET": ["Siswa", "Guru", "Karyawan"],
        "POST": ["Siswa", "Guru", "Karyawan"],
    }

    parser_classes = (MultiPartParser,)
    queryset = PengajuanPeminjamanBarang.objects.all().order_by("-TANGGAL_PENGAJUAN")
    serializer_class = PengajuanPeminjamanBarangSerializer
    # search_fields = ('STATUS_PENGAJUAN')

    def get_queryset(self):
        current_user = self.request.user
        queryset = PengajuanPeminjamanBarang.objects.filter(USER=current_user).order_by(
            "-TANGGAL_PENGAJUAN"
        )
        return queryset

    def get_serializer_class(self):
        current_user = self.request.user
        if self.request.method == "GET":
            return PengajuanPeminjamanBarangListSerializer
        elif self.request.method == "POST":
            return PengajuanPeminjamanBarangSerializer

        return super().get_serializer_class()

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        sarana = request.data["ALAT"]

        if check_sarana_tersedia(sarana):
            return super().create(request, *args, **kwargs)
        else:
            return Response(
                data={"error": "Sarana yang dipilih tidak tersedia untuk dipinjam."},
                status=status.HTTP_404_NOT_FOUND,
            )


class PengajuanPeminjamanBarangDetailView(generics.RetrieveAPIView):
    """
    get: Menampilkan detail pengajuan peminjaman (Siswa, Guru, Karyawan).
    """

    permission_classes = [IsSuperAdmin | HasGroupPermissionAny]
    required_groups = {
        "GET": ["Siswa", "Guru", "Karyawan"],
    }

    queryset = PengajuanPeminjamanBarang.objects.all()
    serializer_class = PengajuanPeminjamanBarangListSerializer
    # search_fields = ('STATUS_PENGAJUAN')

    def get_queryset(self):
        current_user = self.request.user
        queryset = PengajuanPeminjamanBarang.objects.filter(USER=current_user)
        return queryset

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class PengajuanPeminjamanBarangAdminListView(generics.ListAPIView):
    """
    get: Menampilkan daftar pengajuan peminjaman (Staf Sarpras).
    """

    permission_classes = [IsSuperAdmin | HasGroupPermissionAny]
    required_groups = {
        "GET": ["Staf Sarpras"],
    }

    queryset = PengajuanPeminjamanBarang.objects.all().order_by("-TANGGAL_PENGAJUAN")
    serializer_class = PengajuanPeminjamanBarangAdminSerializer
    # search_fields = ('STATUS_PENGAJUAN')

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class PengajuanPeminjamanBarangAdminDetailView(generics.RetrieveAPIView):
    """
    get: Menampilkan detail pengajuan peminjaman (Staf Sarpras).
    """

    permission_classes = [IsSuperAdmin | HasGroupPermissionAny]
    required_groups = {
        "GET": ["Staf Sarpras"],
    }

    queryset = PengajuanPeminjamanBarang.objects.all()
    serializer_class = PengajuanPeminjamanBarangAdminSerializer
    # search_fields = ('STATUS_PENGAJUAN')

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class RiwayatPeminjamanBarangListView(generics.ListAPIView):
    """
    get: Menampilkan daftar riwayat peminjaman (Siswa, Guru, Karyawan).
    """

    permission_classes = [IsSuperAdmin | HasGroupPermissionAny]
    required_groups = {
        "GET": ["Siswa", "Guru", "Karyawan"],
    }

    queryset = RiwayatPeminjamanBarang.objects.all().order_by("-TANGGAL_PENGAJUAN")
    serializer_class = RiwayatPeminjamanBarangSerializer

    def get_queryset(self):
        current_user = self.request.user
        queryset = RiwayatPeminjamanBarang.objects.filter(USER=current_user).order_by(
            "-TANGGAL_PENGAJUAN"
        )
        return queryset

    def get_serializer_class(self):
        current_user = self.request.user
        if self.request.method == "POST":
            return RiwayatPeminjamanBarangSerializer
        elif self.request.method == "GET":
            return RiwayatPeminjamanBarangListSerializer

        return super().get_serializer_class()

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class RiwayatPeminjamanBarangDetailView(generics.RetrieveAPIView):
    """
    get: Menampilkan detail riwayat peminjaman (Siswa, Guru, Karyawan).
    """

    permission_classes = [IsSuperAdmin | HasGroupPermissionAny]
    required_groups = {
        "GET": ["Siswa", "Guru", "Karyawan"],
    }

    queryset = RiwayatPeminjamanBarang.objects.all()
    serializer_class = RiwayatPeminjamanBarangListSerializer

    def get_queryset(self):
        current_user = self.request.user
        queryset = RiwayatPeminjamanBarang.objects.filter(USER=current_user)
        return queryset

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class AccPengajuanPeminjamanBarangView(APIView):
    permission_classes = [IsSuperAdmin | HasGroupPermissionAny]
    required_groups = {
        "GET": ["Staf Sarpras"],
    }

    def get(self, request, pk, format=None):
        """
        Menampilkan status pengajuan peminjaman siswa berhasil disetujui (Staf Perpustakaan).
        """
        try:
            obj = PengajuanPeminjamanBarang.objects.get(pk=pk)
            obj.STATUS_PENGAJUAN = "Disetujui"
            obj.save()

            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            return Response(data={"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class TolakPengajuanPeminjamanBarangView(APIView):
    permission_classes = [IsSuperAdmin | HasGroupPermissionAny]
    required_groups = {
        "GET": ["Staf Sarpras"],
    }

    def get(self, request, pk, format=None):
        """
        Menampilkan status pengajuan peminjaman siswa berhasil ditolak (Staf Perpustakaan).
        """
        try:
            obj = PengajuanPeminjamanBarang.objects.get(pk=pk)
            obj.STATUS_PENGAJUAN = "Ditolak"
            obj.save()

            return Response(
                data={"status": "Berhasil menolak permintaan peminjaman"},
                status=status.HTTP_200_OK,
            )
        except Exception as e:
            return Response(data={"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class KatalogRuanganListView(generics.ListAPIView):
    """
    get: Menampilkan daftar katalog buku.
    """

    permission_classes = [IsSuperAdmin | HasGroupPermissionAny]
    required_groups = {
        "GET": ["Guru", "Siswa", "Karyawan"],
    }

    def get_queryset(self):
        queryset = Ruangan.objects.all()

        return queryset

    queryset = Ruangan.objects.all()
    serializer_class = KatalogRuanganSerializer
    search_fields = ("NAMA", "JENIS__KATEGORI", "STATUS")

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class PengajuanPeminjamanRuanganListView(generics.ListCreateAPIView):
    """
    get: Menampilkan daftar pengajuan peminjaman (Siswa, Guru, Karyawan).
    post: Membuat pengajuan peminjaman (Siswa, Guru, Karyawan).
    """

    permission_classes = [IsSuperAdmin | HasGroupPermissionAny]
    required_groups = {
        "GET": ["Siswa", "Guru", "Karyawan"],
        "POST": ["Siswa", "Guru", "Karyawan"],
    }

    parser_classes = (MultiPartParser,)
    queryset = PengajuanPeminjamanRuangan.objects.all().order_by("-TANGGAL_PENGAJUAN")
    serializer_class = PengajuanPeminjamanRuanganSerializer
    # search_fields = ('STATUS_PENGAJUAN')

    def get_queryset(self):
        current_user = self.request.user
        queryset = PengajuanPeminjamanRuangan.objects.filter(
            USER=current_user
        ).order_by("-TANGGAL_PENGAJUAN")
        return queryset

        return super().get_queryset()

    def get_serializer_class(self):
        current_user = self.request.user
        if self.request.method == "POST":
            return PengajuanPeminjamanRuanganSerializer
        elif self.request.method == "GET":
            return PengajuanPeminjamanRuanganListSerializer

        return super().get_serializer_class()

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except Exception as e:
            return Response(data={"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class PengajuanPeminjamanRuanganDetailView(generics.RetrieveAPIView):
    """
    get: Menampilkan detail pengajuan peminjaman (Siswa, Guru, Karyawan).
    """

    permission_classes = [IsSuperAdmin | HasGroupPermissionAny]
    required_groups = {
        "GET": ["Siswa", "Guru", "Karyawan"],
    }

    queryset = PengajuanPeminjamanRuangan.objects.all()
    serializer_class = PengajuanPeminjamanRuanganListSerializer
    # search_fields = ('STATUS_PENGAJUAN')

    def get_queryset(self):
        current_user = self.request.user
        if not is_in_group(current_user, "Staf Sarpras"):
            queryset = PengajuanPeminjamanRuangan.objects.filter(USER=current_user)
            return queryset

        return super().get_queryset()

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class PengajuanPeminjamanRuanganAdminListView(generics.ListAPIView):
    """
    get: Menampilkan daftar pengajuan peminjaman (Staf Sarpras).
    """

    permission_classes = [IsSuperAdmin | HasGroupPermissionAny]
    required_groups = {
        "GET": ["Staf Sarpras"],
    }

    queryset = PengajuanPeminjamanRuangan.objects.all().order_by("-TANGGAL_PENGAJUAN")
    serializer_class = PengajuanPeminjamanRuanganListSerializer
    # search_fields = ('STATUS_PENGAJUAN')

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class PengajuanPeminjamanRuanganAdminDetailView(generics.RetrieveAPIView):
    """
    get: Menampilkan detail pengajuan peminjaman (Staf Sarpras).
    """

    permission_classes = [IsSuperAdmin | HasGroupPermissionAny]
    required_groups = {
        "GET": ["Staf Sarpras"],
    }

    queryset = PengajuanPeminjamanRuangan.objects.all()
    serializer_class = PengajuanPeminjamanRuanganListSerializer
    # search_fields = ('STATUS_PENGAJUAN')

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class RiwayatPeminjamanRuanganListView(generics.ListAPIView):
    """
    get: Menampilkan daftar riwayat peminjaman (Siswa, Guru, Karyawan).
    """

    permission_classes = [IsSuperAdmin | HasGroupPermissionAny]
    required_groups = {
        "GET": ["Siswa", "Guru", "Karyawan"],
    }

    queryset = RiwayatPeminjamanRuangan.objects.all().order_by("-TANGGAL_PENGAJUAN")
    serializer_class = RiwayatPeminjamanRuanganListSerializer

    def get_queryset(self):
        current_user = self.request.user
        queryset = RiwayatPeminjamanRuangan.objects.filter(USER=current_user).order_by(
            "-TANGGAL_PENGAJUAN"
        )
        return queryset

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class RiwayatPeminjamanRuanganDetailView(generics.RetrieveAPIView):
    """
    get: Menampilkan detail riwayat peminjaman (Siswa, Guru, Karyawan).
    """

    permission_classes = [IsSuperAdmin | HasGroupPermissionAny]
    required_groups = {
        "GET": ["Siswa", "Guru", "Karyawan"],
    }

    queryset = RiwayatPeminjamanRuangan.objects.all()
    serializer_class = RiwayatPeminjamanRuanganListSerializer

    def get_queryset(self):
        current_user = self.request.user
        queryset = RiwayatPeminjamanRuangan.objects.filter(USER=current_user)
        return queryset

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class RiwayatPeminjamanRuanganAdminListView(generics.ListAPIView):
    """
    get: Menampilkan daftar riwayat peminjaman (Staf Sarpras).
    """

    permission_classes = [IsSuperAdmin | HasGroupPermissionAny]
    required_groups = {
        "GET": ["Staf Sarpras"],
    }

    queryset = RiwayatPeminjamanRuangan.objects.all().order_by("-TANGGAL_PENGAJUAN")
    serializer_class = RiwayatPeminjamanRuanganListSerializer

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class RiwayatPeminjamanRuanganAdminDetailView(generics.RetrieveAPIView):
    """
    get: Menampilkan detail riwayat peminjaman (Staf Sarpras).
    """

    permission_classes = [IsSuperAdmin | HasGroupPermissionAny]
    required_groups = {
        "GET": ["Staf Sarpras"],
    }

    queryset = RiwayatPeminjamanRuangan.objects.all()
    serializer_class = RiwayatPeminjamanRuanganListSerializer

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class AccPengajuanPeminjamanRuanganView(APIView):
    permission_classes = [IsSuperAdmin | HasGroupPermissionAny]
    required_groups = {
        "GET": ["Staf Sarpras"],
    }

    def get(self, request, pk, format=None):
        """
        Menampilkan status pengajuan peminjaman siswa berhasil disetujui (Staf Perpustakaan).
        """
        try:
            obj = PengajuanPeminjamanRuangan.objects.get(pk=pk)
            obj.STATUS = "Sedang Dipinjam"
            obj.save()

            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            return Response(data={"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class TolakPengajuanPeminjamanRuanganView(APIView):
    permission_classes = [IsSuperAdmin | HasGroupPermissionAny]
    required_groups = {
        "GET": ["Staf Sarpras"],
    }

    def get(self, request, pk, format=None):
        """
        Menampilkan status pengajuan peminjaman siswa berhasil ditolak (Staf Perpustakaan).
        """
        try:
            obj = PengajuanPeminjamanRuangan.objects.get(pk=pk)
            obj.STATUS = "Ditolak"
            obj.save()

            return Response(
                data={"status": "Berhasil menolak permintaan peminjaman"},
                status=status.HTTP_200_OK,
            )
        except Exception as e:
            return Response(data={"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
