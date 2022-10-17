from .models import *
from rest_framework import serializers

from dataprofil.models import DataSiswa, DataGuru, DataKaryawan


class LogUKSListSerializer(serializers.Serializer):
    ID = serializers.IntegerField()
    NAMA = serializers.CharField()
    JENIS_PTK = serializers.CharField()
    TANGGAL = serializers.DateField()
    DETAIL_URL = serializers.URLField()


class LogUKSDetailSiswaSerializer(serializers.ModelSerializer):
    NAMA = serializers.SerializerMethodField("get_nama")

    class Meta:
        model = LogUKSSiswa
        fields = "__all__"

    def get_nama(self, obj):
        return str(obj.NAMA)


class LogUKSDetailTendikSerializer(serializers.ModelSerializer):
    NAMA = serializers.SerializerMethodField("get_nama")

    class Meta:
        model = LogUKSTendik
        fields = "__all__"

    def get_nama(self, obj):
        return str(obj.NAMA)


class LogUKSDetailKaryawanSerializer(serializers.ModelSerializer):
    NAMA = serializers.SerializerMethodField("get_nama")

    class Meta:
        model = LogUKSKaryawan
        fields = "__all__"

    def get_nama(self, obj):
        return str(obj.NAMA)


class TambahLogUKSSiswaSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogUKSSiswa
        exclude = ("JENIS_PTK",)

    def create(self, validated_data):
        validated_data["JENIS_PTK"] = "Siswa"

        return super().create(validated_data)


class TambahLogUKSTendikSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogUKSTendik
        fields = "__all__"


class TambahLogUKSKaryawanSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogUKSKaryawan
        fields = "__all__"


class BukuTamuListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BukuTamu
        fields = "__all__"


class BukuTamuPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BukuTamu
        exclude = ("HARI",)


class DataSiswaHumasSerializer(serializers.ModelSerializer):
    NAMA = serializers.SerializerMethodField("get_nama")
    KELAS = serializers.SerializerMethodField("get_kelas")

    class Meta:
        model = KelasSiswa
        fields = "__all__"

    def get_nama(self, obj):
        return str(obj.NIS)

    def get_kelas(self, obj):
        return str(obj.KELAS)


class DataGuruTendikSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataGuru
        fields = "__all__"


class DataKaryawanTendikSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataKaryawan
        fields = "__all__"
