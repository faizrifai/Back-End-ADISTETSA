from .models import *
from rest_framework import serializers


class KTSPSerializer(serializers.ModelSerializer):
    class Meta:
        model = KTSP
        fields = '__all__'


class SilabusRPBSerializer(serializers.ModelSerializer):
    class Meta:
        model = SilabusRPB
        fields = '__all__'


class TataTertibSerializer(serializers.ModelSerializer):
    class Meta:
        model = TataTertib
        fields = '__all__'


class PoinPelanggaranSerializer(serializers.ModelSerializer):
    class Meta:
        model = PoinPelanggaran
        fields = '__all__'

class JadwalPekanAktifSerializer(serializers.ModelSerializer):
    MINGGU_EFEKTIF = serializers.SerializerMethodField('get_minggu_efektif')
    MINGGU_TIDAK_EFEKTIF = serializers.SerializerMethodField('get_minggu_tidak_efektif')

    class Meta:
        model = JadwalPekanAktif
        fields = '__all__'

    def get_minggu_efektif(self, obj):
        minggu_efektif = []

        for m2m in obj.MINGGU_EFEKTIF.all():
            minggu_efektif.append(
                {
                    'BULAN': m2m.BULAN, 'JUMLAH_MINGGU': m2m.JUMLAH_MINGGU, 'JUMLAH_MINGGU_EFEKTIF': m2m.JUMLAH_MINGGU_EFEKTIF, 'JUMLAH_MINGGU_TIDAK_EFEKTIF': m2m.JUMLAH_MINGGU_TIDAK_EFEKTIF, 'KETERANGAN': m2m.KETERANGAN
                }
            )

        return minggu_efektif

    def get_minggu_tidak_efektif(self, obj):
        minggu_tidak_efektif = []

        for m2m in obj.MINGGU_TIDAK_EFEKTIF.all():
            minggu_tidak_efektif.append(
                {
                    'URAIAN_KEGIATAN': m2m.URAIAN_KEGIATAN, 'JUMLAH_MINGGU': m2m.JUMLAH_MINGGU, 'KETERANGAN': m2m.KETERANGAN
                }
            )

        return minggu_tidak_efektif