from django.shortcuts import render
from .models import *
from .serializers import *

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated 
from rest_framework.authentication import TokenAuthentication

# Create your views here.

class ObtainAuthTokenView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
        })

class HomeView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'user': str(request.user),
            'auth': str(request.auth),
        }
        return Response(content)

class DataSiswaListView(APIView):
    """
    List all snippets, or create a new snippet.
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        data_siswa = DataSiswa.objects.all()
        serializer = DataSiswaSerializer(data_siswa, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DataSiswaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DataSiswaDetailView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return DataSiswa.objects.get(pk=pk)
        except DataSiswa.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        siswa = self.get_object(pk)
        serializer = DataSiswaSerializer(siswa)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        siswa = self.get_object(pk)
        serializer = DataSiswaSerializer(siswa, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        siswa = self.get_object(pk)
        siswa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class DataOrangTuaSiswaListView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        data_orang_tua = DataOrangTua.objects.all()
        serializer = DataOrangTuaSerializer(data_orang_tua, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DataOrangTuaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DataOrangTuaDetailView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return DataOrangTua.objects.get(pk=pk)
        except DataOrangTua.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        orang_tua = self.get_object(pk)
        serializer = DataOrangTuaSerializer(orang_tua)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        orang_tua = self.get_object(pk)
        serializer = DataOrangTuaSerializer(orang_tua, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        orang_tua = self.get_object(pk)
        orang_tua.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





class DataKaryawanListView(APIView): 
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        data_karyawan = DataKaryawan.objects.all()
        serializer = DataKaryawanSerializer(data_karyawan, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DataKaryawanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DataKaryawanDetailView(APIView):
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return DataKaryawan.objects.get(pk=pk)
        except DataKaryawan.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        karyawan = self.get_object(pk)
        serializer = DataKaryawanSerializer(karyawan)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        karyawan = self.get_object(pk)
        serializer = DataKaryawanSerializer(karyawan, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        karyawan = self.get_object(pk)
        karyawan.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





class DataGuruListView(APIView): 
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        data_guru = DataGuru.objects.all()
        serializer = DataGuruSerializer(data_guru, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DataGuruSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DataGuruDetailView(APIView):
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return DataGuru.objects.get(pk=pk)
        except DataGuru.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        guru = self.get_object(pk)
        serializer = DataGuruSerializer(guru)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        guru = self.get_object(pk)
        serializer = DataGuruSerializer(guru, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        guru = self.get_object(pk)
        guru.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)