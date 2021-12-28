from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(DataSiswa)

# class anak_inline(admin.TabularInline):
#     model = DataOrangTua.DATA_ANAK.through
#     extra = 1
#     verbose_name = 'Siswa'
#     verbose_name_plural = 'Daftar Anak'
    
#     # def get_queryset(self, request):
#     #     qs = 
#     #     return super().get_queryset(request)
    
    
class DataOrangTuaAdmin(admin.ModelAdmin):
    filter_horizontal = ('DATA_ANAK',)

admin.site.register(DataOrangTua, DataOrangTuaAdmin)