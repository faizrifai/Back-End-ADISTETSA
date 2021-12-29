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


class DataPegawaiSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataPegawai
        fields = '__all__'