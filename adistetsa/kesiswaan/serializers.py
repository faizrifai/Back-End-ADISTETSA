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

class DaftarSiswaListSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataSiswa
        fields = '__all__'

class KatalogEkskulSerializer(serializers.ModelSerializer):
    class Meta:
        model = KatalogEkskul
        fields = '__all__'

class JadwalEkskulSerializer(serializers.ModelSerializer):
    class Meta:
        model = JadwalEkskul
        fields = '__all__'

class JadwalEkskulListSerializer(serializers.ModelSerializer):
    PELATIH = serializers.SerializerMethodField('get_pelatih')
    TAHUN_AJARAN = serializers.SerializerMethodField('get_tahun_ajaran')
    SEMESTER = serializers.SerializerMethodField('get_semester')
    EKSKUL = serializers.SerializerMethodField('get_ekskul')
    class Meta:
        model = JadwalEkskul
        fields = '__all__'
    def get_pelatih(self, obj):
        return str(obj.PELATIH)
    def get_tahun_ajaran(self, obj):
        return str(obj.TAHUN_AJARAN)
    def get_semester(self, obj):
        return str(obj.SEMESTER)
    def get_ekskul(self, obj):
        return str(obj.EKSKUL)

class DaftarJurnalEkskulSerializer(serializers.ModelSerializer):
    class Meta:
        model = DaftarJurnalEkskul
        fields = '__all__'

class DaftarJurnalEkskulListSerializer(serializers.ModelSerializer):
    PELATIH = serializers.SerializerMethodField('get_pelatih')
    JADWAL_EKSKUL = serializers.SerializerMethodField('get_jadwal_ekskul')
    SEMESTER = serializers.SerializerMethodField('get_semester')
    EKSKUL = serializers.SerializerMethodField('get_ekskul')
    class Meta:
        model = DaftarJurnalEkskul
        fields = '__all__'
    def get_pelatih(self, obj):
        return str(obj.PELATIH)
    def get_jadwal_ekskul(self, obj):
        return str(obj.JADWAL_EKSKUL)
    def get_semester(self, obj):
        return str(obj.SEMESTER)
    def get_ekskul(self, obj):
        return str(obj.EKSKUL)

class JurnalEkskulSerializer(serializers.ModelSerializer):
    class Meta:
        model = JurnalEkskul
        fields = '__all__'

class JurnalEkskulListSerializer(serializers.ModelSerializer):
    PELATIH = serializers.SerializerMethodField('get_pelatih')
    DAFTAR = serializers.SerializerMethodField('get_daftar')
    class Meta:
        model = JurnalEkskul
        fields = '__all__'
    def get_pelatih(self, obj):
        return str(obj.PELATIH)
    def get_daftar(self, obj):
        return str(obj.DAFTAR)

class AbsensiEkskulSerializer(serializers.ModelSerializer):
    class Meta:
        model = AbsensiEkskul
        fields = '__all__'

class AbsensiEkskulListSerializer(serializers.ModelSerializer):
    JURNAL_EKSKUL = serializers.SerializerMethodField('get_jurnal_ekskul')
    class Meta:
        model = AbsensiEkskul
        fields = '__all__'
    def get_jurnal_ekskul(self, obj):
        return str(obj.JURNAL_EKSKUL)

class PengajuanEkskulSerializer(serializers.ModelSerializer):
    class Meta:
        model = PengajuanEkskul
        fields = '__all__'

class PengajuanEkskulListSerializer(serializers.ModelSerializer):
    KELAS_SISWA = serializers.SerializerMethodField('get_kelas_siswa')
    EKSKUL = serializers.SerializerMethodField('get_ekskul')
    TAHUN_AJARAN = serializers.SerializerMethodField('get_tahun_ajaran')
    class Meta:
        model = PengajuanEkskul
        fields = '__all__'
    def get_kelas_siswa(self, obj):
        return str(obj.KELAS_SISWA)
    def get_ekskul(self, obj):
        return str(obj.EKSKUL)
    def get_tahun_ajaran(self, obj):
        return str(obj.TAHUN_AJARAN)

class AnggotaEkskulSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnggotaEkskul
        fields = '__all__'

class AnggotaEkskulListSerializer(serializers.ModelSerializer):
    KELAS_SISWA = serializers.SerializerMethodField('get_kelas_siswa')
    EKSKUL = serializers.SerializerMethodField('get_ekskul')
    TAHUN_AJARAN = serializers.SerializerMethodField('get_tahun_ajaran')
    class Meta:
        model = AnggotaEkskul
        fields = '__all__'
    def get_kelas_siswa(self, obj):
        return str(obj.KELAS_SISWA)
    def get_ekskul(self, obj):
        return str(obj.EKSKUL)
    def get_tahun_ajaran(self, obj):
        return str(obj.TAHUN_AJARAN)

class ProgramKerjaEkskulSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgramKerjaEkskul
        fields = '__all__'

class ProgramKerjaEkskulListSerializer(serializers.ModelSerializer):
    PELATIH = serializers.SerializerMethodField('get_pelatih')
    EKSKUL = serializers.SerializerMethodField('get_ekskul')
    TAHUN_AJARAN = serializers.SerializerMethodField('get_tahun_ajaran')
    class Meta:
        model = ProgramKerjaEkskul
        fields = '__all__'
    def get_pelatih(self, obj):
        return str(obj.PELATIH)
    def get_ekskul(self, obj):
        return str(obj.EKSKUL)
    def get_tahun_ajaran(self, obj):
        return str(obj.TAHUN_AJARAN)

class NilaiEkskulSerializer(serializers.ModelSerializer):
    class Meta:
        model = NilaiEkskul
        fields = '__all__'

class NilaiEkskulListSerializer(serializers.ModelSerializer):
    DATA_ANGGOTA = serializers.SerializerMethodField('get_data_anggota')
    SEMESTER = serializers.SerializerMethodField('get_semester')
    class Meta:
        model = NilaiEkskul
        fields = '__all__'
    def get_data_anggota(self, obj):
        return str(obj.DATA_ANGGOTA)
    def get_semester(self, obj):
        return str(obj.SEMESTER)

        