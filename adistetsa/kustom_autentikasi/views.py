from django.contrib.auth.models import Group
from django.db.models import query
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import RoleUserSerializer

from adistetsa.permissions import HasGroupPermissionAny, is_in_group
from dataprofil.models import DataSiswa, DataGuru, DataOrangTua, DataKaryawan
from dataprofil.serializers import DataSiswaSerializer, DataGuruSerializer, DataOrangTuaSerializer, DataKaryawanSerializer

# Create your views here.
class ProfilDetailView(APIView):
    """
    get: Menampilkan profil user
    """
    permission_classes = [HasGroupPermissionAny]
    required_groups = {
        'GET': ['Siswa', 'Orang Tua', 'Guru', 'Karyawan'],
    }

    def get_queryset(self):
        user = self.request.user
        if (is_in_group(user, 'Siswa')):
            return DataSiswa.objects.get(NISN=user.username)
        elif (is_in_group(user, 'Orang Tua')):
            data_orang_tua_user = DataOrangTuaUser.objects.get(USER=user)
            return DataOrangTua.objects.get(pk=data_orang_tua_user.DATA_ORANG_TUA.ID)
        elif (is_in_group(user, 'Guru')):
            data_guru_user = DataGuruUser.objects.get(USER=user)
            return DataGuru.objects.get(pk=data_guru_user.DATA_GURU.ID)
        elif (is_in_group(user, 'Karyawan')):
            data_karyawan_user = DataKaryawanUser.objects.get(USER=user)
            return DataKaryawan.objects.get(pk=data_karyawan_user.DATA_KARYAWAN)
        else:
            return None

    def get_serializer(self, *args, **kwargs):
        user = self.request.user
        if (is_in_group(user, 'Siswa')):
            return DataSiswaSerializer
        elif (is_in_group(user, 'Orang Tua')):
            return DataOrangTuaSerializer
        elif (is_in_group(user, 'Guru')):
            return DataGuruSerializer
        elif (is_in_group(user, 'Karyawan')):
            return DataKaryawanSerializer
        else:
            return None

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer()
        response = serializer(queryset).data
        return Response(response)

class RoleUserView(APIView):
    """
    get: Menampilkan role yang dimiliki oleh user
    """
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Group.objects.filter(user=user).all()

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = RoleUserSerializer
        response = serializer(queryset, many=True).data
        return Response(response)