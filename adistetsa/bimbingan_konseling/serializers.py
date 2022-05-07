from kustom_autentikasi.models import *
from kurikulum.models import NamaOfferingKelas
from rest_framework import serializers
from utility.permissions import is_in_group

from .models import *

class KatalogKonselorListSerializer(serializers.ModelSerializer):
    NAMA = serializers.SerializerMethodField('get_user')
    class Meta:
        model = KatalogKonselor
        
        exclude = ('KOMPETENSI','ALUMNUS','WHATSAPP','CONFERENCE')

    def get_user(self, obj): 
        if (is_in_group(obj.USER, 'Guru')):
            data_guru = DataGuruUser.objects.get(USER=obj.USER).DATA_GURU
            return str(data_guru.NAMA_LENGKAP)    

class KatalogKonselorDetailSerializer(serializers.ModelSerializer):
    NIP = serializers.SerializerMethodField('get_nip')

    class Meta:
        model = KatalogKonselor
        fields = '__all__'

    def get_nip(self, obj):
        data_guru = DataGuruUser.objects.get(USER=obj.USER).DATA_GURU
        return str(data_guru.NIP)

class KonselorDetailSerializer(serializers.ModelSerializer):
    NIP = serializers.SerializerMethodField('get_nip')

    class Meta:
        model = KatalogKonselor
        fields = '__all__'

    def get_nip(self, obj):
        data_guru = DataGuruUser.objects.get(USER=obj.USER).DATA_GURU

        return str(data_guru.NIP)

    def create(self, validated_data):
        request = self.context.get('request', None)
        current_user = request.user
        validated_data['USER'] = current_user

        data_konselor = KatalogKonselor.objects.create(**validated_data)

        return data_konselor

class KonsultasiListSerializer(serializers.ModelSerializer):
    NAMA = serializers.SerializerMethodField('get_nama')
    class Meta:
        model = Konsultasi
        
        exclude = ('KONSELOR','JAM_AWAL','JAM_AKHIR','JENIS_MASALAH','RATING','KRITIK_SARAN')

    def get_nama(self, obj):
        if (is_in_group(obj.USER, 'Siswa')):
            data_siswa = DataSiswaUser.objects.get(USER=obj.USER).DATA_SISWA
            return str(data_siswa.NAMA)    
        if (is_in_group(obj.USER, 'Guru')):
            data_guru = DataGuruUser.objects.get(USER=obj.USER).DATA_GURU
            return str(data_guru.NAMA_LENGKAP)    
        if (is_in_group(obj.USER, 'Karyawan')):
            data_karyawan = DataKaryawanUser.objects.get(USER=obj.USER).DATA_KARYAWAN
            return str(data_karyawan.NAMA_LENGKAP)
        if (is_in_group(obj.USER, 'Orang Tua')):
            data_orang_tua = DataOrangTuaUser.objects.get(USER=obj.USER).DATA_ORANG_TUA
            return str(data_orang_tua.NAMA_AYAH)
           
class KonsultasiDetailSerializer(serializers.ModelSerializer):
    USER = serializers.SerializerMethodField('get_user')

    class Meta:
        model = Konsultasi
        exclude = ('KONSELOR','RATING','KRITIK_SARAN')

    def get_user(self, obj):
        if (is_in_group(obj.USER, 'Orang Tua')):
            data_pelatih = DataOrangTuaUser.objects.get(USER=obj.USER).DATA_ORANG_TUA
            return str(data_pelatih.NAMA_AYAH)    
        if (is_in_group(obj.USER, 'Siswa')):
            data_siswa = DataSiswaUser.objects.get(USER=obj.USER).DATA_SISWA
            return str(data_siswa.NAMA)    
        if (is_in_group(obj.USER, 'Guru')):
            data_guru = DataGuruUser.objects.get(USER=obj.USER).DATA_GURU
            return str(data_guru.NAMA_LENGKAP)    
        if (is_in_group(obj.USER, 'Karyawan')):
            data_karyawan = DataKaryawanUser.objects.get(USER=obj.USER).DATA_KARYAWAN
            return str(data_karyawan.NAMA_LENGKAP)

    def create(self, validated_data):
        request = self.context.get('request', None)
        current_user = request.user

        id_konselor = request.parser_context.get('kwargs').get('id_konselor')
        validated_data['KONSELOR'] = KatalogKonselor.objects.get(pk=id_konselor)
        validated_data['USER'] = current_user

        return super().create(validated_data)

class PengajuanKonsultasiListSerializer(serializers.ModelSerializer):
    NAMA_KONSELOR = serializers.SerializerMethodField('get_konselor')
    class Meta:
        model = Konsultasi
        exclude = ('JAM_AWAL','JAM_AKHIR','JENIS_MASALAH', 'RATING','KRITIK_SARAN')

    def get_konselor(self, obj):
        data_guru = KatalogKonselor.objects.get(USER=obj.KONSELOR.USER)
        return str(data_guru.NAMA)   

class KonsultasiDetailOrangTuaSerializer(serializers.ModelSerializer):
    NAMA_AYAH = serializers.SerializerMethodField('get_nama')
    NIK_AYAH = serializers.SerializerMethodField('get_nik')
    KONSELOR = serializers.SerializerMethodField('get_konselor')

    class Meta:
        model = Konsultasi
        fields = '__all__'

    def get_nama(self, obj):
        data_ortu = DataOrangTuaUser.objects.get(USER=obj.USER).DATA_ORANG_TUA
        
        return str(data_ortu.NAMA_AYAH)   
    def get_nik(self, obj):
        data_ortu = DataOrangTuaUser.objects.get(USER=obj.USER).DATA_ORANG_TUA
        return str(data_ortu.NIK_AYAH) 
    def get_konselor(self, obj):
        return str(obj.KONSELOR.NAMA)

class KonsultasiDetailSiswaSerializer(serializers.ModelSerializer):
    NAMA = serializers.SerializerMethodField('get_nama')
    NIS = serializers.SerializerMethodField('get_nis')
    NISN = serializers.SerializerMethodField('get_nisn')
    KELAS = serializers.SerializerMethodField('get_kelas')
    KONSELOR = serializers.SerializerMethodField('get_konselor')

    class Meta:
        model = Konsultasi
        fields = '__all__'

    def get_nama(self, obj):
        data_siswa = DataSiswaUser.objects.get(USER=obj.USER).DATA_SISWA
        return str(data_siswa.NAMA)  

    def get_nis(self, obj):
        data_siswa = DataSiswaUser.objects.get(USER=obj.USER).DATA_SISWA
        return str(data_siswa.NIS)   

    def get_nisn(self, obj):
        data_siswa = DataSiswaUser.objects.get(USER=obj.USER).DATA_SISWA
        return str(data_siswa.NISN)    

    def get_kelas(self, obj):
        data_siswa = DataSiswaUser.objects.get(USER=obj.USER).DATA_SISWA
        kelas_siswa = KelasSiswa.objects.filter(NIS=data_siswa).last()
        return str(kelas_siswa.KELAS.KELAS.TINGKATAN) + " " + str(kelas_siswa.KELAS.KELAS.JURUSAN) + " " + str(kelas_siswa.KELAS.OFFERING.NAMA)  

    def get_konselor(self, obj):
        return str(obj.KONSELOR.NAMA)

class KonsultasiDetailGuruSerializer(serializers.ModelSerializer):
    NAMA_LENGKAP = serializers.SerializerMethodField('get_nama')
    NIP = serializers.SerializerMethodField('get_nip')
    KONSELOR = serializers.SerializerMethodField('get_konselor')

    class Meta:
        model = Konsultasi
        fields = '__all__'

    def get_nama(self, obj):
        data_guru = DataGuruUser.objects.get(USER=obj.USER).DATA_GURU
        return str(data_guru.NAMA_LENGKAP)  
    def get_nip(self, obj):
        data_guru = DataGuruUser.objects.get(USER=obj.USER).DATA_GURU
        return str(data_guru.NIP)
    def get_konselor(self, obj):
        return str(obj.KONSELOR.NAMA)

class KonsultasiDetailKaryawanSerializer(serializers.ModelSerializer):
    NAMA_LENGKAP = serializers.SerializerMethodField('get_nama')
    NIK = serializers.SerializerMethodField('get_nik')
    KONSELOR = serializers.SerializerMethodField('get_konselor')

    class Meta:
        model = Konsultasi
        fields = '__all__'

    def get_nama(self, obj):
        data_karyawan = DataKaryawanUser.objects.get(USER=obj.USER).DATA_KARYAWAN
        return str(data_karyawan.NAMA_LENGKAP) 
    def get_nik(self, obj):
        data_karyawan = DataKaryawanUser.objects.get(USER=obj.USER).DATA_KARYAWAN
        return str(data_karyawan.NIK)
    def get_konselor(self, obj):
        return str(obj.KONSELOR.NAMA)

class DataAlumniListSerializer(serializers.ModelSerializer):

    class Meta:
        model = DataAlumni
        exclude = ('NISN','TAHUN_AJARAN','NAMA_PT','PROGRAM_STUDI','MEDIA_SOSIAL','EMAIL', 'ALAMAT','TEMPAT_BEKERJA')

class DataAlumniDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = DataAlumni
        fields = '__all__'

class PeminatanLintasMinatListSerializer(serializers.ModelSerializer):
    KELAS = serializers.SerializerMethodField('get_kelas')
    NAMA = serializers.SerializerMethodField('get_nama')

    class Meta:
        model = PeminatanLintasMinat
        fields = '__all__'  

    def get_nama(self, obj):
        return str(obj.KELAS_SISWA.NIS.NAMA)

    def get_kelas(self, obj):
        return str(obj.KELAS_SISWA.KELAS)

class ParameterJurusanListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jurusan
        fields = '__all__'

class ParameterKelasListSerializer(serializers.ModelSerializer):
    class Meta:
        model = NamaOfferingKelas
        fields = '__all__'