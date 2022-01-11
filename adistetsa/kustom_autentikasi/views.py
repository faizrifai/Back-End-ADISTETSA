import datetime
from django.contrib.auth.models import Group
from django.http import HttpResponse
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
import tablib

from adistetsa.permissions import HasGroupPermissionAny, IsSuperAdmin, is_in_group
from dataprofil.importexportresources import DataGuruResource, DataSiswaResource, DataKaryawanResource, DataOrangTuaResource
from dataprofil.models import DataSiswa, DataGuru, DataOrangTua, DataKaryawan
from dataprofil.serializers import DataSiswaSerializer, DataGuruSerializer, DataOrangTuaSerializer, DataKaryawanSerializer

from .importexportresources import DataSiswaUserResource, DataGuruUserResource, DataKaryawanUserResource
from .models import *
from .serializers import RoleUserSerializer
from .doc_schema import *

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
            return DataSiswa.objects.get(NIS=user.username)
        elif (is_in_group(user, 'Orang Tua')):
            data_orang_tua_user = DataOrangTuaUser.objects.get(USER=user)
            return DataOrangTua.objects.get(pk=data_orang_tua_user.DATA_ORANG_TUA.ID)
        elif (is_in_group(user, 'Guru')):
            data_guru_user = DataGuruUser.objects.get(USER=user)
            return DataGuru.objects.get(pk=data_guru_user.DATA_GURU.ID)
        elif (is_in_group(user, 'Karyawan')):
            data_karyawan_user = DataKaryawanUser.objects.get(USER=user)
            return DataKaryawan.objects.get(pk=data_karyawan_user.DATA_KARYAWAN.ID)
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


class ImportDataSiswaView(APIView):
    """
    post: Melakukan import data siswa (Super Admin/ Staf PPDB).
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'POST': ['Staf PPDB'],
    }
    parser_classes= (MultiPartParser,)

    @swagger_auto_schema(
        manual_parameters=[param_importexportfile,],
        responses={'200': 'Berhasil mengupdate data siswa', '400': 'Gagal mengupdate data siswa, ada kesalahan',}
    )
    def post(self, request, format=None):
        file = request.FILES['file']

        str_text = ''
        for line in file:
            str_text = str_text + line.decode()

        data_siswa_resource = DataSiswaResource()
        csv_data = tablib.import_set(str_text, format='csv')
        print(csv_data)
        
        try:
            result = data_siswa_resource.import_data(csv_data, dry_run=True, raise_errors=True)

            if not result.has_errors():
                data_siswa_resource.import_data(csv_data, dry_run=False)

                return Response({'Result': 'Berhasil mengupdate data siswa'}, status=200)
        except Exception as e:
            return Response({'Result': str(e)}, status=400)

        return Response({'Result': 'Gagal mengupdate data siswa, ada kesalahan'}, status=400)


class ExportDataSiswaView(APIView):
    """
    get: Melakukan export data siswa (Super Admin/ Staf PPDB).
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Staf PPDB'],
    }

    def get(self, request, format=None):
        data_siswa_resource = DataSiswaResource()
        try:
            dataset = data_siswa_resource.export()
            today = datetime.date.today()
            filename = 'data_siswa-' + str(today) + '.csv'
            response = HttpResponse(dataset.csv, content_type='text/csv')
            response['Content-Disposition'] = u'attachment; filename="%s"' %  (filename)

            return response
        except Exception as e:
            return Response({'Result': 'Gagal mengexport data siswa, ada kesalahan'}, status=400)


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
        responses={'200': 'Berhasil mengupdate data guru', '400': 'Gagal mengupdate data guru, ada kesalahan',}
    )
    def post(self, request, format=None):
        file = request.FILES['file']

        str_text = ''
        for line in file:
            str_text = str_text + line.decode()

        data_guru_resource = DataGuruResource()
        csv_data = tablib.import_set(str_text, format='csv')
        
        try:
            result = data_guru_resource.import_data(csv_data, dry_run=True, raise_errors=True)

            if not result.has_errors():
                data_guru_resource.import_data(csv_data, dry_run=False)

                return Response({'Result': 'Berhasil mengupdate data guru'}, status=200)
        except Exception as e:
            return Response({'Result': str(e)}, status=400)

        return Response({'Result': 'Gagal mengupdate data guru, ada kesalahan'}, status=400)


class ExportDataGuruView(APIView):
    """
    get: Melakukan export data guru (Super Admin/ Staf PPDB).
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Staf PPDB'],
    }

    def get(self, request, format=None):
        data_guru_resource = DataGuruResource()
        try:
            dataset = data_guru_resource.export()
            today = datetime.date.today()
            filename = 'data_guru-' + str(today) + '.csv'
            response = HttpResponse(dataset.csv, content_type='text/csv')
            response['Content-Disposition'] = u'attachment; filename="%s"' %  (filename)

            return response
        except:
            return Response({'Result': 'Gagal mengexport data guru, ada kesalahan'}, status=400)


class ImportDataKaryawanView(APIView):
    """
    post: Melakukan import data karyawan (Super Admin/ Staf PPDB).
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'POST': ['Staf PPDB'],
    }
    parser_classes= (MultiPartParser,)

    @swagger_auto_schema(
        manual_parameters=[param_importexportfile,],
        responses={'200': 'Berhasil mengupdate data karyawan', '400': 'Gagal mengupdate data karyawan, ada kesalahan',}
    )
    def post(self, request, format=None):
        file = request.FILES['file']

        str_text = ''
        for line in file:
            str_text = str_text + line.decode()

        data_karyawan_resource = DataKaryawanResource()
        csv_data = tablib.import_set(str_text, format='csv')
        
        try:
            result = data_karyawan_resource.import_data(csv_data, dry_run=True, raise_errors=True)

            if not result.has_errors():
                data_karyawan_resource.import_data(csv_data, dry_run=False)

                return Response({'Result': 'Berhasil mengupdate data karyawan'}, status=200)
        except Exception as e:
            return Response({'Result': 'Gagal mengupdate data karyawan, ada kesalahan'}, status=400)

        return Response({'Result': 'Gagal mengupdate data karyawan, ada kesalahan'}, status=400)


class ExportDataKaryawanView(APIView):
    """
    get: Melakukan export data karyawan (Super Admin/ Staf PPDB).
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Staf PPDB'],
    }

    def get(self, request, format=None):
        data_karyawan_resource = DataGuruResource()
        try:
            dataset = data_karyawan_resource.export()
            today = datetime.date.today()
            filename = 'data_karyawan-' + str(today) + '.csv'
            response = HttpResponse(dataset.csv, content_type='text/csv')
            response['Content-Disposition'] = u'attachment; filename="%s"' %  (filename)

            return response
        except:
            return Response({'Result': 'Gagal mengexport data karyawan, ada kesalahan'}, status=400)


class ImportDataOrangTuaView(APIView):
    """
    post: Melakukan import data orang tua (Super Admin/ Staf PPDB).
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'POST': ['Staf PPDB'],
    }
    parser_classes= (MultiPartParser,)

    @swagger_auto_schema(
        manual_parameters=[param_importexportfile,],
        responses={'200': 'Berhasil mengupdate data orang tua', '400': 'Gagal mengupdate data orang tua, ada kesalahan',}
    )
    def post(self, request, format=None):
        file = request.FILES['file']

        str_text = ''
        for line in file:
            str_text = str_text + line.decode()

        data_orang_tua_resource = DataOrangTuaResource()
        csv_data = tablib.import_set(str_text, format='csv')
        
        try:
            result = data_orang_tua_resource.import_data(csv_data, dry_run=True, raise_errors=True)

            if not result.has_errors():
                data_orang_tua_resource.import_data(csv_data, dry_run=False)

                return Response({'Result': 'Berhasil mengupdate data orang tua'}, status=200)
        except Exception as e:
            return Response({'Result': str(e)}, status=400)

        return Response({'Result': 'Gagal mengupdate data orang tua, ada kesalahan'}, status=400)


class ExportDataOrangTuaView(APIView):
    """
    get: Melakukan export data orang tua (Super Admin/ Staf PPDB).
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Staf PPDB'],
    }

    def get(self, request, format=None):
        data_orang_tua_resource = DataOrangTuaResource()
        try:
            dataset = data_orang_tua_resource.export()
            today = datetime.date.today()
            filename = 'data_orang_tua-' + str(today) + '.csv'
            response = HttpResponse(dataset.csv, content_type='text/csv')
            response['Content-Disposition'] = u'attachment; filename="%s"' %  (filename)

            return response
        except:
            return Response({'Result': 'Gagal mengexport data orang tua, ada kesalahan'}, status=400)


class ImportDataSiswaUserView(APIView):
    """
    post: Melakukan import data untuk pembuatan/ update data user siswa (Super Admin/ Staf PPDB).
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'POST': ['Staf PPDB'],
    }
    parser_classes= (MultiPartParser,)

    @swagger_auto_schema(
        manual_parameters=[param_importexportfile,],
        responses={'200': 'Berhasil membuat/ mengupdate data user siswa ', '400': 'Gagal import data, ada kesalahan',}
    )
    def post(self, request, format=None):
        file = request.FILES['file']

        str_text = ''
        for line in file:
            str_text = str_text + line.decode()

        data_siswa_user_resource = DataSiswaUserResource()
        csv_data = tablib.import_set(str_text, format='csv')
        
        try:
            result = data_siswa_user_resource.import_data(csv_data, dry_run=True, raise_errors=True)

            if not result.has_errors():
                data_siswa_user_resource.import_data(csv_data, dry_run=False)

                return Response({'Result': 'Berhasil menambahkan/ mengupdate data user siswa'}, status=200)
        except Exception as e:
            return Response({'Result': str(e)}, status=400)

        return Response({'Result': 'Gagal import data, ada kesalahan'}, status=400)


class ExportDataSiswaUserView(APIView):
    """
    get: Melakukan export data user siswa (Super Admin/ Staf PPDB).
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Staf PPDB'],
    }

    def get(self, request, format=None):
        data_siswa_user_resource = DataSiswaUserResource()
        try:
            dataset = data_siswa_user_resource.export()
            today = datetime.date.today()
            filename = 'data_siswa_user-' + str(today) + '.csv'
            response = HttpResponse(dataset.csv, content_type='text/csv')
            response['Content-Disposition'] = u'attachment; filename="%s"' %  (filename)

            return response
        except:
            return Response({'Result': 'Gagal mengexport data user siswa, ada kesalahan'}, status=400)


class ImportDataGuruUserView(APIView):
    """
    post: Melakukan import data untuk pembuatan/ update data user guru (Super Admin/ Staf PPDB).
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'POST': ['Staf PPDB'],
    }
    parser_classes= (MultiPartParser,)

    @swagger_auto_schema(
        manual_parameters=[param_importexportfile,],
        responses={'200': 'Berhasil membuat/ mengupdate data user siswa ', '400': 'Gagal import data, ada kesalahan',}
    )
    def post(self, request, format=None):
        file = request.FILES['file']

        str_text = ''
        for line in file:
            str_text = str_text + line.decode()

        data_guru_user_resource = DataGuruUserResource()
        csv_data = tablib.import_set(str_text, format='csv')
        
        try:
            result = data_guru_user_resource.import_data(csv_data, dry_run=True, raise_errors=True)

            if not result.has_errors():
                data_guru_user_resource.import_data(csv_data, dry_run=False)

                return Response({'Result': 'Berhasil menambahkan/ mengupdate data user guru'}, status=200)
        except Exception as e:
            return Response({'Result': str(e)}, status=400)

        return Response({'Result': 'Gagal import data, ada kesalahan'}, status=400)


class ExportDataGuruUserView(APIView):
    """
    get: Melakukan export data user guru (Super Admin/ Staf PPDB).
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Staf PPDB'],
    }

    def get(self, request, format=None):
        data_guru_user_resource = DataGuruUserResource()
        try:
            dataset = data_guru_user_resource.export()
            today = datetime.date.today()
            filename = 'data_guru_user-' + str(today) + '.csv'
            response = HttpResponse(dataset.csv, content_type='text/csv')
            response['Content-Disposition'] = u'attachment; filename="%s"' %  (filename)

            return response
        except:
            return Response({'Result': 'Gagal mengexport data user guru, ada kesalahan'}, status=400)


class ImportDataKaryawanUserView(APIView):
    """
    post: Melakukan import data untuk pembuatan/ update data user karyawan (Super Admin/ Staf PPDB).
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'POST': ['Staf PPDB'],
    }
    parser_classes= (MultiPartParser,)

    @swagger_auto_schema(
        manual_parameters=[param_importexportfile,],
        responses={'200': 'Berhasil membuat/ mengupdate data user karyawan', '400': 'Gagal import data, ada kesalahan',}
    )
    def post(self, request, format=None):
        file = request.FILES['file']

        str_text = ''
        for line in file:
            str_text = str_text + line.decode()

        data_karyawan_user_resource = DataKaryawanUserResource()
        csv_data = tablib.import_set(str_text, format='csv')
        
        try:
            result = data_karyawan_user_resource.import_data(csv_data, dry_run=True, raise_errors=True)

            if not result.has_errors():
                data_karyawan_user_resource.import_data(csv_data, dry_run=False)

                return Response({'Result': 'Berhasil menambahkan/ mengupdate data user karyawan'}, status=200)
        except Exception as e:
            return Response({'Result': str(e)}, status=400)

        return Response({'Result': 'Gagal import data, ada kesalahan'}, status=400)


class ExportDataKaryawanUserView(APIView):
    """
    get: Melakukan export data user karyawan (Super Admin/ Staf PPDB).
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Staf PPDB'],
    }

    def get(self, request, format=None):
        data_karyawan_user_resource = DataGuruUserResource()
        try:
            dataset = data_karyawan_user_resource.export()
            today = datetime.date.today()
            filename = 'data_karyawan_user-' + str(today) + '.csv'
            response = HttpResponse(dataset.csv, content_type='text/csv')
            response['Content-Disposition'] = u'attachment; filename="%s"' %  (filename)

            return response
        except:
            return Response({'Result': 'Gagal mengexport data user karyawan, ada kesalahan'}, status=400)