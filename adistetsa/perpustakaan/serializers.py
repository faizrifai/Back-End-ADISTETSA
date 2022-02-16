from .models import *
from rest_framework import serializers

from adistetsa.permissions import is_in_group
from kustom_autentikasi.models import DataSiswaUser, DataGuruUser


class KatalogBukuCopySerializer(serializers.ModelSerializer):
    REGISTER = serializers.SerializerMethodField('get_register')
    JUDUL = serializers.SerializerMethodField('get_judul')
    PENULIS = serializers.SerializerMethodField('get_kode_author')   
    BAHASA = serializers.SerializerMethodField('get_bahasa')
    TAHUN_TERBIT = serializers.SerializerMethodField('get_tahun_terbit')
    MEDIA = serializers.SerializerMethodField('get_kode_media')

    class Meta:
        model = KatalogBukuCopy
        fields = ('id', 'REGISTER', 'JUDUL', 'PENULIS', 'BAHASA', 'TAHUN_TERBIT', 'MEDIA')

    def get_register(self, obj):
        return str(obj.REGISTER_COPY)

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
    JENIS_BUKU = serializers.SerializerMethodField('get_jenis_buku')
    
    class Meta:
        model = KatalogBuku
        fields = ('REGISTER', 'JUDUL', 'PENULIS', 'BAHASA', 'TAHUN_TERBIT', 'MEDIA', 'TERSEDIA', 'JENIS_BUKU')

    def get_bahasa(self, obj):
        return obj.BAHASA.BAHASA

    def get_kode_media(self, obj):
        return obj.KODE_MEDIA.NAMA_MEDIA

    def get_kode_author(self, obj):
        return obj.KODE_AUTHOR.NAMA_AUTHOR

    def get_jenis_buku(self, obj):
        return obj.KODE_TIPE.NAMA_TIPE

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


class PengajuanPeminjamanSiswaListSerializer(serializers.ModelSerializer):
    BUKU = serializers.SerializerMethodField('get_buku')

    class Meta:
        model = PengajuanPeminjamanSiswa
        exclude = ('NIS',)

    def get_buku(self, obj):
        buku = obj.BUKU
        daftar_buku = []
        for data in buku.all():
            daftar_buku.append(str(data))

        return daftar_buku


class PengajuanPeminjamanSiswaAdminSerializer(serializers.ModelSerializer):
    NAMA = serializers.SerializerMethodField('get_nama')
    BUKU = serializers.SerializerMethodField('get_buku')

    class Meta:
        model = PengajuanPeminjamanSiswa
        fields = '__all__'

    def get_nama(self, obj):
        data_siswa = DataSiswa.objects.get(pk=obj.NIS.NIS)
        
        return data_siswa.NAMA

    def get_buku(self, obj):
        buku = obj.BUKU
        daftar_buku = []
        for data in buku.all():
            daftar_buku.append(str(data))

        return daftar_buku


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


class PengajuanPeminjamanGuruListSerializer(serializers.ModelSerializer):
    BUKU = serializers.SerializerMethodField('get_buku')

    class Meta:
        model = PengajuanPeminjamanGuru
        exclude = ('DATA_GURU',)

    def get_buku(self, obj):
        buku = obj.BUKU
        daftar_buku = []
        for data in buku.all():
            daftar_buku.append(str(data))

        return daftar_buku


class PengajuanPeminjamanGuruAdminSerializer(serializers.ModelSerializer):
    NAMA = serializers.SerializerMethodField('get_nama')
    BUKU = serializers.SerializerMethodField('get_buku')

    class Meta:
        model = PengajuanPeminjamanGuru
        fields = '__all__'

    def get_nama(self, obj):
        data_guru = DataGuru.objects.get(pk=obj.DATA_GURU.ID)
        
        return data_guru.NAMA_LENGKAP

    def get_buku(self, obj):
        buku = obj.BUKU
        daftar_buku = []
        for data in buku.all():
            daftar_buku.append(str(data))

        return daftar_buku


class RiwayatPeminjamanSiswaSerializer(serializers.ModelSerializer):
    BUKU = serializers.SerializerMethodField('get_buku')

    class Meta:
        model = RiwayatPeminjamanSiswa
        exclude = ('NIS',)

    def get_buku(self, obj):
        buku = obj.BUKU
        daftar_buku = []
        for data in buku.all():
            daftar_buku.append(str(data))

        return daftar_buku


class RiwayatPeminjamanSiswaAdminSerializer(serializers.ModelSerializer):
    NAMA = serializers.SerializerMethodField('get_nama')
    BUKU = serializers.SerializerMethodField('get_buku')

    class Meta:
        model = RiwayatPeminjamanSiswa
        fields = '__all__'

    def get_nama(self, obj):
        data_siswa = DataSiswa.objects.get(pk=obj.NIS.NIS)
        
        return data_siswa.NAMA

    def get_buku(self, obj):
        buku = obj.BUKU
        daftar_buku = []
        for data in buku.all():
            daftar_buku.append(str(data))

        return daftar_buku


class RiwayatPeminjamanGuruSerializer(serializers.ModelSerializer):
    BUKU = serializers.SerializerMethodField('get_buku')

    class Meta:
        model = RiwayatPeminjamanGuru
        exclude = ('DATA_GURU',)

    def get_buku(self, obj):
        buku = obj.BUKU
        daftar_buku = []
        for data in buku.all():
            daftar_buku.append(str(data))

        return daftar_buku


class RiwayatPeminjamanGuruAdminSerializer(serializers.ModelSerializer):
    NAMA = serializers.SerializerMethodField('get_nama')
    BUKU = serializers.SerializerMethodField('get_buku')
    DATA_GURU = serializers.SerializerMethodField('get_nik')

    class Meta:
        model = RiwayatPeminjamanGuru
        fields = '__all__'

    def get_nama(self, obj):
        data_guru = DataGuru.objects.get(pk=obj.DATA_GURU.ID)
        
        return data_guru.NAMA_LENGKAP

    def get_buku(self, obj):
        buku = obj.BUKU
        daftar_buku = []
        for data in buku.all():
            daftar_buku.append(str(data))

        return daftar_buku

    def get_nik(self, obj):
        data_guru = DataGuru.objects.get(pk=obj.DATA_GURU.ID)
        
        return data_guru.NIK
