from os import name
from django.shortcuts import render
from .models import *
from .serializers import *
from .doc_schema import *
from rest_framework.parsers import MultiPartParser
from .models import SilabusRPB

from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from collections import namedtuple

from adistetsa.permissions import HasGroupPermissionAny, IsSuperAdmin, is_in_group

SilabusRPBWithFilter = namedtuple('SilabusRPBWithFilter', ('silabus_rpb', 'tahun', 'mapel', 'kelas', 'semester'))

# Create your views here. 

class DataSilabusRPBListView(generics.ListAPIView):
    """
    get: Menampilkan seluruh daftar Riwayat Karir karyawan (Super Admin/ Karyawan).
    post: Menambahkan data Riwayat Karir karyawan (Super Admin/ Karyawan).
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Staf Kurikulum'],
        'POST': ['Staf Kurikulum'],
    }
    queryset = SilabusRPB.objects.all()
    serializer_class = SilabusRPBWithFilterSerializer


    def list(self, request, *args, **kwargs):
        queryset=self.get_queryset()
        tahun = TahunAjaran.objects.all()
        mapel = MataPelajaran.objects.all()
        kelas = Kelas.objects.all()
        semester = DataSemester.objects.all()
        silabus_rpbtahun = SilabusRPBWithFilter(silabus_rpb=queryset, tahun=tahun, mapel=mapel, kelas=kelas, semester=semester)

        serializer = SilabusRPBWithFilterSerializer(silabus_rpbtahun)

        # if serializer.is_valid():
        return Response(serializer.data)

        

    # @swagger_auto_schema(
    #     manual_parameters=[param_importexportfile, param_tahunajaran],
    #     responses={'201': 'Berhasil', '400': 'Gagal',}
    # )
    # def post(self, request, format=None):
    #     serializer = SilabusRPBSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DataSilabusRPBCreateView(generics.CreateAPIView):
    """
    get: Menampilkan seluruh daftar Riwayat Karir karyawan (Super Admin/ Karyawan).
    post: Menambahkan data Riwayat Karir karyawan (Super Admin/ Karyawan).
    """
    permission_classes = [IsSuperAdmin|HasGroupPermissionAny]
    required_groups = {
        'GET': ['Staf Kurikulum'],
        'POST': ['Staf Kurikulum'],
    }
    queryset = SilabusRPB.objects.all()
    serializer_class = SilabusRPBSerializer
    parser_classes= (MultiPartParser,)
   
    
class DataSilabusRPBDetailView(APIView):
    """
    get: Menampilkan data SilabusRPB.
    put: Mengubah atribut keseluruhan data SilabusRPB.
    patch: Mengubah beberapa atribut data SilabusRPB.
    delete: Menghapus data SilabusRPB.
    """
    permission_classes = [HasGroupPermissionAny]
    required_groups = {
        'GET': ['Staf Kurikulum'],
        'PUT': ['Staf Kurikulum'],
        'PATCH': ['Staf Kurikulum'],
        'DELETE': ['Staf Kurikulum'],
    }
    serializer_class = SilabusRPBSerializer
    parser_classes= (MultiPartParser,)
    def get_queryset(self, pk):
        return SilabusRPB.objects.get(pk=self.kwargs['pk'])

    def get(self, request, pk, *args, **kwargs):
        queryset = self.get_queryset(pk)
        serializer = self.serializer_class
        response = serializer(queryset).data

        return Response(response)

    @swagger_auto_schema(
        manual_parameters=[param_importexportfile,param_tahunajaran],
        responses={'201': 'Berhasil', '400': 'Gagal',},
    )
    def put(self, request, pk, format=None):
        queryset = self.get_queryset(pk)
        serializer = self.serializer_class(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    @swagger_auto_schema(
        manual_parameters=[param_importexportfile,param_tahunajaran],
        responses={'201': 'Berhasil', '400': 'Gagal',},
    )
    def patch(self, request, pk):
        queryset = self.get_queryset(pk)
        serializer = self.serializer_class(queryset, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        queryset = self.get_queryset(pk)
        serializer = self.serializer_class(queryset, data=request.data, partial=True)
        if serializer.is_valid():
           
            queryset.delete()
            return Response(serializer.data)    
        return Response(status=status.HTTP_204_NO_CONTENT)   