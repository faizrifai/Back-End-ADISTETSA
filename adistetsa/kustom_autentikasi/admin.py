from django.contrib import admin

from .models import *

# Register your models here.
class DataSiswaUserAdmin(admin.ModelAdmin):
    autocomplete_fields = ['DATA_SISWA', ]

admin.site.register(DataSiswaUser, DataSiswaUserAdmin)
admin.site.register(DataOrangTuaUser)
admin.site.register(DataGuruUser)
admin.site.register(DataKaryawanUser)