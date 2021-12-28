from django.shortcuts import render
from .models import *
from .serializers import *

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework import permissions

# Create your views here.

class DataSiswaListView(APIView):
    """
    List all snippets, or create a new snippet.
    """
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
    """
    Retrieve, update or delete a snippet instance.
    """
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