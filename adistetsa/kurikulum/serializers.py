from datetime import datetime

from rest_framework import serializers

from .models import *


class KTSPSerializer(serializers.ModelSerializer):
    class Meta:
        model = KTSP
        fields = "__all__"


class KTSPListSerializer(serializers.ModelSerializer):
    TAHUN_AJARAN = serializers.SerializerMethodField("get_tahun_ajaran")

    class Meta:
        model = KTSP
        fields = "__all__"

    def get_tahun_ajaran(self, obj):
        return str(obj.TAHUN_AJARAN)


class SilabusRPBSerializer(serializers.ModelSerializer):
    class Meta:
        model = SilabusRPB
        fields = "__all__"


class SilabusRPBListSerializer(serializers.ModelSerializer):
    MATA_PELAJARAN = serializers.SerializerMethodField("get_mata_pelajaran")
    TAHUN_AJARAN = serializers.SerializerMethodField("get_tahun_ajaran")
    KELAS = serializers.SerializerMethodField("get_kelas")
    SEMESTER = serializers.SerializerMethodField("get_semester")

    class Meta:
        model = SilabusRPB
        fields = "__all__"

    def get_mata_pelajaran(self, obj):
        return str(obj.MATA_PELAJARAN.NAMA)

    def get_tahun_ajaran(self, obj):
        return str(obj.TAHUN_AJARAN)

    def get_kelas(self, obj):
        return str(obj.KELAS)

    def get_semester(self, obj):
        return str(obj.SEMESTER)


class PoinPelanggaranSerializer(serializers.ModelSerializer):
    class Meta:
        model = PoinPelanggaran
        fields = "__all__"


class JadwalPekanAktifListSerializer(serializers.ModelSerializer):
    MATA_PELAJARAN = serializers.SerializerMethodField("get_mata_pelajaran")
    KELAS = serializers.SerializerMethodField("get_kelas")
    SEMESTER = serializers.SerializerMethodField("get_semester")

    class Meta:
        model = JadwalPekanAktif
        exclude = ("MINGGU_EFEKTIF", "MINGGU_TIDAK_EFEKTIF")

    def get_mata_pelajaran(self, obj):
        return str(obj.MATA_PELAJARAN.NAMA)

    def get_kelas(self, obj):
        return str(obj.KELAS)

    def get_semester(self, obj):
        return str(obj.SEMESTER)


class JadwalPekanAktifDetailSerializer(serializers.ModelSerializer):
    MATA_PELAJARAN = serializers.SerializerMethodField("get_mata_pelajaran")
    KELAS = serializers.SerializerMethodField("get_kelas")
    SEMESTER = serializers.SerializerMethodField("get_semester")
    MINGGU_EFEKTIF = serializers.SerializerMethodField("get_minggu_efektif")
    MINGGU_TIDAK_EFEKTIF = serializers.SerializerMethodField("get_minggu_tidak_efektif")

    class Meta:
        model = JadwalPekanAktif
        fields = "__all__"

    def get_mata_pelajaran(self, obj):
        return str(obj.MATA_PELAJARAN.NAMA)

    def get_kelas(self, obj):
        return str(obj.KELAS)

    def get_semester(self, obj):
        return str(obj.SEMESTER)

    def get_minggu_efektif(self, obj):
        minggu_efektif = []

        for m2m in obj.MINGGU_EFEKTIF.all():
            minggu_efektif.append(
                {
                    "BULAN": m2m.BULAN,
                    "JUMLAH_MINGGU": m2m.JUMLAH_MINGGU,
                    "JUMLAH_MINGGU_EFEKTIF": m2m.JUMLAH_MINGGU_EFEKTIF,
                    "JUMLAH_MINGGU_TIDAK_EFEKTIF": m2m.JUMLAH_MINGGU_TIDAK_EFEKTIF,
                    "KETERANGAN": m2m.KETERANGAN,
                }
            )

        return minggu_efektif

    def get_minggu_tidak_efektif(self, obj):
        minggu_tidak_efektif = []

        for m2m in obj.MINGGU_TIDAK_EFEKTIF.all():
            minggu_tidak_efektif.append(
                {
                    "URAIAN_KEGIATAN": m2m.URAIAN_KEGIATAN,
                    "JUMLAH_MINGGU": m2m.JUMLAH_MINGGU,
                    "KETERANGAN": m2m.KETERANGAN,
                }
            )

        return minggu_tidak_efektif


class JadwalMengajarSerializer(serializers.ModelSerializer):
    GURU = serializers.SerializerMethodField("get_guru")
    TAHUN_AJARAN = serializers.SerializerMethodField("get_tahun_ajaran")
    KELAS = serializers.SerializerMethodField("get_kelas")
    MATA_PELAJARAN = serializers.SerializerMethodField("get_mata_pelajaran")
    WAKTU_PELAJARAN = serializers.SerializerMethodField("get_waktu_pelajaran")
    SEMESTER = serializers.SerializerMethodField("get_semester")
    HARI = serializers.SerializerMethodField("get_hari")

    class Meta:
        model = JadwalMengajar
        exclude = ("JUMLAH_WAKTU",)

    def get_guru(self, obj):
        return obj.GURU.NAMA_LENGKAP

    def get_tahun_ajaran(self, obj):
        return str(obj.TAHUN_AJARAN)

    def get_kelas(self, obj):
        return str(obj.KELAS)

    def get_mata_pelajaran(self, obj):
        return str(obj.MATA_PELAJARAN)

    def get_waktu_pelajaran(self, obj):
        waktu_pelajaran = []
        for data in obj.WAKTU_PELAJARAN.all():
            waktu_pelajaran.append(str(data))

        return waktu_pelajaran

    def get_semester(self, obj):
        return str(obj.SEMESTER)

    def get_hari(self, obj):
        return str(obj.HARI)


class DaftarJurnalBelajarGuruListSerializer(serializers.ModelSerializer):
    GURU = serializers.SerializerMethodField("get_guru")
    MATA_PELAJARAN = serializers.SerializerMethodField("get_mata_pelajaran")
    KELAS = serializers.SerializerMethodField("get_kelas")
    SEMESTER = serializers.SerializerMethodField("get_semester")
    WAKTU_PELAJARAN = serializers.SerializerMethodField("get_waktu_pelajaran")

    class Meta:
        model = DaftarJurnalBelajar
        fields = "__all__"

    def get_guru(self, obj):
        return str(obj.GURU.NAMA_LENGKAP)

    def get_mata_pelajaran(self, obj):
        return str(obj.MATA_PELAJARAN.NAMA)

    def get_kelas(self, obj):
        return str(obj.KELAS)

    def get_semester(self, obj):
        return str(obj.SEMESTER)

    def get_waktu_pelajaran(self, obj):
        waktu_pelajaran = []
        data_jadwal = JadwalMengajar.objects.filter(
            GURU=obj.GURU,
            MATA_PELAJARAN=obj.MATA_PELAJARAN,
            KELAS=obj.KELAS,
            SEMESTER=obj.SEMESTER,
        ).order_by("-HARI")

        for data in data_jadwal:
            waktu = []

            for w in data.WAKTU_PELAJARAN.all():
                waktu.append(str(w.JAM_KE))

            s = "Jam " + ", ".join(waktu)
            waktu_pelajaran.append(f"{str(data.HARI)} {s}")

        return waktu_pelajaran


class JurnalBelajarGuruSerializer(serializers.ModelSerializer):
    class Meta:
        model = JurnalBelajar
        exclude = ("DAFTAR", "GURU", "TANGGAL_MENGAJAR")

    def create(self, validated_data):
        request = self.context.get("request")
        pk = request.parser_context.get("kwargs").get("id_jurnal_belajar_mengajar")
        daftar_jurnal_belajar = DaftarJurnalBelajar.objects.get(pk=pk)

        validated_data["DAFTAR"] = daftar_jurnal_belajar
        validated_data["GURU"] = daftar_jurnal_belajar.GURU
        validated_data["TANGGAL_MENGAJAR"] = datetime.today()

        try:
            return super().create(validated_data)
        except Exception as e:
            if "UNIQUE constraint failed" in str(e):
                raise serializers.ValidationError(
                    "Pertemuan " + str(validated_data["PERTEMUAN"]) + " sudah ada"
                )
            else:
                raise serializers.ValidationError(str(e))


class JurnalBelajarGuruListSerializer(serializers.ModelSerializer):
    GURU = serializers.SerializerMethodField("get_guru")
    MATA_PELAJARAN = serializers.SerializerMethodField("get_mata_pelajaran")
    KELAS = serializers.SerializerMethodField("get_kelas")
    SEMESTER = serializers.SerializerMethodField("get_semester")
    HARI = serializers.SerializerMethodField("get_hari")

    class Meta:
        model = JurnalBelajar
        exclude = ("DAFTAR",)

    def get_guru(self, obj):
        return str(obj.GURU.NAMA_LENGKAP)

    def get_mata_pelajaran(self, obj):
        return str(obj.DAFTAR.MATA_PELAJARAN)

    def get_kelas(self, obj):
        return str(obj.DAFTAR.KELAS)

    def get_semester(self, obj):
        return str(obj.DAFTAR.SEMESTER)

    def get_hari(self, obj):
        return str(obj.DAFTAR.JADWAL_MENGAJAR.HARI)


class TambahKelasSiswaSerializer(serializers.ModelSerializer):
    class Meta:
        model = KelasSiswa
        fields = "__all__"


class AbsensiSiswaListSerializer(serializers.ModelSerializer):
    NAMA = serializers.SerializerMethodField("get_nama")

    class Meta:
        model = AbsensiSiswa
        exclude = ("JURNAL_BELAJAR",)

    def get_nama(self, obj):
        return obj.NIS.NAMA


class AbsensiSiswaSerializer(serializers.ModelSerializer):
    class Meta:
        model = AbsensiSiswa
        exclude = ("JURNAL_BELAJAR",)
