from .models import *
from rest_framework import serializers

class KatalogBukuSerializer(serializers.ModelSerializer):
    class Meta:
        model = KatalogBuku
        fields = '__all__'

class KatalogBukuListSerializer(serializers.ModelSerializer):
    BAHASA = serializers.SerializerMethodField('get_bahasa')
    KODE_MEDIA = serializers.SerializerMethodField('get_kode_media')
    TIPE_KODE = serializers.SerializerMethodField('get_tipe_kode')
    KODE_AUTHOR = serializers.SerializerMethodField('get_kode_author')   
    TAHUN_TERBIT = serializers.SerializerMethodField('get_tahun_terbit')
    KODE_LOKASI = serializers.SerializerMethodField('get_kode_lokasi')
    LOKASI_SPESIFIK = serializers.SerializerMethodField('get_lokasi_spesifik')
    KODE_DONASI = serializers.SerializerMethodField('get_kode_donasi')
    OPERATOR_CODE = serializers.SerializerMethodField('get_operator_code') 
    
    class Meta:
        model = KatalogBuku
        fields = '__all__'

    def get_bahasa(self, obj):
        return str(obj.BAHASA)

    def get_kode_media(self, obj):
        return str(obj.KODE_MEDIA)

    def get_tipe_kode(self, obj):
        return str(obj.TIPE_KODE)

    def get_kode_author(self, obj):
        return str(obj.KODE_AUTHOR) 

    def get_tahun_terbit(self, obj):
        return str(obj.TAHUN_TERBIT) 

    def get_kode_lokasi(self, obj):
        return str(obj.KODE_LOKASI)

    def get_lokasi_spesifik(self, obj):
        return str(obj.LOKASI_SPESIFIK)

    def get_kode_donasi(self, obj):
        return str(obj.KODE_DONASI)

    def get_operator_code(self, obj):
        return str(obj.OPERATOR_CODE) 

class PengajuanPeminjamanSiswaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PengajuanPeminjamanSiswa
        fields = '__all__'

class RiwayatPeminjamanSiswaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PengajuanPeminjamanSiswa
        fields = '__all__'

class KatalogBukuCopyListSerializer(serializers.ModelSerializer):
    
    DATA_BUKU = serializers.SerializerMethodField('get_data_buku')
    
    class Meta:
        model = KatalogBukuCopy
        fields = '__all__'

    def get_data_buku(self, obj):
        return str(obj.DATA_BUKU)

class PengajuanPeminjamanGuruSerializer(serializers.ModelSerializer):
    class Meta:
        model = PengajuanPeminjamanGuru
        exclude = ('DATA_GURU',)

class PengajuanPeminjamanGuruListSerializer(serializers.ModelSerializer):
    DATA_GURU = serializers.SerializerMethodField('get_data_guru')
    BUKU = serializers.SerializerMethodField('get_buku')

    class Meta:
        model = PengajuanPeminjamanGuru
        fields = '__all__'

    def get_data_guru(self, obj):
        return str(obj.DATA_GURU)

    def get_buku(self, obj):
        return str(obj.BUKU)

class RiwayatPeminjamanGuruSerializer(serializers.ModelSerializer):
    class Meta:
        model = RiwayatPeminjamanGuru
        fields = '__all__'

class RiwayatPeminjamanGuruListSerializer(serializers.ModelSerializer):
    DATA_GURU = serializers.SerializerMethodField('get_data_guru')
    BUKU = serializers.SerializerMethodField('get_buku')
    class Meta:
        model = RiwayatPeminjamanGuru
        fields = '__all__'
    
    def get_data_guru(self, obj):
        return str(obj.DATA_GURU)

    def get_buku(self, obj):
        return str(obj.BUKU)
