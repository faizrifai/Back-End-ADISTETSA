from django.shortcuts import render
from .models import *
from .serializers import *

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated 
from rest_framework.authentication import TokenAuthentication
from drf_yasg.utils import swagger_auto_schema

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

class DataSiswaListView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = DataSiswaSerializer
    queryset = DataSiswa.objects.all()

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






class DataKompetensiGuruListView(APIView): 
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        data_kompetensi_guru = DataKompetensiGuru.objects.all()
        serializer = DataKompetensiGuruSerializer(data_kompetensi_guru, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DataKompetensiGuruSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DataKompetensiGuruDetailView(APIView):
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return DataKompetensiGuru.objects.get(pk=pk)
        except DataKompetensiGuru.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        kompetensi_guru = self.get_object(pk)
        serializer = DataKompetensiGuruSerializer(kompetensi_guru)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        kompetensi_guru = self.get_object(pk)
        serializer = DataKompetensiGuruSerializer(kompetensi_guru, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        kompetensi_guru = self.get_object(pk)
        kompetensi_guru.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)







class DataKompetensiKaryawanListView(APIView): 
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        data_kompetensi_karyawan = DataKompetensiKaryawan.objects.all()
        serializer = DataKompetensiKaryawanSerializer(data_kompetensi_karyawan, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DataKompetensiKaryawanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DataKompetensiKaryawanDetailView(APIView):
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return DataKompetensiKaryawan.objects.get(pk=pk)
        except DataKompetensiKaryawan.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        kompetensi_karyawan = self.get_object(pk)
        serializer = DataKompetensiKaryawanSerializer(kompetensi_karyawan)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        kompetensi_karyawan = self.get_object(pk)
        serializer = DataKompetensiKaryawanSerializer(kompetensi_karyawan, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        kompetensi_karyawan = self.get_object(pk)
        kompetensi_karyawan.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class DataAnakGuruListView(APIView): 
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        data_anak_guru = DataAnakGuru.objects.all()
        serializer = DataAnakGuruSerializer(data_anak_guru, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DataAnakGuruSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DataAnakGuruDetailView(APIView):
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return DataAnakGuru.objects.get(pk=pk)
        except DataAnakGuru.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        anak_guru = self.get_object(pk)
        serializer = DataAnakGuruSerializer(anak_guru)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        anak_guru = self.get_object(pk)
        serializer = DataAnakGuruSerializer(anak_guru, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        anak_guru = self.get_object(pk)
        anak_guru.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)







class DataAnakKaryawanListView(APIView): 
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        data_anak_karyawan = DataAnakKaryawan.objects.all()
        serializer = DataAnakKaryawanSerializer(data_anak_karyawan, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DataAnakKaryawanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DataAnakKaryawanDetailView(APIView):
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return DataAnakKaryawan.objects.get(pk=pk)
        except DataAnakKaryawan.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        anak_karyawan = self.get_object(pk)
        serializer = DataAnakKaryawanSerializer(anak_karyawan)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        anak_karyawan = self.get_object(pk)
        serializer = DataAnakKaryawanSerializer(anak_karyawan, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        anak_karyawan = self.get_object(pk)
        anak_karyawan.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class DataBeasiswaGuruListView(APIView): 
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        data_beasiswa_guru = DataBeasiswaGuru.objects.all()
        serializer = DataBeasiswaGuruSerializer(data_beasiswa_guru, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DataBeasiswaGuruSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DataBeasiswaGuruView(APIView): 
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]

    def get(self, request, id):
        data_beasiswa_guru = DataBeasiswaGuru.objects.filter(OWNER=id)
        serializer = DataBeasiswaGuruSerializer(data_beasiswa_guru, many=True)
        return Response(serializer.data)


class DataBeasiswaGuru2View(APIView): 
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]

    def get(self, request, id, pk):
        data_beasiswa_guru = DataBeasiswaGuru.objects.filter(OWNER=id, pk=pk)
        serializer = DataBeasiswaGuruSerializer(data_beasiswa_guru, many=True)
        return Response(serializer.data)
    

class DataBeasiswaGuruDetailView(APIView):
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return DataBeasiswaGuru.objects.get(pk=pk)
        except DataBeasiswaGuru.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        beasiswa_guru = self.get_object(pk)
        serializer = DataBeasiswaGuruSerializer(beasiswa_guru)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        beasiswa_guru = self.get_object(pk)
        serializer = DataBeasiswaGuruSerializer(beasiswa_guru, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        beasiswa_guru = self.get_object(pk)
        beasiswa_guru.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)






class DataBeasiswaKaryawanListView(APIView): 
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        data_beasiswa_karyawan = DataBeasiswaKaryawan.objects.all()
        serializer = DataBeasiswaKaryawanSerializer(data_beasiswa_karyawan, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DataBeasiswaKaryawanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DataBeasiswaKaryawanDetailView(APIView):
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return DataBeasiswaKaryawan.objects.get(pk=pk)
        except DataBeasiswaKaryawan.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        beasiswa_karyawan = self.get_object(pk)
        serializer = DataBeasiswaKaryawanSerializer(beasiswa_karyawan)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        beasiswa_karyawan = self.get_object(pk)
        serializer = DataBeasiswaKaryawanSerializer(beasiswa_karyawan, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        beasiswa_karyawan = self.get_object(pk)
        beasiswa_karyawan.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)