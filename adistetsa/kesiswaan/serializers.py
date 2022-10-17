from .models import *
from rest_framework import serializers

from utility.permissions import is_in_group
from kurikulum.models import Configuration
from kustom_autentikasi.models import DataPelatihUser, DataSiswaUser


class PengajuanLaporanPelanggaranSerializer(serializers.ModelSerializer):
    class Meta:
        model = PengajuanLaporanPelanggaran
        fields = "__all__"


class PengajuanLaporanPelanggaranListSerializer(serializers.ModelSerializer):
    DATA_SISWA = serializers.SerializerMethodField("get_data_siswa")
    JENIS_PELANGGARAN = serializers.SerializerMethodField("get_jenis_pelanggaran")

    class Meta:
        model = PengajuanLaporanPelanggaran
        fields = "__all__"

    def get_data_siswa(self, obj):
        return str(obj.DATA_SISWA)

    def get_jenis_pelanggaran(self, obj):
        return str(obj.JENIS_PELANGGARAN)


class PelanggaranSiswaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PelanggaranSiswa
        fields = "__all__"


class PelanggaranSiswaListSerializer(serializers.ModelSerializer):
    DATA_SISWA = serializers.SerializerMethodField("get_data_siswa")

    class Meta:
        model = PelanggaranSiswa
        fields = "__all__"

    def get_data_siswa(self, obj):
        return str(obj.DATA_SISWA)


class RiwayatLaporanPelanggaranSerializer(serializers.ModelSerializer):
    class Meta:
        model = RiwayatLaporanPelanggaran
        fields = "__all__"


class RiwayatLaporanPelanggaranListSerializer(serializers.ModelSerializer):
    DATA_SISWA = serializers.SerializerMethodField("get_data_siswa")
    JENIS_PELANGGARAN = serializers.SerializerMethodField("get_jenis_pelanggaran")

    class Meta:
        model = RiwayatLaporanPelanggaran
        fields = "__all__"

    def get_data_siswa(self, obj):
        return str(obj.DATA_SISWA)

    def get_jenis_pelanggaran(self, obj):
        return str(obj.JENIS_PELANGGARAN)


class KategoriProgramKebaikanSerializer(serializers.ModelSerializer):
    class Meta:
        model = KategoriProgramKebaikan
        fields = "__all__"


class ProgramKebaikanSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgramKebaikan
        fields = "__all__"


class ProgramKebaikanListSerializer(serializers.ModelSerializer):
    KATEGORI = serializers.SerializerMethodField("get_kategori")

    class Meta:
        model = ProgramKebaikan
        fields = "__all__"

    def get_kategori(self, obj):
        return str(obj.KATEGORI)


class PoinProgramKebaikanSerializer(serializers.ModelSerializer):
    class Meta:
        model = PoinProgramKebaikan
        fields = "__all__"


class PengajuanProgramKebaikanSerializer(serializers.ModelSerializer):
    class Meta:
        model = PengajuanProgramKebaikan
        exclude = ("DATA_SISWA",)

    def create(self, validated_data):
        request = self.context.get("request", None)
        current_user = request.user
        if is_in_group(current_user, "Siswa"):
            data_siswa_user = DataSiswaUser.objects.get(USER=current_user)
            validated_data["DATA_SISWA"] = data_siswa_user.DATA_SISWA

        data_pengajuan = PengajuanProgramKebaikan.objects.create(**validated_data)

        return data_pengajuan


class PengajuanProgramKebaikanListSerializer(serializers.ModelSerializer):
    DATA_SISWA = serializers.SerializerMethodField("get_data_siswa")
    JENIS_PROGRAM_KEBAIKAN = serializers.SerializerMethodField(
        "get_jenis_program_kebaikan"
    )

    class Meta:
        model = PengajuanProgramKebaikan
        fields = "__all__"

    def get_data_siswa(self, obj):
        return str(obj.DATA_SISWA)

    def get_jenis_program_kebaikan(self, obj):
        return str(obj.JENIS_PROGRAM_KEBAIKAN)


class RiwayatProgramKebaikanSerializer(serializers.ModelSerializer):
    class Meta:
        model = RiwayatProgramKebaikan
        fields = "__all__"


class RiwayatProgramKebaikanListSerializer(serializers.ModelSerializer):
    DATA_SISWA = serializers.SerializerMethodField("get_data_siswa")
    JENIS_PROGRAM_KEBAIKAN = serializers.SerializerMethodField(
        "get_jenis_program_kebaikan"
    )

    class Meta:
        model = RiwayatProgramKebaikan
        fields = "__all__"

    def get_data_siswa(self, obj):
        return str(obj.DATA_SISWA)

    def get_jenis_program_kebaikan(self, obj):
        return str(obj.JENIS_PROGRAM_KEBAIKAN)


class DaftarSiswaListSerializer(serializers.ModelSerializer):
    KELAS = serializers.SerializerMethodField("get_kelas")

    class Meta:
        model = DataSiswa
        fields = ("NIS", "NISN", "NAMA", "KELAS")

    def get_kelas(self, obj):
        data_siswa = KelasSiswa.objects.filter(NIS=obj.NIS).order_by("-ID")[0]

        if data_siswa:
            return str(data_siswa.KELAS)
        else:
            return "Tidak ada kelas"


class KatalogEkskulSerializer(serializers.ModelSerializer):
    JADWAL = serializers.SerializerMethodField("get_jadwal")

    class Meta:
        model = KatalogEkskul
        fields = "__all__"

    def get_jadwal(self, obj):
        jadwal = JadwalEkskul.objects.filter(EKSKUL=obj)

        list_jadwal = []
        for data in jadwal:
            list_jadwal.append(data.HARI + ", " + str(data))

        return list_jadwal


class JadwalEkskulSerializer(serializers.ModelSerializer):
    class Meta:
        model = JadwalEkskul
        fields = "__all__"


class JadwalEkskulListSerializer(serializers.ModelSerializer):
    PELATIH = serializers.SerializerMethodField("get_pelatih")
    TAHUN_AJARAN = serializers.SerializerMethodField("get_tahun_ajaran")
    SEMESTER = serializers.SerializerMethodField("get_semester")
    EKSKUL = serializers.SerializerMethodField("get_ekskul")

    class Meta:
        model = JadwalEkskul
        fields = "__all__"

    def get_pelatih(self, obj):
        return str(obj.PELATIH)

    def get_tahun_ajaran(self, obj):
        return str(obj.TAHUN_AJARAN)

    def get_semester(self, obj):
        return str(obj.SEMESTER)

    def get_ekskul(self, obj):
        return str(obj.EKSKUL)


class DaftarJurnalEkskulSerializer(serializers.ModelSerializer):
    class Meta:
        model = DaftarJurnalEkskul
        fields = "__all__"


class DaftarJurnalEkskulListSerializer(serializers.ModelSerializer):
    PELATIH = serializers.SerializerMethodField("get_pelatih")
    JADWAL_EKSKUL = serializers.SerializerMethodField("get_jadwal_ekskul")
    SEMESTER = serializers.SerializerMethodField("get_semester")
    EKSKUL = serializers.SerializerMethodField("get_ekskul")
    TAHUN_AJARAN = serializers.SerializerMethodField("get_tahun_ajaran")

    class Meta:
        model = DaftarJurnalEkskul
        fields = "__all__"

    def get_pelatih(self, obj):
        return str(obj.PELATIH)

    def get_jadwal_ekskul(self, obj):
        return str(obj.JADWAL_EKSKUL)

    def get_semester(self, obj):
        return str(obj.SEMESTER)

    def get_ekskul(self, obj):
        return str(obj.EKSKUL)

    def get_tahun_ajaran(self, obj):
        return str(obj.JADWAL_EKSKUL.TAHUN_AJARAN)


class JurnalEkskulSerializer(serializers.ModelSerializer):
    class Meta:
        model = JurnalEkskul
        exclude = ("PELATIH", "DAFTAR")

    def create(self, validated_data):
        request = self.context.get("request", None)
        current_user = request.user

        data_pelatih_user = DataPelatihUser.objects.get(USER=current_user)
        id_daftar_jurnal_ekskul = request.parser_context.get("kwargs").get(
            "id_daftar_jurnal_ekskul"
        )

        validated_data["PELATIH"] = data_pelatih_user.DATA_PELATIH
        validated_data["DAFTAR"] = DaftarJurnalEkskul.objects.get(
            pk=id_daftar_jurnal_ekskul
        )

        return super().create(validated_data)


class JurnalEkskulListSerializer(serializers.ModelSerializer):
    PELATIH = serializers.SerializerMethodField("get_pelatih")
    EKSKUL = serializers.SerializerMethodField("get_ekskul")
    HARI = serializers.SerializerMethodField("get_hari")
    TAHUN_AJARAN = serializers.SerializerMethodField("get_tahun_ajaran")
    SEMESTER = serializers.SerializerMethodField("get_semester")

    class Meta:
        model = JurnalEkskul
        exclude = ("DAFTAR",)

    def get_pelatih(self, obj):
        return str(obj.PELATIH)

    def get_ekskul(self, obj):
        return str(obj.DAFTAR.EKSKUL)

    def get_hari(self, obj):
        return str(obj.DAFTAR.JADWAL_EKSKUL.HARI)

    def get_tahun_ajaran(self, obj):
        return str(obj.DAFTAR.JADWAL_EKSKUL.TAHUN_AJARAN)

    def get_semester(self, obj):
        return str(obj.DAFTAR.SEMESTER)


class AbsensiEkskulSerializer(serializers.ModelSerializer):
    class Meta:
        model = AbsensiEkskul
        fields = "__all__"


class AbsensiEkskulListSerializer(serializers.ModelSerializer):
    NAMA = serializers.SerializerMethodField("get_nama")

    class Meta:
        model = AbsensiEkskul
        exclude = ("JURNAL_EKSKUL",)

    def get_nama(self, obj):
        return str(obj.NIS.NAMA)


class PengajuanEkskulSerializer(serializers.ModelSerializer):
    class Meta:
        model = PengajuanEkskul
        exclude = ("KELAS_SISWA", "EKSKUL", "TAHUN_AJARAN")

    def create(self, validated_data):
        request = self.context.get("request", None)
        current_user = request.user

        tahun_ajaran_aktif = Configuration.current().TAHUN_AJARAN_AKTIF
        data_siswa_user = DataSiswaUser.objects.get(USER=current_user)
        kelas_siswa = KelasSiswa.objects.get(
            NIS=data_siswa_user.DATA_SISWA,
            KELAS__KELAS__TAHUN_AJARAN=tahun_ajaran_aktif,
        )
        id_ekskul = request.parser_context.get("kwargs").get("id_katalog_ekskul")
        ekskul = KatalogEkskul.objects.get(pk=id_ekskul)

        # cek sudah melakukan pengajuan
        try:
            mengajukan = PengajuanEkskul.objects.get(
                KELAS_SISWA=kelas_siswa, EKSKUL=ekskul, TAHUN_AJARAN=tahun_ajaran_aktif
            )
        except:
            mengajukan = None

        if mengajukan:
            raise serializers.ValidationError(
                "Sudah pernah mengajukan pendaftaran, silahkan tunggu konfirmasi dari pelatih"
            )

        # cek sudah terdaftar
        try:
            terdaftar = AnggotaEkskul.objects.get(
                KELAS_SISWA=kelas_siswa, EKSKUL=ekskul, TAHUN_AJARAN=tahun_ajaran_aktif
            )
        except:
            terdaftar = None

        if terdaftar:
            raise serializers.ValidationError(
                "Sudah terdaftar di ekskul " + ekskul.NAMA
            )

        validated_data["KELAS_SISWA"] = kelas_siswa
        validated_data["TAHUN_AJARAN"] = tahun_ajaran_aktif
        validated_data["EKSKUL"] = ekskul

        return super().create(validated_data)


class PengajuanEkskulListSerializer(serializers.ModelSerializer):
    NIS = serializers.SerializerMethodField("get_nis")
    NAMA = serializers.SerializerMethodField("get_nama")
    KELAS = serializers.SerializerMethodField("get_kelas_siswa")
    EKSKUL = serializers.SerializerMethodField("get_ekskul")
    TAHUN_AJARAN = serializers.SerializerMethodField("get_tahun_ajaran")

    class Meta:
        model = PengajuanEkskul
        fields = "__all__"

    def get_nis(self, obj):
        return str(obj.KELAS_SISWA.NIS)

    def get_nama(self, obj):
        return str(obj.KELAS_SISWA.NIS.NAMA)

    def get_kelas_siswa(self, obj):
        return str(obj.KELAS_SISWA.KELAS)

    def get_ekskul(self, obj):
        return str(obj.EKSKUL)

    def get_tahun_ajaran(self, obj):
        return str(obj.TAHUN_AJARAN)


class ProgramKerjaEkskulSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgramKerjaEkskul
        fields = "__all__"


class ProgramKerjaEkskulListSerializer(serializers.ModelSerializer):
    PELATIH = serializers.SerializerMethodField("get_pelatih")
    EKSKUL = serializers.SerializerMethodField("get_ekskul")
    TAHUN_AJARAN = serializers.SerializerMethodField("get_tahun_ajaran")

    class Meta:
        model = ProgramKerjaEkskul
        fields = "__all__"

    def get_pelatih(self, obj):
        return str(obj.PELATIH)

    def get_ekskul(self, obj):
        return str(obj.EKSKUL)

    def get_tahun_ajaran(self, obj):
        return str(obj.TAHUN_AJARAN)


class NilaiEkskulSerializer(serializers.ModelSerializer):
    class Meta:
        model = NilaiEkskul
        fields = "__all__"


class NilaiEkskulListSerializer(serializers.ModelSerializer):
    DATA_ANGGOTA = serializers.SerializerMethodField("get_data_anggota")
    SEMESTER = serializers.SerializerMethodField("get_semester")

    class Meta:
        model = NilaiEkskul
        fields = "__all__"

    def get_data_anggota(self, obj):
        return str(obj.DATA_ANGGOTA)

    def get_semester(self, obj):
        return str(obj.SEMESTER)


class AnggotaEkskulListSerializer(serializers.ModelSerializer):
    NIS = serializers.SerializerMethodField("get_nis")
    NAMA = serializers.SerializerMethodField("get_nama")
    KELAS_SISWA = serializers.SerializerMethodField("get_kelas_siswa")

    class Meta:
        model = AnggotaEkskul
        exclude = ("EKSKUL", "TAHUN_AJARAN")

    def get_nis(self, obj):
        return str(obj.KELAS_SISWA.NIS.NIS)

    def get_nama(self, obj):
        return str(obj.KELAS_SISWA.NIS.NAMA)

    def get_kelas_siswa(self, obj):
        return str(obj.KELAS_SISWA.KELAS)
