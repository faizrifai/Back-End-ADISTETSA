from .custom_filter import *
from kustom_autentikasi.models import *
from .models import *
from .serializers import *
from rest_framework.views import Response, APIView
from rest_framework.parsers import MultiPartParser

from rest_framework import generics, status

from utility.permissions import HasGroupPermissionAny, IsSuperAdmin, is_in_group
from kurikulum.serializers import PoinPelanggaranSerializer

# Create your views here.


class PengajuanLaporanPelanggaranListView(generics.ListCreateAPIView):
    """
    get: Menampilkan data daftar Pengajuan Laporan Pelanggaran (All Role).
    post: Menambahkan data Pengajuan Laporan Pelanggaran (All Role).
    """

    permission_classes = [IsSuperAdmin | HasGroupPermissionAny]
    required_groups = {
        "GET": ["Siswa", "Guru", "Orang Tua", "Karyawan"],
        "POST": ["Siswa", "Guru", "Orang Tua", "Karyawan"],
    }
    parser_classes = (MultiPartParser,)

    queryset = PengajuanLaporanPelanggaran.objects.all()
    serializer_class = PengajuanLaporanPelanggaranSerializer

    def get_serializer_class(self):
        if self.request.method == "GET":
            return PengajuanLaporanPelanggaranListSerializer

        elif self.request.method == "POST":
            return PengajuanLaporanPelanggaranSerializer

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class RiwayatLaporanPelanggaranListView(generics.ListAPIView):
    """
    get: Menampilkan data Riwayat Laporan Pelanggaran (Siswa).
    """

    permission_classes = [IsSuperAdmin | HasGroupPermissionAny]
    required_groups = {
        "GET": ["Siswa"],
    }

    queryset = RiwayatLaporanPelanggaran.objects.all()
    serializer_class = RiwayatLaporanPelanggaranSerializer

    def get_serializer_class(self):
        if self.request.method == "GET":
            return RiwayatLaporanPelanggaranListSerializer

    def get_queryset(self):
        current_user = self.request.user
        if is_in_group(current_user, "Siswa"):
            data_siswa_user = DataSiswaUser.objects.get(USER=current_user)
            queryset = RiwayatLaporanPelanggaran.objects.filter(
                DATA_SISWA=data_siswa_user.DATA_SISWA
            )

            return queryset

        return super().get_queryset()

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class PengajuanProgramKebaikanListView(generics.ListCreateAPIView):
    """
    get: Menampilkan data daftar Pengajuan Program Kebaikan.
    post: Menambahkan data Pengajuan Program Kebaikan.
    """

    permission_classes = [IsSuperAdmin | HasGroupPermissionAny]
    required_groups = {
        "GET": ["Siswa"],
        "POST": ["Siswa"],
    }
    parser_classes = (MultiPartParser,)

    queryset = PengajuanProgramKebaikan.objects.all()
    serializer_class = PengajuanProgramKebaikanSerializer

    def get_serializer_class(self):
        if self.request.method == "GET":
            return PengajuanProgramKebaikanListSerializer

        elif self.request.method == "POST":
            return PengajuanProgramKebaikanSerializer

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class RiwayatProgramKebaikanListView(generics.ListAPIView):
    """
    get: Menampilkan data Riwayat Laporan Pelanggaran.
    """

    permission_classes = [IsSuperAdmin | HasGroupPermissionAny]
    required_groups = {
        "GET": ["Siswa"],
    }

    queryset = RiwayatProgramKebaikan.objects.all()
    serializer_class = RiwayatProgramKebaikanSerializer

    def get_serializer_class(self):
        if self.request.method == "GET":
            return RiwayatProgramKebaikanListSerializer

    def get_queryset(self):
        current_user = self.request.user
        if is_in_group(current_user, "Siswa"):
            data_siswa_user = DataSiswaUser.objects.get(USER=current_user)
            queryset = RiwayatProgramKebaikan.objects.filter(
                DATA_SISWA=data_siswa_user.DATA_SISWA
            )

            return queryset

        return super().get_queryset()

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class DaftarSiswaListView(generics.ListAPIView):
    """
    get: Menampilkan daftar siswa (All Role).
    """

    permission_classes = [IsSuperAdmin | HasGroupPermissionAny]
    required_groups = {
        "GET": ["Siswa", "Guru", "Karyawan", "Orang Tua"],
    }

    queryset = DataSiswa.objects.all()
    serializer_class = DaftarSiswaListSerializer
    filterset_fields = ("NIS", "NAMA")
    search_fields = ("NIS", "NAMA")

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class DataPelanggaranListView(generics.ListAPIView):
    """
    get: Menampilkan data pelanggaran (All Role).
    """

    permission_classes = [IsSuperAdmin | HasGroupPermissionAny]
    required_groups = {
        "GET": ["Siswa", "Guru", "Karyawan", "Orang Tua"],
    }

    queryset = PoinPelanggaran.objects.all()
    serializer_class = PoinPelanggaranSerializer
    search_fields = ["KETERANGAN", "POIN"]

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class DataKebaikanListView(generics.ListAPIView):
    """
    get: Menampilkan data program kebaikan (All Role).
    """

    permission_classes = [IsSuperAdmin | HasGroupPermissionAny]
    required_groups = {
        "GET": ["Siswa", "Guru", "Karyawan", "Orang Tua"],
    }

    queryset = PoinProgramKebaikan.objects.all()
    serializer_class = PoinProgramKebaikanSerializer
    search_fields = ["KETERANGAN", "POIN"]

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class PelanggaranSayaListView(generics.ListAPIView):
    """
    get: Melihat pelanggaran saya (Siswa)
    """

    permission_classes = [IsSuperAdmin | HasGroupPermissionAny]
    required_groups = {
        "GET": ["Siswa"],
    }

    queryset = RiwayatLaporanPelanggaran.objects.all()
    serializer_class = RiwayatLaporanPelanggaranListSerializer

    def get_queryset(self):
        current_user = self.request.user
        data_siswa_user = DataSiswaUser.objects.get(USER=current_user)
        riwayat_pelanggaran = RiwayatLaporanPelanggaran.objects.filter(
            DATA_SISWA=data_siswa_user.DATA_SISWA, STATUS_PENGAJUAN="Disetujui"
        )

        return riwayat_pelanggaran

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class KatalogEkskulListView(generics.ListAPIView):
    """
    get: Menampilkan data katalog ekskul (Siswa).
    """

    permission_classes = [IsSuperAdmin | HasGroupPermissionAny]
    required_groups = {
        "GET": ["Siswa", "Pelatih"],
    }

    queryset = KatalogEkskul.objects.all()
    serializer_class = KatalogEkskulSerializer
    search_fields = ["NAMA", "KATEGORI"]

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class KatalogEkskulDetailView(generics.RetrieveAPIView):
    """
    get: Menampilkan detail data katalog ekskul (Siswa).
    """

    permission_classes = [HasGroupPermissionAny]
    required_groups = {
        "GET": ["Siswa"],
    }

    queryset = KatalogEkskul.objects.all()
    serializer_class = KatalogEkskulSerializer


class AjukanEkskulListView(generics.CreateAPIView):
    """
    post: Mengajukan ekskul (Siswa).
    """

    permission_classes = [IsSuperAdmin | HasGroupPermissionAny]
    required_groups = {
        "POST": ["Siswa"],
    }

    queryset = PengajuanEkskul.objects.all()
    serializer_class = PengajuanEkskulSerializer

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class PengajuanEkskulListView(generics.ListAPIView):
    """
    get: Menampilkan data daftar Pengajuan ekskul.
    """

    permission_classes = [IsSuperAdmin | HasGroupPermissionAny]
    required_groups = {
        "GET": ["Siswa", "Pelatih"],
    }
    parser_classes = (MultiPartParser,)

    queryset = PengajuanEkskul.objects.all()
    serializer_class = PengajuanEkskulListSerializer
    search_fields = (
        "EKSKUL__NAMA",
        "KELAS_SISWA__NIS__NIS",
        "KELAS_SISWA__NIS__NAMA",
        "KELAS_SISWA__KELAS__KELAS__KODE_KELAS",
    )

    def get_queryset(self):
        tahun_ajaran_aktif = Configuration.current().TAHUN_AJARAN_AKTIF

        current_user = self.request.user

        if is_in_group(current_user, "Siswa"):
            data_siswa_user = DataSiswaUser.objects.get(USER=current_user)
            kelas_siswa = KelasSiswa.objects.get(
                NIS=data_siswa_user.DATA_SISWA,
                KELAS__KELAS__TAHUN_AJARAN=tahun_ajaran_aktif,
            )
            queryset = PengajuanEkskul.objects.filter(KELAS_SISWA=kelas_siswa)

            return queryset
        else:
            data_pelatih_user = DataPelatihUser.objects.get(USER=current_user)
            jadwal_ekskul = JadwalEkskul.objects.filter(
                PELATIH=data_pelatih_user.DATA_PELATIH, TAHUN_AJARAN=tahun_ajaran_aktif
            )
            ids_ekskul = []
            for ekskul in jadwal_ekskul:
                ids_ekskul.append(ekskul.EKSKUL.ID)

            queryset = PengajuanEkskul.objects.filter(EKSKUL_id__in=ids_ekskul)

            return queryset

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class PengajuanEkskulDetailView(generics.RetrieveDestroyAPIView):
    """
    get: Menampilkan detail pengajuan ekskul (Siswa).
    delete: Menghapus pengajuan ekskul (Siswa).
    """

    permission_classes = [IsSuperAdmin | HasGroupPermissionAny]
    required_groups = {
        "GET": ["Siswa", "Pelatih"],
        "DELETE": ["Siswa", "Pelatih"],
    }

    queryset = PengajuanEkskul.objects.all()
    serializer_class = PengajuanEkskulListSerializer

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class AccPengajuanEkskulView(APIView):
    permission_classes = [IsSuperAdmin | HasGroupPermissionAny]
    required_groups = {
        "GET": ["Pelatih"],
    }

    def get(self, request, pk, format=None):
        """
        Menampilkan status pengajuan bergabung ekskul disetujui (Pelatih).
        """
        try:
            obj = PengajuanEkskul.objects.get(pk=pk)
            obj.STATUS_PENGAJUAN = "Disetujui"
            obj.save()

            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            return Response(data={"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class EkskulSayaListView(generics.ListAPIView):
    """
    get: Melihat ekskul yang sudah diambil (Siswa).
    """

    permission_classes = [IsSuperAdmin | HasGroupPermissionAny]
    required_groups = {
        "GET": ["Siswa"],
    }

    queryset = KatalogEkskul.objects.all()
    serializer_class = KatalogEkskulSerializer
    search_fields = ("NAMA", "KATEGORI")

    def get_queryset(self):
        tahun_ajaran_aktif = Configuration.current().TAHUN_AJARAN_AKTIF

        current_user = self.request.user
        data_siswa_user = DataSiswaUser.objects.get(USER=current_user)
        kelas_siswa = KelasSiswa.objects.get(
            NIS=data_siswa_user.DATA_SISWA,
            KELAS__KELAS__TAHUN_AJARAN=tahun_ajaran_aktif,
        )
        ekskul_yang_diambil = AnggotaEkskul.objects.filter(
            KELAS_SISWA=kelas_siswa, STATUS="Aktif"
        )
        ids_ekskul = []
        for ekskul in ekskul_yang_diambil:
            ids_ekskul.append(ekskul.EKSKUL.ID)

        queryset = KatalogEkskul.objects.filter(pk__in=ids_ekskul)

        return queryset

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class DaftarAnggotaListView(generics.ListAPIView):
    """
    get: Melihat daftar anggota ekskul (Pelatih).
    """

    permission_classes = [IsSuperAdmin | HasGroupPermissionAny]
    required_groups = {
        "GET": ["Pelatih"],
    }

    queryset = AnggotaEkskul.objects.all()
    serializer_class = AnggotaEkskulListSerializer
    search_fields = (
        "KELAS_SISWA__NIS__NIS",
        "KELAS_SISWA__NIS__NAMA",
        "KELAS_SISWA__KELAS__KELAS__KODE_KELAS",
        "STATUS",
    )

    def get_queryset(self):
        id_ekskul = self.kwargs["id_katalog_ekskul"]
        queryset = AnggotaEkskul.objects.filter(EKSKUL_id=id_ekskul)

        return queryset

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class DaftarAnggotaDetailView(generics.RetrieveUpdateAPIView):
    """
    get: Melihat detail anggota ekskul (Pelatih).
    patch: Mengubah status keanggotaan (Pelatih).
    """

    permission_classes = [IsSuperAdmin | HasGroupPermissionAny]
    required_groups = {"GET": ["Pelatih"], "PATCH": ["Pelatih"]}

    queryset = AnggotaEkskul.objects.all()
    serializer_class = AnggotaEkskulListSerializer

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)


class JadwalEkskulListView(generics.ListAPIView):
    """
    get: Melihat jadwal ekskul (Pelatih).
    """

    permission_classes = [IsSuperAdmin | HasGroupPermissionAny]
    required_groups = {
        "GET": ["Pelatih"],
    }

    queryset = JadwalEkskul.objects.all()
    serializer_class = JadwalEkskulListSerializer
    filterset_fields = (
        "TAHUN_AJARAN",
        "HARI",
    )
    search_fields = (
        "TAHUN_AJARAN",
        "HARI",
    )

    def get_queryset(self):
        current_user = self.request.user
        data_pelatih_user = DataPelatihUser.objects.get(USER=current_user)
        queryset = JadwalEkskul.objects.filter(PELATIH=data_pelatih_user.DATA_PELATIH)

        return queryset

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class DaftarJurnalEkskulListView(generics.ListAPIView):
    """
    get: Melihat daftar jurnal ekskul (Pelatih).
    """

    permission_classes = [IsSuperAdmin | HasGroupPermissionAny]
    required_groups = {
        "GET": ["Pelatih"],
    }

    queryset = DaftarJurnalEkskul.objects.all()
    serializer_class = DaftarJurnalEkskulListSerializer
    filter_class = DaftarJurnalEkskulFilter

    def get_queryset(self):
        current_user = self.request.user
        data_pelatih_user = DataPelatihUser.objects.get(USER=current_user)
        queryset = DaftarJurnalEkskul.objects.filter(
            PELATIH=data_pelatih_user.DATA_PELATIH
        )

        return queryset

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class JurnalEkskulListView(generics.ListAPIView):
    """
    get: Melihat daftar pertemuan jurnal ekskul (Pelatih).
    """

    permission_classes = [IsSuperAdmin | HasGroupPermissionAny]
    required_groups = {
        "GET": ["Pelatih"],
    }

    queryset = JurnalEkskul.objects.all()
    serializer_class = JurnalEkskulListSerializer
    search_fields = ("PERTEMUAN",)

    def get_queryset(self):
        current_user = self.request.user
        data_pelatih_user = DataPelatihUser.objects.get(USER=current_user)
        queryset = JurnalEkskul.objects.filter(
            PELATIH=data_pelatih_user.DATA_PELATIH,
            DAFTAR_id=self.kwargs["id_daftar_jurnal_ekskul"],
        )

        return queryset

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class IsiJurnalEkskulListView(generics.CreateAPIView):
    """
    post: Mengisi jurnal pertemuan ekskul (Pelatih).
    """

    permission_classes = [IsSuperAdmin | HasGroupPermissionAny]
    required_groups = {
        "POST": ["Pelatih"],
    }

    parser_classes = (MultiPartParser,)
    queryset = JurnalEkskul.objects.all()
    serializer_class = JurnalEkskulSerializer

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class PresensiEkskulListView(generics.ListAPIView):
    """
    get: Melihat presensi anggota ekskul (Pelatih).
    """

    permission_classes = [IsSuperAdmin | HasGroupPermissionAny]
    required_groups = {
        "GET": ["Pelatih"],
    }

    queryset = AbsensiEkskul.objects.all()
    serializer_class = AbsensiEkskulListSerializer
    search_fields = ("NIS__NIS", "NIS__NAMA", "KETERANGAN")

    def get_queryset(self):
        queryset = AbsensiEkskul.objects.filter(
            JURNAL_EKSKUL_id=self.kwargs["id_jurnal_ekskul_pertemuan"]
        )

        return queryset

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class PresensiEkskulDetailView(generics.RetrieveUpdateAPIView):
    """
    get: Melihat detail presensi anggota ekskul (Pelatih).
    patch: Mengubah keterangan presensi anggota ekskul (Pelatih).
    """

    permission_classes = [IsSuperAdmin | HasGroupPermissionAny]
    required_groups = {
        "GET": ["Pelatih"],
        "PATCH": ["Pelatih"],
    }

    queryset = AbsensiEkskul.objects.all()
    serializer_class = AbsensiEkskulListSerializer

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
