from .models import *
from rest_framework import serializers

from adistetsa.permissions import is_in_group
from kustom_autentikasi.models import DataSiswaUser, DataGuruUser


class KatalogSaranaSerializer(serializers.ModelSerializer):
    JENIS = serializers.SerializerMethodField('get_jenis')
    # PENULIS = serializers.SerializerMethodField('get_kode_author')   
    # BAHASA = serializers.SerializerMethodField('get_bahasa')
    # TAHUN_TERBIT = serializers.SerializerMethodField('get_tahun_terbit')
    # MEDIA = serializers.SerializerMethodField('get_kode_media')

    class Meta:
        model = Sarana
        fields = '__all__'

    # def get_bahasa(self, obj):
    #     return obj.DATA_DONASI.REGISTER_DONASI.BAHASA.BAHASA

    # def get_kode_media(self, obj):
    #     return obj.DATA_DONASI.REGISTER_DONASI.KODE_MEDIA.NAMA_MEDIA

    # def get_kode_author(self, obj):
    #     return obj.DATA_DONASI.REGISTER_DONASI.KODE_AUTHOR.NAMA_AUTHOR

    # def get_tahun_terbit(self, obj):
    #     return obj.DATA_DONASI.REGISTER_DONASI.TAHUN_TERBIT.TAHUN_TERBIT

    def get_jenis(self, obj):
        return obj.JENIS.KATEGORI


class PengajuanPeminjamanBarangSerializer(serializers.ModelSerializer):
    ALAT = serializers.PrimaryKeyRelatedField(many=True, queryset=Sarana.objects.all())

    class Meta:
        model = PengajuanPeminjamanBarang
        exclude = ('USER',)

    def create(self, validated_data):
        request = self.context.get('request', None)
        current_user = request.user
        validated_data['USER'] = current_user

        alat = validated_data.pop('ALAT')
        data_pengajuan = PengajuanPeminjamanBarang.objects.create(**validated_data)

        for data in alat:
            data_pengajuan.ALAT.add(data)

        return data_pengajuan


class PengajuanPeminjamanBarangListSerializer(serializers.ModelSerializer):
    ALAT = serializers.SerializerMethodField('get_alat')

    class Meta:
        model = PengajuanPeminjamanBarang
        exclude = ('USER',)

    def get_alat(self, obj):
        alat = obj.ALAT
        daftar_alat = []
        for data in alat.all():
            daftar_alat.append(str(data))

        return daftar_alat


class PengajuanPeminjamanBarangAdminSerializer(serializers.ModelSerializer):
    ALAT = serializers.SerializerMethodField('get_alat')

    class Meta:
        model = PengajuanPeminjamanBarang
        fields = '__all__'

    def get_alat(self, obj):
        alat = obj.ALAT
        daftar_alat = []
        for data in alat.all():
            daftar_alat.append(str(data))

        return daftar_alat


class RiwayatPeminjamanBarangSerializer(serializers.ModelSerializer):
    class Meta:
        model = RiwayatPeminjamanBarang
        fields = '__all__'


class RiwayatPeminjamanBarangListSerializer(serializers.ModelSerializer):
    ALAT = serializers.SerializerMethodField('get_alat')

    class Meta:
        model = RiwayatPeminjamanBarang
        fields = '__all__'

    def get_alat(self, obj):
        alat = obj.ALAT
        daftar_alat = []
        for data in alat.all():
            daftar_alat.append(str(data))

        return daftar_alat


class KatalogRuanganSerializer(serializers.ModelSerializer):
    JENIS = serializers.SerializerMethodField('get_jenis')
    # PENULIS = serializers.SerializerMethodField('get_kode_author')   
    # BAHASA = serializers.SerializerMethodField('get_bahasa')
    # TAHUN_TERBIT = serializers.SerializerMethodField('get_tahun_terbit')
    # MEDIA = serializers.SerializerMethodField('get_kode_media')

    class Meta:
        model = Ruangan
        fields = '__all__'

    # def get_bahasa(self, obj):
    #     return obj.DATA_DONASI.REGISTER_DONASI.BAHASA.BAHASA

    # def get_kode_media(self, obj):
    #     return obj.DATA_DONASI.REGISTER_DONASI.KODE_MEDIA.NAMA_MEDIA

    # def get_kode_author(self, obj):
    #     return obj.DATA_DONASI.REGISTER_DONASI.KODE_AUTHOR.NAMA_AUTHOR

    # def get_tahun_terbit(self, obj):
    #     return obj.DATA_DONASI.REGISTER_DONASI.TAHUN_TERBIT.TAHUN_TERBIT

    def get_jenis(self, obj):
        return obj.JENIS.KATEGORI


class PengajuanPeminjamanRuanganSerializer(serializers.ModelSerializer):
    RUANGAN = serializers.PrimaryKeyRelatedField(many=True, queryset=JadwalPenggunaanRuangan.objects.all())

    class Meta:
        model = PengajuanPeminjamanRuangan
        exclude = ('USER',)

    def create(self, validated_data):
        request = self.context.get('request', None)
        current_user = request.user
        validated_data['USER'] = current_user

        ruangan = validated_data.pop('RUANGAN')
        data_pengajuan = PengajuanPeminjamanRuangan.objects.create(**validated_data)

        for data in ruangan:
            data_pengajuan.RUANGAN.add(data)

        return data_pengajuan


class PengajuanPeminjamanRuanganListSerializer(serializers.ModelSerializer):
    RUANGAN = serializers.SerializerMethodField('get_ruangan')

    class Meta:
        model = PengajuanPeminjamanRuangan
        exclude = ('USER',)

    def get_ruangan(self, obj):
        ruangan = obj.RUANGAN
        daftar_ruangan = []
        for data in ruangan.all():
            daftar_ruangan.append(str(data))

        return daftar_ruangan


class RiwayatPeminjamanRuanganSerializer(serializers.ModelSerializer):
    class Meta:
        model = RiwayatPeminjamanRuangan
        fields = '__all__'


class RiwayatPeminjamanRuanganListSerializer(serializers.ModelSerializer):
    RUANGAN = serializers.SerializerMethodField('get_ruangan')

    class Meta:
        model = RiwayatPeminjamanRuangan
        fields = '__all__'

    def get_ruangan(self, obj):
        ruangan = obj.RUANGAN
        daftar_ruangan = []
        for data in ruangan.all():
            daftar_ruangan.append(str(data))

        return daftar_ruangan