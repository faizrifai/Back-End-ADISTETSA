from .models import *
from rest_framework import serializers

from adistetsa.permissions import is_in_group
from kustom_autentikasi.models import *

class SanitasiDrainaseListSerializer(serializers.ModelSerializer):

    class Meta:
        model = SanitasiDrainase
        fields = '__all__'

class JaringanKerjaListSerializer(serializers.ModelSerializer):

    class Meta:
        model = JaringanKerja
        fields = '__all__'

class PublikasiListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Publikasi
        fields = '__all__'

class KaderListSerializer(serializers.ModelSerializer):
    NAMA = serializers.SerializerMethodField('get_nama')

    class Meta:
        model = DaftarKader
        fields = '__all__'

    def get_nama(self, obj):
        data_siswa = DataSiswa.objects.get(NIS=obj.NIS.NIS)
        return str(data_siswa.NAMA)  

class KegiatanKaderListSerializer(serializers.ModelSerializer):

    class Meta:
        model = KegiatanKader
        fields = '__all__'

class KonservasiListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Konservasi
        fields = '__all__'

class PembibitanPohonListSerializer(serializers.ModelSerializer):

    class Meta:
        model = PembibitanPohon
        fields = '__all__'

class PemeliharaanPohonListSerializer(serializers.ModelSerializer):

    class Meta:
        model = PemeliharaanPohon
        fields = '__all__'

class KaryaInovatifListSerializer(serializers.ModelSerializer):

    class Meta:
        model = KaryaInovatif
        fields = '__all__'

class PenerapanPRLHListSerializer(serializers.ModelSerializer):

    class Meta:
        model = PenerapanPRLH
        fields = '__all__'

class ReuseReduceRecycleListSerializer(serializers.ModelSerializer):

    class Meta:
        model = ReuseReduceRecycle
        fields = '__all__'

class PemeliharaanSampahListSerializer(serializers.ModelSerializer):

    class Meta:
        model = PemeliharaanSampah
        fields = '__all__'