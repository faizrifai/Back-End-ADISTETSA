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