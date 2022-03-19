from attr import field
from .models import *
from rest_framework import serializers

from adistetsa.permissions import is_in_group
from kustom_autentikasi.models import *

class KatalogKonselorListSerializer(serializers.ModelSerializer):
    NAMA = serializers.SerializerMethodField('get_user')
    class Meta:
        model = KatalogKonselor
        
        exclude = ('KOMPETENSI','ALUMNUS','WHATSAPP','CONFERENCE','FOTO')

    def get_user(self, obj): 
        if (is_in_group(obj.USER, 'Guru')):
            data_guru = DataGuruUser.objects.get(USER=obj.USER).DATA_GURU
            return str(data_guru.NAMA_LENGKAP)       
    # # USER = serializers.SerializerMethodField('get_user')
    # class Meta:
    #     model = KatalogKonselor
    #     exclude = ('KOMPETENSI','ALUMNUS','WHATSAPP','CONFERENCE','FOTO')


    # # def get_user(self, obj): 
    # #     if (is_in_group(obj.USER, 'Staf BK')):
    # #         data_guru = DataGuruUser.objects.get(USER=obj.USER).DATA_GURU
    # #         queryset = DataGuru.objects.get(NIS=data_guru.NAMA_LENGKAP)

    # #         return queryset 

class KonselorDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = KatalogKonselor
        fields = '__all__'

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
        if (not is_in_group(obj.USER, 'Staf BK')):
            data_guru = KatalogKonselor.objects.get(USER=obj.KONSELOR.USER)
            return str(data_guru.NAMA)   

class KonsultasiDetailOrangTuaSerializer(serializers.ModelSerializer):
    NAMA_AYAH = serializers.SerializerMethodField('get_nama')
    NIK_AYAH = serializers.SerializerMethodField('get_nik')

    class Meta:
        model = Konsultasi
        exclude = ('KONSELOR','RATING','KRITIK_SARAN')

    def get_nama(self, obj):
        data_ortu = DataOrangTuaUser.objects.get(USER=obj.USER).DATA_ORANG_TUA
        
        return str(data_ortu.NAMA_AYAH)   
    def get_nik(self, obj):
        data_ortu = DataOrangTuaUser.objects.get(USER=obj.USER).DATA_ORANG_TUA
        return str(data_ortu.NIK_AYAH)   

class KonsultasiDetailSiswaSerializer(serializers.ModelSerializer):
    NAMA = serializers.SerializerMethodField('get_nama')
    NIS = serializers.SerializerMethodField('get_nis')
    NISN = serializers.SerializerMethodField('get_nisn')
    KELAS = serializers.SerializerMethodField('get_kelas')


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
        kelas_siswa = KelasSiswa.objects.get(NIS=data_siswa)
        return str(kelas_siswa.KELAS.KELAS.TINGKATAN) + " " + str(kelas_siswa.KELAS.KELAS.JURUSAN) + " " + str(kelas_siswa.KELAS.OFFERING.NAMA)  

class KonsultasiDetailGuruSerializer(serializers.ModelSerializer):
    NAMA_LENGKAP = serializers.SerializerMethodField('get_nama')
    NIP = serializers.SerializerMethodField('get_nip')

    class Meta:
        model = Konsultasi
        exclude = ('KONSELOR','RATING','KRITIK_SARAN')

    def get_nama(self, obj):
        data_guru = DataGuruUser.objects.get(USER=obj.USER).DATA_GURU
        return str(data_guru.NAMA_LENGKAP)  
    def get_nip(self, obj):
        data_guru = DataGuruUser.objects.get(USER=obj.USER).DATA_KARYAWAN
        return str(data_guru.NIP) 

class KonsultasiDetailKaryawanSerializer(serializers.ModelSerializer):
    NAMA_LENGKAP = serializers.SerializerMethodField('get_nama')
    NIK = serializers.SerializerMethodField('get_nik')

    class Meta:
        model = Konsultasi
        exclude = ('KONSELOR','RATING','KRITIK_SARAN')

    def get_nama(self, obj):
        data_karyawan = DataKaryawanUser.objects.get(USER=obj.USER).DATA_KARYAWAN
        return str(data_karyawan.NAMA_LENGKAP) 
    def get_nik(self, obj):
        data_karyawan = DataKaryawanUser.objects.get(USER=obj.USER).DATA_KARYAWAN
        return str(data_karyawan.NIK) 

class DataAlumniListSerializer(serializers.ModelSerializer):

    class Meta:
        model = DataAlumni
        exclude = ('NISN','TAHUN_AJARAN','NAMA_PT','PROGRAM_STUDI','MEDIA_SOSIAL','EMAIL', 'ALAMAT','TEMPAT_BEKERJA')

class DataAlumniDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = DataAlumni
        fields = '__all__'

class PeminatanLintasMinatListSerializer(serializers.ModelSerializer):

    class Meta:
        model = PeminatanLintasMinat
        fields = '__all__'  

# class KonsultasiDetailKaryawanSerializer(serializers.ModelSerializer):
#     NAMA_LENGKAP = serializers.SerializerMethodField('get_nama')
#     NIP = serializers.SerializerMethodField('get_nip')

#     class Meta:
#         model = Konsultasi
#         exclude = ('KONSELOR','RATING','KRITIK_SARAN')

#     def get_nama(self, obj):
#         data_siswa = DataKaryawanUser.objects.get(USER=obj.USER).DATA_KARYAWAN
#         return str(data_siswa.NAMA_LENGKAP)  

#     def get_nip(self, obj):
#         data_siswa = DataKaryawanUser.objects.get(USER=obj.USER).DATA_KARYAWAN
#         return str(data_siswa.NIP)   

