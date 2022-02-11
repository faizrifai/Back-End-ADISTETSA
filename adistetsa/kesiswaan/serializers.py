from .models import *
from rest_framework import serializers

from adistetsa.permissions import is_in_group
from kustom_autentikasi.models import DataSiswaUser

class PengajuanLaporanPelanggaranSerializer(serializers.ModelSerializer):
    class Meta:
        model = PengajuanLaporanPelanggaran
        fields = '__all__'


class PengajuanLaporanPelanggaranListSerializer(serializers.ModelSerializer):
    DATA_SISWA = serializers.SerializerMethodField('get_data_siswa')
    JENIS_PELANGGARAN = serializers.SerializerMethodField('get_jenis_pelanggaran')

    class Meta:
        model = PengajuanLaporanPelanggaran
        fields = '__all__'

    def get_data_siswa(self, obj):
        return str(obj.DATA_SISWA)

    def get_jenis_pelanggaran(self, obj):
        return str(obj.JENIS_PELANGGARAN)


class PelanggaranSiswaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PelanggaranSiswa
        fields = '__all__'

class PelanggaranSiswaListSerializer(serializers.ModelSerializer):
    DATA_SISWA = serializers.SerializerMethodField('get_data_siswa')
    class Meta:
        model = PelanggaranSiswa
        fields = '__all__'

    def get_data_siswa(self, obj):
        return str(obj.DATA_SISWA)

class RiwayatLaporanPelanggaranSerializer(serializers.ModelSerializer):
    class Meta:
        model = RiwayatLaporanPelanggaran
        fields = '__all__'

class RiwayatLaporanPelanggaranListSerializer(serializers.ModelSerializer):
    DATA_SISWA = serializers.SerializerMethodField('get_data_siswa')
    JENIS_PELANGGARAN = serializers.SerializerMethodField('get_jenis_pelanggaran')
    class Meta:
        model = RiwayatLaporanPelanggaran
        fields = '__all__'

    def get_data_siswa(self, obj):
        return str(obj.DATA_SISWA)

    def get_jenis_pelanggaran(self, obj):
        return str(obj.JENIS_PELANGGARAN)

class KategoriProgramKebaikanSerializer(serializers.ModelSerializer):
    class Meta:
        model = KategoriProgramKebaikan
        fields = '__all__'

class ProgramKebaikanSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgramKebaikan
        fields = '__all__'

class ProgramKebaikanListSerializer(serializers.ModelSerializer):
    KATEGORI = serializers.SerializerMethodField('get_kategori')
    
    class Meta:
        model = ProgramKebaikan
        fields = '__all__'

    def get_kategori(self, obj):
        return str(obj.KATEGORI)

class PoinProgramKebaikanSerializer(serializers.ModelSerializer):
    class Meta:
        model = PoinProgramKebaikan
        fields = '__all__'

class PengajuanProgramKebaikanSerializer(serializers.ModelSerializer):
    class Meta:
        model = PengajuanProgramKebaikan
        exclude = ('DATA_SISWA',)

    def create(self, validated_data):
        request = self.context.get('request', None)
        current_user = request.user
        if (is_in_group(current_user, 'Siswa')):
            data_siswa_user = DataSiswaUser.objects.get(USER=current_user)
            validated_data['DATA_SISWA'] = data_siswa_user.DATA_SISWA

        data_pengajuan = PengajuanProgramKebaikan.objects.create(**validated_data)

        return data_pengajuan

class PengajuanProgramKebaikanListSerializer(serializers.ModelSerializer):
    DATA_SISWA = serializers.SerializerMethodField('get_data_siswa')
    JENIS_PROGRAM_KEBAIKAN = serializers.SerializerMethodField('get_jenis_program_kebaikan')
    
    class Meta:
        model = PengajuanProgramKebaikan
        fields = '__all__'

    def get_data_siswa(self, obj):
        return str(obj.DATA_SISWA)
    def get_jenis_program_kebaikan(self, obj):
        return str(obj.JENIS_PROGRAM_KEBAIKAN)

class RiwayatProgramKebaikanSerializer(serializers.ModelSerializer):
    class Meta:
        model = RiwayatProgramKebaikan
        fields = '__all__'

class RiwayatProgramKebaikanListSerializer(serializers.ModelSerializer):
    DATA_SISWA = serializers.SerializerMethodField('get_data_siswa')
    JENIS_PROGRAM_KEBAIKAN = serializers.SerializerMethodField('get_jenis_program_kebaikan')
    
    class Meta:
        model = RiwayatProgramKebaikan
        fields = '__all__'

    def get_data_siswa(self, obj):
        return str(obj.DATA_SISWA)
    def get_jenis_program_kebaikan(self, obj):
        return str(obj.JENIS_PROGRAM_KEBAIKAN)