from django.contrib.auth.models import User, Group
from import_export import resources
from .models import *

class LogUKSTendikResource(resources.ModelResource):
    class Meta:
        model = LogUKSTendik
        exclude = ('ID',)
        
class LogUKSSiswaResource(resources.ModelResource):
    class Meta:
        model = LogUKSSiswa
        exclude = ('ID',)
        
class BukuTamuResource(resources.ModelResource):
    class Meta:
        model = BukuTamu
        exclude = ('ID',)