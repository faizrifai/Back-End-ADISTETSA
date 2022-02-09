from .models import *
from rest_framework import serializers

from adistetsa.permissions import is_in_group
from kustom_autentikasi.models import DataSiswaUser, DataGuruUser


class KatalogBukuCopySerializer(serializers.ModelSerializer):
    JUDUL = serializers.SerializerMethodField('get_judul')
    PENULIS = serializers.SerializerMethodField('get_kode_author')   
    BAHASA = serializers.SerializerMethodField('get_bahasa')
    TAHUN_TERBIT = serializers.SerializerMethodField('get_tahun_terbit')
    MEDIA = serializers.SerializerMethodField('get_kode_media')

    class Meta:
        model = KatalogBukuCopy
        fields = ('id', 'JUDUL', 'PENULIS', 'BAHASA', 'TAHUN_TERBIT', 'MEDIA')

    def get_bahasa(self, obj):
        return obj.DATA_DONASI.REGISTER_DONASI.BAHASA.BAHASA

    def get_kode_media(self, obj):
        return obj.DATA_DONASI.REGISTER_DONASI.KODE_MEDIA.NAMA_MEDIA

    def get_kode_author(self, obj):
        return obj.DATA_DONASI.REGISTER_DONASI.KODE_AUTHOR.NAMA_AUTHOR

    def get_tahun_terbit(self, obj):
        return obj.DATA_DONASI.REGISTER_DONASI.TAHUN_TERBIT.TAHUN_TERBIT

    def get_judul(self, obj):
        return obj.DATA_DONASI.REGISTER_DONASI.JUDUL


class KatalogBukuListSerializer(serializers.ModelSerializer):
    PENULIS = serializers.SerializerMethodField('get_kode_author')   
    BAHASA = serializers.SerializerMethodField('get_bahasa')
    TAHUN_TERBIT = serializers.SerializerMethodField('get_tahun_terbit')
    MEDIA = serializers.SerializerMethodField('get_kode_media')
    TERSEDIA = serializers.SerializerMethodField('get_tersedia')
    
    class Meta:
        model = KatalogBuku
        fields = ('JUDUL', 'PENULIS', 'BAHASA', 'TAHUN_TERBIT', 'MEDIA', 'TERSEDIA')

    def get_bahasa(self, obj):
        return obj.BAHASA.BAHASA

    def get_kode_media(self, obj):
        return obj.KODE_MEDIA.NAMA_MEDIA

    def get_kode_author(self, obj):
        return obj.KODE_AUTHOR.NAMA_AUTHOR

    def get_tahun_terbit(self, obj):
        return obj.TAHUN_TERBIT.TAHUN_TERBIT

    def get_tersedia(self, obj):
        total_tersedia = 0
        total = 0
        
        donasi_buku = DonasiBuku.objects.filter(REGISTER_DONASI=obj.REGISTER)
        for data_donasi in donasi_buku:
            buku_copy = KatalogBukuCopy.objects.filter(DATA_DONASI=data_donasi)
            for data in buku_copy:
                if data.STATUS == 'Sudah Dikembalikan':
                    total_tersedia += 1
                
                total += 1
                
        return str(total_tersedia) + '/' + str(total)


class PengajuanPeminjamanSiswaSerializer(serializers.ModelSerializer):
    BUKU = serializers.PrimaryKeyRelatedField(many=True, queryset=KatalogBukuCopy.objects.all())

    class Meta:
        model = PengajuanPeminjamanSiswa
        exclude = ('NIS',)

    def create(self, validated_data):
        request = self.context.get('request', None)
        current_user = request.user
        if (is_in_group(current_user, 'Siswa')):
            data_siswa_user = DataSiswaUser.objects.get(USER=current_user)
            validated_data['NIS'] = data_siswa_user.DATA_SISWA

        buku = validated_data.pop('BUKU')
        data_pengajuan = PengajuanPeminjamanSiswa.objects.create(**validated_data)

        for data in buku:
            data_pengajuan.BUKU.add(data)

        return data_pengajuan


class PengajuanPeminjamanSiswaAdminSerializer(serializers.ModelSerializer):
    BUKU = serializers.PrimaryKeyRelatedField(many=True, queryset=KatalogBukuCopy.objects.all())

    class Meta:
        model = PengajuanPeminjamanSiswa
        fields = '__all__'


class PengajuanPeminjamanGuruSerializer(serializers.ModelSerializer):
    BUKU = serializers.PrimaryKeyRelatedField(many=True, queryset=KatalogBukuCopy.objects.all())

    class Meta:
        model = PengajuanPeminjamanGuru
        exclude = ('DATA_GURU',)

    def create(self, validated_data):
        request = self.context.get('request', None)
        current_user = request.user
        if (is_in_group(current_user, 'Guru')):
            data_guru_user = DataGuruUser.objects.get(USER=current_user)
            validated_data['DATA_GURU'] = data_guru_user.DATA_GURU

        buku = validated_data.pop('BUKU')
        data_pengajuan = PengajuanPeminjamanGuru.objects.create(**validated_data)

        for data in buku:
            data_pengajuan.BUKU.add(data)

        return data_pengajuan


class PengajuanPeminjamanGuruAdminSerializer(serializers.ModelSerializer):
    BUKU = serializers.PrimaryKeyRelatedField(many=True, queryset=KatalogBukuCopy.objects.all())

    class Meta:
        model = PengajuanPeminjamanGuru
        fields = '__all__'


class RiwayatPeminjamanSiswaSerializer(serializers.ModelSerializer):
    class Meta:
        model = RiwayatPeminjamanSiswa
        exclude = ('NIS',)


class RiwayatPeminjamanSiswaAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = RiwayatPeminjamanSiswa
        fields = '__all__'


class RiwayatPeminjamanGuruSerializer(serializers.ModelSerializer):
    class Meta:
        model = RiwayatPeminjamanGuru
        exclude = ('DATA_GURU',)


class RiwayatPeminjamanGuruAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = RiwayatPeminjamanGuru
        fields = '__all__'
