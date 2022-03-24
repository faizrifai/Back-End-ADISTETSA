from .models import *
from rest_framework import serializers
from rest_framework.reverse import reverse

class LogUKSListSerializer(serializers.Serializer):
    ID = serializers.IntegerField()
    NAMA = serializers.CharField()
    JENIS_PTK = serializers.CharField()
    TANGGAL = serializers.DateField()
    DETAIL_URL = serializers.URLField()

class LogUKSDetailSiswaSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogUKSSiswa
        fields = '__all__'

class LogUKSDetailTendikSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogUKSTendik
        fields = '__all__'

class TambahLogUKSSiswaSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogUKSSiswa
        exclude = ('JENIS_PTK',)

    def create(self, validated_data):
        validated_data['JENIS_PTK'] = 'Siswa'
        
        return super().create(validated_data)

class TambahLogUKSTendikSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogUKSTendik
        fields = '__all__'

class BukuTamuListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BukuTamu
        exclude = ('HARI',)