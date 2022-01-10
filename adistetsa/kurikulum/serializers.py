from .models import *
from rest_framework import serializers

class KTSPSerializer(serializers.ModelSerializer):
    class Meta:
        model = KTSP
        fields = '__all__'


class KTSPWithFilterSerializer(serializers.Serializer):
    ktsp = KTSPSerializer(many=True)
    tahun_ajaran_filter = serializers.SerializerMethodField('get_tahun_ajaran_filter')

    def get_tahun_ajaran_filter(self, obj):
        tahun_ajaran = TahunAjaran.objects.all()
        daftar = []
        for data in tahun_ajaran.values():
            str_tahun = str(data['TAHUN_AJARAN_AWAL']) + '/' + str(data['TAHUN_AJARAN_AKHIR'])
            daftar.append(str_tahun)

        return daftar

# class TahunFilterSerializer(serializers.ModelSerializer):
#     TAHUN_AJARAN = serializers.SerializerMethodField('get_tahun_ajaran_filter')

#     class Meta:
#         model = KTSP
#         fields = '__all__'

#     def get_tahun_ajaran_filter(self, obj):
#         tahun_ajaran = TahunAjaran.objects.all()
#         daftar = []
#         for data in tahun_ajaran.values():
#             str_tahun = str(data['TAHUN_AJARAN_AWAL']) + '/' + str(data['TAHUN_AJARAN_AKHIR'])
#             daftar.append(str_tahun)

#         return daftar