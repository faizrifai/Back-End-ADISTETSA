from django.shortcuts import render
from .models import *
from .serializers import *

from rest_framework import viewsets
from rest_framework import permissions

# Create your views here.
class DataSiswaViewSet(viewsets.ModelViewSet):
    queryset = DataSiswa.objects.all()
    serializer_class = DataSiswaSerializer
    # permission_classes = [permissions.IsAuthenticated]