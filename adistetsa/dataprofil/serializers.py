from .models import *
from rest_framework import serializers

class DataSiswaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataSiswa
        fields = '__all__'

class DataOrangTuaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataOrangTua
        fields = '__all__'
        
class DataKaryawanSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataKaryawan
        fields = '__all__'
       
class DataGuruSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataGuru
        fields = '__all__'

class DataKompetensiGuruSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataKompetensiGuru
        exclude = ['OWNER']

class DataKompetensiKaryawanSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataKompetensiKaryawan
        exclude = ['OWNER']

class DataAnakGuruSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataAnakGuru
        exclude = ['OWNER']

class DataAnakKaryawanSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataAnakKaryawan
        exclude = ['OWNER']

class DataBeasiswaGuruSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataBeasiswaGuru
        exclude = ['OWNER']

class DataBeasiswaKaryawanSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataBeasiswaKaryawan
        exclude = ['OWNER']

class DataBukuKaryawanSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataBukuKaryawan
        exclude = ['OWNER']

class DataDiklatKaryawanSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataDiklatKaryawan
        exclude = ['OWNER']

class DataKaryaTulisKaryawanSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataKaryaTulisKaryawan
        exclude = ['OWNER']

class DataKesejahteraanKaryawanSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataKesejahteraanKaryawan
        exclude = ['OWNER']

class DataTunjanganKaryawanSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataTunjanganKaryawan
        exclude = ['OWNER']

class DataTugasTambahanKaryawanSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataTugasTambahanKaryawan
        exclude = ['OWNER']

class DataPenghargaanKaryawanSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataPenghargaanKaryawan
        exclude = ['OWNER']

class DataNilaiTesKaryawanSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataNilaiTesKaryawan
        exclude = ['OWNER']

class DataRiwayatGajiBerkalaKaryawanSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataRiwayatGajiBerkalaKaryawan
        exclude = ['OWNER']

class DataRiwayatJabatanStrukturalKaryawanSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataRiwayatJabatanStrukturalKaryawan
        exclude = ['OWNER']

class DataRiwayatKepangkatanKaryawanSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataRiwayatKepangkatanKaryawan
        exclude = ['OWNER']
        
class DataRiwayatPendidikanFormalKaryawanSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataRiwayatPendidikanFormalKaryawan
        exclude = ['OWNER']
        
class DataRiwayatSertifikasiKaryawanSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataRiwayatSertifikasiKaryawan
        exclude = ['OWNER']
        
class DataRiwayatJabatanFungsionalKaryawanSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataRiwayatJabatanFungsionalKaryawan
        exclude = ['OWNER']
        
class DataRiwayatKarirKaryawanSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataRiwayatKarirKaryawan
        exclude = ['OWNER']
        