from django.contrib.auth.models import Group
from django.db.models import query
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import parser_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
from tablib import Dataset
import csv

import tablib

from .models import *
from .serializers import RoleUserSerializer
from .doc_schema import *

from adistetsa.permissions import HasGroupPermissionAny, IsSuperAdmin, is_in_group
from dataprofil.admin import DataGuruResource
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


class ImportDataGuruView(APIView):
    """
    post: Melakukan import data guru (Super Admin/ Staf PPDB).
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'POST': ['Staf PPDB'],
    }
    parser_classes= (MultiPartParser,)

    @swagger_auto_schema(
        manual_parameters=[param_importexportfile,],
        responses={'200': 'Berhasil mengupdate data guru', '400': 'Bad Request',}
    )
    def post(self, request, format=None):
        file = request.FILES['file']

        str_text = ''
        for line in file:
            str_text = str_text + line.decode()

        data_guru_resource = DataGuruResource()
        csv_data = tablib.import_set(str_text, format='csv')
        result = data_guru_resource.import_data(csv_data, dry_run=True)

        if not result.has_errors():
            data_guru_resource.import_data(csv_data, dry_run=False)

            return Response({'Result': 'Berhasil mengupdate data guru'}, status=200)    

        return Response({'Result': 'Gagal mengupload data guru'}, status=400)