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
        fields = '__all__'

class DataKompetensiKaryawanSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataKompetensiKaryawan
        fields = '__all__'



class DataAnakGuruSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataAnakGuru
        fields = '__all__'

class DataAnakKaryawanSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataAnakKaryawan
        fields = '__all__'


class DataBeasiswaGuruSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataBeasiswaGuru
        fields = '__all__'

class DataBeasiswaKaryawanSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataBeasiswaKaryawan
        fields = '__all__'