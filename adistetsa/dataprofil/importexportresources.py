from django.contrib.auth.models import User, Group

from import_export.fields import Field
from import_export.widgets import ForeignKeyWidget
from import_export import resources

from .models import *

# Register your import_export resource model here
class DataSiswaResource(resources.ModelResource):

    class Meta:
        model = DataSiswa
        import_id_fields = ('NISN',)

class DataOrangTuaResource(resources.ModelResource):

    class Meta:
        model = DataOrangTua
        exclude = ('ID',)
        import_id_fields = ('NIK_AYAH', 'NIK_IBU')

class DataGuruResource(resources.ModelResource):

    class Meta:
        model = DataGuru
        exclude = ('ID',)
        import_id_fields = ('NIK',)

class DataKaryawanResource(resources.ModelResource):
    class Meta:
        model = DataKaryawan
        exclude = ('ID',)
        import_id_fields = ('NIK',)