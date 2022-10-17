from rest_framework import serializers

from .models import *


class MataPelajaranSerializer(serializers.ModelSerializer):
    class Meta:
        model = MataPelajaran
        fields = "__all__"


class TahunAjaranSerializer(serializers.ModelSerializer):
    tahun_ajaran = serializers.SerializerMethodField("get_tahun_ajaran")

    class Meta:
        model = TahunAjaran
        fields = ("ID", "tahun_ajaran")

    def get_tahun_ajaran(self, obj):
        str_tahun = str(obj.TAHUN_AJARAN_AWAL) + "/" + str(obj.TAHUN_AJARAN_AKHIR)

        return str_tahun


class SemesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataSemester
        fields = ("id", "NAMA")


class KelasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kelas
        fields = ("ID", "KODE_KELAS")


class JadwalPekanEfektifSemesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = JadwalPekanEfektifSemester
        fields = "__all__"


class JadwalPekanTidakEfektifSerializer(serializers.ModelSerializer):
    class Meta:
        model = JadwalPekanTidakEfektif
        fields = "__all__"


class KelasSiswaSerializer(serializers.ModelSerializer):
    KELAS = serializers.SerializerMethodField("get_kelas")

    class Meta:
        model = KelasSiswa
        fields = "__all__"

    def get_kelas(self, obj):
        return str(obj.KELAS)
