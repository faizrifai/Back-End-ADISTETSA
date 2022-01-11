from .models import *
from rest_framework import serializers


class KTSPSerializer(serializers.ModelSerializer):
    class Meta:
        model = KTSP
        fields = '__all__'


class SilabusRPBSerializer(serializers.ModelSerializer):
    class Meta:
        model = SilabusRPB
        fields = '__all__'

class TataTertibSerializer(serializers.ModelSerializer):
    class Meta:
        model = TataTertib
        fields = '__all__'

# class SilabusRPBWithFilterSerializer(serializers.Serializer):
#     silabus_rpb = SilabusRPBSerializer(many=True)
#     tahun_ajaran_filter = serializers.SerializerMethodField('get_tahun_ajaran_filter')
#     mata_pelajaran_filter = serializers.SerializerMethodField('get_mata_pelajaran_filter')
#     kelas_filter = serializers.SerializerMethodField('get_kelas_filter')
#     semester_filter = serializers.SerializerMethodField('get_semester_filter')

#     def get_tahun_ajaran_filter(self, obj):
#         tahun_ajaran = TahunAjaran.objects.all()
#         daftar = []
#         for data in tahun_ajaran.values():
#             str_tahun = str(data['TAHUN_AJARAN_AWAL']) + '/' + str(data['TAHUN_AJARAN_AKHIR'])
#             tahun = {'ID': data['ID'], 'TAHUN_AJARAN': str_tahun}
#             daftar.append(tahun)

#         return daftar

#     def get_mata_pelajaran_filter(self, obj):
#         mata_pelajaran = MataPelajaran.objects.all()
#         daftar = []
#         for data in mata_pelajaran.values():
#             daftar.append(data)

#         return daftar

#     def get_kelas_filter(self, obj):
#         kelas = Kelas.objects.all()
#         daftar = []
#         for data in kelas.values():
#             kelas = {'ID': data['ID'], 'KELAS': data['KODE_KELAS']}
#             daftar.append(kelas)

#         return daftar


#     def get_semester_filter(self, obj):
#         semester = DataSemester.objects.all()
#         daftar = []
#         for data in semester.values():
#             semester = {'ID': data['id'], 'SEMESTER': data['KE']}
#             daftar.append(semester)

#         return daftar


class TataTertibSerializer(serializers.ModelSerializer):
    class Meta:
        model = TataTertib
        fields = '__all__'


class PoinPelanggaranSerializer(serializers.ModelSerializer):
    class Meta:
        model = PoinPelanggaran
        fields = '__all__'
