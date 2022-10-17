from .models import (
    SanitasiDrainase,
    JaringanKerja,
    Publikasi,
    DaftarKader,
    KegiatanKader,
    PembibitanPohon,
    PemeliharaanPohon,
    PemeliharaanSampah,
    PenanamanPohon,
    PenerapanPRLH,
    KaryaInovatif,
    Konservasi,
    ReuseReduceRecycle,
)
from rest_framework import serializers

from kustom_autentikasi.models import DataSiswa


class SanitasiDrainaseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SanitasiDrainase
        fields = "__all__"


class JaringanKerjaListSerializer(serializers.ModelSerializer):
    class Meta:
        model = JaringanKerja
        fields = "__all__"


class PublikasiListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publikasi
        fields = "__all__"


class KaderListSerializer(serializers.ModelSerializer):
    NAMA = serializers.SerializerMethodField("get_nama")
    NOMOR_HP = serializers.SerializerMethodField("get_nomor_hp")
    ALAMAT = serializers.SerializerMethodField("get_alamat")

    class Meta:
        model = DaftarKader
        fields = "__all__"

    def get_nama(self, obj):
        data_siswa = DataSiswa.objects.get(NIS=obj.NIS.NIS)
        return str(data_siswa.NAMA)

    def get_nomor_hp(self, obj):
        data_siswa = DataSiswa.objects.get(NIS=obj.NIS.NIS)
        return str(data_siswa.HP)

    def get_alamat(self, obj):
        data_siswa = DataSiswa.objects.get(NIS=obj.NIS.NIS)
        return str(data_siswa.ALAMAT)


class KegiatanKaderListSerializer(serializers.ModelSerializer):
    class Meta:
        model = KegiatanKader
        fields = "__all__"


class KonservasiListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Konservasi
        fields = "__all__"


class PembibitanPohonListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PembibitanPohon
        fields = "__all__"


class PemeliharaanPohonListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PemeliharaanPohon
        fields = "__all__"


class KaryaInovatifListSerializer(serializers.ModelSerializer):
    class Meta:
        model = KaryaInovatif
        fields = "__all__"


class PenerapanPRLHListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PenerapanPRLH
        fields = "__all__"


class ReuseReduceRecycleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReuseReduceRecycle
        fields = "__all__"


class PemeliharaanSampahListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PemeliharaanSampah
        fields = "__all__"


class PenanamanPohonListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PenanamanPohon
        fields = "__all__"


class TabunganSampahListSerializer(serializers.Serializer):
    bulan = serializers.CharField()
    sampah_kering = serializers.IntegerField()
    sampah_basah = serializers.IntegerField()
    total_tabungan = serializers.IntegerField()
