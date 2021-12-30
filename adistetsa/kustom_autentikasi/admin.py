from django.contrib import admin
from django.contrib.auth.models import User

from import_export import resources
from import_export.admin import ImportExportModelAdmin, ExportActionMixin
from import_export.fields import Field
from import_export.widgets import ForeignKeyWidget

from .models import *

# Register your import_export resource model here
class DataSiswaUserResource(resources.ModelResource):

    class Meta:
        model = DataSiswaUser

class DataGuruUserResource(resources.ModelResource):
    # username = Field(
    #     column_name='username',
    #     attribute='username',
    #     widget=ForeignKeyWidget(DataGuruUser, 'USER__username')
    # )

    class Meta:
        model = DataGuruUser
        exclude = ('id', 'USER')
        fields = ('USER__username', 'DATA_GURU')
        import_id_fields = ('DATA_GURU')

# Register your models here.
class DataSiswaUserAdmin(ImportExportModelAdmin):
    autocomplete_fields = ['DATA_SISWA', 'USER',]
    search_fields = ['DATA_SISWA__NISN', 'DATA_SISWA__NAMA', 'USER__username']
    list_display = ('nama_lengkap', 'username',)

    resource_class = DataSiswaUserResource

    def username(self, obj):
        return obj.USER.username

    def nama_lengkap(self, obj):
        return obj.DATA_SISWA.NAMA

class DataGuruUserAdmin(ImportExportModelAdmin):
    autocomplete_fields = ['DATA_GURU', 'USER',]
    search_fields = ['DATA_GURU__NIP', 'DATA_GURU__NAMA_LENGKAP', 'USER__username']
    list_display = ('nama_lengkap', 'username',)

    resource_class = DataGuruUserResource

    def username(self, obj):
        return obj.USER.username

    def nama_lengkap(self, obj):
        return obj.DATA_GURU.NAMA_LENGKAP

admin.site.register(DataSiswaUser, DataSiswaUserAdmin)
admin.site.register(DataOrangTuaUser)
admin.site.register(DataGuruUser, DataGuruUserAdmin)
admin.site.register(DataKaryawanUser)