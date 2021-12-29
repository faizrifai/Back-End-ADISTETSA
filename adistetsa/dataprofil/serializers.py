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
        
class DataKompetensiPegawaiSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataKompetensiPegawai
        fields = '__all__'

class DataAnakPegawaiSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataAnakPegawai
        fields = '__all__'